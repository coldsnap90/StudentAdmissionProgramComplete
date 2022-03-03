from student_class_admission_program import student
from totScore_class_admission_program import totalScore


#international students (child class) of student
class internationalStudent(student):
    
    #international student lists to store data points
    I_student_list = []
    student_list = []
    
    #derived class constructor and instances
    def __init__(self,country = None,score = None,first_name = None,last_name = None,research_score = None,cgpa = None):
        self._country = country
        self._score = score
        super(internationalStudent,self).__init__(first_name,last_name,research_score,cgpa)
    
            
    #accessor & mutators-----------------------------------------------
    #extra data points country and score, along with error checking
    def set_country(self,country):
        list = ['china','india','korea','iran','idian']
        if self.error_check_str(country) == True:
            if country in list:
                if(country == list[4]):
                    self._country = 'india'
                else:
                    self._country = country
            
    def get_country(self):
        return self._country

    def set_score(self,score):
            if(self.error_check_int(score) == True):
                self._score = score
    
    def get_score(self):
        return self._score
    #----------------------------------------------------------------- 
        
    #derived class print method
    def print_student_info(self):    
        if(self._first_name != None and self._last_name != None and self._country != None and self._research_score  != None and self._cgpa != None):
            print('International Student : ', self._first_name,self._last_name, ', Research Score : ',self._research_score,
                ', Cgpa : ', self._cgpa, ', Country: ', self._country,', Total Score: ',self._score)
        else: 
            print('Invalid data point entry.')
        
    #derived print method for international student list
    def print_student_list(self):
        print('Printing International student list: ')
        for i in self.student_list:
            print(' ',i,sep='')
      
    #international student list data appender, copy list -> clear ->repeat
    def I_stu_list(self):
            self.I_student_list.append(self._first_name)
            self.I_student_list.append(self._last_name)
            self.I_student_list.append(self._country)
            self.I_student_list.append(self._cgpa)
            self.I_student_list.append(self._research_score)
            self.I_student_list.append(self._score)
            self.student_list.append(self.I_student_list.copy())            
            self.I_student_list.clear()
 
    #merge sort method, Big- O : O(n*logn)  
    def stu_sort_merge(self,i,left,right):
        if len(left)== 0:
            return right
        if len(right)== 0:
            return left
        result =[]
        l_index = r_index = 0
        
        #same sorting method as domesstic student
        while len(result) < (len(left) + len(right)):
       
            if left[l_index][i] <= right[r_index][i]:
                result.append(left[l_index])
                l_index+=1
            else:
                result.append(right[r_index])
                r_index+=1
            if(r_index == len(right)):
                result += left[l_index:]
                break
            if(l_index == len(left)):
                result+= right[r_index:]
                break
        return result
    
    
    #2nd merge sort method for recursive portion, sorts based on data point selected inside list
    def merge_sorts(self,array,i): #i value is based name,cgpa,research_score excetra
        if len(array) < 2:
            return array
        midpoint = len(array)//2
        return self.stu_sort_merge(i,left=self.merge_sorts(array[:midpoint],i),right = self.merge_sorts(array[midpoint:],i))
    
    #method to initiate the sorting
    def I_sort_merge_lists(self,student_list):         
        #input menu for sorting choice controlled by bool
        flag = True
        while flag == True:
            print('1. Enter 0 to sort by first name.') 
            print('2. Enter 1 to sort by last name.') 
            print('3. Enter 2 to sort by country') 
            print('4. Enter 3 to sort by cgpa.')
            print('5. Enter 4 to sort by research score.') 
            print('6. Enter 5 by total Score.')
            print('7. Enter r to return the registry')
            print('Note: You must sort and return international students using the same data point as domestic students for '+
                  'intended results.')  
            E = input('Enter: ')
            
            #conditional statements on what data point to sort by
            #first name
            if E.lower() == '0':
                self.student_list = self.merge_sorts(self.student_list,0)
                print('List sorted by first name:')
                for i in self.student_list:
                    print(i)
                choice = 0   
            #last name
            elif E.lower() == '1':
                self.student_list = self.merge_sorts(self.student_list,1)
                print('List sorted by last name:')
                for i in self.student_list:
                    print(i)
                choice = 1
            #country
            elif E.lower() == '2':
                self.student_list = self.merge_sorts(self.student_list,2)
                print('List sorted by last country:')
                for i in self.student_list:
                    print(i)
                choice = 2
            #research score
            elif E.lower() == '3':
                self.student_list = self.merge_sorts(self.student_list,4)
                print('List sorted by research score:')
                for i in self.student_list:
                    print(i)
                choice = 3
            #cgpa
            elif E.lower() == '4':
                self.student_list = self.merge_sorts(self.student_list,3)
                print('List sorted by cgpa:')
                for i in self.student_list:
                    print(i)
                choice = 4
            #total score
            elif E.lower() == '5':
                self.student_list = self.merge_sorts(self.student_list,5)
                print('List sorted by total score:')
                for i in self.student_list:
                    print(i)
                choice = 5
            #returns sorted list
            elif E.lower() == 'r':
                return self.student_list,choice  #to make sure sort return inputs are =
                
            else:
                print('Incorrect selection, please re-enter.')
                      
    #search for international student name in registry           
    def search_student(self,internationalStudent):
        print('Would you like to find a student from the registry?')
        print('1. Enter y to find or n to return.')
        Z = input()
        
        #decision tree, same structure as domestic student method
        if Z.lower() == 'y':
         
          E_flag = False
          while E_flag == False:
            
            self.print_search_message()
            E = input() # input to search by name or academics
           
             
            if E.lower() == 'name':  #look up student by first and last                
                
                name_flag = False
                while name_flag == False: #name entry control
                    print('Input first Name: ')
                    first = input()
                    print('Input a last name: ')
                    last = input()
                    if self.error_check_str(first) == True and self.error_check_str(last) == True:
                        name_flag = True
                    else:
                        self.print_entry_error()
                        
                f_name = False
                l_name = False
                
                for i in self.student_list:
                        #searches through list index's that store names if bool f & l name are true prints name
                        if first.lower() == i[0] and last.lower() == i[1]:
                            print(first,last)
                            f_name = True
                            l_name = True
                            

                        if(f_name == True and l_name == True): #gives option to delete found student
                            print('Do you want to delete this student?')
                            print('1. Enter y to delete  student.')
                            print('2. Enter e to return to the previous menu. ')
                            print('3. Enter another key to return to the main menu.')                           
                            #delete student then break
                            remove = input()
                            if (remove.lower() == 'y'):
                                self.student_list.remove(i)
                                break
                            elif(remove.lower() == 'e'):
                                break
                            else:
                                return
                if f_name == False and l_name == False:
                    print('Student not found.')
                        
            #same structure as the domestic student class but one data point added for total socre      
            elif E.lower() == 'academic':
                flag = True
                while flag == True:
                    print('\n1. To search students based on cgpa minimum and error : input "cgpa".')
                    print('2. To search students based on research score minimum and error : input "rs".')
                    print('3. To search students based on total score minimum and error : input "ts".')
                    print('4. To to delete students who fail to meet the minimum threshold : input "y".')
                    print('5. To return to previous menu : input "n".')
                    print('6. To return to start menu : input "r".')
                    cin = input()
                    
                    #checks studens based on miminum or faulty  score
                    if cin.lower() == 'cgpa':
                        for i in self.student_list:
                            if i[3] < 3 or i[3] > 4.33: #cgpa of 3.00 is minimum or else they get dropped from registry
                                print(i[0],i[1],' - ',i[3]) #prints name and cgoa
        
                    if cin.lower() == 'rs':
                        for i in self.student_list:
                            if i[4] < 75 or i[4] > 100: #research score of 75 is minimum
                                print(i[0],i[1],' - ',i[4]) #prints name and rs
                                
                    if cin.lower() == 'ts':
                        for i in self.student_list:
                            if i[5] > 120 or i[5] < 80: #total score 80 is minimum 
                                print(i[0],i[1],' - ',i[5]) #prints name and ts
                        
                    
                    #removes students based on under minima or above maxima scores
                    if cin.lower() == 'y':
                        
                        print('1. Removing all international students who dont make the minimum research score threshold, < 75.')
                        print('2. Removing all international students who dont make the minimum cgpa threshold, < 3.00.')
                        print('3. Removing all international Students who dont make the minimum score threshold, < 80.')
                        tempList = [] #create a new list to hold acceptable values while disgarding values below threshold
                        
                        for i in self.student_list:
                            #appends student with research score and cgpa above minimum
                            if i[4] >= 75 and i[4] <= 100 and i[3] >= 3 and i[3] <= 4.33 and i[5] >= 80 and i[5] <= 120:
                                print(i[0],i[1],': Removed')
                                tempList.append(i[:])
                                
                            else:
                                print('Removing Name : ',i[0],i[1])
                          
                        self.student_list = tempList #assign new list
                                
                    if cin.lower() == 'n': #break loop
                        flag = False
                        
                    #return list with removed students
                    if(cin.lower() == 'r'):
                        return self.student_list
                                
            elif E.lower() != 'name' or E.lower() != 'academic' or E.lower() != 'n':
                self.print_entry_error()
             
        else:
            return #exit conidition
    
    #adds new student to the registry, same method as dom student class but extra point for score
    def add_student(self):
        i = 0
        while(i < 7):
            print('Input first name')
            f_name = input()
            self.set_first_name(f_name) #sets new first name of student
            if self.get_first_name() == f_name:
                i+=1
            else:
                self.print_entry_error() #bad entry message and restart while lop
                i = 0
                continue
            
            print('Input Last Name')
            l_name = input()
            self.set_last_name(l_name) #sets new last name
            if self.get_last_name() == l_name:
                i+=1
            else:
                self.print_entry_error()
                i = 0
                continue
            
            print('Input country.')
            print('Currently, were only accepting international students from iran, china, korea, and india.')
            s_country = input()
            self.set_country(s_country) #sets country, error checking involved for countries allowed
            if self.get_country() == s_country:
                    i+=1
            else:
                self.print_entry_error()
                i = 0
                continue
            
            print('Input cpga.')
            s_cgpa = input()
            try:
                s_cgpa = float(s_cgpa) #try catch for bad input value
                self.set_cgpa(s_cgpa)
            except:
                self.print_entry_error()
                i = 0
                continue
                
            if self.get_cgpa() == s_cgpa:
                i+=1
            else:
                self.print_entry_error()
                i = 0
                continue
            
            print('Input research score.')
            s_research_score = input()
            try:
                s_research_score = int(s_research_score) #try catch for bad int
                self.set_research_score(s_research_score)
            except:
                self.print_entry_error()
                i = 0
                continue
            if self.get_research_score() == s_research_score:
                i+=1
            else:
                self.print_entry_error()
                i = 0
                continue
                
            print('Input total score.')
            t_score = input()
            try: #try catch for bad int
                t_score = int(t_score)
                self.set_score(t_score)
            except:
                self.print_entry_error()
                i = 0
                continue
            
            if self.get_score() == t_score:
                i+=1
            else:
                self.print_entry_error()
                i = 0
                continue
            
            #sets new student if i is increased to 6
            if i == 6:
                self.I_stu_list()
                
                print('1. Would you like to enter another student? Type y to enter a new student or enter any key to quit')
                enter = input()
                #restart loop for another entry
                if enter.lower() == 'y':
                    i = 0
                #quit while
                else:
                    return #exits while loop and method
                    

    #method to clear list   
    def empty_list(self):
        self.I_student_list[:] = []
        self.student_list[:] = []
       
                   
                   