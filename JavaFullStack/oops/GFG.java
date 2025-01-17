
class GFG{
    static String Emp_Name;
    static float Emp_salary;

    static void set(String n, float s){
        Emp_Name = n;
        Emp_salary = s;
    }
    static void get(){
        System.out.println("EmployeeName: " +Emp_Name);
        System.out.println("EmployeeSalary: " +Emp_salary);
    }

    public static void main(String[] args){
        GFG.set("SusruthiKanaparthi", 15000);
        GFG.get();
    }

}