import datetime
# task_list=[]
#
task=""
# while task != 'q':
#     task=input("Enter task: ")
#     task_list.append(task)


with open('category.txt','a', newline="\n") as file:
    while task != 'q':
        task=input("Please enter category: ")
        if task != 'q':
            file.write(task)



# category_choice=input("Please enter type of list:")
#

#
with open('category.txt', 'r') as file:

    print(list(file))

# def date():
#     year=int(input("Year: "))
#     month=int(input("Month: "))
#     day=int(input("Day: "))
#     hour=int(input("Hour: "))
#     minutes=int(input("Minutes: "))
#     deadline=datetime.datetime(year,month,day,hour,minutes)
#     return deadline
