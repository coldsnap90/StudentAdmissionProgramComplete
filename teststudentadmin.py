import unittest
from main import student 
from main import domesticStudent as domStu
from main import internationalStudent as intStu
from main import totalScore as totSco
from help_func_admission_program import *
'''
Unit test for several features of the student admissions program
such as accessor's & mutators for each class, search and add methods, sorting algoritms, and final sort
11 total tests
'''
class testStudentAdmissionsProgram(unittest.TestCase):
    #instatianating class objects to test
    def setUp(cls):
       cls.domesticStu1 = domStu()
       cls.intStu1 = intStu()
       cls.tScore = totSco()
       def print_in():
           print('in')
       def print_out():
            print('out')
    def tearDown(self):
        del self.domesticStu1
        del self.intStu1
        del self.tScore
        return super().tearDown()
    
    #testing constructor, accessor + mutators, and print func for domesticStudent class
    def test_1(self):
        print('Test 1')
        try:
            self.domesticStu1.set_first_name('x-Ae12') #entering invalid characters
            self.domesticStu1.set_last_name('Marston')
            self.domesticStu1.set_province('BC')
            self.domesticStu1.set_cgpa(4.00)
            self.domesticStu1.set_research_score(75)
            self.domesticStu1.print_student_info() #should print invalid entries do to invalid characters
        except:
            print('fail')
          
        self.domesticStu2 = domStu('Qc','jack','march',4.2,70) #object instantiation
        self.domesticStu2.print_student_info()
        #testing accessors
        self.domesticStu1.set_first_name('John')
        self.domesticStu1.set_last_name('Marston')
        self.domesticStu1.set_province('BC')
        self.domesticStu1.set_cgpa(4.00)
        self.domesticStu1.set_research_score(75)
        self.domesticStu1.print_student_info() 
        #testing mutators
        self.assertEqual(self.domesticStu1.get_first_name(),'John')
        self.assertEqual(self.domesticStu1.get_last_name(),'Marston')
        self.assertEqual(self.domesticStu1.get_province(),'BC')
        self.assertEqual(self.domesticStu1.get_cgpa(),4.00)
        self.assertEqual(self.domesticStu1.get_research_score(),75)
       
    #testing accessor and mutators for internationalStudent and totalScore class
    def test_2(self):
        print('Test 2')
        #testing mutator invalid entry retrieval
        try:
            self.tScore.set_reading(20)  
            self.tScore.set_writing(20)
            self.tScore.set_speaking(20)
            self.tScore.set_listening(20)
            self.tScore.__add__()
            self.intStu1.set_first_name('$-Ae12?') #entering invalid characters
            self.intStu1.set_last_name('Mar.ston')
            self.intStu1.set_country('B-C')
            self.intStu1.set_score(self.tScore.get_score())
            self.intStu1.set_cgpa(5.00)
            self.intStu1.set_research_score(110)
            self.intStu1.print_student_info() #should print invalid entries do to invalid characters
        except:
            print('fail')
        self.intStu2 = intStu('iran',120,'mohammed','mosadeq',100,4.33) #country,score,first,last,rs,cgpa
        self.intStu2.print_student_info()
        #testing mutators
        self.intStu1.set_first_name('Jun')
        self.intStu1.set_last_name('Lee')
        self.intStu1.set_country('korea')
        self.intStu1.set_cgpa(3.33)
        self.intStu1.set_research_score(80)
        self.intStu1.set_score(100)
        self.intStu1.print_student_info()
        #testing accessors
        self.assertEqual(self.intStu1.get_first_name(),'Jun')
        self.assertEqual(self.intStu1.get_last_name(),'Lee')
        self.assertEqual(self.intStu1.get_country(),'korea')
        self.assertEqual(self.intStu1.get_research_score(),80)
        self.assertEqual(self.intStu1.get_cgpa(),3.33)
        self.assertEqual(self.intStu1.get_score(),100)
       
    #testing totalScore class acessors,mutators, overloading operator.
    def test_3(self):
        print('Test 3')
        self.tScore.set_reading(20)  
        self.tScore.set_writing(20)
        self.tScore.set_speaking(20)
        self.tScore.set_listening(20)
        self.tScore.__add__()
        self.assertEqual(self.tScore.get_reading(),self.tScore.get_writing())
        self.assertEqual(self.tScore.get_speaking(),self.tScore.get_listening())
        self.assertEqual(self.tScore.get_score(),80)   
       
        
    #testing domesticStudent class accessors and mutators, data appender, and merge sort
    def test_4(self):
        self.domesticStu1.D_student_list[:] = []
        self.domesticStu1.student_list[:] = []
        
        print('Test 4')
        #accessor and mutator testing and list appending for domestic student
        self.domesticStu1.set_first_name('Genie')
        self.domesticStu1.set_last_name('Bell')
        self.domesticStu1.set_province('AB')
        self.domesticStu1.set_cgpa(4.00)
        self.domesticStu1.set_research_score(75)
        self.domesticStu1.stu_list()
        self.assertEqual(self.domesticStu1.student_list[0][1],'Bell') #test if student in list
        
         #accessor and mutator testing and list appending for domestic student
        self.domesticStu1 = domStu('on','Frank','Castle',3.5,95)
        self.domesticStu1.stu_list()
        self.assertIn('Frank',self.domesticStu1.student_list[1][0]) #test if student in list
        
        #merge sort test to see if sorting was done correctly
        self.domesticStu1 = domStu('BC','Mandy','Cheemo',3.20,75)
        self.domesticStu1.stu_list()  
        self.domesticStu1 = domStu('AB','Man','emo',3.27,77)
        self.domesticStu1.stu_list()
        self.domesticStu1.student_list = self.domesticStu1.merge_sort(self.domesticStu1.student_list,0)
        self.assertEqual(self.domesticStu1.student_list[0][0],'Frank')
        self.domesticStu1.print_student_list()
        
       
    #Tests domesticStudent class to see if objects are in the list and uses search_student() method to find objects.
    def test_5(self): 
        self.domesticStu1.D_student_list[:] = []
        self.domesticStu1.student_list[:] = []
        
        print('Test 5')
        #tests creation of two students and append to list
        self.domesticStu1 = domStu('BC','Mandy','Cheemo',3.20,75)
        self.domesticStu1.stu_list()  
        self.domesticStu1 = domStu('AB','Man','emo',3.27,77)
        self.domesticStu1.stu_list()
        self.assertIn( 'Mandy',self.domesticStu1.student_list[0][0])  #test to see if in list
        
        #tests search method for students added above
        self.domesticStu1.search_student(self.domesticStu1)# search added student
        self.domesticStu1.print_student_list()
        self.assertNotIn('Fran',self.domesticStu1.student_list)
        
    #Testing domesticStudent class add_student() method
    def test_6(self):
        self.domesticStu1.D_student_list[:] = []
        self.domesticStu1.student_list[:] = []
        
        print('Test 6')
        list = ['Mike','tsukov','sk',4.00,97]
        self.domesticStu1.add_student() #add above list info into add student
        self.assertListEqual(list,self.domesticStu1.student_list[0]) #was added properly
        
    #Testing internationalStudent class accessors and mutators, data appender, and merge_sorts()
    def test_7(self):
        self.intStu1.I_student_list[:] = []
        self.intStu1.student_list[:] = []
        
        print('Test 7')
        #add intStu
        self.intStu1.set_first_name('Jun')
        self.intStu1.set_last_name('Jee')
        self.intStu1.set_country('korea')
        self.intStu1.set_cgpa(4.00)
        self.intStu1.set_research_score(75)
        self.intStu1.set_score(110)
        self.intStu1.I_stu_list()
        self.assertEqual(self.intStu1.student_list[0][1],'Jee') #in list
        #add another int stu
        self.intStu1 = intStu('china',120,'Quan','Xi',3.5,95)
        self.intStu1.I_stu_list()
        self.assertIn('Quan', self.intStu1.student_list[1][0]) #in list
        #add another intStu
        self.intStu1 = intStu('iran',110,'Rez','azzian',3.20,75)
        self.intStu1.I_stu_list()
        self.assertIn('iran',self.intStu1.student_list[2]) #in list
        #add last intStu  
        self.intStu1 = intStu('idiam',100,'Man','emo',3.27,77)
        self.intStu1.I_stu_list()
        self.assertIn('Xi',self.intStu1.student_list[1][1]) #check wether 2nd editiom is right place
        
        self.intStu1.student_list =  self.intStu1.merge_sorts(self.intStu1.student_list,0)#merge sort firstname
        self.assertEqual(self.intStu1.student_list[0][0],'Jun')
        self.intStu1.print_student_list()
       
    #Testing internationalStudent class search_student() method
    def test_8(self):
        self.intStu1.I_student_list[:] = []
        self.intStu1.student_list[:] = []
        
        print('Test 8')
        #add int stu
        self.intStu1 = intStu('china',120,'Quan','Xi',3.5,95)
        self.intStu1.I_stu_list()
        self.assertIn('Quan',self.intStu1.student_list[0]) #check in list
        self.intStu1.search_student(self.intStu1) #search for the intStu added
        self.assertNotIn('xaio',self.intStu1.student_list)#not in luist

    #testing add_student() method for international student   
    def test_9(self):
        self.intStu1.I_student_list[:] = []
        self.intStu1.student_list[:] = []
        
        print('Test 9')
        list = ['bikram','singh','india',4.00,97,120]
        self.intStu1.add_student() #add data from list above
        self.intStu1.print_student_list()
        self.assertListEqual(list,self.intStu1.student_list[0]) #check to see if in property place
        
    #testing empty_list() method and equality of empty derived class lists 
    def test_10(self):
        self.intStu1.I_student_list[:] = []
        self.intStu1.student_list[:] = []
        self.domesticStu1.D_student_list[:] = []
        self.domesticStu1.student_list[:] = []
        
        print('Test 10')
        self.intStu1 = intStu('china',120,'Quan','Xi',3.5,95)
        self.intStu1.I_stu_list()
        self.intStu1.empty_list()
        
        self.domesticStu1 = domStu('BC','Mandy','Cheemo',3.20,75)
        self.domesticStu1.stu_list()
        self.domesticStu1.empty_list()
        
        self.assertListEqual(self.intStu1.student_list,self.domesticStu1.student_list) #assert both are empty
        
    #Testing domesticStudent class method merge_sort() & internationalStudent class merge_sorts() algorithm
    #along with helper function student_operations() with nested function merge_lists()
    def test_11(self):
      self.intStu1.I_student_list[:] = []
      self.intStu1.student_list[:] = []
      self.domesticStu1.D_student_list[:] = []
      self.domesticStu1.student_list[:] = []
      
      #adds domesticStudent objects
      self.domesticStu1 = domStu('on','Frank','Castle',3.5,95)
      self.domesticStu1.stu_list()
      self.domesticStu1 = domStu('BC','Mandy','Cheemo',3.20,75)
      self.domesticStu1.stu_list()  
      self.domesticStu1 = domStu('AB','Man','emo',3.27,77)
      self.domesticStu1.stu_list()
      
      #adds internationalStudent objects
      self.intStu1 = intStu('china',120,'Quan','Xi',3.5,95)
      self.intStu1.I_stu_list()
      self.intStu1 = intStu('iran',110,'Rez','azzian',3.20,75)
      self.intStu1.I_stu_list()
      self.intStu1 = intStu('idiam',100,'Man','emo',3.27,99)
      self.intStu1.I_stu_list()
       
      #sort derived class lists
      list3 =[]
      list1= self.intStu1.merge_sorts(self.intStu1.student_list,0)
      list2= self.domesticStu1.merge_sort(self.domesticStu1.student_list,0)  
      list3 = student_operations(list1,list2,list3,0) #sort based on first name
      self.assertLess(list3[0][0],list3[5][0]) #checks first name first 1st position < then last
      #sort another derived class list
      list6 =[]
      list4= self.intStu1.merge_sorts(self.intStu1.student_list,3)
      list5= self.domesticStu1.merge_sort(self.domesticStu1.student_list,3) 
      list6 = student_operations(list4,list5,list6,3)#sort based on rs
      self.assertGreater(list6[5][3],list6[0][3]) #checks research score in last pos is > then 1st
    
    
        
if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()


