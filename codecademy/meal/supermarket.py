shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


# Write your code below!
def compute_bill(food):
    total = 0
    for item in food:
        for s in stock:
            if item == s and stock[s] > 0:
                for k in prices:
                    if item == k:
                        total = total + prices[k]
                        stock[s] -= 1

    return total

print(compute_bill(shopping_list))
