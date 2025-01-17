
class Employee{
    int salary = 60000;
}
class Engineer extends Employee{
    int benifits = 1000;
}
class InheritanceExample2{
    public static void main(String[] args){
        Engineer e = new Engineer();
        System.out.println("salary:" +e.salary+"\nBenifits:"+e.benifits);
    }
}