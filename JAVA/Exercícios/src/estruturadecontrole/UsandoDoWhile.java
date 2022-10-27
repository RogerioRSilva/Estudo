package estruturadecontrole;

import java.util.Scanner;

public class UsandoDoWhile {
	public static void main(String[] args) {
		
		Scanner entrada = new Scanner (System.in);
		
		String texto = "";
		
		
		do {
			System.out.println("Digite a senha: ");
			texto = entrada.nextLine();	
			
			if(texto.equalsIgnoreCase("rog1234")) {
				System.out.println("OLÁ SEJA BEM VINDO A NARNIA!!!");
			}else {
				System.out.println("SENHA INCORRETA!!!");
			}
			
		} while(!texto.equalsIgnoreCase("rog1234"));
		
		entrada.close();
		
	}
}
