note = [2,4,5,4,2,6,7]
box = []
for numbers in note:
    if numbers not in box:
        box.append(numbers)   
print(box)        