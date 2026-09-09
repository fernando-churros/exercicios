public class Petshop {
    private int capacidadeMaxAgua = 30;
    private int capacidadeMaxShampoo = 10;
    private int nivelAgua = this.capacidadeMaxAgua;
    private int nivelShampoo = this.capacidadeMaxShampoo;
    private Pet pet = null;

    public int verificarAgua() { return this.nivelAgua; }
    public int verificarShampoo() { return this.nivelShampoo; }

    public void colocarPet(Pet pet) {
        if (this.pet != null) { System.out.printf("%s, está ocupando a máquina.%n", this.pet.getName()); return; }

        this.pet = pet;
        System.out.printf("%s está na máquina%n", pet.getName());
    }

    public void retirarPet() {
        if (this.pet == null) { System.out.println("Máquina vazia"); return; }

        System.out.printf("%s retirado da máquina%n", this.pet.getName());
        this.pet = null;
    }

    public void darBanho() {
        if (this.pet == null) { System.out.println("Máquina vazia, não é possivel dar banho."); return; }

        if (this.pet.isLimpo()) {System.out.printf("%s já está limpo, não é possivel dar banho.%n", this.pet.getName()); return; }

        if (this.nivelAgua >= 10 && this.nivelShampoo >= 2) {
            this.nivelAgua -= 10;
            this.nivelShampoo -= 2;
            this.pet.setLimpo(true);

            System.out.printf("%s está limpo.%n", this.pet.getName());
        } else { System.out.println("Água ou Shampoo insuficientes."); }
    }

    public void abastecer(String item) {
        switch (item) {
            case "Água":
                if (this.nivelAgua + 5 > this.capacidadeMaxAgua ) { System.out.println("Não é possivel abastecer"); return; }

                this.nivelAgua += 5;
                System.out.printf("Abastecido 5L de água, nivel atual: %s%n", this.nivelAgua);
                break;

            case "Shampoo":
                if (this.nivelShampoo + 2 > this.capacidadeMaxShampoo) { System.out.println("Não é possivel abastecer"); return; }

                this.nivelShampoo += 2;
                System.out.printf("Abastecido 2L de Shampoo, nivel atual: %s%n", this.nivelShampoo);
                break;

            default:
                System.out.println("Abastecimento incorreto.");
        }
    }
}
