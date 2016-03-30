#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Calculate P(r>0.5|X) and P(r<0.5|X) and compare

import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# Calculate complete pdf to obtain cdf
delta_r = 0.001  # Space between r values to integrate (sum)
r = np.arange(0, 1 + delta_r, delta_r)  # r range [0,1]
values = np.array([math.pow(x, 18) * math.pow((1 - x), 15) for x in r])  # Summing value (array)

# Determine denominator value with an integral
integral_1 = integrate.quad(lambda x: math.pow(x, 18) * math.pow((1 - x), 15), 0, 1.)[0] * (1 / delta_r)

# Calculate CDF up to r<0.5. It will be useful for P(r<0.5|X) and P(r>0.5|X) = 1 - P(r<0.5|X)
r_half = r = np.arange(0, 0.5 + delta_r, delta_r)  # r range [0,0.5]
values_half = np.array([math.pow(x, 18) * math.pow((1 - x), 15) for x in r_half])  # Summing value (array)

# Sum the array vaules = CDF(r<0.5)
cdf_half = np.sum((values_half / integral_1))

# Output CDF values
print('P(r>0.5|X) = %.3f' % (1 - cdf_half))
print('P(r<0.5|X) = %.3f' % cdf_half)
