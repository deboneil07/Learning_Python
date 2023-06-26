numb = {
    "1" : "one",
    "2" : "two"
}

phone = input("phone: ")
output = " "
for i in phone:
    output += numb.get(i, "?") + " "
print(output)    
