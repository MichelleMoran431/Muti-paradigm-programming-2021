
// clock class in java as an OOP . structure similar to python. 
// syntax is different 
//public denotes visibility - whos sees it - grp functions and data together and manipulate whos sees it 
// have to declare the variables that see in the class , strongly type language 
// private means nobody outside class can access the hrs mins secs to access data
// line 7 is the construct - take in 3 infos and store in class  as h , m, s . Call info and validate it . if it doesnt majke sense and then it defaults back to 0
//tick method - allows the clock to control how its values change , as it gets called in the function


public class CLock {

    private int hours;
    private int mins;
    private int secs;

    public CLock (int h, int m, int s)
        hours = h;
        mins = m;
        secs = s;
        validate();
}

    private void validate (){
        if (hours >12 || mins> 60 || secs>60){
            hours = 0;
            mins = 0;
            secs = 0;

        }
    }
    
    public void tick(){
        secs+=1;

        if (secs > 59){
            mins +=1;
            secs = 0;
        }
        if (mins > 59){
            hours +=1;
            mins = 0;
        }
        if (hours > 12){
            hours=1;
            mins +=1;
            secs = 0;
    }
}
    public String toString(){
         return hours+":"+mins+":"+secs;
}

    public static void main(String[] args) throws InterruptedException {
        Clock c = new Clock (10,20,50);

        while (true){
             c.tick();
            System.out.printIn(c);
            Thread.sleep(1000);
    
         }
    }
}