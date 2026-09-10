public class Main {
    public static void main(String[] args) {
        Ingressos ing1 = new MeiaEntrada("Deu a louca na chapeúzinho", "DUB");
        Ingressos ing2 = new Familia("As branquelas", "LEG", 4);

        ing1.info();
        System.out.println(ing1.getValor());
        ing2.info();
        System.out.println(ing2.getValor());
    }
}
