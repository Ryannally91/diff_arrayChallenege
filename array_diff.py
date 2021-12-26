# def array_diff(a, b):
#     for i in b:
#         for j in a:
#             if j == i:
#                 a.remove(i)
#             print(a)
#     return a

# array_diff([3,4,4,5], [3,5,7,7,7,4])


# def dif_array(a,b):
#     for i in b:
#         if i in a:
#             a.remove(i)
#         print(a)
#     return a

# dif_array([3,3,3,3,3], [3])

#The above functions did not work because when you remove 
# items from a list the index of each number changes, so it effectively skips it

def array_diff(a,b):
    newList=[]
    for i in a:
        if i not in b:
            newList.append(i)
    print(newList)
    return newList

array_diff([3,3,3,3,3, 1], [3, 2])
