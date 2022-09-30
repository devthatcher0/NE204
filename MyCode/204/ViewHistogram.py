import numpy as np
import matplotlib.pyplot as plt

filelocation = input("Enter spectra location: ")
filelocation = filelocation.strip('"')
spectra = np.load(filelocation)
filelocation = input("Enter spectra2 location: ")
filelocation = filelocation.strip('"')
spectra2 = np.load(filelocation)
ratio = float(np.amax(spectra2))/float(np.amax(spectra))
spectraratio = []
for a in range(np.size(spectra)):
    spectraratio.append(spectra2[a]/spectra[a])
ratio = np.average(spectraratio)
for a in range(np.size(spectra)):
    spectra[a]=ratio*spectra[a]
resolution = int(np.amax(spectra)/20)
plt.hist(spectra, bins=resolution, histtype='step', label='raw_data max pulse height')
plt.hist(spectra2, bins=resolution, histtype='step', label='after trapezoidal filter + pole zero correction')
plt.xlim(0)
plt.legend(loc='upper left')
plt.show()
