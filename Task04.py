def main():
    x = "Task4"
    #===============================
    # Task 4: Rocket Countdown
    # Write a program that counts down from a given number to 1.
    # Each line should be in the format: "T-minus {number}"

    #===============================
    # Write your code here
    #-------------------------------
    start = int(input("Enter a starting number: "))
    for start in range (start, 0,-1):
       print("T-minus")
    #-------------------------------
    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
