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

# Set up a list to hold the Covid Data

testDataList = []

testDataList.append(CovidData("04012020", 1000, 45))
testDataList.append(CovidData("04022020", 2241, 155))
testDataList.append(CovidData("04032020", 1406, 75))
testDataList.append(CovidData("04042020", 1376, 62))
testDataList.append(CovidData("04052020", 845, 37))
testDataList.append(CovidData("04062020", 2949, 155))
testDataList.append(CovidData("04072020", 2176, 112))
testDataList.append(CovidData("04082020", 1863, 91))
testDataList.append(CovidData("04092020", 1777, 71))
testDataList.append(CovidData("04102020", 2341, 137))

# Function to determine length of list
def listlength(x):
    return len(x)

# Function to calculate average of list attribute
def average(x,y):
    return x/y

# Counts the number of items in the list
n = listlength(testDataList)
print("Number of data points -- ",n)

# Calculates the average daily postive tests for Oregon
total = 0
for i in range(n-1):
    total = total + testDataList[i].positivetests

totalpostests = average(total,n)
print("Total positive tests -- ", totalpostests)

#Calculates the average daily total tests in Oregon
total = 0
for i in range(n-1):
    total = total + testDataList[i].totaltests

totaltests = average(total,n)
print("Total tests -- ", totaltests)

# Calculates the indicated infection rate of persons tested

infectrate = totalpostests/totaltests
print("Indicated infection rate -- ", infectrate)


