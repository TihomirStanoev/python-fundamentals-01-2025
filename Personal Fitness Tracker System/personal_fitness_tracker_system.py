# Personal Fitness Tracker System 🏋️‍♂️

MAX_DURATION = 400
# Lists to store fitness data
workouts = []  # To store workout types and durations
calories = []  # To store calorie intake for meals

# Variables for daily goals
workout_goal = 0  # Daily workout goal in minutes
calorie_goal = 0  # Daily calorie intake goal


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
        return print('You don\'t have@ any workouts recorded yet')

    # Header of "table"
    table = '🏋️ Workout / ⏱️ Duration\n'
    workouts_count = 0
    total_duration = 0
    longest_workout, longest_workout_index = 0, 0

    #Loop for separate workouts and duration

    for index in range(len(workouts)):
        if index % 2 == 0:
            workouts_count += 1
            table += f'  {workouts[index]} - '
        else:
            total_duration += workouts[index]
            table += f'{workouts[index]} min \n'
            if workouts[index] > longest_workout:
                longest_workout = workouts[index]
                longest_workout_index = index

    # Take top activity
    print(f'Longest workout {workouts[longest_workout_index-1]} - '
          f'{workouts[longest_workout_index]} min' )

    # Printing summary info for workouts
    print(table)
    print(f'TOTAL: {total_duration} min for {workouts_count} workouts.')
    print(f'Average duration of workout: {total_duration/workouts_count:.0f} min.')

    process = input("Press ENTER to continue..")

    pass


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
        print(workouts)

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
            type =''
            duraiton = 0
            while True:
                workout_choose = input('Choose a workout from the menu, you can save your own workout by choosing "Other":\n\n'
                      '1. 🏃‍♂️ Running\n'
                      '2. 🚲 Cycling\n'
                      '3. 🚶‍♂️ Walking\n'
                      '4. 💪 Fitness\n'
                      '5. Other\n\n'
                      'You\'r choice: ')

                if workout_choose == '1':
                    type = 'Running'
                elif workout_choose == '2':
                    type = 'Cycling'
                elif workout_choose == '3':
                    type = 'Walking'
                elif workout_choose == '4':
                    type = 'Fitness'
                elif workout_choose == '5':
                    type = input('Training type: ')

                else:
                    print('⭕ Invalid choice!')
                    continue
                break

            while True:
                duraiton_choose = int(input('⏳ Workout Duration [min]: '))
                if 0 < duraiton_choose < MAX_DURATION:
                    duraiton = duraiton_choose
                    break
                else:
                    print(f'Invalid Duration {duraiton_choose} min. The duration must be between 1 and {MAX_DURATION} minutes. ')
                    continue

            log_workout(type, duraiton)


            pass
        elif choice == '2':
            # Prompt for calories consumed
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