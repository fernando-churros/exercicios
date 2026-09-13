public final class Brasil extends Relogio {
    public Brasil(int horas, int minutos, int segundos) {
        super(horas, minutos, segundos);
    }

    public void setHora(int hora) {
        if ( hora < 0 || hora > 23 ) { this.horas = 0; } else { this.horas = hora; }
    }

    public void convert(Relogio other) {
        int hora = other.getHora();

        if (other instanceof Americano americano) {
            String periodo = americano.getPeriodo();

            switch (periodo) {
                case "AM" -> {
                    if (hora == 12) { hora = 0; }
                }
                case "PM" -> {
                    if (hora == 12) { hora = 12; } else { hora += 12; }
                }
            }
        }

        this.horas = hora;
        this.minutos = other.getMinutos();
        this.segundos = other.getSegundos();
    }
}
