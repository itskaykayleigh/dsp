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

Both list and set contain a sequence of items. Lists are ordered, while sets are not. Ses require items to be hashable, lists don't, so if some elements are non-hasable, cannot use sets. Sets forbid duplicates, lists do not. And due to this feature, sets are usually used to build sequence of unique items.   

a = set([1, 2, 3, 4])  
b = set([3, 4, 5, 6])  
a | b # Union  
{1, 2, 3, 4, 5, 6}  

a = [1,2,3,4]  
b = [3,4,5,6]  
a + b  
[1,2,3,4,3,4,5,6]   

market = ['apples', 'oranges', 'apples', 'bananas', 'pears', 'tomatos']  
And to create a collection with only unique fruits in the market   
fruits = set(market)  
'orange' in fruits    
True   
Fast membership testing   

In terms of finding an element (as in x in s), sets are significantly faster, especially for large sets. This is because sets use a hash function to map to a bucket. Whenever we add an object to a set, the position within the memory of the set object is determined using the hash of the object to be added. When testing for membership, all that needs to be done is basically to look if the object is at the position determined by its hash, so the speed of this operation does not depend on the size of the set. In contrast, Python has to compare every single member for equality to find out existance of an item in a list, i.e. the test is O(n).

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Python enables the creation of anonymous functions, which is functions defined without a name, using a keyword called `lambda`, instead of _def_. And a lambda function has the below syntax, with any number of arguments but only one expression. Expression is to be evaluated and returned. `lambda` function is used mostly for a short period of time, or as an argument to a higher-order function. 

lambda arguments: expression

Program to show the use of lambda functions

double = lambda x: x * 2  
print(double(5))  

mylist = [3,6,3,2,4,8,23]  
sorted(mylist, key=lambda x: x%2==0)  
[3, 3, 23, 6, 2, 4, 8]  
So what the function does is it specifies the key as a lambda function, which returns an even number. And sorted will sort mylist once based on the key specified. And since True = 1, False = 0 in boolean expression, odd number comes in first. 

mylist = [(3, 10, 8), (6, 2, 8), ( 2, 6, 4), (6, 8, 5)]  
sorted(mylist, key=lambda x: x[1])  
[(6, 2, 8), (2, 6, 4), (6, 8, 5), (3, 10, 8)]  
And below is the rationale behind the result we get:   
The sorted methods is to sort the list named mylist. While the key argument specifies that, for each element (x) in mylist, return index 1 of that element, then sort all of the elements of the original list 'mylist' by the sorted order of the list calculated by the lambda function. Result from the lamda function is (2, 6, 8, 5), which will be the order each tuple is placed in the final list after sorted(). 

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





