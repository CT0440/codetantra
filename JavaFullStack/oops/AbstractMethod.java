
abstract class Shape{
    String color;

    abstract double area();
    public abstract String toString();

    public Shape(String color){
        System.out.println("Shape Constructer Called");
        this.color = color;
    }
    public String getColor(){
        return color;
    }

}
class Circle extends Shape{
    double radius;

    public Circle(String color, double radius){
        super(color);
        System.out.println("Circle Constructer called");
        this.radius = radius;
    }
    @Override double area(){
        return Math.PI * Math.pow(radius, 2);
    }
    @Override public String toString(){
        return "Circle color is: "+ super.getColor() + "the Area of Circle is:"+ area();
    }

}
class Rectangle extends Shape{
    double length;
    double width;

    public Rectangle(String color, double length, double width){
        super(color);
        System.out.println("Rectangle Constructer Called");
        this.length = length;
        this.width = width;
    }

     double area(){
        return length * width;
    }

     public  String toString(){
        return "Recatngle color is " + super.getColor()+"and area is: "+area();
    }    

}

class AbstractMethod{
public static void main(String[] args){
    Shape c = new Circle("red", 2.0);
    Shape r = new Rectangle("Yellow", 2.0, 3.0);

    System.out.println(c.toString());
    System.out.println(r.toString());

    }
}