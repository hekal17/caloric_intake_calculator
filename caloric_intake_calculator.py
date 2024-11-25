# -*- coding: utf-8 -*-

'''
Write a Python program that calculates a person's daily caloric needs based on their personal details, including weight, height, age, gender, activity level, and fitness goal (gain, lose, or maintain weight). The program should follow these steps:

Input: Prompt the user for their age, gender, weight, height, activity level, and fitness goal.

Gender should be entered as either "male" or "female".
Activity level should be chosen from: "sedentary", "lightly active", "moderately active", "very active", or "super active".
Fitness goal should be one of: "gain", "lose", or "maintain".
Calculate BMR: Use the Mifflin-St Jeor equation to calculate the Basal Metabolic Rate (BMR) based on the user's weight, height, age, and gender:

Adjust for Activity: Adjust the BMR based on the user's activity level using the following multipliers:


Sedentary: 1.2
Lightly active: 1.375
Moderately active: 1.55
Very active: 1.725
Super active: 1.9
Adjust for Goal: Modify the adjusted caloric needs based on the user's goal:

To gain weight, add 500 calories.
To lose weight, subtract 500 calories.
To maintain weight, use the adjusted caloric needs without modification.
Output: Display the calculated daily caloric needs and write the result to a text file (caloric_needs.txt).

Repeat or Exit: Allow the user to perform multiple calculations or exit the program.

'''

def calculate_bmr(weight, height, age, gender):
    """Calculate the Basal Metabolic Rate (BMR) based on personal information."""
    # BMR calculation for males based on the Mifflin-St Jeor Equation
    if gender.lower() == 'male':
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    # BMR calculation for females based on the Mifflin-St Jeor Equation
    elif gender.lower() == 'female':
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    # If an invalid gender is entered, print an error and return None
    else:
        print("Oops, looks like you entered an invalid gender.")
        return None

# Dictionary to store activity multipliers based on lifestyle
activity_levels = {
    'sedentary': 1.2,        # Little or no exercise
    'lightly active': 1.375, # Light exercise or sports 1-3 days a week
    'moderately active': 1.55, # Moderate exercise or sports 3-5 days a week
    'very active': 1.725,    # Hard exercise or sports 6-7 days a week
    'super active': 1.9      # Very hard exercise or physical full-time job
}
    
def get_valid_input(prompt, valid_values=None, value_type=str): # Helper function to repeatedly ask for input until it's valid.
    while True:
        user_input = input(prompt).strip().lower()
        
        # Validate string inputs (gender, activity level, goal)
        if valid_values and user_input in valid_values:
            return user_input
        
        # Validate integer inputs (age)
        if value_type == int:
            try:
                return int(user_input)
            except ValueError:
                print(f"{user_input} is not a valid number. Please try again.")
        
        # Validate float inputs (weight, height)
        if value_type == float:
            try:
                return float(user_input)
            except ValueError:
                print(f"{user_input} is not a valid number. Please try again.")

        # If no valid match for string or number, print the error message
        print(f"{user_input} is not a valid input. Please try again.")
    

def main():
    while True:
        # Get valid inputs with validation for age (integer), weight (float), height (float)
        age = get_valid_input("How old are you? ", value_type=int)  # Validate age as integer
        gender = get_valid_input("What's your gender? (male/female): ", valid_values=["male", "female"])  # Validate gender
        weight = get_valid_input("What's your weight in kg? ", value_type=float)  # Validate weight as float
        height = get_valid_input("How tall are you (in cm)? ", value_type=float)  # Validate height as float
        activity_level = get_valid_input("How active are you? (sedentary, lightly active, moderately active, very active, super active): ", 
                                         valid_values=["sedentary", "lightly active", "moderately active", "very active", "super active"])  # Validate activity level
        goal = get_valid_input("What's your goal? (gain, lose, maintain): ", valid_values=["gain", "lose", "maintain"])  # Validate goal

        # Quick review of what the user entered
        print("\nHere's what you've told me:")
        user_info = [f"Age: {age}", f"Gender: {gender}", f"Weight: {weight} kg", f"Height: {height} cm", f"Activity Level: {activity_level}", f"Goal: {goal}"]
        for info in user_info:
            print(info)

        # Calculate BMR using the previously defined function
        bmr = calculate_bmr(weight, height, age, gender)

        if bmr is not None:
            # If BMR is valid, calculate daily caloric needs based on the activity level
            if activity_level in activity_levels:
                daily_calories = bmr * activity_levels[activity_level]
                
                # Adjust caloric needs based on the goal (gain, lose, or maintain)
                if goal == 'gain':
                    daily_calories += 500  # Add extra calories for weight gain
                elif goal == 'lose':
                    daily_calories -= 500  # Subtract calories for weight loss

                # Display the recommended daily caloric intake to the user
                print(f"\nTo {goal} weight, you should aim for about {int(daily_calories)} calories per day.")

                # Write the result to a text file for future reference
                with open("caloric_needs.txt", "w") as file:
                    file.write(f"To {goal} weight, your recommended daily caloric intake is {int(daily_calories)} calories.\n")
            else:
                print("Sorry, that doesn't seem to be a valid activity level.")  # Handle invalid activity level
        else:
            print("There was an issue with your BMR calculation.")  # If BMR calculation failed

        # Ask the user if they want to perform another calculation
        repeat = input("\nWant to calculate again? (yes/no): ").strip().lower()
        if repeat != 'yes':
            print("Thanks for using the calculator! Stay healthy!")  # Thank user before exiting
            break  # Exit the loop if the user doesn't want to continue

# Check if this script is being run directly and not imported
if __name__ == "__main__":
    main()  # Start the main program



