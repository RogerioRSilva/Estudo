package fundamentos;

import java.util.Scanner;

public class Console {
	public static void main(String[] args) {
		System.out.println("OLA TUDO BEM!!!");
   		System.out.print("BOM");
   		System.out.print(" DIA");
		System.out.println("\n==============================================\n");
   		
		Scanner entrada = new Scanner (System.in);
		
   		System.out.print("Qual o seu nome: ");
   		var nome = entrada.nextLine();
   		
   		System.out.print("Qual o seu sobrenome: ");
   		var sobrenome = entrada.nextLine();
   		
   		System.out.print("Qual a sua idade: ");
   		var idade = entrada.nextInt();
   		
   		System.out.printf("\n\nNome = %s %s", nome, sobrenome);
   		
   		System.out.printf("\n%s vc tem %d anos de idade!!!", nome, idade);
   		
   		entrada.close(); // Fecha o recurso scanner
   		
   		
	}
}
