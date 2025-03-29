menu = {
    'sandwich':50,
    'samosa':40,
    'nimco':80,
    'tea':50,
    'jalebi':150,
}

print("Welcome to Lal Qila")
print("sandwich: Rs 50\nsamosa: Rs 40\nnimco: Rs 80\ntea: Rs 50\njalebi: Rs 150")

order_total = 0

item_1 = input("enter the name of your item = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"ordered item{item_1} is not available yet!")

another_order = input("do you want to add another item? (yes/no) ")
if another_order == "yes":
    item_2 = input("enter the name of your second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your item {item_2} has been added to your order")
    else:
        print(f"ordered item{item_2} is not available!")

print(f"the total amount of your order is {order_total}")
