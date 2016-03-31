#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Plot P(r) in [0,1] and in R - [0,1]

import numpy as np
import matplotlib.pyplot as plt

# Create intervals
delta_r = 0.001
r = np.arange(-0.5, 1.5, delta_r)
prob = [1 if (0 <= i) and (i <= 1) else 0 for i in r]

plt.plot(r, prob)
#plt.xlim(r[0], r[-1])
plt.xlabel('r')
plt.ylim(-0.01, 1.1)
plt.ylabel('$\mathbb{P}(r)$')
# plt.savefig('T1_p2_c_pr.pdf')
plt.show()
