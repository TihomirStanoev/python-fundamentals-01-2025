from get_calorie import nutri_list


# Personal Fitness Tracker System 🏋️‍♂️

MAX_DURATION = 400.0
# Lists to store fitness data
workouts = []  # To store workout types and durations
calories = []  # To store calorie intake for meals

# Variables for daily goals
workout_goal = 0 # Daily workout goal in minutes
calorie_goal = 0  # Daily calorie intake goal

# Variables for sum of total values
duration_total = 0
calories_total = 0

def calculations(data_list, parameter):  # First argument list, second str 'workout'/'meal'
    """
    Calculations.
    - Calculate all data needed for progres.
    """
    # Default table
    table = ' ===   === \n'
    unit = ' '
    # Check header of table
    if parameter == 'workout':
        table = '🏋️ Workout  ⏱️ \n'  # Table header if parameter is 'workout'
        unit = ' min'
    elif parameter == 'meal':
        table = '🥓️ Meal    ⚡⚡⚡\n'  # Table header if parameter is 'meal'
        unit = ' cal'

    count = 0  # Count str values
    total = 0  # Sum of numeric values
    best_list = []  # List with two items
    best, best_index = 0, 0  # 'best' is the highest value in list, best_index is his index or index-1 is TEXT of highest value

    #Loop for separate workouts/meals and duration/calories
    for index in range(len(data_list)):

        # Meal or Workout [text]
        if index % 2 == 0:
            count += 1
            table += f'  {data_list[index]} - '
        else:

            # Calories or Minutes [numeric]
            total += data_list[index]
            table += f'{data_list[index]}{unit} \n'
            if data_list[index] > best:
                best = data_list[index]
                best_index = index

    # Extract the highest workout/meal and append in best_list
    best_list.append(data_list[best_index - 1])
    best_list.append(data_list[best_index])

    return table, count, total, best_list

def save_data(list_data, parameter, total):
    """
    Save data in main lists.
    """
    global duration_total
    global calories_total

    save = input(f"Do you want to save this {parameter}?\n"
                         f"1. ✅ 2. ❌\nEnter your choice: ")

    if save == '1' and parameter == 'meal':
        calories.extend(list_data)
        calories_total += total

    elif save == '1' and parameter == 'workout':
        workouts.extend(list_data)
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
        workout_choose = input(
            'Choose a workout from the menu, you can save your own workout by choosing "Other":\n\n'
            '\t1. 🏃‍♂️ Running\n'
            '\t2. 🚲 Cycling\n'
            '\t3. 🚶‍♂️ Walking\n'
            '\t4. 💪 Fitness\n'
            '\t5. Other\n'
            '\t6. Back\n\n'
            'You\'r choice: ')

        if workout_choose == '1':
            type_of_workout = 'Running'
        elif workout_choose == '2':
            type_of_workout = 'Cycling'
        elif workout_choose == '3':
            type_of_workout = 'Walking'
        elif workout_choose == '4':
            type_of_workout = 'Fitness'
        elif workout_choose == '5':
            type_of_workout = input('Training type: ')
        elif workout_choose == '6':
            return print("Back to main menu.")
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

    print(f"Do you want to save a {type_of_workout} with {duration} min?\n")

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

    while True:
        meal_input = input().lower()

        if meal_input == 's' or meal_input == 'e':
            break

        meal_list = nutri_list(meal_input)  # Get calories

        if meal_list == 'error':
            print("Wrong input, try again with correct meal: ", end='')
            continue

        for index in range(len(meal_list)):  # Print and append elements from temp list
            if index % 2 == 0:
                meal_name = meal_list[index].title()
                print(f'{meal_name} is', end=' ')
                total_meals.append(meal_name)
            else:
                cals = round(meal_list[index], 1)
                print(f'{cals} calories, add other meals or input \'s\' for save: ', end='')
                total_meals.append(cals)

    print('\n\n')

    if not total_meals or meal_input == 'e':  # Continue if total_meals no elements or first input == 's'
        return print("Aborted!!!")

    calculation_type = 'meal'  # Type for calculation, only used for UoM and table header

    meals = calculations(total_meals, calculation_type)
    meals_table = meals[0]  # Table
    meals_count = meals[1]  # Count of meals
    calorie_total = meals[2]  # Sum of calories

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
        workout_table, workouts_count, total_duration, longest_workout = calculations(workouts, calculation_type)

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
        meal_table, meals_count, total_calories, most_calorie = calculations(calories, calculation_type)

        print(meal_table)  #test
        print(f'Total meals: {meals_count}')  #test
        print(f'Total cals: {total_calories}')  #test
        print(f'Top meal: {most_calorie[0]} - {most_calorie[1]} cal\n')  #test
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
