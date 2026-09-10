public final class MeiaEntrada extends Ingressos {
    public MeiaEntrada(String nome, String voice) {
        super(nome, voice);
    }

    public double getValor() { return this.valor / 2; }
}
