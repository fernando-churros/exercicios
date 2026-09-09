public class Pet {
    private String name;
    private boolean limpo = false;

    public Pet(String name) {
        this.name = name;
    }

    public String getName() { return this.name; }

    public boolean isLimpo() { return this.limpo; }
    public void setLimpo(boolean x) { this.limpo = x; }
}
