# How to copy a list in python 


li = [1,2,3,4,5,6]


copy_li = li.copy() # copy the list

# copy_li = li // reference only
#  that a different copy vs refference

li[0] = 0
print(copy_li)

