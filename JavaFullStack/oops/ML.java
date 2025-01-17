class Code{
    public void code(){
        System.err.print("CODE");
    }
}
class Tantra extends Code{
    public void tantra(){
        System.err.print(" TANTRA");
    }
}

class Tech extends Tantra{
    public void tech(){
        System.err.print(" TECH SOLUTIONS");
    }
}

class ML{
    public static void main(String[] args) {
        Tech t = new Tech();
        t.code();
        t.tantra();
        t.tech();
    }
}