import os

words = { #Here, we´re creating a dictionary named "words" that will give us the numbers related with the key words
"erase": 1,
"new task": 2,
"see the tasks": 3
}

answer_2 = input("Do you want to use this program?  ")

while answer_2 == "yes":
    answer = words.get(input("What do you want to do:  " )) #asks the user what he wants to do and get the command in the dictionary related with the answer
    if answer == 1: #first case
        trash_word = input("Tell me the word you want to delete:  ")#gets the word that the user wants to delete

        #start with
        with open(r"C:\Users\nunes\NovaPasta\tasks_programming\To-dolist(python)\tasks.txt", "r") as i: #opens the file with "read mode"
            my_list = [] #creates an array that will contain the words the user wants to keep

            file = i.readline() #reads the first line of the file
            number = 0
            #start while
            while file: #repeat loop that will stop when the string in variable "file" is empty
                number += 1
                if file != (str(number) + ". " + trash_word + "\n"): #writes in the list all the words that the user wnats to keep in the list but the "trash word"
                    result = (str(number) + ". " + file[3:])
                    my_list.append(result)
                    print(my_list)
                else:
                    number -= 1
                file = i.readline()
            #end while
        #end with
        #start with
        with open(r"C:\Users\nunes\NovaPasta\tasks_programming\To-dolist(python)\tasks.txt", "w") as a:
            pass
        #end with

        #start with
        with open(r"C:\Users\nunes\NovaPasta\tasks_programming\To-dolist(python)\tasks.txt", "a") as a:
                a.writelines(my_list)
        #end with


    elif answer == 2:
        new_task = input("Write here the new task:  ") + "\n"
        number = 1

        print("Current working directory:", os.getcwd())
        with open(r"C:\Users\nunes\NovaPasta\tasks_programming\To-dolist(python)\tasks.txt", "r") as f:
            file = f.readline()
            while file:
                number += 1
                file = f.readline()
            
            number = str(number)

        with open(r"C:\Users\nunes\NovaPasta\tasks_programming\To-dolist(python)\tasks.txt", "a") as f:
            f.write(number + ". " + new_task)

    elif answer == 3:
        with open(r"C:\Users\nunes\NovaPasta\tasks_programming\To-dolist(python)\tasks.txt", "r") as f:
            file = f.readline()
            while file:
                print(file, end="")
                file = f.readline()
    answer_2 = input("Do you want to keep using this program?  ")
    

    

    



