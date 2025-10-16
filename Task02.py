def main():
    x = "Task2"
    #===============================
    # Task 2: Animal Sound
    # Write a program that returns the sound of a given animal.
    # Recognized animals: dog -> "Woof!", cat -> "Meow!", cow -> "Moo!"
    # Any other input -> "Unknown sound"

    #===============================
    # Write your code here
    #-------------------------------
    animal = input("Enter an animal: ").lower() 
    if animal == dog: 
        print("woof")
    elif animal == cat: 
        print("Meow")
    elif animal == cow: 
        print("Moo")
    else:
        print("Unknown sound")

    #-------------------------------
    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
