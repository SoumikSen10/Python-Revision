# List uniqueness checker

items = ["apple","banana","orange","apple","mango"]

unique_item = set()

for str in items :
    if str in unique_item:
        print("Duplicate : ",str)
        break
    else:
        unique_item.add(str)
        