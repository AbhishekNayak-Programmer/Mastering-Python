import numpy as np

# Getting the version of numpy
print(np.__version__) 

# Single Dimensional Array
arr = np.array([1,2,3,4])
print(arr)
print(type(arr))
print(arr * 2)


# Multi Dimensional Array
multi_arr = np.array([['A', 'B', 'C'], ['E', 'F', 'G'], ['H', 'I', 'J']])
print(multi_arr.ndim) # To find out how many nesting list are there
print(multi_arr.shape)

# Accessing elements using numpy
print(multi_arr[1][1])
print(multi_arr[1,1])
# print(multi_arr[1][1][1]) # gives error as unable to find

# String concatenation using numpy
word = multi_arr[0,0] + multi_arr[0,1] + multi_arr[2][0] + multi_arr[2][1]
print(word)


# slicing in array
arr = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
# syntax = array[start:end:step]

# Working with rows
print("Selecting first 3 rows")
print(arr[0:3])
print("Selecting rows from 2nd to end")
print(arr[2:4])

print("Select based on step")
print(arr[0:4:2]) # Getting all even rows
print(arr[::-2]) # Getting all even rows from end as starting

# Working with columns
# Accessing colums in matrix
print(arr[:,0])
print(arr[:,1])
print(arr[:,3])
print(arr[:,-1])

# Creating a matrix from 0 to 3 column with all values
print(arr[:, 0:3])
print(arr[:, 1:])
print(arr[:, ::2]) # based on step
print(arr[:, 1::2]) # based on step but skip first column

# Scalar Arithmetic
array = np.array([1,2,3])
print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5)

# Vectorized Math Funcs
array = np.array([1.1234,2.34,3.99])
print(np.sqrt(array))
print(np.round(array))
print(np.pi)

# Area of a circle for all the circles radii
radii = np.array([1, 2, 3])
print(np.pi * radii ** 2)


# array arithmetic
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)

# comparision using Numpy array
scores = np.array([91,55,100,73,82,64])
print(scores == 100)
print(scores < 60)
print(scores > 60)

# checking the index which have scores less than 60 we will make that score as 0
scores[scores < 60] = 0
print(scores)

# broadcasting
array1 = np.array([[1,2,3,4]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape)
print(array2.shape)

print(array1  * array2)

# Aggregate Functions
arr = np.array([[1,2,3,4], [5,6,7,8]])
print(np.sum(arr))
print(np.mean(arr))
print(np.std(arr))
print(np.var(arr))
print(np.min(arr))
print(np.argmin(arr)) # get the index of min number in arr
print(np.argmax(arr)) # get the index of max number in arr

print(np.sum(arr, axis=0)) # Sum of all the columns
print(np.sum(arr, axis=1)) # Sum of all the rows


# Filtering in Numpy
ages = np.array([[21,17,19,20,16,30,18,65], [39,22,15,99,18,19,20,21]])
teenagers = ages[ages < 18]
print(teenagers)

adults = ages[(ages >= 18) & (ages <= 60)]
print(adults)

seniors = ages[ages > 60]
print(seniors)

even_ages = ages[ages % 2 == 0]
odd_ages = ages[ages % 2 != 0]
print(even_ages, odd_ages)

adults = np.where(ages >= 18, ages, 0) # condition, array, fill which are false values
print(adults)

# Generating Random numbers using Numpy
rng = np.random.default_rng()
print(rng.integers(1, 7))
print(rng.integers(low=1, high=101, size=3))
print(rng.integers(low=1, high=101, size=(3,3)))

print(np.random.uniform(low=-1, high=1))
print(np.random.uniform(low=-1, high=1, size=3))
print(np.random.uniform(low=-1, high=1, size=(3,2)))


# Shuffle the array using Numpy
rng = np.random.default_rng()
array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

fruits = np.array(["apple", "mango", 'banana', 'orange', "pineapple", "cocount"])
fruit = rng.choice(fruits) # Selecting random choice
print(fruit)
fruitArr = rng.choice(fruits, size=3) # Selecting random choice for size defined
print(fruitArr)
fruitMatrix = rng.choice(fruits, size=(3,2)) # Selecting random choice for size defined
print(fruitMatrix)