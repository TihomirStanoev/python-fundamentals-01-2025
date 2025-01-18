from colorama import Fore

# 🖼️ Python Pattern Drawing Project

def save_to_file(save_result,symbol):
    print(' 💾 Do you want to save the shape to a file?')
    save_to = input("  Enter " + Fore.GREEN + "\'y\'" + Fore.RESET + " to save:  ")

    # Replace symbol in saved file
    save_result = save_result.replace(symbol, '*')

    if save_to == 'y':
        file = open('file.txt', 'w')
        file.write(save_result)
        file.close()
        print('The shape is saved!')
    else:
        print('The shape is NOT saved!')

def choose_symbol():

    print('  From the menu you can select a symbol with which to print\n '
          'the figure or enter a symbol of your choice.')
    print("\t "+ Fore.BLUE + "[1.🔷    2.⚽    3.😁    4. Custom]\n" + Fore.RESET)

    choice_symbol = int(input("Choice: "))

    if choice_symbol == 1:
        return '🔷'
    elif choice_symbol == 2:
        return '⚽'
    elif choice_symbol == 3:
        return '😁'
    else:
        return input()


while True:

    # Step 1: Display a menu to the user
    print("🌟 Welcome to the Python Pattern Drawing Program!")
    print("Choose a pattern type:")
    print("1. Right-angled Triangle")
    print("2. Square with Hollow Center")
    print("3. Diamond")
    print("4. Left-angled Triangle")
    print("5. Hollow Square")
    print("6. Pyramid")
    print("7. Reverse Pyramid")
    print("8. Rectangle with Hollow Center")

    # Step 2: Get the user's choice
    choice = int(input("Enter the number corresponding to your choice: "))

    rows = 0 # bypass undefined
    size = 0 # bypass undefined
    result = ''
    s = '*' # Default symbol for print

    # Step 3: Get dimensions based on choice
    if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
        while rows % 2 == 0:
            print(Fore.RED + "⚠️ Please enter an odd number.")
            print(Fore.RESET + '')
            rows = int(input("Enter the number of rows: "))
    elif choice in [2, 5]:  # Patterns that need size
        size = int(input("Enter the size of the square/rectangle: "))



    # Step 4: Generate the selected pattern
    if choice == 1:  # Right-angled Triangle
        # TODO: Loop through rows and print increasing stars

        result = f'Right-angled Triangle \n\t A = B = C = {rows} \n'

        # Selecting a random character to print
        s = choose_symbol()

        columns = 1
        for r in range(rows):
            for c in range(columns):
                result += s
            columns += 1
            result += '\n'

        # Print the result
        print(result)


    elif choice == 2:  # Square with Hollow Center
        # TODO: Create a square with a hollow center

        result = f'Square with Hollow Center \n\t A = {size} \n'

        columns = size
        for r in range(size):
            for c in range(columns):
                if r == 0 or r == size - 1 or c == 0 or c == columns - 1:
                    result += s
                    continue
                result += ' '
            result += '\n'

        # Print the result
        print(result)



    elif choice == 3:  # Diamond
        # TODO: Create a diamond shape using loops

        result = f'Diamond \n A = {rows} \n'

        center = rows // 2  # 3
        l_side = center - 1
        r_side = center + 1
        row = 0

        for c in range(center):
            for r in range(rows):
                if c == row and l_side < r < r_side:
                    result += s

                else:
                    result += ' '
            result += '\n'
            row += 1
            l_side -= 1
            r_side += 1

        center = rows // 2
        l_side = 0 - 1
        r_side = rows

        row = 0

        for c in range(center + 1):
            for r in range(rows):
                if c == row and l_side < r < r_side:
                    result += s
                else:
                    result += ' '
            result += '\n'
            l_side += 1
            r_side -= 1
            row += 1

        # Print the result
        print(result)


    elif choice == 4:  # Left-angled Triangle
        # TODO: Print decreasing stars for each row
        result = f'Left-angled Triangle \n A = {rows} \n'
        column = 0

        s = choose_symbol()

        for c in range(rows):
            for r in range(rows):
                if r <= column:
                    result += s
                else:
                    result += ' '
            column += 1
            result += '\n'

        # Print the result
        print(result)


    elif choice == 5:  # Hollow Square
        # TODO: Similar to choice 2 but ensure perfect square logic
        result = f'Hollow Square \n A = {size} \n'

        for r in range(size):
            for c in range(size):
                if r == 0 or r == size - 1 or c == 0 or c == size - 1:
                    result += s

                else:
                    result += ' '

            result += '\n'

        # Print the result
        print(result)


    elif choice == 6:  # Pyramid
        # TODO: Center-align stars to form a pyramid

        result = f'Pyramid \n A = {rows} \n'

        center = rows // 2
        l_side = center - 1
        r_side = center + 1
        row = 0

        for c in range(center + 1):
            for r in range(rows):
                if c == row and l_side < r < r_side:
                    result += s
                else:
                    result += ' '
            result += '\n'
            row += 1
            l_side -= 1
            r_side += 1

        print(result)


    elif choice == 7:  # Reverse Pyramid
        # TODO: Create an upside-down pyramid

        result = f'Reverse Pyramid\n ROWS = {rows}\n'

        s = '*'
        center = rows // 2
        l_side = 0 - 1
        r_side = rows
        row = 0

        for c in range(center + 1):
            for r in range(rows):
                if c == row and l_side < r < r_side:
                    result += s
                else:
                    result += ' '
            result += '\n'
            l_side += 1
            r_side -= 1
            row += 1

        print(result)


    elif choice == 8:  # Rectangle with Hollow Center
        # TODO: Handle separate width and height inputs for rectangle
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))

        result = f'Rectangle with Hollow Center \n A = {width} B = {height} \n'

        for r in range(height):
            for c in range(width):
                if r == 0 or r == height - 1 or c == 0 or c == width - 1:
                    result += '*'

                else:
                    result += ' '

            result += '\n'

        print(result)


    else:
        print("❌ Invalid choice! Please restart the program.")

    # Ask for save
    save_to_file(result,s)

    # Step 5: Optional - Allow the user to restart or exit
    print("Do you want to restart the program?")
    restart = input("  Press " + Fore.GREEN + "'y'" + Fore.RESET + " for restart or " + Fore.RED + "'n'" + Fore.RESET + " for exit: ")

    if restart != 'y':
        break

    print('\n'*50) # Clear the screen
