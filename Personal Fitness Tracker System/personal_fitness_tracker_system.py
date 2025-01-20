from get_calorie import nutri_list

# Personal Fitness Tracker System 🏋️‍♂️

MAX_DURATION = 400
# Lists to store fitness data
workouts = []  # To store workout types and durations
calories = []  # To store calorie intake for meals

# Variables for daily goals
workout_goal = 0  # Daily workout goal in minutes
calorie_goal = 0  # Daily calorie intake goal

def calculations(data_list, parameter): # First argument list, second str 'workout'/'meal'
    """
    Calculations.
    - Calculate all data needed for progres.
    """
    # Default table
    table = ' ===   === \n'
    unit = ' '
    # Check header of table
    if parameter == 'workout':
        table = '🏋️ Workout  ⏱️ \n' # Table header if parameter is 'workout'
        unit = ' min'
    elif parameter == 'meal':
        table = '🥓️ Meal    ⚡⚡⚡\n' # Table header if parameter is 'meal'
        unit = ' cal'


    count = 0 # Count str values
    total = 0 # Sum of numeric values
    best_list = [] # List with two items
    best, best_index = 0, 0 # 'best' is the highest value in list, best_index is his index or index-1 is TEXT of highest value

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


def log_workout(workout_type, duration): # Input srt, int
    """
    Log a workout.
    - Append the workout type and duration to the workouts list.
    - Print a confirmation message.
    """
    print()
    save_workout = input(f"Do you want to save a {workout_type} with {duration} min?\n"
                         f"1. ✅ 2. ❌\nEnter your choice: ")
    if save_workout == '1':
        workouts.append(workout_type)
        workouts.append(duration)

        print(f'\n💾 {workout_type} with duration {duration} min is saved successfully!' + '\n' * 3)

    else:
        print("The workout is not saved!")
    print()

def log_calorie_intake(calories_consumed): # !Input list
    """
    Log calorie intake for a meal.
    - Append the calorie amount to the calories list.
    - Print a confirmation message.
    """
    calculation_type = 'meal' # Type for calculation, only used for UoM and table header

    meals = calculations(calories_consumed, calculation_type)
    meals_table = meals[0] # Table
    meals_count = meals[1] # Count of meals
    calorie_total = meals[2] # Sum of calories

    print(f'Do you want to save {meals_count} meals with total {calorie_total} calories:\n')
    print(f'{meals_table}')
    print('1. ✅ 2. ❌')
    save_meals = input("Enter your choice: ")

    if save_meals == '1':
        # Unpacked elements from list  and append with calories[]
        [calories.append(meals) for meals in calories_consumed]
    else:
        print("The meals are not saved!\n")



def view_progress(choose):
    """
    Display a summary of the user's progress for the day.
    - Calculate the total workout time and total calories.
    - Print motivational feedback.
    """
    # Calories, Workout, Summary


    if choose == '1' or choose == '3':
        # Check for recorded workout.
        if not workouts:
            return print('You don\'t have any workouts recorded yet')


        calculation_type = 'workout' # Set calculations for workouts
        workout_table, workouts_count, total_duration, longest_workout = calculations(workouts, calculation_type)


        # Printing summary info for workouts
        print('📊 Let\'s see a summary view of all you\'r workouts.\n')
        print('▫️All your training until the moment:\n' + workout_table)
        print(f'▫️So far you have {workouts_count} workouts with a total duration {total_duration} mins.')
        print(f'▫️Average duration per workout: {total_duration/workouts_count:.0f} min.')
        print(f'▫️Yo\'re best workout is {longest_workout[0].lower()} with {longest_workout[1]} min duration!\n')
        input("Press ENTER to continue..")

    if choose == '2' or choose == '3':
        if not calories:
            return print('You don\'t have any melas recorded yet')

        calculation_type = 'meal' # Set calculations for calories
        meal_table, meals_count, total_calories, most_calorie = calculations(calories, calculation_type)

        print(meal_table) #test
        print(f'Total meals: {meals_count}') #test
        print(f'Total cals: {total_calories}') #test
        print(f'Top meal: {most_calorie[0]} - {most_calorie[1]} cal') #test
        input("Press ENTER to continue..")


def reset_progress():
    """
    Clear all data from the workouts and calories lists.
    - Print a confirmation message.
    """
    pass


def set_daily_goals(workout_minutes, calorie_limit):
    """
    Set daily goals for workout time and calorie intake.
    - Update the global variables workout_goal and calorie_goal.
    - Print a confirmation message.
    """
    pass


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
        # Print workouts list to check for working
#        print(workouts) # print workouts just for "log workout" test.

        # Display menu options
        print("1. Log Workout")
        print("2. Log Calorie Intake")
        print("3. View Progress")
        print("4. Reset Progress")
        print("5. Set Daily Goals")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("\nEnter your choice: ")

        if choice == '1':
            # Prompt for workout type and duration
            type_of_workout = ''
            duration = 0
            while True:
                workout_choose = input('Choose a workout from the menu, you can save your own workout by choosing "Other":\n\n'
                      '\t1. 🏃‍♂️ Running\n'
                      '\t2. 🚲 Cycling\n'
                      '\t3. 🚶‍♂️ Walking\n'
                      '\t4. 💪 Fitness\n'
                      '\t5. Other\n\n'
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

                else:
                    print('⭕ Invalid choice!')
                    continue
                break

            while True:
                duration_choose = int(input('⏳ Workout Duration [min]: '))
                if 0 < duration_choose < MAX_DURATION:
                    duration = duration_choose
                    break
                else:
                    print(f'Invalid Duration {duration_choose} min. The duration must be between 1 and {MAX_DURATION} minutes. ')
                    continue

            log_workout(type_of_workout, duration)


            pass
        elif choice == '2':
            # Prompt for calories consumed
            print("Add your meals to the moment. The meals should be in a format, for example 150g chicken,\n "
                  "the program will calculate the calories itself. [Input \'e\' for exit..]\n Enter a meal: ", end='')

            total_meals = [] # List with meals for save

            while True:
                meal_input = input().lower()

                if meal_input == 's' or meal_input == 'e':
                    break

                meal_list = nutri_list(meal_input) # Get calories

                if meal_list == 'error':
                    print("Wrong input, try again with correct meal: ", end='')
                    continue

                for index in range(len(meal_list)): # Print and append elements from temp list
                    if index % 2 == 0:
                        meal_name = meal_list[index].title()
                        print(f'{meal_name} is', end=' ')
                        total_meals.append(meal_name)
                    else:
                        cals = round(meal_list[index], 1)
                        print(f'{cals} calories, add other meals or input \'s\' for save: ', end='')
                        total_meals.append(cals)


            print('\n\n')

            if not total_meals or meal_input == 'e': # Continue if first input = 's'
                continue
            else:
                log_calorie_intake(total_meals) # Send a list for a calculations before being saved.


        elif choice == '3':
            # Call view_progress function
            print("🚀 Check your progress so far by selecting an option from the menu.\n")
            print('\t1. 💪 Workouts')
            print('\t2. 🍴 Meals')
            print('\t3. Summary')
            progress_choice = input("\nEnter your choice: ")

            view_progress(progress_choice)

        elif choice == '4':
            # Call reset_progress function
            pass
        elif choice == '5':
            # Prompt for daily goals
            pass
        elif choice == '6':
            # Print a goodbye message and break the loop
            print("Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break
        else:
            print("Invalid choice, please try again.")

        print(calories)


if __name__ == "__main__":
    main()