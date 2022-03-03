#class for handling total score, complete arbitrary decision to just add unecessary complexity to
#the program, this could have been put in the i student class               
class totalScore():
    #constructor
    def __init__(self,reading = None,writing = None,speaking = None,listening = None):
        self._reading = reading
        self._writing = writing
        self._speakimg = speaking
        self._listening = listening
        
    #accessors & mutators-------------------------
    #5 data points with error checking
    def get_writing(self):
        return self._writing
    def get_listening(self):
        return self._listening
    def get_speaking(self):
        return self._speaking
    def get_reading(self):
        return self._reading
    def get_score(self):
        return self._score
    
    def set_writing(self,writing):
        if(self.error_check_int(writing) == True):
            self._writing = writing
            
    def set_reading(self,reading):
        if(self.error_check_int(reading) == True):
            self._reading = reading
            
    def set_listening(self,listening):
        if(self.error_check_int(listening)== True):
            self._listening = listening
            
    def set_speaking(self,speaking):
        if(self.error_check_int(speaking) == True):
            self._speaking = speaking
    #-----------------------------------------------
    #overloading operator
    def __add__(self):
        self._score = self._reading + self._writing + self._listening + self._speaking
    
    def set_score(self):
            self.__add__()
    
    #set error checking function     
    def error_check_int(self,integer):
        if(isinstance(integer,int) == False):
            print('Data is not an int')
            return False
        else:
            return True