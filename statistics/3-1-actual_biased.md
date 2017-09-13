[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

*Exercise 1   Something like the class size paradox appears if you survey children and ask how many children are in their family. Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample.
Use the NSFG respondent variable NUMKDHH to construct the actual distribution for the number of children under 18 in the household.
Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household.*

*Plot the actual and biased distributions, and compute their means. As a starting place, you can use chap03ex.ipynb.*

import nsfg   
import first  
import thinkstats2  
import thinkplot  

1. First read the file as resp  
resp = nsfg.ReadFemResp()  

2. Actual distribution for the number of childern under 18 in a household:   
actual = resp.numkdhh  
pmf = thinkstats2.Pmf(actual, label='numkdhh')  

3. Biased ditribution if asked childern under 18:   
def BiasPmf(pmf, label):  
    new_pmf = pmf.Copy(label=label)  

    for x, p in pmf.Items():  
        new_pmf.Mult(x, x)  
        
    new_pmf.Normalize()  
    return new_pmf  
  
4. Plot the actual and biased distributions   

biased_pmf = BiasPmf(pmf, label='biased')  
thinkplot.PrePlot(2)  
thinkplot.Pmfs([pmf, biased_pmf])  
thinkplot.Config(xlabel='Children Under 18', ylabel='PMF')  

print('Actual mean of children under 18', pmf.Mean())  
print('Biased mean of children under 18', biased_pmf.Mean())  
