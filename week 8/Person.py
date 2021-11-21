class Person:
    def __init__(self,n,a):
        self.name = n
        self.name = a
    

 # property age = whatever the age is enter   
    def age (self):
        return self._age

# this is the age setter - sets criteria for the age entered ,more than 1 and less than 120. controlling the data entered

    def age (self,arg):
        if (arg>=1 and arg<=120):
            self._age = arg
    
    def __repr__(self):
        return f"{self.name} is {self._age} years old"

class Student(Person):

    def __init__(self, n, a, courses):
        super().__init__(n,a)
        self.courses = courses
    def takes_courses (self,list):
        for course in self.courses:
            if course in list:
                return True
        return False

if __name__ == '__main__':
    print("hello")
    clara = Person ("clara", 1)
    print (clara)
    clara.age = 18
    print( clara)

    paul = Student ("Paul", 52,["Intro to Management","Programming 101"])
    print (paul)
    paul.age = 300
    print(paul)
    print(paul.takes_class(["HR Admin"]))
    print(paul.takes_class(["Intro to Management"]))