class Tantra{
    public void tantra(){
        System.err.print("TANTRA");
    }
}
class Code extends Tantra{
    public void code(){
        System.out.print("CODE ");
    }

}
class SI{
    public static void main(String[] args) {
        Code c = new Code();
        c.code();
        c.tantra();

    }

}