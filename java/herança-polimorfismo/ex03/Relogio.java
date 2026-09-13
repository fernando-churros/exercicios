public sealed abstract class Relogio permits Brasil, Americano {
    protected int horas;
    protected int minutos;
    protected int segundos;

    public Relogio(int hora, int minutos, int segundos) {
        this.setHora(hora);
        this.minutos = this.validaDado(minutos);
        this.segundos = this.validaDado(segundos);
    }

    public int getHora() { return this.horas; }
    public int getMinutos() { return this.minutos; }
    public int getSegundos() { return this.segundos; }

    public String getHorario() { return String.format("%02d:%02d:%02d", this.horas, this.minutos, this.segundos); }

    public abstract void setHora(int hora);
    public abstract void convert(Relogio other);

    public void setMinutos(int minutos) { this.minutos = this.validaDado(minutos); }
    public void setSegundos(int segundos) { this.segundos = this.validaDado(segundos); }

    private static int validaDado(int x) {
        if ( x >= 60 ) { x = 0; } else if ( x < 0 ) { x = 0; }

        return x;
    }

}
