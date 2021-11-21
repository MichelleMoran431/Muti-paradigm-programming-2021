#an example of object orientated programmining 

#NB : difference between OOP and PP - the data is separate from the functions, which manipulate the data

# in OOP , the class contains both the data and algorithms
# method double underlined - reserved method name in python and important function called constructor . Many clocks in a house , but use the same blue
# print. same algorithms but u can use different data

import time
# has control over its own data
class Clock:
    def __init__ (self,hours,mins,secs):
        self.hours = hours
        self.mins = mins
        self.secs = secs
        self.validate()


# check what the person enters , if its not aligned with a clock. it reverts to 0 
    def validate (self):
        if (self.hours > 12 or self.mins >60 or self.secs >60):
            self.hours = 0
            self.mins = 0
            self.secs = 0


    # tick method for moving the clock along , by 1 sec , if it is increase , the hrs and mins increases
    def tick (self):
        self.secs +=1

        if  (self.secs >59):
            self.mins += 1
            self.secs = 0

        if  (self.mins >59):
            self.hours += 1
            self.mins = 0
        
        if  (self.hours > 12):
            self.hours = 1
            self.mins =0
            self.secs = 0


      # this special method returns a instance of the class    , state of the class. returns a string based 
      # self means hours
      # init methods. hours is send into method.   
    def __rep__(self):
        return f"{self.hours}:{self.mins}:{self.secs}"
        
if __name__=='__main__':
    c = Clock(10, 20, 50)
    c2 = Clock(11,23,55);

    while(True):
        c.tick()
        print(c)
        time.sleep(1)

