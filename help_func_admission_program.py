#helper functions for main
def student_operations(list1,list2,complete_student_list,i):
    
    def merge_lists(list1,list2,complete_student_list,i): #inner function, recursive sort algorithim for two previously sorted lists
        counter1 = 0 #counters for list length
        counter2 = 0
        i = int(i) #sorting selection chosen
        #merge the lists based on previous sorting protocal
        print('----------Analyzing Studesnts, Please Wait----------')
        
        if(len(list1) == 0):
            complete_student_list = list2
        if(len(list2)==0):
            complete_student_list = list1
      
        #overall sorting favours domestic students, sorts low to high
        while(counter1 != len(list1) and counter2 != len(list2)):
            if(list1[counter1][i] > list2[counter2][i]):
                complete_student_list.append(list2[counter2])
                counter2+=1
            elif(list1[counter1][i] < list2[counter2][i]):
                complete_student_list.append(list1[counter1])
                counter1+=1
            else:
                complete_student_list.append(list1[counter1])
                counter1+=1
                
        if(counter1 == len(list1)): #if list1 reaches end append rest of list22
                complete_student_list+=list2[counter2:]
        else:
             complete_student_list+=list1[counter1:]   

        #return new sorted list
        return complete_student_list
        
    return merge_lists(list1,list2,complete_student_list,i)
                     
# ---------- helper functions for main ------------------------------------------

#helper function to print final merged list, adds a student number and email
def print_final_list(complete_student_list):
    print('----------Students Admitted----------')
    flag = True
    while(flag == True):
        for i in complete_student_list:
            print('Student name : ',i[0],i[1], ', Country: ',i[2], ', Cgpa: ',i[3],', Research Score: ',i[4],end='')
            if(i[5] <= 120):
                print(', Total Score: ',i[5],end='')
            else:
                print(', Student number: ',i[5],end='')
            if(isinstance(i[6],int)==True):
                print(', Student number: ',i[6],end='')
            else:
                print(', Student email: ',i[6],end='')
            try:
                if(isinstance(i[7],str)==True):
                    print(', Student email: ',i[7],end='')
            except:
                pass
            print('\n'+'----------------------------------------------------------------------------------------------------'+
                  '------------------------------------------------')
        i = input('Input again : ')
        if( i == 'y'):
            flag = True
        else:
            flag = False
            
#error print warning for bad chouce
def print_warning():
    print('Make another selection or enter e to quit.')
    print('Note: You cannot proceed without sorting the domestic students first.')
    
#print list method
def print_list(list): 
    for i in list:
        print(i)
#error func return false, print func  
def data_corrupted_warning():
    print('Data corrupted, deleting student.')

#---------------------------------------------------------------------------------       
    

