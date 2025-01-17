class MyThread1 extends Thread{

    public void run(){
        System.out.println("This is MyThread1 class");
    }
}
class MyThread2 extends Thread{
     public void run(){
            System.out.println("This is MyThread2 class");
    }
}
class Threads{
    public static void main(String[] args){
        MyThread1 obj1 = new MyThread1();
        MyThread1 obj2 = new MyThread1();

        obj1.start();
        obj2.start();;

    }
}