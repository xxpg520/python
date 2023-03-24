my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0
new_my_list1 = []
while index < len(my_list):
    element = my_list[index]
    if element % 2 == 0:
        new_my_list1.append(element)
    index += 1
print(new_my_list1)

new_my_list2 = []
for element in my_list:
    if element % 2 == 0:
        new_my_list2.append(element)
print(new_my_list2)
