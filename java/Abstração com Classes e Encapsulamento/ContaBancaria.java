public class ContaBancaria {

    private float saldo;
    private float cheque_especial;
    private float limite_cheque_especial;
    private float divida_cheque = 0;
    private float juros = 0;
    

    public ContaBancaria() {
        this.saldo = 0;
        this.limite_cheque_especial = this.setterChequeEspecial(this.saldo);
        this.cheque_especial = this.limite_cheque_especial;
    }

    public ContaBancaria (float saldo) {
        this.saldo = saldo;
        this.limite_cheque_especial = this.setterChequeEspecial(saldo);
        this.cheque_especial = this.limite_cheque_especial;
    }

    public float getSaldo() { return this.saldo; }
    public float getChequeEspecial() { return this.cheque_especial; }
    public float getDivida() { return this.divida_cheque + this.juros; }

    public float setterChequeEspecial(float valor) {
        if ( valor <= 500 ) {
            this.limite_cheque_especial = 50;
        } else {
            this.limite_cheque_especial = valor * 0.5f;
        }

        return this.limite_cheque_especial;
    }

    public void depositar(float valor) {
        if ( valor <= 0 ) return;

        if ( this.divida_cheque != 0) {
            if ( valor >= this.divida_cheque + this.juros ) {
                this.saldo += valor - (this.divida_cheque - this.juros);
                this.divida_cheque = 0;
                this.juros = 0;
                this.cheque_especial = this.limite_cheque_especial;
                return;
            }

            if ( valor >= this.juros ) {
                valor -= this.juros;
                this.juros = 0;
            } else {
                this.juros -= valor;
                valor = 0;
            }

            this.divida_cheque -= valor;
            this.cheque_especial += valor;
            valor = 0;
        }

        this.saldo += valor;
    }

    public void sacar(float valor) {
        if ( valor <= 0 || valor > this.saldo ) return;

        this.saldo -= valor;
    }

    public boolean pagar_boleto(float valor) {
        if ( valor > this.saldo ) {
            if ( valor > this.saldo + this.cheque_especial ) return false;

            float taxa = valor - this.saldo;

            this.saldo = 0;
            this.cheque_especial -= taxa;

            this.juros += taxa * 0.2f;
            this.divida_cheque += taxa;

            return true;
        }

        this.saldo -= valor;
        return true;
    }

}