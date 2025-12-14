To_do_list = []
Completed_tasks = []

def add():
    if value == 1:
        added_task = input("Task you want to add: ")
        To_do_list.append(added_task)
        
def remove():
    if value == 2:
        removed_task= input("Task you want to remove:")
        To_do_list.remove(removed_task)
def edit() :
    if value == 3:
        edited_task= input(" Task you want to remove")
        To_do_list.remove(edited_task)
        ed_task = input("Task you want to add ")
        To_do_list.append(ed_task)
def completed() :
    if value == 4:
        task_completed= input(" Task you've completed successfully")
        To_do_list.remove(task_completed)
        Completed_tasks.append(task_completed)
def exit():
    if value == 5:
        print("byeee")
    
while True:
    print("---TO_DO_LIST---")
    print(To_do_list)
    print("---COMPLETED_TASK---")
    print(Completed_tasks)
    print("===MAIN MENU== \n 1.Add tasks 2. Remove any task of your choice 3. Edit the tasks all you want 4. Mark as completed 5. Exit")
    
    value = int(input("Give me your choice number from the main menu: "))
    add()
    remove()
    edit()
    completed()
    exit()
    
    
    
    if value == 5:
        break
    
    
