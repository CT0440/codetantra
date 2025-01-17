import java.io.*;

abstract class Animal{
    private String name;

    public Animal(String name){
        this.name = name;
    }
    public abstract void makeSound();

    public String getname(){
        return name;
    }

}
class Dog extends Animal{
    Dog(String name){
        super(name);
    }
    public void makeSound(){
        System.out.println(getname() + "barks");
        
    }

}
class Cat extends Animal{
    Cat(String  name){
        super(name);
    }
    public void makeSound(){
        System.out.println(getname() + "meows");
    }

}

class AbstractionExample{
    public static void main(String[] args){
        Animal d = new Dog("Jacky");
        Animal c = new Cat("Kitty");

        d.makeSound();
        c.makeSound();
    }
}