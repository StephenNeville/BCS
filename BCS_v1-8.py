# Author: Stephen Neville
# Date:
# This program will attempt to explain various paradigms used in programming
# I will use a GUI interface which will allow a user to select
# and read a description of each type or paradigm and also provide
# coded examples of each
# Easygui is being used which is based on tkinter and developed by
# Stephen Ferg, the creator of easygui
# Students can copy the code form the GUI window and then paste and run the code in Python IDLE 
    
import easygui as eg
import os
    
def choice_list_About():
    
    """
    This function will call on functions from the module easygui.
    It calls on msgbox, choicebox, codebox and ccbox to create the GUI interface

    This procedure will read in files (a description of each paradigm) and output them to a GUI window
    """
    # use text box here to describe program
    eg.msgbox("Let`s take a look at brief description of three  different programming paradigms: Procedural(Imperative),Functional and Object Oriented ")

    msg ="Choose one of the following from the list"
    title = "About Paradigms"
    choices = ["Introduction", "Procedural", "Functional", "Object Oriented"]
    choice = eg.choicebox(msg, title, choices)

    # This section will check which of the choices are selected
    # and read in the associated  file

    #Select introduction to three type programming paradigms
    if choice == "Introduction":
        filename = os.path.normcase("about_paradigms/intro.txt")
        f = open(filename, "r")
        text = f.readlines()
        f.close()
        eg.codebox("Contents of file " + filename, "Show File Contents", text)
        
    #Select and read in file about procedural paradigm    
    elif choice == "Procedural":
        filename = os.path.normcase("about_paradigms/proc.txt")
        f = open(filename, "r")
        text = f.readlines()
        f.close()
        eg.codebox("Contents of file " + filename, "Show File Contents", text)

    #Select and read in file about functional paradigm   
    elif choice == "Functional":
        filename = os.path.normcase("about_paradigms/func.txt")
        f = open(filename, "r")
        text = f.readlines()
        f.close()
        eg.codebox("Contents of file " + filename, "Show File Contents", text)

    #Select and read in file about object oriented  paradigm   
    elif choice == "Object Oriented":
        filename = os.path.normcase("about_paradigms/oop.txt")
        f = open(filename, "r")
        text = f.readlines()
        f.close()
        eg.codebox("Contents of file " + filename, "Show File Contents", text)
    

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if eg.ccbox(msg, title):     # show a Continue/Cancel dialog
        Para_buttonbox()
    else:
        # to create a procedure called quit program
        print("Quit Program")          # user


    
def choice_list_Procedural():
    
    """
    This function will call on functions from the module easygui.
    It calls on msgbox, choicebox, codebox and ccbox to create the GUI interface
    """
    # use text box here to describe program
    eg.msgbox("This section contains examples of code for Procedural(Imperative) programming style")

    msg ="Choose from the program examples"
    title = "Examples of Programs using a Procedural Style(Paradigm) "
    choices = ["square_nums", "add_two_numbers", "sample3"]
    choice = eg.choicebox(msg, title, choices)

    # This section will check which of the choices are selected
    # and read in the associated  file
    if choice == "square_nums":
        filename = os.path.normcase("sample_code/proc/square_proc.py")
        f = open(filename, "r")
        text = f.readlines()
        f.close()
        eg.codebox("Contents of file " + filename, "Show File Contents", text)
    elif choice == "add_two_numbers":
        filename = os.path.normcase("sample_code/proc/sample2.txt")
        f = open(filename, "r")
        text = f.readlines()
        f.close()
        eg.codebox("Contents of file " + filename, "Show File Contents", text)
    elif choice == "sample3":
        filename = os.path.normcase("sample_code/proc/sample3.txt")
        f = open(filename, "r")
        text = f.readlines()
        f.close()
        eg.codebox("Contents of file " + filename, "Show File Contents", text)
        
    elif choice == "sample3":
        filename = os.path.normcase("sample_code/proc/sample3.txt")
        f = open(filename, "r")
        text = f.readlines()
        f.close()
        eg.codebox("Contents of file " + filename, "Show File Contents", text)
    else:
        

        msg = "Do you want to continue?"
        title = "Please Confirm"
        if eg.ccbox(msg, title):     # show a Continue/Cancel dialog
            Para_buttonbox()
        else:
            print("Quit Program")          # user
            

def choice_list_Functional():
    
    """
    This function will call on functions from the module easygui.
    It calls on msgbox, choicebox, codebox and ccbox to create the GUI interface
    """
    # use text box here to describe program
    eg.msgbox("This section contains examples of code for a functional programming style")

    msg ="Choose afrom one the the examples in the list"
    title = "Examples of Programs using a Procedural Style(Paradigm) "
    choices = ["square_nums_map", "square_nums_lambda", "sample3"]
    choice = eg.choicebox(msg, title, choices)

    # This section will check which of the choices are selected
    # and read in the associated  file
    if choice == "square_nums_map":
        filename = os.path.normcase("sample_code/func/square_nums_map.py")
        f = open(filename, "r")
        text = f.readlines()
        f.close()
        eg.codebox("Contents of file " + filename, "Show File Contents", text)
    elif choice == "square_nums_lambda":
        filename = os.path.normcase("sample_code/func/square_nums_lambda.py")
        f = open(filename, "r")
        text = f.readlines()
        f.close()
        eg.codebox("Contents of file " + filename, "Show File Contents", text)
    elif choice == "sample3":
        filename = os.path.normcase("sample_code/func/sample3.txt")
        f = open(filename, "r")
        text = f.readlines()
        f.close()
        eg.codebox("Contents of file " + filename, "Show File Contents", text)
        
    elif choice == "sample3":
        filename = os.path.normcase("sample_code/func/sample3.txt")
        f = open(filename, "r")
        text = f.readlines()
        f.close()
        eg.codebox("Contents of file " + filename, "Show File Contents", text)
    else:
        

        msg = "Do you want to continue?"
        title = "Please Confirm"
        if eg.ccbox(msg, title):     # show a Continue/Cancel dialog
            Para_buttonbox()
        else:
            print("Quit Program")          # user

def choice_list_ObjectOriented():
    
    """
    This function will call on functions from the module easygui.
    It calls on msgbox, choicebox, codebox and ccbox to create the GUI interface
    """
    # use text box here to describe program
    eg.msgbox("This section contains examples of code for Object-oriented programming style")

    msg ="Choose an example program which you can copy, paste and test in Python"
    title = "Examples of Programs using an Object-oriented programmingStyle(Paradigm) Feel free to copy, paste and test in Python "
    choices = ["classHuman", "classEmployee", "sample3"]
    choice = eg.choicebox(msg, title, choices)

    # This section will check which of the choices are selected
    # and read in the associated  file
    if choice == "classHuman":
        filename = os.path.normcase("sample_code/oop/class_human.py")
        f = open(filename, "r")
        text = f.readlines()
        f.close()
        eg.codebox("Contents of file " + filename, "Show File Contents", text)
    elif choice == "classEmployee":
        filename = os.path.normcase("sample_code/oop/class_Employee.py")
        f = open(filename, "r")
        text = f.readlines()
        f.close()
        eg.codebox("Contents of file " + filename, "Show File Contents", text)
    elif choice == "sample3":
        filename = os.path.normcase("sample_code/oop/sample3.txt")
        f = open(filename, "r")
        text = f.readlines()
        f.close()
        eg.codebox("Contents of file " + filename, "Show File Contents", text)
        
    elif choice == "sample3":
        filename = os.path.normcase("sample_code/oop/sample3.txt")
        f = open(filename, "r")
        text = f.readlines()
        f.close()
        eg.codebox("Contents of file " + filename, "Show File Contents", text)
    else:
        

        msg = "Do you want to continue?"
        title = "Please Confirm"
        if eg.ccbox(msg, title):     # show a Continue/Cancel dialog
            Para_buttonbox()
        else:
            print("Quit Program")          # user
  



def Para_buttonbox():
    """
    This function calls the function buttonbox
    This function will create a set of buttons to choose from
    It will return the button selected

    arguments : none
    returns: value
    """
    
    value = eg.buttonbox(
        title="Programming Paradigms in Python",
        msg="If you want to know more about programming paradigms then choose from one of the following options below. About Programming Paradigms provides a brief explanation. Each of the other buttons link to code examples for each paradigm",
        choices=["About Programming Paradigms", "Procedural", "Functional", "Object Oriented","Quit"],
        default_choice="About Programming Paradigms")
    print("Return: {}".format(value))
    return value
    
def menu_choice(choiceP):
    """
    This procedure will call the functions which display a gui with a list
    of choices.
    arguments : choiceP
    returns: none
    """
    if choiceP == "About Programming Paradigms":
        choice_list_About()
    elif choiceP == "Procedural":
        choice_list_Procedural()
    elif choiceP == "Functional":
        choice_list_Functional()        
    elif choiceP == "Object Oriented":
        choice_list_ObjectOriented()
    
    else:
        print("another menu choice")
        
    
   



def main():
    choiceP =" "
    while choiceP != "Quit":
        choiceP = Para_buttonbox()
        print("button choice is: ", choiceP)
        menu_choice(choiceP)
        
    print("You have quit the program")    
    


main()        
    





