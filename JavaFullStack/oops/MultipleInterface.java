
interface A{
    public void display();

}
interface B {
    public void show();

}
interface C extends A, B{
    public void display();
}
class Child implements C{
    @Override public void display(){
        System.out.println("This is Child Class");
    }
    public void show(){
        System.out.println("This is show method in c");
    }
}

class MultipleInterface{
    public static void main(String[] args) {
         Child c = new Child();
        c.display();
        c.show();
        c.display();
    }
}