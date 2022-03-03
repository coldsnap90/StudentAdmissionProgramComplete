from unicodedata import name
from student_class_admission_program import student
#domestic students (child class) of student 
class domesticStudent(student):
    #lists to store data points
    D_student_list = []
    student_list = []
    
    #constructor and instances
    def __init__(self,province=None,first_name=None,last_name=None,research_score=None,cgpa=None):
        self._province = province
        super(domesticStudent,self).__init__(first_name,last_name,research_score,cgpa)
                
    #------- accessors & mutators---------------------------------------------------------
    
    #dom stu derived has additional member variable province, error checking for real provinces    
    def set_province(self,province):
        prov_list =['bc','ab','mb','sk','on','qc','ns','pe','wh','nl','yt','nt','nb','nu']
        if self.error_check_str(province) == True and province.lower() in prov_list:
            self._province = province
        
    def get_province(self):
        return self._province
    # ------------------------------------------------------------------------------------
    
    # ------ class methods
    
    #return object string data
    def __str__(self):
        return f'{self._province}'
    
    #print function, prints list of domestic students
    def print_student_list(self):
        print('Printing Domestic student list : ')
        for i in self.student_list:
            print(i)
        
    #groups data for each student, appends it to list, copy->clear-> repeat
    def stu_list(self):
        self.D_student_list.append(self._first_name)
        self.D_student_list.append(self._last_name)
        self.D_student_list.append(self._province)
        self.D_student_list.append(self._cgpa)
        self.D_student_list.append(self._research_score)
        self.student_list.append(self.D_student_list.copy())
        self.D_student_list.clear()
    
    #merge sort, Big- O : O(n*logn)  
    def stu_sort_merge(self,i,left,right):
        if len(left)== 0:
            return right
        if len(right)== 0:
            return left
        result =[]
        l_index = r_index = 0
        
        while len(result) < len(left) + len(right):
            #merge sort conditional logic, self evident,the extra index [i] is for data points
            if left[l_index][i] <= right[r_index][i]:
                result.append(left[l_index])
                l_index+=1   
            else:
                result.append(right[r_index])
                r_index+=1
                
            if r_index == len(right):
                result += left[l_index:]
                break
            if l_index == len(left):
                result+= right[r_index:]
                break
            
        return result
    
    #2nd merge sort method for recursive portion, i parameter is for member variable types
    def merge_sort(self,array,i):
        if len(array) < 2:
            return array
        midpoint = len(array)//2
        return self.stu_sort_merge(i,left=self.merge_sort(array[:midpoint],i),right = self.merge_sort(array[midpoint:],i))
    
    #derived class print method for last student added
    def print_student_info(self):
        if self._first_name and self._last_name and self._province and self._cgpa and self._research_scor  != None:
            print('Domestic Student : ', 'Name : ',self._first_name,self._last_name, ', Research Score : ',self._research_score,
                ', Cgpa : ', self._cgpa, ', Province: ', self._province)
        else:
            print('Invalid Data entries.')
    
    #method to merge individual lists
    def sort_merge_lists(self,student_list):       
        flag = True
        while flag == True:
            print('1. Enter 0 to sort by first name.') 
            print('2. Enter 1 to sort by last name.') 
            print('3. Enter 2 to sort by country') 
            print('4. Enter 3 to sort by cgpa.')
            print('5. Enter 4 to sort by research score.') 
            print('6. Enter r to return the registry')
            print('Note: You must sort and return international students using the same data point as domestic students for '+
                  'intended results.')   
            E = input('Enter: ')
            
            #sorting by first name
            if E.lower() == '0':
                self.student_list = self.merge_sort(self.student_list,0)
                print('List sorted by first name: ')
                for i in self.student_list:
                    print(i) #prints sorted list
                choice = 0

            #sorting by last name  
            elif E.lower() == '1':
                self.student_list = self.merge_sort(self.student_list,1)
                print('List sorted by last name:')
                for i in self.student_list:
                    print(i) #prints sorted list
                choice = 1
            #sort by province
            elif E.lower() == '2':
                self.student_list = self.merge_sort(self.student_list,2)
                print('List sorted by province:')
                for i in self.student_list:
                        print(i) #prints sorted list
                choice = 2      
            #sort by cgpa
            elif E.lower() == '3':
                self.student_list = self.merge_sort(self.student_list,4)
                print('List sorted by research score:')
                for i in self.student_list:
                        print(i) #prints sorted list 
                choice = 3
            #sort by research score
            elif E.lower() == '4':
                self.student_list = self.merge_sort(self.student_list,3)
                print('List sorted by cgpa:')
                for i in self.student_list:
                        print(i) #prints sorted list
                choice = 4
            #return sorted list in order last sorted
            elif E.lower() == 'r':
                return self.student_list,choice
                
            else:
                self.print_value_error()
            
     #look for domestic students in registry, search by full name or academic score       
    def search_student(self,domesticStudent):
        print('Would you like to find a student from the registry?')
        print('Enter y to find or any key to return.')
        Z = input() #input to search or quit
        
        if Z.lower() == 'y':
         
          E_flag = False
          while(E_flag == False):
            
            self.print_search_message()
            E = input() # input to search by name or academics
            #look up student by name
            if(E.lower() == 'name'):
                
                name_flag = False
                while(name_flag == False): #loop conntrol for error free name entry
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

                        if f_name == True and l_name == True: #gives option to delete found student
                            print('Do you want to delete this student?')
                            print('1. Enter y to delete  student.')
                            print('2. Enter e to return to the previous menu. ')
                            print('3. Enter another key to return to the main menu.')                           
                            #delete student then break
                            remove = input()
                            if remove.lower() == 'y':
                                self.student_list.remove(i)
                                break
                            elif remove.lower() == 'e':
                                break
                            else:
                                return self.student_list
                            
                if f_name == False and l_name == False:
                    print('Student not found.') #conditon print for student not found
             
            #search students by academic score   
            elif E.lower() == 'academic':
                flag = True
                
                while flag == True:
                    #choice menu
                    print('\n1. To search students based on cgpa minimum and error : input "cgpa".')
                    print('2. To search students based on research score minimum and error : input "rs".')
                    print('4. To to delete students who fail to meet the minimum threshold : input "y".')
                    print('5. To return to previous menu : input "n".')
                    print('6. To return to start menu : input "r".')
                    cin = input()
                    
                    if cin.lower() == 'cgpa':
                        for i in self.student_list:
                            if i[3] < 3 :
                                print(i[0],i[1],' - ',i[3])
                                
                    if cin.lower() == 'rs':
                        for i in self.student_list:
                            if i[4] < 75:
                                print(i[0],i[1],' - ',i[4])
                                
        
                    #auto deletes all students who dont make the defined threshold for research score and cgpa
                    if cin.lower() == 'y':
                        print('1. Removing all domestic students who dont make the minimum research score threshold, < 75.')
                        print('2. Removing all domestic students who dont make the minimum cgpa threshold, < 3.00.')
                        tempList = [] #create a new list to hold acceptable values while disgarding values below threshold
                        
                        for i in self.student_list:
                            #appends student with research score and cgpa above minimum
                            if i[4] >= 75 and i[4] <= 100 and i[3] >= 3 and i[3] <= 4.33:
                                print(i[0],i[1],': Removed')
                                tempList.append(i[:])
                                
                            else:
                                print('Removing Name : ',i[0],i[1])
                          
                        self.student_list = tempList #assign new list
                        
                     #exit condition           
                    if(cin.lower() == 'n'):
                        flag = False
                    #return list with removed students
                    if(cin.lower() == 'r'):
                        return self.student_list
             
            #returns to student list   
            elif(E.lower() == 'n'):
                return self.student_list
            
            elif(E.lower() != 'name' or E.lower() != 'academic' or E.lower() != 'n'):
                self.print_entry_error()
             
        else:
            return self.student_list #exit conidition
    
    #add new student method    
    def add_student(self):
        i = 0
        #4 entry values, first name, last name, research score, and cgpa
        print('Adding a new student to the registry.')
        while i < 6 :
            print('Input first name: ')
            f_name = input()
            self.set_first_name(f_name)
            if self.get_first_name() == f_name:
                i+=1
            else:
                self.print_entry_error()
                i = 0
                continue
            
            print('Input Last Name: ')
            l_name = input()
            self.set_last_name(l_name)
            if self.get_last_name() == l_name:
                i+=1
            else:
                self.print_entry_error()
                i = 0
                continue
                
            # canadian provinces, incase something wrong is entered
            print('Input province initials: ')
            prov = input()
            self.set_province(prov)
            if self.get_province() == prov:
                    i+=1
            else:
                self.print_entry_error()
                i = 0
                continue
            
            print('Input cpga: ')
            s_cgpa = input()
            try:
                s_cgpa = float(s_cgpa) #convert to float error catch
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
            
            print('Input research score: ')
            s_research_score = input()
            try:
                s_research_score = int(s_research_score) #convert to int error catch
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
            
            #sets new student if every value is correct
            print(i)
            if i == 5:
                self.stu_list()
                
                print('Would you like to enter another student? Type y to enter a new student or enter any key to quit.')
                enter = input()
                if enter.lower() == 'y':
                    i = 0
                else:
                    return    
    
    
    #method to clear list
    def empty_list(self):
        self.D_student_list[:] = []
        self.student_list[:] = []
       