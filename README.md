# Year 9 DTE Python Test Package

## Instructions

- Complete each task by writing your code in the corresponding `TaskXX.py` file.
- Each task includes a scenario and UI examples to guide your implementation.
- Do not use `input()` or `print()` unless shown in the UI example.
- Your code will be tested using the provided unit tests in `test_TaskXX.py`.
- Save each task in its own Python file (e.g., `Task01.py`, `Task02.py`, etc.).
- Save each test in its own Python file (e.g., `test_Task01.py`, `test_Task02.py`, etc.).

## Grading Criteria

Your work will be graded according to the following criteria:

- **Correctness:**  
  Your code must produce the correct output for all required cases, including edge cases, as demonstrated in the UI examples and tested by the provided unit tests.

- **Functionality:**  
  Each task must be implemented in the correct file (`TaskXX.py`) and must use the correct function name and signature as expected by the unit tests.

- **Code Structure:**  
  Write your code inside the provided `main()` function and follow the comments for guidance.  
  Do not include unnecessary code outside the specified area.

- **Testing:**  
  Your code must pass all the provided unit tests in the corresponding `test_TaskXX.py` file.  
  Each test is worth one mark; partial marks may be awarded if only some tests pass.

- **Readability:**  
  Use clear and readable code. Add comments where appropriate to explain your logic.

- **No Unnecessary Input/Output:**  
  Only use `input()` or `print()` if shown in the UI example.  
  Do not add extra prompts or outputs.

**Marking Breakdown:**  

- Each task is worth the number of marks shown in the task heading.
- Each unit test passed is worth one mark.
- If your code does not run or does not match the required function signature, you may receive zero for that task.

## Task List

---

### Task 1: Triple Cheer (5 marks)

You’re at a sports game and want to cheer for your team! Write a program that repeats your cheer word three times, separated by exclamation marks.

**UI Examples:**

>Cheer word: Go\
>Go!Go!Go

>Cheer word: Win\
>Win!Win!Win

>Cheer word: Python\
>Python!Python!Python


---

### Task 2: Animal Sound (6 marks)

You’re making a virtual pet game. Write a program that asks for an animal and prints the sound it makes.

**UI Examples:**

>Animal: dog\
>Woof!

>Animal: CAT\
>Meow!

>Animal: Cow\
>Moo!

>Animal: duck\
>Unknown sound


---

### Task 3: Water Reminder (6 marks)

You’re building a health app that reminds people to drink water.

**UI Examples:**

>How many cups of water have you had today? 2  
>Drink more water!


>How many cups of water have you had today? 6  
>Good job staying hydrated!


>How many cups of water have you had today? 10  
>That's a lot of water!


---

### Task 4: Rocket Countdown (4 marks)

You’re helping with a rocket launch! Write a program that counts down from a given number to 1, printing each step.

**UI Examples:**

>Countdown from: 3\
>T-minus 3\
>T-minus 2\
>T-minus 1


>Countdown from: 5\
>T-minus 5\
>T-minus 4\
>T-minus 3\
>T-minus 2\
>T-minus 1


---

### Task 5: Debugging – Ticket Price (7 marks)

You’re writing a ticketing system for a cinema. Fix the code so it prints the correct ticket type based on age.

**UI Examples:**

>Age: 10\
>Child ticket


>Age: 30\
>Adult ticket


>Age: 70\
>Senior ticket


>Age: -5\
>Invalid age


---

### Task 6: Month Names (8 marks)

You’re making a calendar app. Write a program that takes a list of short month names and prints their full names. Ignore any unrecognized names.

| Short Name | Full Name   |
| ---------- | ----------- |
| Jan        | January     |
| Feb        | February    |
| Mar        | March       |
| Apr        | April       |
| May        | May         |
| Jun        | June        |
| Jul        | July        |
| Aug        | August      |
| Sep        | September   |
| Oct        | October     |
| Nov        | November    |
| Dec        | December    |

**UI Examples:**

>Short months: Jan, Mar, Xyz\
>January\
>March


>Short months: Feb, Apr, May\
>February\
>April
>May



>Short months: Dec, Abc, Jul\
>December\
>July


---

## Testing

- Each task has a corresponding unit test file (e.g., `test_Task01.py`).
- Run the tests using `test_Task01.py` (or the appropriate test file).
- Make sure your function names and file names match those specified in the test files.

---

If you have questions about the grading, ask your teacher before submitting your work. Good luck!
