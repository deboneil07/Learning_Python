container = input("Enter a line of text:  ")
splitter = container.split(' ')

emoji = {":)" : "😄",
         ":(" : "😔"}


output = " "
for words in splitter:
    output += emoji.get(words, words) + ' '
    
print(output)

