from get_calorie import nutri_list

# Personal Fitness Tracker System 🏋️‍♂️

MAX_DURATION = 400
# Lists to store fitness data
workouts = []  # To store workout types and durations
calories = []  # To store calorie intake for meals

# Variables for daily goals
workout_goal = 0  # Daily workout goal in minutes
calorie_goal = 0  # Daily calorie intake goal

def workout_calculations(workouts_list):
    """
    Workout calculations.
    - Calculate all data needed for progres.
    """
    # Header of "table"
    table = '🏋️ Workout  ⏱️ \n'
    workouts_count = 0
    total_duration = 0
    longest_workout_list = []
    longest_workout, longest_workout_index = 0, 0

    #Loop for separate workouts and duration
    for index in range(len(workouts_list)):
        if index % 2 == 0:
            workouts_count += 1
            table += f'  {workouts_list[index]} - '
        else:
            total_duration += workouts_list[index]
            table += f'{workouts_list[index]} min \n'
            if workouts_list[index] > longest_workout:
                longest_workout = workouts_list[index]
                longest_workout_index = index

    longest_workout_list.append(workouts_list[longest_workout_index - 1])
    longest_workout_list.append(workouts_list[longest_workout_index])


    return table, workouts_count, total_duration, longest_workout_list


def log_workout(workout_type, duration):
    """
    Log a workout.
    - Append the workout type and duration to the workouts list.
    - Print a confirmation message.
    """
    print()
    save_workout = input(f"Do you want to save a {workout_type} with {duration}?\n"
                         f"1. ✅ 2. ❌\nEnter your choice: ")
    if save_workout == '1':
        workouts.append(workout_type)
        workouts.append(duration)

        print(f'\n💾 {workout_type} with duration {duration} min is saved successfully!' + '\n' * 3)

    else:
        print("The workout is not saved!")
    print()

def log_calorie_intake(calories_consumed):
    """
    Log calorie intake for a meal.
    - Append the calorie amount to the calories list.
    - Print a confirmation message.
    """
    print('These are the meals you want to add so far:')




    pass


def view_progress():
    """
    Display a summary of the user's progress for the day.
    - Calculate the total workout time and total calories.
    - Print motivational feedback.
    """
    # Summary -> Workout -> Calories
    # Check for recorded workout.

    if not workouts:
        return print('You don\'t have any workouts recorded yet')

    # Get data by calling a function workout_calculations with argument workouts list.
    table, workouts_count, total_duration, longest_workout = workout_calculations(workouts)


    # Printing summary info for workouts
    print('📊 Let\'s see a summary view of all you\'r workouts.\n')
    print('▫️All your training until the moment:\n' + table)
    print(f'▫️So far you have {workouts_count} workouts with a total duration {total_duration} mins.')
    print(f'▫️Average duration per workout: {total_duration/workouts_count:.0f} min.')
    print(f'▫️Yo\'re best workout is {longest_workout[0].lower()} with {longest_workout[1]} min duration!\n')
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
                      '1. 🏃‍♂️ Running\n'
                      '2. 🚲 Cycling\n'
                      '3. 🚶‍♂️ Walking\n'
                      '4. 💪 Fitness\n'
                      '5. Other\n\n'
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
            print("Add your meals to date. The meals should be in a format for example 150g chicken,\n "
                  "the program will calculate the calories itself..")

            meal_input = ''
            total_meals = []
            meal_list = []
            while meal_input != 'exit':
                meal_input = input("Your meal: ").lower()

                meal_list = nutri_list(meal_input)

                if not meal_list or 'error' in meal_list:
                    print("Wrong input, try again!")
                    continue

                for index in range(len(meal_list)):
                    if index % 2 == 0:
                        print(f'{meal_list[index].title()} is', end=' ')
                        total_meals.append(meal_list[index])
                    else:
                        print(f'{meal_list[index]} calories add other meals of input \'exit\' for end:')
                        total_meals.append(meal_list[index])

                log_calorie_intake(total_meals)







            pass
        elif choice == '3':
            # Call view_progress function
            view_progress()
            pass
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


if __name__ == "__main__":
    main()