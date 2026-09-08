public class Main {
    public static void main(String[] args) {

        ContaBancaria c1 = new ContaBancaria(100);
        final var pessoa = new ContaBancaria();
        c1.pagar_boleto(150);

        System.out.printf("saldo: %s%n", c1.getSaldo());
        System.out.printf("cheque: %s%n", c1.getChequeEspecial());
        System.out.printf("divida: %s%n", c1.getDivida());

    }
}