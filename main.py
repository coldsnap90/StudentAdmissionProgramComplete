
from student_class_admission_program import student
from domesticStudent_class_admission_program import domesticStudent
from internationalStudent_class_admission_program import internationalStudent
from help_func_admission_program import *
from totScore_class_admission_program import totalScore

#function for domestic stu data reading
def dom_stu_list():  
    #instantiation of derived class
    domestic_stu = domesticStudent()

    print('File extraction') 
    try:
        with open("C:\\Users\\cfarb\\Documents\\domestic-stu.txt","r") as file:
                lines = file.readlines()[1:]
                for line in lines:
                    string = line.strip().split(",")
                    first_name = string[0]
                    last_name = string[1]
                    province = string[2]
                    str_cgpa = string[3].strip('.')
                    str_research_score = string[4]
                    cgpa = float(str_cgpa)
                    research_score = int(str_research_score)
                    
                    #error checking data, if any line as an error in any field,skip it, along with mutator methods
                   
                    domestic_stu.set_first_name(first_name.lower())
                    if(domestic_stu.get_first_name() != first_name.lower()):
                        data_corrupted_warning()
                        del first_name,last_name,province,research_score,cgpa,str_cgpa,str_research_score
                        continue
                        
                    
                    domestic_stu.set_last_name(last_name.lower())
                    if(domestic_stu.get_last_name() != last_name.lower()):
                        data_corrupted_warning()
                        del first_name,last_name,province,research_score,cgpa,str_cgpa,str_research_score
                        continue
                        
                    domestic_stu.set_province(province.lower())
                    if(domestic_stu.get_province() != province.lower()):
                        data_corrupted_warning()
                        del first_name,last_name,province,research_score,cgpa,str_cgpa,str_research_score
                        continue
                   
                    domestic_stu.set_cgpa(cgpa)
                    if(domestic_stu.get_cgpa() != cgpa):
                        data_corrupted_warning()
                        del first_name,last_name,province,research_score,cgpa,str_cgpa,str_research_score
                        continue
                    
                    domestic_stu.set_research_score(research_score)
                    if(domestic_stu.get_research_score() != research_score):
                        data_corrupted_warning()
                        del first_name,last_name,province,research_score,cgpa,str_cgpa,str_research_score
                        continue
                    
                    domestic_stu_data_list = domestic_stu.stu_list()
        file.close()               
    except:
        print('Unable to extract data from file, ending program.')
        exit() 
    
    #user inputted menu function loop
    flag = True
    sort_flag = False
    while(flag == True):
        print('----------Domestic Student Registry Menu----------')
        print('1. To search or remove Domestic students from the registry : input 1.')
        print('2. To sort Domestic students registry : input 2.')
        print('3. To print Domestic students registry : 3.')
        print('4. To add a Domestic student to the registry : input 4.')
        print ('5. To print the last student added to the registry : input 5')
        print('6. To delete all students from registry :  input 6') 
        print('7. To restart the domestic student choice menu : input 7.')
        print('8. To continue after sorting the domestic student registry : input e.')
        i = input()
        if(i == '1'):
            domestic_stu_data_list = domestic_stu.search_student(domestic_stu_data_list) #search child student
        elif(i == '2'):      
            list1,E = domestic_stu.sort_merge_lists(domestic_stu_data_list) #merge sort data lists
            sort_flag = True
        elif(i == '3'):
            domestic_stu.print_student_list() #print last student added
        elif(i == '4'):
            domestic_stu.add_student() #add student
        elif(i == '5'):
            domestic_stu.print_student_info() #print list of students
        elif(i == '6'):
            domestic_stu.empty_list() #empty the list of students
        elif(i == '7'):
            dom_stu_list() #restarts
        elif(i.lower() == 'e' and sort_flag == True):
            flag = False
        else:
            print('Make another selection or enter e to quit.')
            print('Note: You cannot proceed without sorting the domestic students first.')
            
    return list1,E
 
 
#second helper function for reading international stu data, same structure as domestic student
#but adds the totalscore that international students have
def int_stu_list():
    
    international_stu = internationalStudent()
    tot_Score = totalScore()  
     
    print('File extraction')
    try:
        with open("C:\\Users\\cfarb\\Documents\\international-stu.txt","r") as file:
        
                    lines = file.readlines()[1:]
                    #data being read from a file to be processed for object creation
                    for line in lines:
                        string = line.strip().split(",")
                        first_name = string[0]
                        last_name  = string[1]
                        country    = string[2]
                        str_cgpa  = string[3].strip('.')
                        str_research_score = string[4]
                        
                        cgpa = float(str_cgpa)
                        research_score = int(str_research_score)
                        str_reading = string[5]
                        reading = int(str_reading)
                        str_listening = string[6]
                        listening = int(str_listening)
                        str_speaking = string[7]
                        speaking = int(str_speaking)
                        str_writing = string[8]
                        writing = int(str_writing)
                        
                        #error checking data before creation of object
                        
                        tot_Score.set_reading(reading)
                        if(tot_Score.get_reading() != reading):
                            data_corrupted_warning()
                            del reading,listening,speaking,writing,first_name,last_name,country,cgpa,research_score
                            continue
                        
                        tot_Score.set_listening(listening)
                        if(tot_Score.get_listening() != listening):
                            data_corrupted_warning()
                            del reading,listening,speaking,writing,first_name,last_name,country,cgpa,research_score
                            continue
                            
                        tot_Score.set_speaking(speaking)
                        if(tot_Score.get_speaking() != speaking):
                            data_corrupted_warning()
                            del reading,listening,speaking,writing,first_name,last_name,country,cgpa,research_score
                            continue
                    
                        tot_Score.set_writing(writing)
                        if(tot_Score.get_writing() == writing):# final total score data point, can sum them after
                            tot_Score.set_score()
                        else:
                            data_corrupted_warning()
                            del reading,listening,speaking,writing,first_name,last_name,country,cgpa,research_score
                            continue
                        #using based class accessors and mutators below for member variables
                        international_stu.set_first_name(first_name.lower())
                        if(international_stu.get_first_name() != first_name.lower()):
                            data_corrupted_warning()
                            del reading,listening,speaking,writing,first_name,last_name,country,cgpa,research_score
                            continue
                    
                        international_stu.set_last_name(last_name.lower())
                        if(international_stu.get_last_name() != last_name.lower()):
                            data_corrupted_warning()
                            del reading,listening,speaking,writing,first_name,last_name,country,cgpa,research_score
                            continue
                    
                        #2nd part of and is for idian data error case.    
                        international_stu.set_country(country.lower())
                        if(international_stu.get_country() != country.lower() and international_stu.get_country()[0] != country.lower()[0] ):
                            data_corrupted_warning() 
                            del reading,listening,speaking,writing,first_name,last_name,country,cgpa,research_score
                            continue
                    
                        international_stu.set_cgpa(cgpa)
                        if(international_stu.get_cgpa() != cgpa):
                            data_corrupted_warning()
                            del reading,listening,speaking,writing,first_name,last_name,country,cgpa,research_score
                            continue
                        international_stu.set_research_score(research_score)
                        if(international_stu.get_research_score() != research_score):
                            data_corrupted_warning()
                            del reading,listening,speaking,writing,first_name,last_name,country,cgpa,research_score
                            continue
                        
                        #if no errors, add objects to object list
                        international_stu.set_score(tot_Score.get_score())
                        I_stu_data_list = international_stu.I_stu_list()
        file.close()
    except:
        print('Unable to extract data from file, ending program.')
        exit()
       
    #while loop menu function for  international students class 
    flag = True
    sort_flag = False
    while(flag == True):
        print('----------international Student Registry Menu----------')
        print('1. To search or remove international students from the registry: input 1.')
        print('2. To sort the registry of international students : input 2.')
        print('3. To print international students registry : input 3.')
        print('4. To add an international student to the registry : input 4.')
        print('5. To print the last student added to the registry : input 5')
        print('6. To delete all international students from registry : input 6') 
        print('7. To restart international students choice menu : input 7.')
        print('8. To continue after sorting international students : input e.')
     
        i = input()
        if(i == '1'):
          I_stu_data_list = international_stu.search_student(I_stu_data_list) #search student
        elif(i == '2'):      
           list2,E = international_stu.I_sort_merge_lists(I_stu_data_list)  #merge lists
           sort_flag = True
           
        elif(i == '3'):
            international_stu.print_student_list() #print student list
        elif(i == '4'):
            international_stu.add_student() #add student
        elif(i == '5'):
            international_stu.print_student_info() #print last student added
        elif(i == '6'):
            international_stu.empty_list() #empties list
        elif(i == '7'):
            int_stu_list() #restart data stream
            
        elif(i.lower() == 'e' and sort_flag == True): #exit condtion
            flag = False
        else:
            print('Make another selection or enter e to quit.')
            print('Note: You must sort the international students in the same format as domestic students.')
            
    return list2,E 


#first class helper function
def main(dom_stu_list,int_stu_list):
    #list to hold merged lists
    complete_student_list = []
    list1,D = dom_stu_list() 
    list2,I = int_stu_list()
   
    if(D == I): #error check to see if listed were suited in the same manner
        print('Sorting order is identical.')
        print('---------- Interpreting Data, Please Wait----------') #message
    else:
        print('Incorrect sort order, restarting.')
        main(dom_stu_list,int_stu_list)
    
    #merging the sorted lists
    complete_student_list = student_operations(list1,list2,complete_student_list,D)
    print_list(complete_student_list) #printing final list
    
    flag = True
    while(flag == True):
        print('Would you like to admit these students to the university?') #option to admit studets
        admit = input()
    
        if(admit.lower() == 'y'):
            print('Students admitted successfully, assigning student numbers now.')
            student_num = 100000
            for i in complete_student_list: #adds student numbers
                i.append(student_num)
                i.append(i[0][0] + i[1] + '@university.com') #gives them a university email
                student_num+=1
            print_final_list(complete_student_list)
            print('Admission completed, ending program.')
            exit()
                
        elif(admit.lower == 'n'): #clears delete stu list, gives option to run program again            
            print('Removing students from consideration')
            complete_student_list[:] = []
            print('Would you like to reconsider previous students?')
            enter = input()
            if(enter == 'y'):
                main(dom_stu_list,int_stu_list) #restart program and sorting process
            else:
                print('Ending program....')
                exit()
    
    
     

#first class function call
main(dom_stu_list,int_stu_list) 
