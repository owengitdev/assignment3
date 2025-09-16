# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    # Delete the following line and implement your Queue class
    pass
    


def run_help_desk():
    # Create an instance of the Queue class
    

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            
            
            print(f"{name} added to the queue.")
        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            pass # delete this line


        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            pass # delete this line


        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()
