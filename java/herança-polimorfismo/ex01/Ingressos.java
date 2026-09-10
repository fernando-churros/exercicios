public sealed abstract class Ingressos permits MeiaEntrada, Familia {
    protected double valor = 20;
    protected String nome;
    protected String voice;

    public Ingressos(String nome, String voice) {
        this.nome = nome;
        this.voice = voice;
    }

    public void info() {
        System.out.printf("Filme: %s%n", this.nome);
        System.out.printf("Vozes: %s%n", this.voice);
    }

    public abstract double getValor();
}