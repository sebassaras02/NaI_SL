# DEFINICION DE FUNCIONES
# Por: Sebastian Sarasti
# Lista de funciones para el tratamiento de datos de un detector de NaI
# TASA DE CUENTAS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def tasa(spectranuclei):
    """This function helps to transform a spectra in gross spectra. Time of exposition is the
    second value of data recolected"""
    tim=spectranuclei[1]
    for i in spectranuclei:
        spectra_g=spectranuclei[2:len(spectranuclei)]/tim
    return spectra_g
# CONTEO NETO
def netcount(spectranuclei,spectrabk):
    """
    This function help to estimate net count rate.
    The time is not necessary because the second value of vector
    is time of sampling in seconds. Because of zero-index, Python uses
    the first value
    """
    timnuclei=spectranuclei[1]
    timbk=spectrabk[1]
    spectranuclei=spectranuclei[2:len(spectranuclei)]
    spectrabk=spectrabk[2:len(spectrabk)]
    spectran_g=spectranuclei/timnuclei
    spectrabk_g=spectrabk/timbk
    spectran_n=spectran_g-spectrabk_g
    for i in range(len(spectran_n)):
        if spectran_n[i]<0:
            spectran_n[i] =0
        else:
            spectran_n[i]=spectran_n[i]
    return spectran_n
# SUAVIZADO MOVIL 3 VALORES
def smooth_three(spectra):
    spectra_smoothed=np.zeros(len(spectra))
    for i in range (3,len(spectra)-1):
           spectra_smoothed[i+1]=(spectra[i]+spectra[i-1]+spectra[i-2])/3
    return spectra_smoothed
# SUAVIZADO MOVIL 5 VALORES
def smooth_five(spectra):
    spectra_smoothed=np.zeros(len(spectra))
    for i in range (4, len(spectra)-1):
           spectra_smoothed[i+1]=(spectra[i]+spectra[i-1]+spectra[i-2]-spectra[i-3]+spectra[i-4])/5
    return spectra_smoothed
# NORMALIZAR HISTOGRAMA SIMULADO
def normalizar_sim(histograma):
    h=np.histogram(histograma,bins=150)
    y=h[0]
    x=h[1]
    x=x[0:len(x)-1]
    s=max(y)
    y_n=np.zeros(len(y))
    for i in range(len(y_n)):
        y_n[i]=y[i]/s
    return(x,y_n)
# NORMALIZAR ESPECTROS
def normalizar_exp(spectra, nuclei):
    if nuclei== "Cs":
        m=max(spectra[3000:len(spectra)])
        spectra_nor=np.zeros(len(spectra))
        for i in range(len(spectra)):
            spectra_nor[i]=spectra[i]/m
    else:
        m=max(spectra)
        spectra_nor=np.zeros(len(spectra))
        for i in range(len(spectra)):
            spectra_nor[i]=spectra[i]/m
    return(spectra_nor)
# DISTRIBUCION GAUSSIANO
def spectrum(E,osc,sigma):
    """
    Añade la resolucion del detector al espectro simulado
    """
    x=np.linspace(0,2,1500,endpoint=True)
    gE=[]
    for Ei in x:
        tot=0
        for Ej,os in zip(E,osc):
            tot+=os*np.exp(-((((Ej-Ei)/sigma)**2)))
        gE.append(tot)
    x=x[0:1500]
    gE=gE[0:1500]
    return x, gE
# CALCULO DEL SIGMA EN FUNCION DE LA RESOLUCION
def gauss_fit(spec_e_neto,spec_s_bruto,energia, nuclei):
    if nuclei=="Cs":
        spec_e_neto=list(np.float_(spec_e_neto))
        spec_s_bruto=np.histogram(spec_s_bruto,250)
        x=np.linspace(0,spec_s_bruto[1][250], num=1000, endpoint=True)
        sigma=0.001
        res_dif=0
        m=max(spec_e_neto[3000:len(spec_e_neto)])
        indice=spec_e_neto.index(m)
        # se determina la mitad de la altura y se buscan los valores superiores a este
        n=m/2
        p=np.where(spec_e_neto[0:indice]<=n)
        j1=p[0]
        m1=j1[-1]
        q=np.where(spec_e_neto[indice:len(spec_e_neto)]<=n)
        j2=q[0]
        j2=j2+indice
        m2=j2[0]
        # una vez identificados los valores, se busca los indices de este en el arreglo de energia
        x1=energia[m1]
        x2=energia[m2]
        xm=energia[indice]
        # calculo de la resolucion
        res_e=(x2-x1)/xm
        while res_dif<0.01:
            # se suaviza el espectro simulado
            gE=spectrum(spec_s_bruto[1][0:250],spec_s_bruto[0],sigma,x)
            # se determina el maximo y su indice
            m=max(gE)
            indice=gE.index(max(gE))
            # se determina la mitad de la altura y se buscan los valores superiores a este
            n=m/2
            p=np.where(gE[0:indice]<=n)
            j1=p[0]
            m1=j1[-1]
            q=np.where(gE[indice:-1]<=n)
            j2=q[0]
            j2=j2+indice
            m2=j2[0]
            # una vez identificados los valores, se busca los indices de este en el arreglo de energia
            x1=x[m1]
            x2=x[m2]
            xm=x[indice]
            # calculo de la resolucion
            res_s=(x2-x1)/xm
            sigma=sigma+0.001
            res_dif=(res_s-res_e)/res_e             
    else:
        spec_e_neto=list(np.float_(spec_e_neto))
        spec_s_bruto=np.histogram(spec_s_bruto,250)
        x=np.linspace(0,spec_s_bruto[1][250], num=1000, endpoint=True)
        sigma=0.001
        res_dif=0
        m=max(spec_e_neto)
        indice=spec_e_neto.index(max(spec_e_neto))
        # se determina la mitad de la altura y se buscan los valores superiores a este
        n=m/2
        p=np.where(spec_e_neto[0:indice]<=n)
        j1=p[0]
        m1=j1[-1]
        q=np.where(spec_e_neto[indice:len(spec_e_neto)]<=n)
        j2=q[0]
        j2=j2+indice
        m2=j2[0]
        # una vez identificados los valores, se busca los indices de este en el arreglo de energia
        x1=energia[m1]
        x2=energia[m2]
        xm=energia[indice]
        # calculo de la resolucion
        res_e=(x2-x1)/xm
        while res_dif<0.01:
            # se suaviza el espectro simulado
            gE=spectrum(spec_s_bruto[1][0:250],spec_s_bruto[0],sigma,x)
            # se determina el maximo y su indice
            m=max(gE)
            indice=gE.index(max(gE))
            # se determina la mitad de la altura y se buscan los valores superiores a este
            n=m/2
            p=np.where(gE[0:indice]<=n)
            j1=p[0]
            m1=j1[-1]
            q=np.where(gE[indice:-1]<=n)
            j2=q[0]
            j2=j2+indice
            m2=j2[0]
            # una vez identificados los valores, se busca los indices de este en el arreglo de energia
            x1=x[m1]
            x2=x[m2]
            xm=x[indice]
            # calculo de la resolucion
            res_s=(x2-x1)/xm
            sigma=sigma+0.001
            res_dif=(res_s-res_e)/res_e            
    return (gE,x,sigma,res_s,res_e,res_dif)
# AREA
def area(spectra,energy,a,b):
    spec=[]
    spec=spectra
    spec=spec[a:b]
    energy=energy[a:b]
    a=0
    a=np.trapz(spec,energy)
    return a
# INCERTIBUMBRE
def incertidumbre(spectra,bk,energy,a,b,tiempo_s,tiempo_bk):
    a_s=0
    a_bk=0
    a_s=area(spectra,energy,a,b)
    a_b=area(bk,energy,a,b)
    incer=(a_s/tiempo_s+a_b/tiempo_bk)**0.5
    return incer
def f_correcion(d_spectra_e, d_spectra_s, nuclei):
    """
    This function is able to estimate and give spectrum with activity 
    correction and help to estimate correction factor due to PTM and 
    scintillation procces related
    Where:
        d_spectra_e: dictionary with net count rate spectrum
        d_spectra_e: dictionary with simulated spectrum with resolution 
        and activity scaling
    """
    if nuclei=='Eu-1':
        # se determina el máximo de cada espectro experimental
        m_e_=[]
        for i in d_spectra_e:
            m_e_.append(max(d_spectra_e[i][550:700]))
        # se determina el máximo de cada espectro simulado
        m_s_=[]
        for i in range(3):
            m_s_.append(max(d_spectra_s[i]))
        #se determina el factor de corrección en función del fotopico máximo de cada
        # espectro
        f_pmt_=np.array([m_s_[i]/m_e_[i] for i in range(len(m_s_))])

    elif nuclei=='Eu-2':
        # se determina el máximo de cada espectro experimental
        m_e_=[]
        for i in d_spectra_e:
            m_e_.append(max(d_spectra_e[i][1100:1300]))
        # se determina el máximo de cada espectro simulado
        m_s_=[]
        for i in range(3):
            m_s_.append(max(d_spectra_s[i]))
        #se determina el factor de corrección en función del fotopico máximo de cada
        # espectro
        f_pmt_=np.array([m_s_[i]/m_e_[i] for i in range(len(m_s_))])

    elif nuclei=='Eu-3':
        # se determina el máximo de cada espectro experimental
        m_e_=[]
        for i in d_spectra_e:
            m_e_.append(max(d_spectra_e[i][1500:2000]))
        # se determina el máximo de cada espectro simulado
        m_s_=[]
        for i in range(3):
            m_s_.append(max(d_spectra_s[i]))
        #se determina el factor de corrección en función del fotopico máximo de cada
        # espectro
        f_pmt_=np.array([m_s_[i]/m_e_[i] for i in range(len(m_s_))])


    elif nuclei=='Cs':
        # se determina el máximo de cada espectro experimental
        m_e_=[]
        for i in d_spectra_e:
            m_e_.append(max(d_spectra_e[i][2000:5000]))
        # se determina el máximo de cada espectro simulado
        m_s_=[]
        for i in range(3):
            m_s_.append(max(d_spectra_s[i]))
        #se determina el factor de corrección en función del fotopico máximo de cada
        # espectro
        f_pmt_=np.array([m_s_[i]/m_e_[i] for i in range(len(m_s_))])

    elif nuclei=='Co-1':
        # se determina el máximo de cada espectro experimental
        m_e_=[]
        for i in d_spectra_e:
            m_e_.append(max(d_spectra_e[i][5200:5750]))
        # se determina el máximo de cada espectro simulado
        m_s_=[]
        for i in range(3):
            m_s_.append(max(d_spectra_s[i][0:900]))
        #se determina el factor de corrección en función del fotopico máximo de cada
        # espectro
        f_pmt_=np.array([m_s_[i]/m_e_[i] for i in range(len(m_s_))])

    elif nuclei=='Co-2':
        # se determina el máximo de cada espectro experimental
        m_e_=[]
        for i in d_spectra_e:
            m_e_.append(max(d_spectra_e[i][5800:7000]))
        # se determina el máximo de cada espectro simulado
        m_s_=[]
        for i in range(3):
            m_s_.append(max(d_spectra_s[i][900:1500]))
        #se determina el factor de corrección en función del fotopico máximo de cada
        # espectro
        f_pmt_=np.array([m_s_[i]/m_e_[i] for i in range(len(m_s_))])


    else:
        # se determina el máximo de cada espectro experimental
        m_e_=[]
        for i in d_spectra_e:
            m_e_.append(max(d_spectra_e[i]))
        # se determina el máximo de cada espectro simulado
        m_s_=[]
        for i in range(3):
            m_s_.append(max(d_spectra_s[i]))
        #se determina el factor de corrección en función del fotopico máximo de cada
        # espectro
        f_pmt_=np.array([m_s_[i]/m_e_[i] for i in range(len(m_s_))])
    return f_pmt_

def reso(his_sim, sig):
    a= np.histogram(his_sim, bins=np.linspace(0,2,500))
    b=spectrum(a[1][0:499], a[0], sig)
    return b


