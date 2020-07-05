import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
#wartości początkowe rozkładu zmiennej losowej
size = int(input('Add size N: '))
loc = float(input('Add location parametr: '))
scale = float(input('Add scale: '))
s = np.random.default_rng().laplace(loc, scale, size)
print(s)
count, bins, ignored = plt.hist(s, 100, density=True)
x = np.arange(-10., 10., 01.)
#pdf - probability distribution function
pdf = np.exp(-abs(x-loc)/scale)/(2.*scale)
plt.plot(x, pdf)
plt.show()
# wariancja
variance = 2*(scale**2)
print('Variance is: ', variance)
# wartość średnia
mean = loc
print('Mean is: ', mean)
#funkcja autokorelacji
a = np.arange(size)
y = np.array(s)
correlation = np.corrcoef(a,y)
print('Autocorrelation is: ',correlation)

#gęstość widmowa mocy
freqs, psd = signal.welch(correlation)

plt.figure(figsize=(5, 4))
plt.semilogx(freqs, psd)
plt.title('PSD: power spectral density')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.tight_layout()
plt.show()

