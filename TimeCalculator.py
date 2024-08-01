import os

def main():
    while True:     # Runs until Quit
        choice = menu()     # Print menu and return the choice of the user

        match choice:       # goes to specific case depending upon the user's choice
            case "1":
                MinutesToHours()      # Convert minutes to hours
            case "2":
                HoursToMinutes()
            case "3":
                AddTime()      # adds two times
            case "0":
                os.system("clear")
                break       # breaks out of the loop to exit

    print("EXITING!!!")     # last message before exiting

def menu():
    print("Time Calculator")
    print("Menu:")
    print("1. Convert Minutes to Hours")
    print("2. Convert Hours to Minutes")        # TODO 
    print("3. Add times in format of 00:00")        
    print("0. Exit")
    choice = input("Choice: ")
    return choice


def MinutesToHours():
    os.system("clear")
    print("Minutes to Hour Converter")
    print()
    hour = 0
    minutes = int(input("Enter Time in minutes: "))
    while minutes > 59:
        minutes -= 60
        hour += 1

    print(f"{hour}:{minutes}")
    print()

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
    print()
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

    print()


main()
