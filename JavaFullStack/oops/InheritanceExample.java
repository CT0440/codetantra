import java.io.*;

class Bycycle{
    public int gear;
    public int speed;

    public Bycycle(int gear, int speed){
        this.gear = gear;
        this.speed = speed;
    }
    public String toString(){
        return ("no of gears are :" +gear+"\nspeed is:" +speed);
    }
}

class mountainBike extends Bycycle{
    int seatheight;

    public mountainBike(int gear, int speed, int startheight){
        super(gear, speed);
        seatheight = startheight;;
    }
    public String toString(){
        return (super.toString() + "\n seat height is :" +seatheight);
    }
}

class InheritanceExample{
    public static void main(String[] args){
        mountainBike mb = new mountainBike(3, 100, 25);
        System.out.println(mb.toString());

    }
}