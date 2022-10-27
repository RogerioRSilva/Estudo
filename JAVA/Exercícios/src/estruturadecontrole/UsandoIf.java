package estruturadecontrole;

import java.util.Scanner;

public class UsandoIf {
	
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		
		System.out.print("Informe a media: ");
		double media = entrada.nextDouble();
		
		if( media >= 7 ) {
			System.out.println("Vc está aprovado!!!");
		}
		
				
		entrada.close();
	}
}
