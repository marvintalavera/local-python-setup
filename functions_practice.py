def hello():
    print("Hello User")

def pack(item1,item2,item3):
    return([
        item1,
        item2,
        item3
    ])

def eat_lunch(lunch_items):
    if not lunch_items:
        print("My lunchbox is empty!")
    else:
        print("First I eat", lunch_items[0])
        for item in lunch_items[1:]:
            print("Next I eat", item)

hello()
print(pack("item1","item2","item3"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])