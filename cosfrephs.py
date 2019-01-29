import matplotlib.pyplot as plot

import numpy as npy

sf=10000    #sampling fequency

s1f=200     #signal 1 frequency

s2f=100     #signal2 frequency

n=200      #no.of samples
z=npy.arange(n)

r=npy.cos(2*npy.pi*s1f/sf*z)

plot.subplot(211)

plot.plot(z,r)

s=npy.cos(2*npy.pi*s2f/sf*z+90)

plot.subplot(212)

plot.plot(z,s)

plot.xlabel('samples(n)')

plot.ylabel('amplitude(v)')

plot.show( )
