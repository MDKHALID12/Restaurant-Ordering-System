menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Coffee':70,
    'cold coffee':80,
    'salad':90,
    'sandwich':100
}

print("Welcome to Sahara Restuarant")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nCoffee: Rs70\ncold coffee: Rs80\nsalad: Rs90\nsandwich: Rs100")
order_total = 0
item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"ordered item {item_1} is not available yet!")
another_order = input("Do you want to add another item?(YES/NO)")
if another_order == "YES":
    item_2 = input("Enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"ordered item {item_2} is not available!")
# another_order1 = input("Do you want to one more item?(YES/NO)")
# if another_order1 == "YES":
#     item_3 = input("Enter the name of third item =")
#     if item_3 in menu:
#         order_total += menu[item_3]
#         print(f"item {item_3} has been added to order")
#     else:
#         print(f"ordered item {item_3} is not available!")
print(f"The total amount of item to pay is {order_total}")
print(" Thank You for visiting Sahara Restaurant!")

