from colorama import Fore

# 🖼️ Python Pattern Drawing Project



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
    write_to = False
    # Step 3: Get dimensions based on choice
    if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
        while rows % 2 == 0:
            print(Fore.RED + "Please enter an odd number.")
            print(Fore.RESET + '')
            rows = int(input("Enter the number of rows: "))
    elif choice in [2, 5]:  # Patterns that need size
        size = int(input("Enter the size of the square/rectangle: "))



    # Step 4: Generate the selected pattern
    if choice == 1:  # Right-angled Triangle

        # Additional step - write to file
        write_to_file = input("Press 'y' to save the figure in file: ")
        if write_to_file == 'y':
            write_to = True

        # TODO: Loop through rows and print increasing stars
        columns = 1
        for r in range(rows):
            for c in range(columns):
                print("*", end='')
            columns += 1
            print('\n', end='')

        # Write to file
        if write_to:
            file = open('file.txt', 'w')
            file.write("Right-angled Triangle\n\n")
            columns = 1
            for r in range(rows):
                for c in range(columns):
                    file.write("*")
                columns += 1
                file.write('\n')
            file.close()
            write_to = False


    elif choice == 2:  # Square with Hollow Center
        # TODO: Create a square with a hollow center
        columns = size
        for r in range(size):
            for c in range(columns):
                if r == 0 or r == size - 1 or c == 0 or c == columns - 1:
                    print('*', end='')
                    continue
                print(' ', end='')
            print()



    elif choice == 3:  # Diamond
        # TODO: Create a diamond shape using loops
        center = rows // 2  # 3
        l_side = center - 1
        r_side = center + 1
        row = 0

        for c in range(center):
            for r in range(rows):
                if c == row and l_side < r < r_side:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
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
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
            l_side += 1
            r_side -= 1
            row += 1



    elif choice == 4:  # Left-angled Triangle
        # TODO: Print decreasing stars for each row
        column = 0

        for c in range(rows):
            for r in range(rows):
                if r <= column:
                    print('*', end='')
                else:
                    print(' ', end='')
            column += 1
            print()

    elif choice == 5:  # Hollow Square
        # TODO: Similar to choice 2 but ensure perfect square logic
        for r in range(size):
            for c in range(size):
                if r == 0 or r == size - 1 or c == 0 or c == size - 1:
                    # print(f'{r}{c} ', end='')
                    print('*', end='')

                else:
                    print(' ', end='')

            print()

    elif choice == 6:  # Pyramid
        # TODO: Center-align stars to form a pyramid
        center = rows // 2
        l_side = center - 1
        r_side = center + 1
        row = 0

        for c in range(center + 1):
            for r in range(rows):
                if c == row and l_side < r < r_side:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
            row += 1
            l_side -= 1
            r_side += 1

    elif choice == 7:  # Reverse Pyramid
        # TODO: Create an upside-down pyramid
        center = rows // 2
        l_side = 0 - 1
        r_side = rows
        row = 0

        for c in range(center + 1):
            for r in range(rows):
                if c == row and l_side < r < r_side:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
            l_side += 1
            r_side -= 1
            row += 1


    elif choice == 8:  # Rectangle with Hollow Center
        # TODO: Handle separate width and height inputs for rectangle
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))
        for r in range(height):
            for c in range(width):
                if r == 0 or r == height - 1 or c == 0 or c == width - 1:
                    # print(f'{r}{c} ', end='')
                    print('*', end='')

                else:
                    print(' ', end='')

            print()


    else:
        print("❌ Invalid choice! Please restart the program.")


    # Step 5: Optional - Allow the user to restart or exit
    print("Do you want to restart the program?")
    restart = input("  Press " + Fore.GREEN + "'y'" + Fore.RESET + " for restart or " + Fore.RED + "'n'" + Fore.RESET + " for exit: ")

    if restart != 'y':
        break

    print('\n'*50)
