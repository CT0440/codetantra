

class NConstructor{

    NConstructor(String name) {
        System.out.println("one Arument:"+name);
    }

    NConstructor(String name,int age) {
        System.out.println("two Arument:"+name +age);
    }

    NConstructor(float id) {
        System.out.println("float Arument:"+id);
    }
    
  public static void main(String[] args) {
      NConstructor obj1 = new NConstructor("Susruthi");
      NConstructor obj2 = new NConstructor("Susruthi", 34);
      NConstructor obj3 = new NConstructor(1234567);

  }  
}