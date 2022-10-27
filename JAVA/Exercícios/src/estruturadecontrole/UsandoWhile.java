package estruturadecontrole;

import java.util.Scanner;

public class UsandoWhile {
	
	public static void main(String[] args) {
	
		//While Deternimado = quando vc sabe quantas vezes quer repetir.
		int contador = 1;
		
		while(contador <= 10) {
			System.out.println("BOM DIA!!!");
			contador++;
		}
		
		
		//While indeterminado = quando vc não sabe quantas vezes ele vai repetir.
		
		Scanner entrada = new Scanner(System.in);
		
		String valor = "";
		
		while(!valor.equalsIgnoreCase("sair")) {
			System.out.println("Voce diz: ");
			valor = entrada.nextLine();
		}
		
		entrada.close();
		
	}
}
