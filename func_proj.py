def emoji_converter(cut):
    # sourcery skip: use-fstring-for-concatenation, use-join
    bucket = cut.split(" ")
    emoji = {
        ":)" : ":(",
        ":}" : ":3"
    }
    result = ""
    for words in bucket:
        result += emoji.get(words, words) + "  "
    print(result)
box = input("enter the text with an emoji! ")
emoji_converter(box)