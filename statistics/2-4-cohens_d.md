[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

*Exercise 4   Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen’s d to  # quantify the difference between the groups. How does it compare to the difference in pregnancy length?*


1. Whether lighter or heavier - compute mean of each group  
firsts.totalwgt_lb.mean(), others.totalwgt_lb.mean()   
7.201094430437772, 7.325855614973262  
This indicates first babies are slightly lighter than others.  

So in order to find the difference between the groupss, we'd use the CohenEffectSize function to compute the difference in means expressed in number of standard deviations:

def CohenEffectSize(group1, group2):  
    diff = group1.mean() - group2.mean() .  

    var1 = group1.var()  
    var2 = group2.var()   
    n1, n2 = len(group1), len(group2)  

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)   
    d = diff / math.sqrt(pooled_var)   
    return d  
    
CohenEffectiveSize(firsts.totalwgt_lb, others.totalwgt_lb)   
-0.088672927072602006  
This means the difference in means is -0.0887, which is bigger than that of pregnancy length (0.029). 
