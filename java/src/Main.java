import java.util.Scanner;

public class Main {
    public static void main (String[] args) {

        PersonRecord pessoa = new PersonRecord("Fernando", 24);

        System.out.printf("nome = %s | idade = %s%n", pessoa.getName(), pessoa.getAge());
    }
}
