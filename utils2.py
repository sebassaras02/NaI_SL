# Author: Sebastián Alejandro Sarasti Zambonino
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
class spectra_simula:
    sigma=0.026
    def __init__(self, histo_sim,s_par,a_par):
        self.histo_sim=histo_sim
        self.s_par=s_par
        self.a_par=a_par
    def histogram_r(self):
        h=np.histogram(self.histo_sim,bins=1500)
        return h
    # funtion to extract maximun photopeak
    def max_peak(self):
        h=np.histogram(self.histo_sim,bins=1500)
        E=h[1]
        osc=h[0]
        p_max=sum(osc)
        tiem=self.s_par/self.a_par
        return p_max/tiem
    # funcion to add resolution
    def spectrum(self):
        h=np.histogram(self.histo_sim,bins=1500)
        E=h[1]
        osc=h[0]
        x=np.linspace(0,2,1500,endpoint=True)
        gE=[]
        
        for Ei in x:
            tot=0
            for Ej,os in zip(E,osc):
                tot+=os*np.exp(-((((Ej-Ei)/self.sigma)**2)))
            gE.append(tot)
        x=x[0:1500]
        gE=gE[0:1500]
        return x, gE
    def spec_scaled(self):
        
        h=np.histogram(self.histo_sim,bins=1500)
        E=h[1]
        osc=h[0]
        x=np.linspace(0,2,1500,endpoint=True)
        gE=[]
        
        for Ei in x:
            tot=0
            for Ej,os in zip(E,osc):
                tot+=os*np.exp(-((((Ej-Ei)/self.sigma)**2)))
            gE.append(tot)
        x=x[0:1500]
        gE=gE[0:1500]
        tiem=self.s_par/self.a_par
        for i in range(len(gE)):
            gE[i]=gE[i]/tiem
        return x, gE

def draw_c(data_exp, data_sim):
    fig1, ax1 = plt.subplots(3, 3, figsize=(30, 18))

    line1 = ax1[0, 0].plot(data_exp[0][:, 0], data_exp[0][:, 1], color="Blue", linestyle='-', marker="x",
                           label="Experimental")
    ax1[0, 0].set_xlabel("Radioactive source position (m)")
    ax1[0, 0].set_ylabel("Experimental (cps)", color="Blue")
    ax1[0, 0].tick_params(axis='y',labelcolor='Blue')
    ax2 = ax1[0, 0].twinx()
    line2 = ax2.plot(data_sim.iloc[0], data_sim.iloc[1], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1[0, 0].legend(lines, labels)
    plt.title("Detector position 0 0 20 cm")

    line3 = ax1[0, 1].plot(data_exp[1][:, 0], data_exp[1][:, 1], color="Blue", linestyle='-', marker="x",
                           label="Experimental")
    ax1[0, 1].set_xlabel("Radioactive source position (m)")
    ax1[0, 1].set_ylabel("Experimental (cps)", color='Blue')
    ax1[0, 1].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[0, 1].twinx()
    line4 = ax2.plot(data_sim.iloc[0], data_sim.iloc[2], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)",color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line3 + line4
    labels = [l.get_label() for l in lines]
    ax1[0, 1].legend(lines, labels)
    plt.title("Detector position 0 0 40 cm")

    line5 = ax1[0, 2].plot(data_exp[2][:, 0], data_exp[2][:, 1], color="Blue", linestyle='-', marker="x",
                           label="Experimental")
    ax1[0, 2].set_xlabel("Radioactive source position (m)")
    ax1[0, 2].set_ylabel("Experimental (cps)", color='Blue')
    ax1[0, 2].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[0, 2].twinx()
    line6 = ax2.plot(data_sim.iloc[0], data_sim.iloc[3], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line5 + line6
    labels = [l.get_label() for l in lines]
    ax1[0, 2].legend(lines, labels)
    plt.title("Detector position 0 0 60 cm")

    line7 = ax1[1, 0].plot(data_exp[3][:, 0], data_exp[3][:, 1], color="Blue", linestyle='-', marker="x",
                           label="Experimental")
    ax1[1, 0].set_xlabel("Radioactive source position (m)")
    ax1[1, 0].set_ylabel("Experimental (cps)", color='Blue')
    ax1[1, 0].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[1, 0].twinx()
    line8 = ax2.plot(data_sim.iloc[0], data_sim.iloc[4], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line7 + line8
    labels = [l.get_label() for l in lines]
    ax1[1, 0].legend(lines, labels)
    plt.title("Detector position 0 -25 20 cm")

    line9 = ax1[1, 1].plot(data_exp[4][:, 0], data_exp[4][:, 1], color="Blue", linestyle='-', marker="x",
                           label="Experimental")
    ax1[1, 1].set_xlabel("Radioactive source position (m)")
    ax1[1, 1].set_ylabel("Experimental (cps)", color='Blue')
    ax1[1, 1].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[1, 1].twinx()
    line10 = ax2.plot(data_sim.iloc[0], data_sim.iloc[5], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line9 + line10
    labels = [l.get_label() for l in lines]
    ax1[1, 1].legend(lines, labels)
    plt.title("Detector position 0 -25 40 cm")

    line11 = ax1[1, 2].plot(data_exp[5][:, 0], data_exp[5][:, 1], color="Blue", linestyle='-', marker="x",
                            label="Experimental")
    ax1[1, 2].set_xlabel("Radioactive source position (m)")
    ax1[1, 2].set_ylabel("Experimental (cps)", color='Blue')
    ax1[1, 2].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[1, 2].twinx()
    line12 = ax2.plot(data_sim.iloc[0], data_sim.iloc[6], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line11 + line12
    labels = [l.get_label() for l in lines]
    ax1[1, 2].legend(lines, labels)
    plt.title("Detector position 0 -25 60 cm")

    line13 = ax1[2, 0].plot(data_exp[6][:, 0], data_exp[6][:, 1], color="Blue", linestyle='-', marker="x",
                            label="Experimental")
    ax1[2, 0].set_xlabel("Radioactive source position (m)")
    ax1[2, 0].set_ylabel("Experimental (cps)", color='Blue')
    ax1[2, 0].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[2, 0].twinx()
    line14 = ax2.plot(data_sim.iloc[0], data_sim.iloc[7], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line13 + line14
    labels = [l.get_label() for l in lines]
    ax1[2, 0].legend(lines, labels)
    plt.title("Detector position 0 25 20 cm")

    line15 = ax1[2, 1].plot(data_exp[7][:, 0], data_exp[7][:, 1], color="Blue", linestyle='-', marker="x",
                            label="Experimental")
    ax1[2, 1].set_xlabel("Radioactive source position (m)")
    ax1[2, 1].set_ylabel("Experimental (cps)", color='Blue')
    ax1[2, 1].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[2, 1].twinx()
    line16 = ax2.plot(data_sim.iloc[0], data_sim.iloc[8], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line15 + line16
    labels = [l.get_label() for l in lines]
    ax1[2, 1].legend(lines, labels)
    plt.title("Detector position 0 25 40 cm")

    line17 = ax1[2, 2].plot(data_exp[8][:, 0], data_exp[8][:, 1], color="Blue", linestyle='-', marker="x",
                            label="Experimental")
    ax1[2, 2].set_xlabel("Radioactive source position (m)")
    ax1[2, 2].set_ylabel("Experimental (cps)", color='Blue')
    ax1[2, 2].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[2, 2].twinx()
    line18 = ax2.plot(data_sim.iloc[0], data_sim.iloc[9], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line17 + line18
    labels = [l.get_label() for l in lines]
    ax1[2, 2].legend(lines, labels)
    plt.title("Detector position 0 25 60 cm")

    return ax1

def draw_d(data_exp, data_sim):
    fig1, ax1 = plt.subplots(3, 3, figsize=(30, 18))

    line1 = ax1[0, 0].plot(data_exp[0][:, 0], data_exp[0][:, 1], color="Blue", linestyle='-', marker="x",
                           label="Experimental")
    ax1[0, 0].set_xlabel("Radioactive source position (m)")
    ax1[0, 0].set_ylabel("Experimental (cps)", color='Blue')
    ax1[0, 0].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[0, 0].twinx()
    line2 = ax2.plot(data_sim.iloc[0], data_sim.iloc[10], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1[0, 0].legend(lines, labels)
    plt.title("Detector position 24 0 20 cm")

    line3 = ax1[0, 1].plot(data_exp[1][:, 0], data_exp[1][:, 1], color="Blue", linestyle='-', marker="x",
                           label="Experimental")
    ax1[0, 1].set_xlabel("Radioactive source position (m)")
    ax1[0, 1].set_ylabel("Experimental (cps)", color='Blue')
    ax1[0, 1].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[0, 1].twinx()
    line4 = ax2.plot(data_sim.iloc[0], data_sim.iloc[11], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line3 + line4
    labels = [l.get_label() for l in lines]
    ax1[0, 1].legend(lines, labels)
    plt.title("Detector position 24 0 40 cm")

    line5 = ax1[0, 2].plot(data_exp[2][:, 0], data_exp[2][:, 1], color="Blue", linestyle='-', marker="x",
                           label="Experimental")
    ax1[0, 2].set_xlabel("Radioactive source position (m)")
    ax1[0, 2].set_ylabel("Experimental (cps)", color='Blue')
    ax1[0, 2].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[0, 2].twinx()
    line6 = ax2.plot(data_sim.iloc[0], data_sim.iloc[12], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line5 + line6
    labels = [l.get_label() for l in lines]
    ax1[0, 2].legend(lines, labels)
    plt.title("Detector position 24 0 60 cm")

    line7 = ax1[1, 0].plot(data_exp[3][:, 0], data_exp[3][:, 1], color="Blue", linestyle='-', marker="x",
                           label="Experimental")
    ax1[1, 0].set_xlabel("Radioactive source position (m)")
    ax1[1, 0].set_ylabel("Experimental (cps)", color='Blue')
    ax1[1, 0].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[1, 0].twinx()
    line8 = ax2.plot(data_sim.iloc[0], data_sim.iloc[13], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line7 + line8
    labels = [l.get_label() for l in lines]
    ax1[1, 0].legend(lines, labels)
    plt.title("Detector position 24 -25 20 cm")

    line9 = ax1[1, 1].plot(data_exp[4][:, 0], data_exp[4][:, 1], color="Blue", linestyle='-', marker="x",
                           label="Experimental")
    ax1[1, 1].set_xlabel("Radioactive source position (m)")
    ax1[1, 1].set_ylabel("Experimental (cps)", color='Blue')
    ax1[1, 1].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[1, 1].twinx()
    line10 = ax2.plot(data_sim.iloc[0], data_sim.iloc[14], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line9 + line10
    labels = [l.get_label() for l in lines]
    ax1[1, 1].legend(lines, labels)
    plt.title("Detector position 24 -25 40 cm")

    line11 = ax1[1, 2].plot(data_exp[5][:, 0], data_exp[5][:, 1], color="Blue", linestyle='-', marker="x",
                            label="Experimental")
    ax1[1, 2].set_xlabel("Radioactive source position (m)")
    ax1[1, 2].set_ylabel("Experimental (cps)", color='Blue')
    ax1[1, 2].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[1, 2].twinx()
    line12 = ax2.plot(data_sim.iloc[0], data_sim.iloc[15], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line11 + line12
    labels = [l.get_label() for l in lines]
    ax1[1, 2].legend(lines, labels)
    plt.title("Detector position 24 -25 60 cm")

    line13 = ax1[2, 0].plot(data_exp[6][:, 0], data_exp[6][:, 1], color="Blue", linestyle='-', marker="x",
                            label="Experimental")
    ax1[2, 0].set_xlabel("Radioactive source position (m)")
    ax1[2, 0].set_ylabel("Experimental (cps)", color='Blue')
    ax1[2, 0].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[2, 0].twinx()
    line14 = ax2.plot(data_sim.iloc[0], data_sim.iloc[16], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line13 + line14
    labels = [l.get_label() for l in lines]
    ax1[2, 0].legend(lines, labels)
    plt.title("Detector position 24 25 20 cm")

    line15 = ax1[2, 1].plot(data_exp[7][:, 0], data_exp[7][:, 1], color="Blue", linestyle='-', marker="x",
                            label="Experimental")
    ax1[2, 1].set_xlabel("Radioactive source position (m)")
    ax1[2, 1].set_ylabel("Experimental (cps)", color='Blue')
    ax1[2, 1].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[2, 1].twinx()
    line16 = ax2.plot(data_sim.iloc[0], data_sim.iloc[17], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line15 + line16
    labels = [l.get_label() for l in lines]
    ax1[2, 1].legend(lines, labels)
    plt.title("Detector position 0 25 40 cm")

    line17 = ax1[2, 2].plot(data_exp[8][:, 0], data_exp[8][:, 1], color="Blue", linestyle='-', marker="x",
                            label="Experimental")
    ax1[2, 2].set_xlabel("Radioactive source position (m)")
    ax1[2, 2].set_ylabel("Experimental (cps)", color='Blue')
    ax1[2, 2].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[2, 2].twinx()
    line18 = ax2.plot(data_sim.iloc[0], data_sim.iloc[18], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line17 + line18
    labels = [l.get_label() for l in lines]
    ax1[2, 2].legend(lines, labels)
    plt.title("Detector position 24 25 60 cm")
    return ax1

def draw_a(data_exp, data_sim):
    fig1, ax1 = plt.subplots(3, 3, figsize=(30, 18))

    line1 = ax1[0, 0].plot(data_exp[0][:, 0], data_exp[0][:, 1], color="Blue", linestyle='-', marker="x",
                           label="Experimental")
    ax1[0, 0].set_xlabel("Radioactive source position (m)")
    ax1[0, 0].set_ylabel("Experimental (cps)", color='Blue')
    ax1[0, 0].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[0, 0].twinx()
    line2 = ax2.plot(data_sim.iloc[0], data_sim.iloc[19], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1[0, 0].legend(lines, labels)
    plt.title("Detector position -24 0 20 cm")

    line3 = ax1[0, 1].plot(data_exp[1][:, 0], data_exp[1][:, 1], color="Blue", linestyle='-', marker="x",
                           label="Experimental")
    ax1[0, 1].set_xlabel("Radioactive source position (m)")
    ax1[0, 1].set_ylabel("Experimental (cps)", color='Blue')
    ax1[0, 1].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[0, 1].twinx()
    line4 = ax2.plot(data_sim.iloc[0], data_sim.iloc[20], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line3 + line4
    labels = [l.get_label() for l in lines]
    ax1[0, 1].legend(lines, labels)
    plt.title("Detector position -24 0 40 cm")

    line5 = ax1[0, 2].plot(data_exp[2][:, 0], data_exp[2][:, 1], color="Blue", linestyle='-', marker="x",
                           label="Experimental")
    ax1[0, 2].set_xlabel("Radioactive source position (m)")
    ax1[0, 2].set_ylabel("Experimental (cps)", color='Blue')
    ax1[0, 2].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[0, 2].twinx()
    line6 = ax2.plot(data_sim.iloc[0], data_sim.iloc[21], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line5 + line6
    labels = [l.get_label() for l in lines]
    ax1[0, 2].legend(lines, labels)
    plt.title("Detector position -24 0 60 cm")

    line7 = ax1[1, 0].plot(data_exp[3][:, 0], data_exp[3][:, 1], color="Blue", linestyle='-', marker="x",
                           label="Experimental")
    ax1[1, 0].set_xlabel("Radioactive source position (m)")
    ax1[1, 0].set_ylabel("Experimental (cps)", color='Blue')
    ax1[1, 0].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[1, 0].twinx()
    line8 = ax2.plot(data_sim.iloc[0], data_sim.iloc[22], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line7 + line8
    labels = [l.get_label() for l in lines]
    ax1[1, 0].legend(lines, labels)
    plt.title("Detector position -24 -25 20 cm")

    line9 = ax1[1, 1].plot(data_exp[4][:, 0], data_exp[4][:, 1], color="Blue", linestyle='-', marker="x",
                           label="Experimental")
    ax1[1, 1].set_xlabel("Radioactive source position (m)")
    ax1[1, 1].set_ylabel("Experimental (cps)", color='Blue')
    ax1[1, 1].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[1, 1].twinx()
    line10 = ax2.plot(data_sim.iloc[0], data_sim.iloc[23], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line9 + line10
    labels = [l.get_label() for l in lines]
    ax1[1, 1].legend(lines, labels)
    plt.title("Detector position -24 -25 40 cm")

    line11 = ax1[1, 2].plot(data_exp[5][:, 0], data_exp[5][:, 1], color="Blue", linestyle='-', marker="x",
                            label="Experimental")
    ax1[1, 2].set_xlabel("Radioactive source position (m)")
    ax1[1, 2].set_ylabel("Experimental (cps)", color='Blue')
    ax1[1, 2].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[1, 2].twinx()
    line12 = ax2.plot(data_sim.iloc[0], data_sim.iloc[24], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line11 + line12
    labels = [l.get_label() for l in lines]
    ax1[1, 2].legend(lines, labels)
    plt.title("Detector position -24 -25 60 cm")

    line13 = ax1[2, 0].plot(data_exp[6][:, 0], data_exp[6][:, 1], color="Blue", linestyle='-', marker="x",
                            label="Experimental")
    ax1[2, 0].set_xlabel("Radioactive source position (m)")
    ax1[2, 0].set_ylabel("Experimental (cps)", color='Blue')
    ax1[2, 0].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[2, 0].twinx()
    line14 = ax2.plot(data_sim.iloc[0], data_sim.iloc[25], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line13 + line14
    labels = [l.get_label() for l in lines]
    ax1[2, 0].legend(lines, labels)
    plt.title("Detector position -24 25 20 cm")

    line15 = ax1[2, 1].plot(data_exp[7][:, 0], data_exp[7][:, 1], color="Blue", linestyle='-', marker="x",
                            label="Experimental")
    ax1[2, 1].set_xlabel("Radioactive source position (m)")
    ax1[2, 1].set_ylabel("Experimental (cps)", color='Blue')
    ax1[2, 1].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[2, 1].twinx()
    line16 = ax2.plot(data_sim.iloc[0], data_sim.iloc[26], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line15 + line16
    labels = [l.get_label() for l in lines]
    ax1[2, 1].legend(lines, labels)
    plt.title("Detector position -24 25 40 cm")

    line17 = ax1[2, 2].plot(data_exp[8][:, 0], data_exp[8][:, 1], color="Blue", linestyle='-', marker="x",
                            label="Experimental")
    ax1[2, 2].set_xlabel("Radioactive source position (m)")
    ax1[2, 2].set_ylabel("Experimental (cps)", color='Blue')
    ax1[2, 2].tick_params(axis='y', labelcolor='Blue')
    ax2 = ax1[2, 2].twinx()
    line18 = ax2.plot(data_sim.iloc[0], data_sim.iloc[27], color="Red", linestyle='-', label="Simulated")
    ax2.set_ylabel("Simulated (cps)", color='Red')
    ax2.tick_params(axis='y', labelcolor='Red')
    lines = line17 + line18
    labels = [l.get_label() for l in lines]
    ax1[2, 2].legend(lines, labels)
    plt.title("Detector position -24 25 60 cm")
    return ax1

