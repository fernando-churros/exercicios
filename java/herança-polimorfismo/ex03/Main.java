public final class Main {
    public static void main(String[] args) {
        Brasil bra = new Brasil(8, 23, 54);
        Americano eua = new Americano(9, 44, 12, "PM");

        eua.convert(bra);
        System.out.println(bra.getHorario());
        System.out.println(eua.getHorario());
    }
}
