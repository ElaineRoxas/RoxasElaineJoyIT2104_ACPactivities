while True:
    amount = float(input("Enter the total purchase amount: "))
    discount = amount * (0.10 if amount > 5000 else 0.05)
    final_price = amount - discount
    print(f"Initial Purchase Amount: {amount:.2f}")
    print(f"Discount: {discount:.2f}")
    print(f"Final Price: {final_price:.2f}")

    if input("Do you want to try again? (yes/no): ").lower() != 'yes':
        print("Thank you!")
        break
