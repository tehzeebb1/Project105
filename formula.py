import math
import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data=list(reader)

data = file_data[0]

#getting the mean

def mean(data):
    n= len(data)
    total =0
    for x in data:
        total += int(x)

    mean = total / n
    return mean

#Step 2. Subtract the mean from all the values and square them

# squaring and getting the values
squared_list= []
for number in data:
    a = int(number) - mean(data)
    a= a**2
    squared_list.append(a)

#Step 3 . Get the sum of all the elements from the squared list. 
sum =0
for i in squared_list:
    sum =sum + i

#Step 4 . Divide the sum by the number of values in the dataset.

#dividing the sum by the total values
result = sum/ (len(data)-1)

#step 5. get the square root of the result we got earlier from 

# getting the deviation by taking square root of the result
std_deviation = math.sqrt(result)
print(std_deviation)