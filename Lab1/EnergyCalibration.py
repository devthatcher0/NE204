import numpy as np
from scipy.signal import find_peaks, peak_widths
import matplotlib.pyplot as plt
from datetime import datetime

while True:
    isotope = input("Enter name of isotope: ")
    if isotope == '':
        break
    hist = []
    peaklocations2 = []
    peakheights = []
    energylist = []
    while True:
        try:
            filelocation = input("Copy & paste calibration isotope .npy file path: ").strip('"')
            spectra = np.load(filelocation)
            hist, bins = np.histogram(spectra, bins = 5000, range = (0, 1000))
            peaklocations, _ = find_peaks(hist, distance = 10, prominence = int(np.amax(hist))/5)
            FWHM = peak_widths(hist, peaklocations, rel_height = 0.5)
            for x in range(np.size(peaklocations)):
                print('Channel: ' + str(peaklocations[x]) + ' | ' + str(hist[int(peaklocations[x])]) + ' counts | ' + str(FWHM[0][x]) + ' FWHM')
                peaklocations2.append(peaklocations[x])
                peakheights.append(hist[int(peaklocations[x])])
            np_peaklocations2 = np.array(peaklocations2, dtype = int)   
            peakheights.sort(reverse=True)
            plt.plot(hist, label=filelocation)
            plt.plot(np_peaklocations2, hist[np_peaklocations2], "vk")
            plt.xlabel('Channel')
            plt.ylabel('Counts')
            plt.xlim(0)
            plt.legend(loc='upper right')
            plt.show()
            break
        except:
            print("Cannot load file")
    while True:
        try:
            energy = input("Enter energies one by one (in keV) of the tallest peaks indicated (press enter when done): ")
            energylist.append(float(energy))
        except:
            if energy == '':
                break
            else:
                print('Not a valid energy')
    energylist.sort()
    peakheights2 = peakheights[:len(energylist)]
    with open('calibrationdata.txt', 'a') as f:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write('\n' + isotope  + '\n' + dt_string + '\n')
        x = 0
        for y in range(np.size(peaklocations2)):
            if hist[int(peaklocations2[y])] in peakheights2:
                f.write(str(peaklocations2[y]) + ' ' + str(energylist[x]) + '\n')
                x += 1
            else:
                pass