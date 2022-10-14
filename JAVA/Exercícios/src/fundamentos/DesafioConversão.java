package fundamentos;

import java.util.Scanner;

public class DesafioConversão {
	public static void main(String[] args) {
		/*
		 * Criar um programa que receba os ultimos 3 salários e faça uma média
		 * dos seus salários.
		 * 
		 * */
		
		Scanner entrada = new Scanner (System.in);
		
		System.out.print("Digite o 1o Salario: ");
   		double salario1 = Double.parseDouble(entrada.nextLine().replace(",", "."));
   		
   		System.out.print("Digite o 2o Salario: ");
   		double salario2 = Double.parseDouble(entrada.nextLine().replace(",", "."));
   		
   		System.out.print("Digite o 3o Salario: ");
   		double salario3 = Double.parseDouble(entrada.nextLine().replace(",", "."));
   		
   		System.out.printf("R$%.2f  R$%.2f  R$%.2f",salario1, salario2, salario3);
   		
   		double media = (salario1 + salario2 + salario3)/3;
   		System.out.printf("\nA media salarial e: R$%.2f", media);
   		
		entrada.close();
		
	}
}