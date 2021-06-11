# 1. Category input]
with open("categories.txt",'a') as file:
    pass
with open("todo.txt",'a') as file2:
    pass
category=""
todo=""
# 2. Check if category exists if not write input in category while category not in in file\

def check_categories(category:str):
    count = 0
    with open("categories.txt", 'r') as file:
        for category_name in file:
            if category == category_name.replace(category_name[-1], ""):
                count += 1
        return count

def write_item(category:str):
    while category != 'Q':
        category = (input("Please insert category: ")).title()

        if category == 'Q':
            break
        elif check_categories(category) != 0 or category.isspace() is True :
            print("Oops, category already exists.")
        else:
            with open("categories.txt", 'a') as file:
                file.write(f"{category}\n")
        continue

def check_todo(todo: str):
    count = 0
    with open("todo.txt", 'r') as file2:
        for todo_name in file2:
            if todo == todo_name.replace(todo_name[-1], ""):
                count += 1
        return count


def write_todo(todo: str):
    category = (input("Please select the category: ")).title()

    check_categories(category)
    while check_categories(category) == 0:
        category = (input("Doesn't exist. Please select category: ")).title()
    else:
        selected_category = category

    todo = (input("Please insert task: ")).title()
    check_todo(todo)
    while todo != 'Q':
        todo = (input("Please insert task: ")).title()
        if todo == 'Q':
            break
        elif check_categories(todo) != 0 or todo.isspace() is True:
            print("Oops, task already exists.")
        else:
            deadline=input("  Deadline: ")
            person_incharge=input("    Person in charge: ")
            with open("todo.txt", 'a') as file2:
                file2.write(f"{category} {deadline} {person_incharge} {todo}\n")
        continue

write_item(category)
write_todo(todo)

    # for category_list in file:
    #     print(category_list)
    #     if test not
        # for todo_name in list(category_list):
        #     print(todo_name)
        # if category != file:
        #     with open("categories.txt", 'a') as file:
        #         file.write(f"{category}\n")
        #         break


# def category_creator():
#
#     with open('category.txt') as file:
#         content = file.read()
#         category = ""
#         while category != 'q':
#             category=input("Please enter the type of lists you want to create (enter 'q' to exit): ")
#             if category =='q':
#                 break
#             else:
#                 local_list = []
#                 while category in content:
#                     category = input(f"'{category}' already exists, try again: ")
#                     # if category not in content:
#                     #     for word in local_list:
#                     #         while category in local_list:
#                     #             category = input(f"'{category}' already exists, try again: ")
#
#                     # if category not in local_list:
#                     #     with open('category.txt', 'a') as file:
#                     #         file.write(f"{category} ")
#                     #         # local_list.append(category)
#
#                 else:
#                     with open('category.txt', 'a') as file:
#                         file.write(f"{category} ")
#                         print(f"{category} added")
#         return file
#
# category_creator()
