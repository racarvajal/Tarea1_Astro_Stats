#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Simulation of 1000 surveys of Monty Hall Problem.
# It produces results for each survey and a histogram
# Each survey results behave as a Binomial(N,X) distribution

import numpy as np
import matplotlib.pyplot as plt

N = 33  # Number of questioned people per survey
p = 0.5  # Probability of staying with initial choice (door)
x = np.arange(0, 1000)  # Number of surveys
prob = [np.random.binomial(N, p) for value in x]  # Probability in each survey

# Histogram plot
num_bins = 16  # Number of bins. In this case, arbitrary number
n, bins, patches = plt.hist(prob, num_bins, histtype='step')
plt.xlabel('Number of staying people')
plt.ylabel('Number of surveys')
# plt.savefig('hist_binom_X18.pdf')
plt.show()
