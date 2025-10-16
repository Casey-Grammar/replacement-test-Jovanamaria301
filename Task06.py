def main():
    x = "Task6"
    #===============================
    # Task 6: Month Names
    # Write a program that converts short month names to full names.
    # Unrecognized names should be ignored.

    #===============================
    # Write your code here
    #-------------------------------
    short_to_full = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "Spetember",
    "Oct": "October",
    "Nov": "Novemeber",
    "Dec": "Decemeber"
    }
    short_name = input("Enter a short month name: ")
    full_name = short_to_full.get(short_name, None)
    if full_name:
        print(full_name)
    else:
        print("Unrecognized month name")
    #-------------------------------
    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
