public final class Americano extends Relogio {
    protected String periodo;

    public Americano(int hora, int minutos, int segundos, String periodo) {
        super(hora, minutos, segundos);
        this.periodo = periodo;
    }

    public String getPeriodo() { return this.periodo; }

    public void setHora(int hora) {
        if ( hora < 1 || hora > 12 ) { this.horas = 12; } else { this.horas = hora; }
    }

    public void convert(Relogio other) {
        int hora = other.getHora();

        if ( !(other instanceof Americano americano) ) {
            this.periodo = "AM";

            if (hora == 0) { hora = 12; } else if (hora == 12) { this.periodo = "PM"; }
            else if (hora > 12) {
                hora -= 12;
                this.periodo = "PM";
            }
        } else { this.periodo = americano.getPeriodo(); }

        this.horas = hora;
        this.minutos = other.getMinutos();
        this.segundos = other.getSegundos();
    }

    @Override
    public String getHorario() {
        return String.format("%02d:%02d:%02d %s", this.horas, this.minutos, this.segundos, this.periodo);
    }
}
