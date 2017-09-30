import os
import filecmp
import datetime


def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#open file
	f = open(file, "r")
	#create list of headers from first row of csv file
	headers = str(f.readline()).strip("\n").split(",")
	l = []
	for row in f:
		rowdata = str(row.strip("\n")).split(",")
		d = {}
		i = 0
		for data in rowdata:
			d[headers[i]] = data
			i += 1
		l.append(d)
	return l





#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	newdata = sorted(data, key = lambda k:k[col])
	s = newdata[0]["First"]
	s = s + " " + newdata[0]["Last"]
	return s

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	classdict = dict()
	for student in data:
		classdict[student['Class']] = classdict.get(student['Class'], 0) + 1
	classlist = classdict.items()
	classlist = sorted(classlist, key = lambda k: k[1], reverse = True)
	return classlist

# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	days = dict()
	for student in a:
		bday = str(student['DOB'])
		bdays = bday.split('/')
		days[bdays[1]] = days.get(bdays[1], 0) + 1
	sorteddays = sorted(days.items(), key = lambda k: k[1], reverse = True)
	return int(sorteddays[0][0])


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest 
# integer.  You will need to work with the DOB to find their current age.
	total = 0
	num = 0
	for student in a:
		bdate = student['DOB'].split('/')
		born = datetime.date(int(bdate[2]), int(bdate[0]), int(bdate[1]))
		today = datetime.date.today()
		age = today.year - born.year 
		if (today.month < born.month) or (today.month == born.month and today.day < born.day): age -= 1
		if born.year > today.year: age = 0
		total += age
		num += 1
	avgage = round(total / num)
	return int(avgage)

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	newdata = sorted(a, key = lambda k:k[col])
	f = open(fileName, "w")
	for entry in newdata:
		f.write(entry['First'])
		f.write(",")
		f.write(entry['Last'])
		f.write(",")
		f.write(entry['Email'])
		f.write(",\n")
	f.close()
	return f


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)
	'''
	HANNAH TEST DATA START
	
	data3 = getData('206_p1_test.csv')
	findAge(data3),
	
	HANNAH TEST DATA END
	'''
	
	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

