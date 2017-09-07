# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Below is a comparision between *lists* and *tuples*:   

Characters | Lists | Tuples 
---------- | ----- | ------ 
Similarity | a sequence of values | a sequence of values / comma-sperated lists of values 
Similarity | values can be any type | values can be any type 
Similarity | indexed by integers | indexed by integers 
Use of operators | bracket operater indexes an element | bracket operater indexes an element 
Difference | mutable | immutable (cannot modify)
Format | l = ['a', 'b', 'c'] | t = 'a', 'b', 'c' or t = ('a', 'b', 'c')
Format - single element | l1 = ['a'] | t1 = 'a', 
Replacement | l[0] = 'A' | t = ('A',) + t[1:] 
Work as keys in dictionaries | no, only as values - will create different keys with same value if modified | yes, very commonly - each tuple can be a key-value pair 

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

Assuming 365 days a year, and 30 days a month, there are **_936_** days between start and stop date. While the actual days are **_937_** with no assumptions on the days in a year/month. 

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

Assuming 365 days a year, and 30 days a month, there are **_517_** days between start and stop date. While the actual days are **_513_** with no assumptions on the days in a year/month. 


c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

Assuming 365 days a year, and 30 days a month, there are **_7844_** days between start and stop date. While the actual days are **_7810_** with no assumptions on the days in a year/month. 

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





