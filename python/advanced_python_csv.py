# Q5. 
# Write email addresses from Part I to csv file

import csv
with open('faculty.csv', 'r') as csvfile:
	facultyreader = csv.reader(csvfile)

	with open('emails.csv', 'w') as newfile: 
		emailwriter = csv.writer(newfile)

		for line in facultyreader:
				emailwriter.writerow([line[3]])
	
