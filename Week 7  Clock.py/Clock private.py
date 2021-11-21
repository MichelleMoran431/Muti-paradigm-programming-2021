#an example of object orientated programmining 

# creation of private messages in python in OOS - validate change to __. called inside the class
#

import time
# has control over its own data
class Clock:
    def __init__ (self,hours,mins,secs):
        self.hours = hours
        self.mins = mins
        self.secs = secs
        self.__validate()


# check what the person enters , if its not aligned with a clock. it reverts to 0 
    def __validate (self):
        print("i am inside validate")
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
    # this method cant be called cos its outside the class. name mangling can be one way to call a private method  
    #c2.__validate()
    c2._Clock__validate()

    while(True):
        c.tick()
        c2.tick()
        print(f"Clock 1 {c}")
        print(f"Clock 2 {c2}")
        time.sleep(1)

