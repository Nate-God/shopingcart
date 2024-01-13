
cart = []
while True:
    print("\n\n\nOptions:")
    print("'add' to  add an item to cart")
    print("'remove' to remove an item from cart")
    print("'view' to view items in cart")
    print("'checkout' to get the recipt and Quit")
    while True:
        choice = input("\nEnter the option you want: ").lower().strip()
        if choice == 'add' or choice == 'remove' or choice == 'view' or choice == 'checkout':
            break
        else:
            print("that is not a valid option")
    if choice == 'add':
        name = input("Enter item name: ").lower().strip()

        while True:
            price = input("\nEnter the items price: ")
            try:
                price = float(price)
            except:
                print("please enter a valid value")
            else:
                break
        while True:
            quantity = input("Enter item quantity: ")
            try:
                quantity = int(quantity)
            except:
                print("please enter a valid value")
            else:
                break
        item = {'name': name, 'price': price}
        found = 0
        for cart_item in cart:
            if cart_item['item']['name'] == item['name']:
                cart_item['quantity'] += quantity
                found = 1
                break
        if found == 0:
            cart.append({'item': item, 'quantity': quantity})
        print(f"{quantity} {name}(s) added to the cart.")
    elif choice == 'remove':
        name = input("Enter item name to remove: ")

        while True:
            quantity = input("Enter quantity to remove: ")
            try:
                quantity = int(quantity)
            except:
                print("please enter a valid value")
            else:
                break
        for cart_item in cart:
            if cart_item['item']['name'] == name:
                if cart_item['quantity'] > quantity:
                    cart_item['quantity'] -= quantity
                    break
                else:
                    cart.remove(cart_item)
                    break
        print(f"{quantity} {name}(s) removed from the cart.")
    
    elif choice == 'view':
        print("Shopping Cart:")
        for cart_item in cart:
            print(f"{cart_item['item']['name']} - Quantity: {cart_item['quantity']} - Price: ${cart_item['item']['price']}")
    else:
        total = 0
        print("Shopping Cart:")
        for cart_item in cart:
            print(f"{cart_item['item']['name']} - Quantity: {cart_item['quantity']} - Price: ${cart_item['item']['price']}")
            total += cart_item['item']['price'] * cart_item['quantity']
        print(f"Total: ${total}")
        print("Thank you for shopping! Goodbye.")
        break


main()