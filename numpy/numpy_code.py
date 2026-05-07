import numpy as np

# a = np.array([1, 2, 3, 4, 5, 6])

# print(a.dtype)



# data = np.array([
#    [25, 50000],
#    [30, 60000],
#    [30, 60000],
#    [30, 60000],
#    [30, 60000],
#    [30, 60000],
#    [30, 60000],
#    [30, 60000],
#    [30, 60000],
#    [30, 60000],
#    [30, 60000],
#    [30, 60000],
#    [30, 60000],
#    [30, 60000],
#    [30, 60000],
# ])


# print(data.shape)


# print(data + [0, 1000])


# a = np.linspace(0, 1, 10)

# print(a)



# print(a[1:5])


# # data = np.array([
# #    [25, 50000, 30],
# #    [30, 60000, 90]
# # ])


# # print(data + [0, 100, 0])


# # values = np.array(
# #       [
# #          [1.9, 2, 3], 
# #          [3, 4, 4],
# #          [5, 6, 7]
# #       ]
# #    )


# values = np.array(
#       [
#          [1, 2, 3], 
#          [4, 5, 6],
#          [7, 8, 9]
#       ]
# )


# print(values[0][1])



# # name = 


# print(values.dtype)

# print(values + 1)



# print(np.zeros((2,3)))


# print(np.ones((3,7)))


# print(np.eye(20))


# print(np.arange(0,20,2))


# print(np.linspace(0,10,4))


# a = np.array([1,2,3])

# b = a[0]

# b[0] = 100

# print(a)



# num = [1, 2, 3]

# num2 = 1

# num2 = 100

# print(num)


# a = np.array([[1, 2, 3, 4, 5], [10, 20, 30, 40, 50]])

# print(np.sum(a))
# print(np.mean(a))
# print(np.max(a))
# print(np.min(a))


# a = np.arange(6)

# print(a)

# a = a.reshape(2,3)

# print(a)

# a = a.flatten()

# print(a)

# import numpy as np

# col3 = np.genfromtxt("../student-data.csv", delimiter=",", usecols=2)

# print(col3)


# a = np.array([1,2,3,9])
# b = np.array([4,5,6,7])

# print(a * 10)

# a = np.array([1, 2, 3, 4, 5])


# # for i in range(len(a)):
# #    a[i] = a[i] * 2
   
   
   
# a = a * 2
# print(a)




# a = np.array(
#             [
#                [1, 2, 3, 4, 5], 
#                [10, 20, 30, 40, 50],
#                [100, 200, 300, 400, 500]
               
#             ]
#             )


# print(a)

# b = a.flatten()

# print(b)



# print(np.sum(a))
# print(np.mean(a))
# print(np.max(a))
# print(np.min(a))



# b = np.array([1, 2, 3, 4, 5])


# print(a - b)


# a = np.arange(12)

# print(a)


# b = a.reshape(3,4)

# print(b)





# ages = np.genfromtxt("student-data.csv", delimiter=",", usecols=2)

# print(ages.max())


# a = np.linspace(0,12,4)

# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# print(a[0,1])


# a = np.array([1,2,3])
# print("a : ", a)
# b = a[0:2]
# print("b : ", b)
# b[0] = 100
# print("b after modification : ", b)
# print("a after modification : ", a)



a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = 1
print(a + b)