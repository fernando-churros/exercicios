public class Carro {
    private boolean on = false;
    private int velocidade = 0;
    private int min_velocidade = 0;
    private int max_velocidade = 0;
    private int marcha = 0;

    public int getVelocidade() { return this.velocidade; }
    public void ligar() { this.on = true; }
    public void desligar() {
        if ( this.marcha == 0 ) this.on = false;
    }

    public void trocarMarcha(int marcha) {
        boolean is_troca = false;

        if ( !this.on ) return;

        if ( this.marcha + 1 == marcha && this.velocidade == this.max_velocidade) {
            is_troca = true;
        } else if ( this.marcha - 1 == marcha && this.velocidade == this.min_velocidade) {
            is_troca = true;
        }

        if ( is_troca) {
            if ( !(marcha >= 0 && marcha <= 6) ) return;
            
            this.marcha = marcha;

            switch (marcha) {
                case 0 -> { this.min_velocidade = 0; this.max_velocidade = 0; }
                case 1 -> { this.min_velocidade = 0; this.max_velocidade = 2; }
                case 2 -> { this.min_velocidade = 2; this.max_velocidade = 4; }
                case 3 -> { this.min_velocidade = 4; this.max_velocidade = 6; }
                case 4 -> { this.min_velocidade = 6; this.max_velocidade = 8; }
                case 5 -> { this.min_velocidade = 8; this.max_velocidade = 10; }
                case 6 -> { this.min_velocidade = 10; this.max_velocidade = 12; }
            }
        }
        
    }

    public void acelerar() {
        if ( !this.on || this.velocidade >= max_velocidade) return;

        this.velocidade += 1;
    }

    public void desacelerar() {
        if ( !this.on || this.velocidade <= this.min_velocidade ) return;

        this.velocidade -= 1;
    }

    public void virar(String lado) {
        if ( this.velocidade > 0 && this.velocidade <= 4 ) {
            System.out.printf("Virando para %s%n", lado);
        }
    }
}
