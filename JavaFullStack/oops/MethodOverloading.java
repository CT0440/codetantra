class Helper{
    static  int display(int a, int b){
        return a + b;
    }
    static  double display(double a, double b){
        return a + b;
    }
}

class MethodOverloading{
    public static void main(String[] args) {
        System.out.println("integer sum: " +Helper.display(2, 3));
        System.out.println("double sum: " +Helper.display(2.0, 3.0));
    }
}