from decisions import get_factorial, sum_odd_numbers

def display_menu():
    print("Homework 3 Menu")
    print("1-Factorial")
    print("2-Sum odd numbers")
    print("3-Exit")

def get_valid_number(prompt, min_val, max_val):
    while True:
        try:
            num = int(input(prompt))
            if min_val <= num <= max_val:
                return num
            else:
                print(f"Number must be between {min_val} and {max_val}. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = get_valid_number("Enter your choice: ", 1, 3)
        
        if choice == 1:
            num = get_valid_number("Enter a number (1-9): ", 1, 9)
            result = get_factorial(num)
            print(f"The factorial of {num} is: {result}")
        elif choice == 2:
            num = get_valid_number("Enter a number (1-99): ", 1, 99)
            result = sum_odd_numbers(num)
            print(f"The sum of odd numbers up to {num} is: {result}")
        elif choice == 3:
            confirm = input("Are you sure you want to exit? (yes/no): ").lower()
            if confirm == "yes":
                print("Exiting...")
                break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
