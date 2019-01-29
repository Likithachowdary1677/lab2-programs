import matplotlib.pyplot as plot

import numpy as npy

sf=10000    #sampling fequency

s1f=200      #signal 1 frequency

s2f=100     #signal2 frequency

n=200      #no.of samples
z=npy.arange(n)

r=npy.cos(2*npy.pi*s1f/sf*z)

plot.subplot(311)

plot.plot(z,r)

s=npy.cos(2*npy.pi*s2f/sf*z)

plot.subplot(312)

plot.plot(z,s)

c=r+s
plot.subplot(313)
plot.plot(z,c)

plot.title('addition of two sinusoids')

plot.xlabel('samples(n)')

plot.ylabel('amplitude(v)')

plot.show( )

