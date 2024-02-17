# Importing the necessary function from repetition module
from repetition import get_factorial,sum_odd_numbers      

def main():
    while True:
        print("\nHomework 3 Menu")
        print("1-Factorial")
        print("2-Sum odd numbers")
        print("3-Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            while True:
                num = int(input("Enter a number (greater than 0 and less than 10): "))
                if 0 < num < 10:
                    print("Factorial:", get_factorial(num))
                    break
                else:
                    print("Invalid input. Please enter a number greater than 0 and less than 10.")
        elif choice == '2':
            while True:
                num = int(input("Enter a number (greater than 0 and less than 100): "))
                if 0 < num < 100:
                    print("Sum of odd numbers:", sum_odd_numbers(num))
                    break
                else:
                    print("Invalid input. Please enter a number greater than 0 and less than 100.")
        elif choice == '3':
            exit_choice = input("Are you sure you want to exit? (yes/no): ")
            if exit_choice.lower() == 'yes':
                print("Exiting the program...")
                break
            elif exit_choice.lower() == 'no':
                continue
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()