#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Integrator to obtain denominator value in P(r|x) via Bayes Theorem
# Test if P(r|x) is normalized
# Graph P(r|x) and look for maximum value
# Calculate and graph CDF from P(r|x)

import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.integrate as integrate

delta_r = 0.001  # Space between r values to integrate (sum)
r = np.arange(0, 1 + delta_r, delta_r)  # r range [0,1]
values = np.array([math.pow(x, 18) * math.pow((1 - x), 15) for x in r])  # Summing value (array)

# Determine denominator value with an integral
integral_1 = integrate.quad(lambda x: math.pow(x, 18) * math.pow((1 - x), 15), 0, 1.)[0] * (1 / delta_r)

# Test the distribution sums up to 1
print('Distribution sum is: %.3f' % sum(values/(integral_1)))

# Plot P(r|x)
plt.plot(r, (values / (integral_1)))
plt.xlabel('r')
plt.ylabel('$f_{x}$(r)')
# plt.savefig('T1_p2_c_pdf.pdf')
plt.show()

# Look for maximum value in P(r|x)
max_r = r[np.argmax((values / (integral_1)))]
print('Maximum value of r is: %.3f' % max_r)

# Plot CDF
plt.plot(r, np.cumsum((values / (integral_1))))  # equivalent to P(r<r)
plt.xlabel('r')
plt.ylabel('CDF')
# plt.savefig('T1_p2_c_cdf.pdf')
plt.show()
