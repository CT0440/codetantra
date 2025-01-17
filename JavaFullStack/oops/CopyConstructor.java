class Object{
    String name;
    int age;
    Object(String name, int age){
        this.name = name;
        this.age = age;
    }

    Object(Object obj2) {
        this.name = obj2.name;
        this.age = obj2.age;
    }
    
}

class CopyConstructor{
    public static void main(String[] args){
        System.out.println("First Object:\n");
        Object obj = new Object("Susruthi", 22);
        System.out.println("name:"+obj.name+"\nage:"+obj.age); 
        System.out.println();
        System.out.println("SecondObject:\n");
        Object obj2 = new Object(obj);
        System.out.println("name:"+obj2.name+"\nage:"+obj2.age); 

    } 
}