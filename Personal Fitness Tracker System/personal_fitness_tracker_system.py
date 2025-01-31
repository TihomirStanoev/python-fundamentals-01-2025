from get_calorie import nutri_list


# Personal Fitness Tracker System 🏋️‍♂️


MAX_DURATION = 400.0
workout_menu = [['🏃','run'],['🚲','cycling'],['💪', 'fitness'],['🚶‍','walk']]
# Lists to store fitness data
workouts = [['fitness', 3405.0],['running', 345.0],['swimming', 345.0],['walk', 34.0],['fitndess', 2.0]]  # To store workout types and durations
calories = []  # To store calorie intake for meals

# Variables for daily goals
workout_goal = 0 # Daily workout goal in minutes
calorie_goal = 0  # Daily calorie intake goal

# Variables for sum of total values
duration_total = 0
calories_total = 0


def counting(data_list):
    """
    Count total number of workouts or meals
    """
    total_items = len(data_list)

    return  total_items


def total(data_list):
    """
    Sum of minutes/calories
    """
    total_sum = 0

    for values in data_list:
        total_sum += values[1]

    return total_sum


def the_highest(data_list) -> list:
    """
    Find list with the highest values
    """
    max_value = 0
    highest_list = []


    for action, value in data_list:
        if value > max_value:
            highest_list.append(action)
            highest_list.append(value)
            max_value = value

    return highest_list


def table_creation(data_list, parameter):
    """
    Create table
    """
    table = '.---.-----------.---------.----.\n' # Create first lines of the table
    unit = 'n/a'
    index = 1

    # Create icons and first rows
    if parameter == 'workout':
        table += ('|🏋️ |  Workout  |  Time  | ⏱️ |\n'
                  ':---:------------:--------:----:\n')
        unit = 'min'
    elif parameter == 'meal':
        table += ('|🥓️ |   Meals   |  Cal   | ⚡️ |\n'
                  ':---:------------:--------:----:\n')
        unit = 'cal'

    # Create  body of the table
    for action, value in data_list:
        table += f'| {index} | {action.title():<10s} | {str(value)[:6]:>6s} |{unit} |\n'
        index +=1

    table += '\'---\'-----------\'--------\'-----\'\n'

    return table


def add_workout():
    """
    Add custom workout.
    """
    icon,workout = '', '' # Variables for icon and name of workout
    new_workouts = [] # This list will append to workout_menu with elements icon and workout
    message = ''

    print('Add custom workout.')
    icon = input('First select an icon: ') # Choose icon
    workout = input('Now type a name for the workout: ') # Choose workout name
    confirm = input(f'Are you sure you want to add {workout}?\n Type \'1\' for YES: ')

    new_workouts = [icon, workout]

    if confirm == '1':
        workout_menu.append(new_workouts)
        message = 'The workout has been added!'
    else:
        message = 'The workout has not been added!'

    print(message)

    return message



def save_data(list_data, parameter, total):
    """
    Save data in main lists.
    """
    global duration_total, calories_total

    save = input(f"Do you want to save this {parameter}?\n"
                         f"1. ✅ 2. ❌\nEnter your choice: ")

    if save == '1' and parameter == 'meal':
        calories.extend(list_data)
        calories_total += total

    elif save == '1' and parameter == 'workout':
        workouts.append(list_data)
        duration_total += total

    else:
        return print(f'The {parameter} is not saved!')


    return print(f'\n💾  The {parameter} is saved successfully!' + '\n' * 3)



def limitations():
    """
    Returns a message if the targets are out of limits
    """
    limit =  '''
    “Goal Out of Limits 🚫
    Oops! Your goal is outside the allowed range:
    
        Workout Goal: Must be between 0 and 1000 minutes.
        Calorie Goal: Must be between 1200 and 5000 calories.
    
    Please adjust your goal to fit within the limits and try again. Let’s stay on track!”
    '''

    return limit


def menu_statistic(total, goal):
    """
    Draws the bars at the start of the program
    """
    bar_length = 14 # Set length of bar
    fill_symbol, empty_symbol = '#', ' ' # Symbol for fill and empty space
    percentage = total / goal # Percentage from target
    bar_fill = int(percentage * bar_length) # Value for bar filled

    bar = ''

    if percentage >= 1: # If goal is over 100%
        bar += f' Goal achieved: {percentage * 100:.2f}% '

    elif percentage <= 0:
        bar += 'error'
    else:
        bar += '|'
        for fill in range(1, bar_length):
            if bar_fill >= fill:
                bar += f'{fill_symbol}'
            else:
                bar += f'{empty_symbol}'
        bar += f'| {percentage * 100 :.2f}%'

    return bar



def log_workout():
    """
    Log a workout.
    - Append the workout type and duration to the workouts list.
    - Print a confirmation message.
    """

    type_of_workout = ''
    duration = 0
    workout_list = []

    while True:
        menu_length = len(workout_menu)
        print('Choose a workout from the menu.\n')

        for index,element in enumerate(workout_menu): # Print workout_menu
            icon, workout = element
            print(f'{index + 1}. {icon} {workout.title()}')

        print(f'{menu_length + 1}. Make custom. ')
        print(f'{menu_length + 2}. Back to main menu.')


        workout_choose = int(input(f'\nChoose a workout from the menu, you can save your own workout by choosing "Other": '))

        if 0 < workout_choose <= menu_length:
            type_of_workout = workout_menu[workout_choose-1][1]
        elif workout_choose == menu_length + 1:
            print(add_workout())
            continue
        elif workout_choose == menu_length + 2:
            return print('Back to main menu.')
        else:
            print('⭕ Invalid choice!')
            continue
        break

    while True:
        duration_choose = float(input('⏳ Workout Duration [min]: '))
        if 0 < duration_choose < MAX_DURATION:
            duration = round(duration_choose,2)
            break
        else:
            print(
                f'Invalid Duration {duration_choose} min. The duration must be between 1 and {MAX_DURATION} minutes. ')
            continue

    print()
    workout_list.append(type_of_workout)
    workout_list.append(duration)

    print(f"Current workout: {type_of_workout} with {duration} min.\n")

    save_data(workout_list, 'workout', duration)


def log_calorie_intake():  # !Input list
    """
    Log calorie intake for a meal.
    - Append the calorie amount to the calories list.
    - Print a confirmation message.
    """

    print("Add your meals to the moment. The meals should be in a format, for example 150g chicken,\n "
          "the program will calculate the calories itself. [Input \'e\' for exit..]\n Enter a meal: ", end='')

    total_meals = []  # List with meals for save
    calculation_type = 'meal'  # Type for calculation, only used for UoM and table header

    while True:
        meal_input = input().lower()

        if meal_input == 's' or meal_input == 'e':
            break

        meal_list = nutri_list(meal_input)  # Get calories

        if meal_list == 'error':
            print("Wrong input, try again with correct meal: ", end='')
            continue

        print(f'{meal_list[0]} is {meal_list[1]} calories, add other meals or input \'s\' for save: ', end='')
        total_meals.append(meal_list)

    print('\n\n')

    if not total_meals or meal_input == 'e':  # Continue if total_meals no elements or first input == 's'
        print("Aborted!!!")
        return ''

    meals_table = table_creation(total_meals, calculation_type)  # Table
    meals_count = counting(total_meals) # Count of meals
    calorie_total = total(total_meals)  # Sum of calories


    print(f'Do you want to save {meals_count} meals with total {calorie_total} calories:\n')
    print(f'{meals_table}')

    save_data(total_meals ,calculation_type, calorie_total)



def view_progress():
    """
    Display a summary of the user's progress for the day.
    - Calculate the total workout time and total calories.
    - Print motivational feedback.
    """
    # Calories, Workout, Summary

    # Print menu
    print("🚀 Check your progress so far by selecting an option from the menu.\n")
    print('\t1. 💪 Workouts')
    print('\t2. 🍴 Meals')
    print('\t3. Summary')
    print('\t4. Back')
    choose = input("\nEnter your choice: ")


    if choose == '1' or choose == '3':

        # Check for recorded workout.
        if not workouts:
            return print('You don\'t have any workouts recorded yet')

        calculation_type = 'workout'  # Set calculations for workouts
        workout_table = table_creation(workouts, calculation_type)
        workouts_count = counting(workouts)
        total_duration = total(workouts)
        longest_workout = the_highest(workouts)


        # Printing summary info for workouts
        print('📊 Let\'s see a summary view of all you\'r workouts.\n')
        print('▫️All your training until the moment:\n' + workout_table)
        print(f'▫️So far you have {workouts_count} workouts with a total duration {total_duration} mins.')
        print(f'▫️Average duration per workout: {total_duration / workouts_count:.0f} min.')
        print(f'▫️Yo\'re best workout is {longest_workout[0].lower()} with {longest_workout[1]} min duration!\n')
        input("Press ENTER to continue..")

    if choose == '2' or choose == '3':
        if not calories:
            return print('You don\'t have any meals recorded yet')

        calculation_type = 'meal'  # Set calculations for calories

        meal_table = table_creation(calories, calculation_type)
        meals_count = counting(calories)
        total_calories = total(calories)
        most_calorie = the_highest(calories)


        # Printing summary info for meals
        print("You're doing great so far!")
        print(f"▫️You have recorded {meals_count} meals.\n")
        print(f"▫️Your total calorie intake is {total_calories}.\n")
        print(f"▫️The meal with the highest calorie count is '{most_calorie}'.\n\n")
        print(f"Here is the current meal table:\n{meal_table}\n")
        print("Keep up the good work and stay mindful of your eating habits!")
        input("Press ENTER to continue..")


def reset_progress():
    """
    Clear all data from the workouts and calories lists.
    - Print a confirmation message.
    """
    print('❌❌❌ Reset Progress ❌❌❌\n')
    print('After a reset, your progress will be lost.\n')

    # Display menu options
    print('1. 🍴 Reset meals progress.')
    print('2. 💪 Reset workout progress.')
    print('3. Reset all.')
    print('Other for exit.')

    reset = input("\nEnter your choice: ")

    confirm = input('Type \'reset\' for confirmation or press \'enter\' for continue:')

    if confirm == 'reset':
        if reset == '1':
            calories.clear() # Clear calories list
            return print("Calories progress is restarted!!!")

        elif reset == '2':
            workouts.clear() # Clear workout list
            return print("Workout progress is restarted!!!")

        elif reset == '3':
            workouts.clear() # Clear all lists
            calories.clear()
            return print("All progress is restarted!!!")

    return print("Aborted!!!")


def set_daily_goals():
    """
    Set daily goals for workout time and calorie intake.
    - Update the global variables workout_goal and calorie_goal.
    - Print a confirmation message.
    """
    global workout_goal
    global calorie_goal

    print('\tSet Daily Goals 💪🔥')

    print('Take control of your fitness journey by '
          'setting clear daily targets\n')
    while True:
        print('1. Set Workout Goal! 🏋️')
        workout_goal = float(input('\tHow much time will you dedicate to breaking a sweat today (0 - ∞ min): '))
        if workout_goal <= 0:
            print(limitations())
            continue
        else:
            print(f"Workout Goal is set to {workout_goal} min")
            break
    print()
    while True:
        print('2. Set Calorie Goal!')
        calorie_goal = float(input('\tPlan your calorie intake or burn to stay on track.: '))
        if calorie_goal <= 0 or calorie_goal >= 5000:
            print(limitations())
            continue
        else:
            print(f"Calories Goal is set to {calorie_goal} cal")
            break



def encouragement_system():
    """
    Provide motivational feedback based on progress and goals.
    - Compare current totals to the daily goals.
    - Print encouragement messages.
    """
    pass


def main():
    """
    Main function to interact with the user.
    """
    print("Welcome to the Personal Fitness Tracker System 🏋️‍♂️\n")

    while True:
        # Print workout progress bar
        print(workouts)
        if duration_total != 0 and workout_goal != 0:
            print(f'Workout progress {menu_statistic(duration_total, workout_goal)}')
        if calories_total != 0 and calorie_goal != 0:
            print(f'Calorie progress {menu_statistic(calories_total, calorie_goal)}')


        # Display menu options
        print("1. Log Workout")
        print("2. Log Calorie Intake")
        print("3. View Progress")
        print("4. Reset Progress")
        print("5. Set Daily Goals")
        print("6. Exit")



        # Prompt user for their choice
        choice = input("\nEnter your choice: ")
        print()

        if choice == '1':
            # Prompt for workout type and duration
            log_workout()


        elif choice == '2':
            # Prompt for calories consumed
            log_calorie_intake()


        elif choice == '3':
            # Call view_progress function
            view_progress()

        elif choice == '4':
            # Call reset_progress function
            reset_progress()

        elif choice == '5':
            # Prompt for daily goals
            set_daily_goals()
            pass
        elif choice == '6':
            # Print a goodbye message and break the loop
            print("Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break
        else:
            print("Invalid choice, please try again.")




if __name__ == "__main__":
    main()
