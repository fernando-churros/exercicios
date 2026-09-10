public final class Familia extends Ingressos {
    int familiares = 1;
    double desconto = 0.05;

    public Familia(String nome, String voice, int familiares) {
        super(nome, voice);
        this.familiares = familiares;
    }

    public double getValor() {
        double valor = this.valor;
        valor *= this.familiares;

        if (this.familiares > 3) {
            valor = valor - (valor * this.desconto);
        }

        return valor;
    }
}
