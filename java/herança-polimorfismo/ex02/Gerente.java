public final class Gerente extends Usuario {
    public Gerente(String nome, String email, String senha) {
        super(nome, email, senha);
        this.setAdmin();
    }


    public void gerarRelatorio() {
        System.out.println("Gerando relatório.");
    }

    public void consultarVendas() {
        System.out.println("consultando vendas.");
    }
}
