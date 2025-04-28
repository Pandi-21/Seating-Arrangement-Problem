# Problem:
# Calculate the electricity bill based on usage (in kWh) and apply the given slabs.
# The user will input the electricity usage, and the program will calculate the bill
# explaining charges for each slab.

# solution:
# - Take the electricity usage as input.
# - Calculate the cost based on the usage slabs.
# - Display charges for each slab and the total bill.

def bills(use):
    amount = 0
    slab1_cost = slab2_cost = slab3_cost = slab4_cost = 0

    # Slab 1: 0-100 kWh at ₹5/unit
    if use <= 100:
        slab1 = use* 5
        amount += slab1_cost
        print(f"0-100 units @ 5/unit = {slab1} ₹")
    else:
        slab1 = 100 * 5
        amount += slab1
        print(f"0-100 units @ 5/unit = {slab1} ₹")
        use -= 100

        # Slab 2: 101-300 kWh at ₹7/unit
        if use <= 200:
            slab2= use * 7
            amount += slab2
            print(f"101-300 units @ 7/unit = {slab2} ₹")
        else:
            slab2 = 200 * 7
            amount += slab2
            print(f"101-300 units @ 7/unit = {slab2} ₹")
            use -= 200

        # Slab 3: 301-500 kWh at ₹10/unit
            if use <= 200:
                slab3 = use * 10
                amount += slab3
                print(f"301-500 units @ 10/unit = {slab3} ₹")
            else:
                slab3 = 200 * 10
                amount += slab3
                print(f"301-500 units @ 10/unit = {slab3} ₹")
                use -= 200

                # Slab 4: Above 500 kWh at ₹15/unit
                slab4 = use * 15
                amount += slab4
                print(f"Above 500 units @ 15/unit = {slab4} ₹")

    print(f"Total Amount Payes = {amount} ₹")

 
we_usage = float(input("Enter electricity uses in kWh: "))
bills(we_usage)
