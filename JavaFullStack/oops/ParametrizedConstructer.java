
class ParametrizedConstructer{
    String name;
    int age;
    ParametrizedConstructer(){
        this.name = "susruthi";
        this.age = 22;
    }
    public static void main(String[] args){
        ParametrizedConstructer obj = new ParametrizedConstructer();
        System.out.println("name:"+obj.name+"\nage:"+obj.age);
    }
}