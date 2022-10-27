package estruturadecontrole;

import java.util.Scanner;

public class DesafioDiaSemana {
	public static void main(String[] args) {
		
		Scanner entrada = new Scanner(System.in);
		
		System.out.print("Digite o dia da semana: ");
		String diaSemana = entrada.next();
		
		if (diaSemana.equalsIgnoreCase("Domingo")) {
			System.out.printf("Vc digitou %s e esse eh o 1o dia da semana.", diaSemana);
			
		}else if (diaSemana.equalsIgnoreCase("Segunda")) {
			System.out.printf("Vc digitou %s e esse eh o 2o dia da semana.", diaSemana);
			
		}else if (diaSemana.equalsIgnoreCase("Terça")) {
			System.out.printf("Vc digitou %s e esse eh o 3o dia da semana.", diaSemana);
			
		}else if (diaSemana.equalsIgnoreCase("Quarta")) {
			System.out.printf("Vc digitou %s e esse eh o 4o dia da semana.", diaSemana);
			
		}else if (diaSemana.equalsIgnoreCase("Quinta")) {
			System.out.printf("Vc digitou %s e esse eh o 5o dia da semana.", diaSemana);
			
		}else if (diaSemana.equalsIgnoreCase("Sexta")) {
			System.out.printf("Vc digitou %s e esse eh o 6o dia da semana.", diaSemana);
		}else if (diaSemana.equalsIgnoreCase("Sábado")){
			System.out.printf("Vc digitou %s e esse eh o 70 dia da semana.", diaSemana);
		}else {
			System.out.printf("Vc digitou %s e esse nao eh um dia da semana!!!", diaSemana);
		}
	
		entrada.close();
	}
}
