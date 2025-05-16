


# P to print a mirrored right-angled triangle based on user input
def print_mirrored_triangle(rows):
    for i in range(1, rows + 1):
        # Print spaces before the asterisks
        print(" " * (rows - i), end="")
        # Print asterisks
        print("*" * i)

# Get the number of rows from the user
try:
    rows = int(input("Enter the number of rows for the triangle: "))
    if rows <= 0:
        print("Please enter a positive number.")
    else:
        print_mirrored_triangle(rows)
except ValueError:
    print("Please enter a valid integer.")