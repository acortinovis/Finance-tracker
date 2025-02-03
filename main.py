# This program will calculate the average of a set of grades

# Ask the user for their name and greet them
name = input("what is your first name? ").title().strip()
print(f"Hi {name}! Welcome to the marks averaging program! ")

while True: 


    # Ask the user for their marks
    mark1 = float (input("enter first mark: ").strip())
    mark2 = float (input("enter second mark: ").strip())
    mark3 = float (input("enter third marks: ").strip())
    mark4 = float (input("enter fourth marks: ").strip())

    # Calculate the average of those marks
    average = (mark1 + mark2 + mark3 + mark4) / 4
    average =round(average,2) #round to 2 decimal places

    # Show the user the average
    print(f"the average of your marks is {average}")
    # Ask the user if they want to do it again
    choice = input( "would you like to do another calculation [y/n]?" ).strip().lower()
    if choice == "y" or choice == "yes":
        pass
    else:
        break 


# Say goodbye
print( "goodbye")