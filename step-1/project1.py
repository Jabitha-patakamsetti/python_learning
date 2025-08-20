print("Welcome to the Grocery Billing System")

cart = []  # list to store items as dictionaries
total = 0

while True:
    # Input item details
    item = input("Enter item name: ")
    price = float(input(f"Enter price of {item}: "))
    qty = int(input(f"Enter quantity of {item}: "))

    # Calculate cost for this item
    cost = price * qty
    total += cost

    # Save item details in cart
    cart.append({"item": item, "price": price, "qty": qty, "cost": cost})

    # Ask if user wants to add more items
    choice = input("Add another item? (yes/no): ").lower()
    if choice != "yes":
        break

# Apply discount if total is above 100
if total > 100:
    discount = total * 0.1
    total -= discount
    print(f"\nDiscount applied: ${discount:.2f}")

# Print final bill
print("\n===== Final Bill =====")
for c in cart:
    print(f"{c['item']} - {c['qty']} x ${c['price']:.2f} = ${c['cost']:.2f}")
print(f"------------------------")
print(f"Total Amount: ${total:.2f}")
print("========================")
