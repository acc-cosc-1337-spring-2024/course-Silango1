#Importing the decisions module
import decisions

def main():
    # Prompting the user for options
    options = float(input("Enter the number of options: "))

    # Prompting the user for total
    total = float(input("Enter the total number: "))

    # Calculating the ratio using the get_options_ratio function
    result = decisions.get_options_ratio(options, total)

    # Getting the faculty rating based on the result
    faculty_rating = decisions.get_faculty_rating(result)

    # Displaying the faculty rating
    print("Faculty Rating:", faculty_rating)

if __name__ == "__main__":
    main() 