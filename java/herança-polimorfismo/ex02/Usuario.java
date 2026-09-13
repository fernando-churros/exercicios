public sealed abstract class Usuario permits Gerente, Vendedor {
    protected String nome;
    protected String email;
    protected String senha;
    protected boolean isLogged = false;
    protected boolean admin = false;

    public Usuario(String nome, String email, String senha) {
        this.nome = nome;
        this.email = email;
        this.senha = senha;
    }

    public String getNome() { return this.nome; }
    public String getEmail() { return this.email; }
    public boolean getAdmin() { return this.admin; }

    protected void setAdmin() {
        if (this instanceof Gerente) {
            this.admin = true;
        } else System.out.println("Permissão negada.");
    }

    public void login(String email, String senha) {
        if (email.equals(this.email) && senha.equals(this.senha)) {
            this.isLogged = true;
            System.out.println("Logado");
        } else System.out.println("Email ou senha incorretos.");
    }

    public void logoff() {
        this.isLogged = false;
        System.out.println("Desconectado");
    }

    public void alterarDados(String tipo, String newDado) {
        if (isLogged) {
            switch (tipo) {
                case "nome" -> this.nome = newDado;
                case "email" -> this.email = newDado;
            }
        } else System.out.println("Precisa estar logado.");
    }

    public void alterarSenha(String newSenha) {
        if (isLogged) {
            this.senha = newSenha;
        } else System.out.println("Precisa estar logado.");
    }
}
