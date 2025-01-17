class Person{
    private String name;
    private int age;

    public void setName(String name){
        this.name = name;

    }
    public String getName(){
        return name;
    }
    public void setAge(int age){
        this.age = age;
    }
    public int getAge(){
        return age;
    }

    
}
class EncapsulationExample{
    public static void main(String[] args){

        Person p = new Person();
        p.setName("Susruthi");
        p.setAge(22);

        System.out.println("The person name is: "+p.getName());
        System.out.println("The person age is :"+p.getAge());


    }
}