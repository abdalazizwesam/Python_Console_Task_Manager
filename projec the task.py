
# Disgin The Project

print("<-=-=-=-= TASKS PROGRAMING =-=-=-=->")
print("=================================")
my_task = []
while True:
    # عرض العمليات للمستخدم    
    i = 1      
    print("1.Insert The New Task")
    print("2.Select The All Taskes")
    print("3.Delet The Task of The Copmlitly") 
    print("4.Exit The Programing")
    print("==============================") 
    Enter = int(input("Enter The Number of Opration : "))
    
    
    if Enter == 1 :
        Enter_Task = str(input("Enter The New Your Task "))
        my_task.append(Enter_Task)
        print("Insert is sucssifly ")
        print("==============================") 

        
    elif Enter == 2 :
        if my_task == []:
            print("Dosint Task")
            print("==============================") 

        else : 
            print("The All Taskes is ")
            for task in my_task:
                print( i , " : " , task)
                i += 1
            print("==============================") 

            
    elif Enter == 3 :
        for taskes in my_task:
            print( i ," : " , taskes) 
            i += 1
        Enter_Deleat = int(input("Enter The Number of Task Deleat : "))
        if Enter_Deleat > len(my_task) or Enter_Deleat < 0  :
            print("The Enter Number Greter Than Number of Taskes In List Or Enter Number Less Than Zero ")
        else :
            my_task.pop(Enter_Deleat - 1)
            print(" Deleat is sucssifly")
            print("==============================") 

    elif Enter == 4 :
        print("The Exit From Programing is Complitly")
        break
    
    else :
        print(" The Out Of Range")
        print("==============================") 

    
        
        
        
        
        
        