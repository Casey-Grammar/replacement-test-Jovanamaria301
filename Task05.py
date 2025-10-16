def main():
    x = "Task5"
    #===============================
    # Task 5: Ticket Price
    # Write a program that returns ticket type based on age.
    # <0 -> "Invalid age"
    # <13 -> "Child ticket"
    # 13-64 -> "Adult ticket"
    # >=65 -> "Senior ticket"

    #===============================
    # Write your code here
    #-------------------------------
    age = int(input("Enter your age: ")) 
    if age <0: 
        print("invalid age")
    elif age < 13: 
        print("Child ticket")
    elif age <= 64:
        print("Adult ticket")
    else:
        print("Senior ticket")
    #-------------------------------
    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
