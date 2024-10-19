import os

# Function to clear the command line output
def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the current list of products and their prices
def display_products(products):
    total = 0
    print("Products List:")
    for item, price in products:
        print(f"{item:<10} R{price:.2f}")
        total += price
    print("-" * 15)
    print(f"Total:    R{total:.2f}\n")

# Function to add a product to the list
def add_product(products):
    item = input("Enter product name: ")
    
    # Loop until a valid float is entered for the price
    while True:
        try:
            price = float(input(f"Enter price for {item}: R"))
            break  # Break out of the loop if input is valid
        except ValueError:
            print("Invalid price! Please enter a valid number (e.g., 50.99).")
    
    products.append((item, price))

# Main function for the POS system
def run_pos():
    products = []  # List to store all the products and their prices
    sentinel = ''  # Sentinel variable for the loop

    while sentinel.lower() != 'exit':  # Sentinel-based loop
        clear_output()
        display_products(products)
        print("1. Add product")
        print("2. Clear output")
        print("Type 'exit' to finish and see the total.")
        sentinel = input("Choose an option or type 'exit': ").strip()

        if sentinel == '1':
            add_product(products)
        elif sentinel == '2':
            clear_output()

    # Final display of all items and the total
    clear_output()
    print("Final receipt:")
    display_products(products)

# Run the POS system
run_pos()