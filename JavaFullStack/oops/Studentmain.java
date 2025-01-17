class Student{
    String name;
    int age;

    public void printStudent(){
        System.out.println("StudentName:" +name+"\nStudent Age:" +age);
    }   
}

class Studentmain{
    public static void main(String[] args) {
        Student obj = new Student();
        obj.name = "Susruthi";
        obj.age = 22;

        obj.printStudent();
    }
}