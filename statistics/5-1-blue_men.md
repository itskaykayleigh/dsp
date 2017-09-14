[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

*Exercise 1   In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women.
In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf. YOUR RESPONSE*

import scipy.stats  

male1 = (5*12+10)*2.54  
male2 = (6*12 + 1)*2.54 

lowerrange = scipy.stats.norm.cdf(male1, 178, 7.7)
upperrange = scipy.stats.norm.cdf(male2, 178, 7.7)  

Diff = upperrange - lowerrange 

