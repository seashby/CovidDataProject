# This is a program that performs a variety of
# analysis procedures on Covid-19 data generated
# by the Oregon Health Authority.


# Create a class for Covid Data Points
class CovidData:
    def __init__(self, date, tests, positives):
        self.testdate = date
        self.totaltests = tests
        self.positivetests = positives
        print("Data Point Created")

    def __str__(self):
        return "Test Date = %s, Tests performed = %d, Positive Tests = %d" %(self.testdate, self.totaltests,
        self.positivetests)

# Read the data from a CSV file and store
# it in a list for analysis

# Declare Lists and variables to hold data

testDataList = []
templist = []
#read_data = " "

# Opens the data file

f = open('DataFile.csv')

# Loops through the data file and reads it line by line
# and then splits the line into three variables and loads
# them as CovidData objects into the testDataList

for read_data in f:
    #read_data = f.readline()
    read_data = read_data.strip()
    templist = read_data.split(',')
    testDataList.append(CovidData(templist[0], int(templist[1]), int(templist[2])))

# Close the CSV data file

f.close


# Function to determine length of list
def listlength(x):
    return len(x)

# Function to calculate average of list attribute
def average(x,y):
    return x/y

# Counts the number of items in the list
n = listlength(testDataList)
print("Number of data points -- ",n)

# Calculates the average daily positive tests for Oregon
total = 0
for i in range(n-1):
    total = total + testDataList[i].positivetests

totalpostests = average(total,n)
print("Average daily positive tests -- ", totalpostests)

#Calculates the average daily total tests in Oregon
total = 0
for i in range(n-1):
    total = total + testDataList[i].totaltests

totaltests = average(total,n)
print("Average daily tests -- ", totaltests)

# Calculates the indicated infection rate of persons tested

infectrate = totalpostests/totaltests
print("Indicated infection rate -- ", infectrate)


