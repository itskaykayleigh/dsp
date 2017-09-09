

import csv
import re

def process_file(filename):
	hist = {}
	with open('faculty.csv', 'r') as csvfile:
		facultyreader = csv.reader(csvfile)
		
    next(facultyreader)  			

		for line in facultyreader:
			process_line(line, hist)
		return hist 

# Q2.  
# Find how many different titles there are, and their frequencies:  
# Ex:  Assistant Professor, Professor
def process_line(line, hist):
			line = line[2].replace('.', '')
			line = line.lower()
			re.split(' ', line)
			hist[line] = hist.get(line, 0) + 1 

hist = process_file('faculty.csv')		

def different_titles(hist):
	return len(hist)
print 'Number of different titles:', different_titles(hist)	
print hist 


# Q3. 
# Search for email addresses and put them in a list.  
# Print the list of email addresses.

import csv
with open('faculty.csv', 'r') as csvfile:
	facultyreader = csv.reader(csvfile)
	next(facultyreader)  	
	for line in facultyreader:
		emails = []
		emails.append(line[3])
		print emails

# Q4. 
# Find how many different email domains there are 
# (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  
# Print the list of unique email domains.

import csv

def process_file(filename):
	hist = {}
	with open('faculty.csv', 'r') as csvfile:
		facultyreader = csv.reader(csvfile)
# with open('degrees.csv', 'w') as newfile:
# 	degrees_writer = csv.writer(newfile, delimiter='\t')
		next(facultyreader)  			

		for line in facultyreader:
			name, domain = line[3].split('@')
			process_line(domain, hist)
		return hist 

def process_line(domain, hist):
			hist[domain] = hist.get(domain, 0) + 1 

hist = process_file('faculty.csv')		

def different_domain(hist):
	return len(hist)
print 'Number of different domain:', different_domain(hist)	
print hist 
h = list(hist)
print h 

# Number of different domain: 4
# {'email.chop.edu': 1, 'upenn.edu': 12, 'cceb.med.upenn.edu': 1, 'mail.med.upenn.edu': 23}
# ['email.chop.edu', 'upenn.edu', 'cceb.med.upenn.edu', 'mail.med.upenn.edu']
