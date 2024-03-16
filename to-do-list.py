
from datetime import datetime
import pytz
timeZone_PH = pytz.timezone('Asia/Manila')

currTime_PH = datetime.now(timeZone_PH)

def search_string(finished_task,ongoing_task,list,task_number):
    for ongoing_task in list:
        if ongoing_task == finished_task:
            print("The task" +ongoing_task +"has been removed")
            list.remove(ongoing_task)
            task_number-=1
        else:
            print("Task has not been found. Try again.")
            return None
        



print("\nPhilippines Current Time: ", currTime_PH.strftime("%I:%M:%S %p"))



toDoList = []
i = 1 
j = 1
while True:
    print("\nType the things you plan to do today (Type 'stop' if you are done):")
    task = input(f"Task #{i}: ")

    if task.lower() == 'stop':
        break

    toDoList.append(task)
    i+=1


print("\n")


while True:
    print("\nPhilippines Current Time: ", currTime_PH.strftime("%I:%M:%S %p"))
    print("These are the list of things you will do today. Remove the finished task")
    for task  in toDoList:
        print(f"Task #{j}",task)

    finished_task = input("Input: ")

    found_task = search_string(finished_task,task,toDoList,j)

    


