# Q1. Maximum of two numbers in python?

# li = [2,3,4,5,1,6]

# li.sort()

# print(f'maximum number is = {li[5]}')



# Q2. Reversing a list in python without sort and reverse method 

# li = [2,3,4,5,1,6]


# for x in range(len(li)):
#     for j in range(len(li)):
#         if li[x] > li[j]:
#             temp = li[x]
#             li[x] = li[j]
#             li[j] = temp
# print(li)





# Q3. Swap Two elements 
# example 
# a = 10 
# b = 20 
# print(a) # 20
# print(b) # 10

# c = a
# a = b
# b = c
# print(f'a swaping value is {a}')
# print(f'b swaping value is {b}')


# Q4. python program write to find sum and average in list 
# li = [1,2,3,4,5,6]

# sum = 0

# for x in li:
#     sum +=x

# avg = sum/len(li)
# print(f'list sum is {sum}')
# print(f'list average is {avg}')


# Q5. write the code find a list even number and odd number 
# example
li = [1,2,3,4,5,6,7,8,9,10]


for x in li:
    if x%2 == 0:
        print(f'even number is {x}')
    else:
        print(f'odd number is {x}')
# result = odd  1,3,5,7,9
# even 2,4,6,8,10