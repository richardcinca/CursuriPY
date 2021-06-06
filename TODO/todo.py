import datetime

def deadline():
    print('Please select deadline date: ')
    year=int(input("Year: "))
    month=int(input("Month: "))
    day=int(input("Day: "))
    hour=int(input("Hour: "))
    minutes=int(input("Minutes: "))
    #deadline_date=datetime.datetime(year,month,day,hour,minutes)
    return year, month, day, hour, minutes


def category_creator():
    with open('category.txt', 'a') as file:
        task = ""
        while task != 'q':
            task=input("Please enter the type of lists you want to create (enter 'q' to quit): ")
            file.write(f"{task} ")

        return file

category_creator()




category_choice = input("Please enter type of list:")

# with open('category.txt', 'r') as file:
#     print(list(file))


with open('category.txt', 'r') as file:
    selected_cat = ""
    for element in list(file):
        # print(type(element))
        while category_choice not in element:
            category_choice = input("Category doesn't exist. Please enter again category:")
        else:
            selected_cat = category_choice
            with open(f'{selected_cat}_list.txt', 'a') as file2:
                person = input("Please enter person in charge (enter 'q' to quit): ")
                file2.write(f"Person in charge: {person}   \n")
                print('Please select deadline date: ')
                year = int(input("Year: "))
                month = int(input("Month: "))
                day = int(input("Day: "))
                hour = int(input("Hour: "))
                minutes = int(input("Minutes: "))
                general_deadline_date = datetime.datetime(year, month, day, hour, minutes)
                file2.write(f"Deadline - {general_deadline_date}\n")
                todo = ""
                while todo != 'q':
                    todo = input(f"Please enter to-do task for {selected_cat} (enter 'q' to quit): ")
                    if todo== 'q':
                        break
                    deadline_choice=input('Do you want to set a deadline time? (type yes/no):   ')
                    if deadline_choice == "yes":
                        print('Please select deadline time: ')

                        hour = int(input("Hour: "))
                        minutes = int(input("Minutes: "))
                        deadline_date = datetime.datetime(year, month, day,hour, minutes)
                        file2.write(f"{todo} - {deadline_date}\n")
                    elif deadline_choice == "no":
                        file2.write(f"{todo} \n")
                    else:
                        deadline_choice=input('Do you want to set a deadline? (type yes/no):   ')
                else:
                    break





