# my_list=[[[1,2,3],4,5],[7,5,6,],6,7]
# def flatten(nested_list):
#     flat_list=[]
#     for item in nested_list:
#         if isinstance(item,list):
#             flat_list.extend(flatten(item))
#         else:
#             flat_list.append(item)
#     return flat_list


# myfl=flatten(my_list)
# print(myfl)

# l1=[1,2,3]
# l2=[4,5,6]
# print(list(zip(l1,l2)))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

[for row in matrix for col in matrix]