# Problem:
# Allow the user to input a series of bank transactions (credits and debits).
# For each transaction, record it, print the balance after the transaction, and 
# provide a final summary at the end.

# solution:
# - Take transactions from the user, where each transaction is either a debit (withdrawal) or credit (deposit).
# - Update and print the balance after each transaction.
# - Print the final balance and the transaction history.

def bank_transaction():
    balance = 0
    transactions = []

    while True:
        # Ask user for transaction input
        transaction = input("Enter a transaction (credit/debit amount: ").strip().lower()
        
        if transaction == 'exit':
            break
        
        # Split transaction into action (credit or debit) and amount
        try:
            action, amount = transaction.split()
            amount = float(amount)
            
            if action == 'credit':
                balance += amount
                transactions.append(f"Credited: {amount} ₹")
            elif action == 'debit':
                if balance >= amount:
                    balance -= amount
                    transactions.append(f"Debited: {amount} ₹")
                else:
                    print("Insufficient balance for this debit account user.")
                    continue
            else:
                print("Invalid action! Please enter 'credit' or 'debit'.")
                continue

            print(f"Balance after transaction: {balance} ₹")
        
        except ValueError:
            print("Invalid input! Please enter a valid transaction : credit/debit amount.")
    
    # Final summary
    print("\nTransaction Summary:")
    for transaction in transactions:
        print(transaction)
    print(f"Final balance: {balance} ₹")

# Run the bank transaction analyzer
bank_transaction()

#enter output format like this

# #Enter a transaction (credit/debit amount or 'exit' to finish): credit 500
# Balance after transaction: 500.0 ₹
# Enter a transaction (credit/debit amount or 'exit' to finish): debit 200
# Balance after transaction: 300.0 ₹
# Enter a transaction (credit/debit amount or 'exit' to finish): credit 100
# Balance after transaction: 400.0 ₹
# Enter a transaction (credit/debit amount or 'exit' to finish): exit

