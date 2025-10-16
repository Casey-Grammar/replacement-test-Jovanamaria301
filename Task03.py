def main():
    x = "Task3"
    #===============================
    # Task 3: Water Reminder
    # Write a program that gives hydration advice based on number of cups of water.
    # <4 -> "Drink more water!"
    # 4-8 -> "Good job staying hydrated!"
    # >8 -> "That's a lot of water!"

    #===============================
    # Write your code here
    #-------------------------------
    cups = int(input("How many cups of water did you drink today? "))
    if cups <4:
        print("Drink more water!")
    elif cups <=8: 
        print("Good job staying hydrated!")
    else: 
        print("thats a lot of water!")
    #-------------------------------
    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
