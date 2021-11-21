#create a alarm clock - prints a message which the alarm time 
# feature of OOP inheritance - take the functionality from clock and use it in another class and add an alarm 
#superclass - clock
#subclass - Alarmclock , it inherits from clock class
# need to store where the alarm is going to go off


from Clock import *

class AlarmClock (Clock):

    def __init__(self, hours, mins, secs, aHour , aMin, aSec):
        super().__init__(hours,mins,secs)
        self.aHour = aHour
        self.aMin = aMin
        self.aSec = aSec

#def tick and repr are examples of method overwriting : calling the superclass methods
    
    def tick (self):
        super().tick()
        if (self.hours== self.aHour and self.mins == self.aMin and self.secs == self.aSec):
            print ("Alarm, get up !!!!")

        super().tick()

    def __repr__(self)
        return f"AlarmClock:{super().__repr__()}"

if __name__== '__main__':
    c = AlarmClock (10,20,50,10,20,55)

    while (True):
        c.tick()
        print(c)
        time.sleep(1)


