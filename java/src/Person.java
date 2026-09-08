public class Person {

    private String name;
    private int age;

    // Construtor
    public Person (String name, int age) {
        this.name = this.setterName(name);
        this.age = age;
    }

    public String getName() {
        return this.name;
    }
    public String setterName(String name) {
        if (!name.equals("")){
            this.name = name;
        } else {
            this.name = "burro";
        }

        return this.name;
    }

    public int getAge() {
        return this.age;
    }

}

