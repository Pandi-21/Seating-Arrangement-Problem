# Problem:
# Check if a customer's order can be fully, partially, or not fulfilled based on inventory and budget.

# solution:
# - For each item, check available quantity and price.
# - Try to buy as much as possible within the budget.
# - After checking all items, decide if fully, partially, or not fulfillable.

def fulfill_order_system(inventory, order, budget):
    cost = 0
    items_purchased = {}
    
    for item in order:
        if item in inventory:
            price = inventory[item]['price']
            available = inventory[item]['quantity']
            need = order[item]
            
            buy = min(available, need, budget // price)
            cost_ = buy * price
            budget -= cost_
            cost += cost_
            
            if buy > 0:
                items_purchased[item] = buy

    # Check status
    if all(order[item] == items_purchased.get(item, 0) for item in order):
        print("Order  is completed fully  fulfilled.")
    elif items_purchased:
        print("Order is overall partially fulfilled.")
    else:
        print("Order cannot be fulfilled.")

    # Print details
    print("Items brings:", items_purchased)
    print("Total cost:", cost)
    print("Remaining budget:", budget)
 
inventory = {
    'apple': {'quantity': 20, 'price':10},
    'starberry': {'quantity': 25, 'price': 29},
    'orange': {'quantity': 58, 'price': 13}
}

order = {
    'apple': 14,
    'starberry':15,
    'orange': 15
}

budget = 1000

fulfill_order_system(inventory, order, budget)
