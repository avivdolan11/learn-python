bubble_tea = [
    ["Honeydew", "Mango", "Passionfruit"],
    ["Peach", "Plum", "Strawberry", "Taro"],
    ["Kiwi", "Chocolate"]
]

print(len(bubble_tea))
print(bubble_tea)

print(bubble_tea[1])
print(bubble_tea[-1])

print(len(bubble_tea[-1]))

print(bubble_tea[1][2])
print(bubble_tea[0][0])
print(bubble_tea[2][1])

all_flavours = []

for flavour in bubble_tea:
    for flav in flavour:
        all_flavours.append(flav)


print(all_flavours)


def nested_sum(list_nums):
    total = 0
    for nums in list_nums:
        for num in nums:
            total = total + num
    
    return total 


def fancy_concatenate(strings_list):
    final_string = ""
    for strings in strings_list:
        if len(strings) == 3:
            for string in strings:
                final_string = final_string + string
    
    return final_string

print(fancy_concatenate([["A", "C"], ["D","E","F"]]))