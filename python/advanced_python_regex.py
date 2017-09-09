

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
