def bubble(list):
    for x in range(len(list) - 1):
        for y in range(len(list) - 1 - x):
            if list[y] > list[y+1]:
                list[y], list[y+1] = list[y+1], list[y]
    return list


        
print(bubble(list = [3, 22, 77, 5, 12, 15]))

