# e-RTP Calibration and Data Analysis


This repository contains the GEANT4 applications built, experimental data, and jupyter notebooks employed for the data analysis.

**Table of Contents**
* **Cal-Exp-Data folder**: has the data for detector calibration.

* **G4-Only-Det folder**: has the GEANT4 application just for one detector without the RPT system.

* **G4-RPT folder**: has the GEANT4 application with detector and macrocommands to move it.

* **RPT-Exp-data folder**: has experimental data acquired.

* **RPT-macros folder** has the macrofiles generated for GEANT4 simulations.

* **RPT-sim-data folder** has the results from the GEANT4 simulation.

* **RPT_1D_data_analysis.ipynb** is the data treatment, data analisis, and data visualization of the results.

* **utils.py y utils2.py** are functions and classes to modularize the jupyter notebooks.
### Data 

----
- The experimental data come from several experiments done in the Nuclear Science Department at Escuela Politécnica Nacional, Quito - Ecuador.
- The simulated data come from simulations run on a linux server. Thanks to Corporación Ecuatoriana para el Desarrollo de la Investigación y la Academia (CEDIA) for giving us access to your cluster.
### e-RPT 
---
**1. What is e-RPT?**
Ecuadorian Radioactive Particle Tracking (e-RPT) is an attempt to do the Radioactive Particle Tracking (RPT) technique in Ecuador. 

**2. What is only RPT?**
The RPT is a nuclear technique to tracking radioactive particles and reconstruct the path of those particles. 

An example of the RPT system is ilustrated in the following picture.

![descarga](https://user-images.githubusercontent.com/82113558/189548912-ea04f459-0735-480d-9715-e71046b4bbd3.png)


Picture obtained from:  Mohd Amirul Syafiq Mohd Yunos et al 2019 IOP Conf. Ser.: Mater. Sci. Eng. 554 012005


**3. What is radiation detector calibration?**
The calibration of the radiation detector is process to measure how many particles are effectively registered by a radiation detector, and this is done by the Full Energy Peak Efficiency (FEPE). The FEPE was done for static source, and then used for scaled the simulated data. 

$$ FEPE = \frac{AP}{E*P} $$

Where:
- AP: is the area of a photopeak for a energy window
- E: is the activity of the radioactive source
- P: is the probability of the emission
                
### FlowChart of the Data Treatment
---
```flow
st=>start: Data Acquisition for static sources
experimentally and from the GEANT4 simulation
op=>operation: FEPE calibration for experimental data
and simulated data
cond=>condition: Static Calibration 
Successfull Yes or No
op2=>operation: Data acquisition experimentally 
and from the simulation for the RPT system
e2=>end: Start again all the process
e=>end: Particle position reconstruction

st->op->cond->op2->e
cond(no)->
cond(yes)->op2
```
