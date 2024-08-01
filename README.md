# Time Calculator

A simple Python program to perform basic time-related conversions and operations. The program provides a menu-driven interface to convert minutes to hours, convert hours to minutes, and add two times in HH:MM format.

## Features

- **Convert Minutes to Hours:** Convert a given number of minutes to hours and minutes.
- **Convert Hours to Minutes:** Convert a given time in hours and minutes to total minutes (functionality to be implemented).
- **Add Times:** Add two times in HH:MM format and display the result.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/muabdullahtech/Time-Calculator
   cd Time-Calculator
   ```

2. **Run the Program:**
   ```bash
   python TimeCalculator.py
   ```

3. **Menu Options:**
   - `1`: Convert Minutes to Hours
   - `2`: Convert Hours to Minutes (To be implemented)
   - `3`: Add times in the format of 00:00
   - `0`: Exit the program

## Code Overview

```python
import os

def main():
    while True:
        choice = menu()
        match choice:
            case "1":
                MinutesToHours()
            case "2":
                HoursToMinutes()
            case "3":
                AddTime()
            case "0":
                os.system("clear")
                break
    print("EXITING!!!")

def menu():
    print("Time Calculator")
    print("Menu:")
    print("1. Convert Minutes to Hours")
    print("2. Convert Hours to Minutes")
    print("3. Add times in format of 00:00")
    print("0. Exit")
    choice = input("Choice: ")
    return choice

def MinutesToHours():
    os.system("clear")
    print("Minutes to Hour Converter")
    hour = 0
    minutes = int(input("Enter Time in minutes: "))
    while minutes > 59:
        minutes -= 60
        hour += 1
    print(f"{hour}:{minutes}")

def HoursToMinutes():
    os.system("clear")
    print("Hours to Minutes Converter")
    print()
    hours = int(input("Enter Time in hours: "))
    minutes = hours * 60
    print(f"{hours} hours is equal to {minutes} minutes.")
    print()

def AddTime():
    os.system("clear")
    print("Time Adder")
    time1 = input("Enter time (00:00): ")
    hrs1, mins1 = time1.split(":")
    time2 = input("Enter time to be added (00:00): ")
    hrs2, mins2 = time2.split(":")
    hrs = int(hrs1) + int(hrs2)
    mins = int(mins1) + int(mins2)
    while mins > 59:
        mins -= 60
        hrs += 1
    if mins == 0:
        mins = str(mins) + "0"
    time = str(hrs) + ":" + str(mins)
    print(f"Total time is {time}")

main()
```

## Future Enhancements

- Implement the `HoursToMinutes` function to convert hours and minutes to total minutes.
- Improve user interface and input validation.
- Add more time-related functionalities.

---

Feel free to contribute to this project by forking the repository and submitting pull requests.

For any issues or feature requests, please open an issue on the GitHub repository.

---

**Author:** Muhammad Abdullah

**Contact:** mu.abdullahtech@gmail.com

