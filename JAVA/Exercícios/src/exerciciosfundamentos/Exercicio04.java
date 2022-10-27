package exerciciosfundamentos;

import java.util.Scanner;

public class Exercicio04 {
	
	public static void main(String[] args) {
		/*
		 * Criar um programa que leia um valor e apresente 
		 * os resultados ao quadrado e ao cubo do valor.
		 **/
		
		Scanner entrada = new Scanner (System.in);
		
		System.out.print("Informe um numero: ");
		double numero = entrada.nextDouble();
		
		double numQuadrado = Math.pow(numero, 2);
		double numCubo = Math.pow(numero, 3);
		
		System.out.printf("\nO numero %.2f elevado ao quadrado eh = %.2f", numero, numQuadrado);
		System.out.printf("\n\nO numero %.2f elevado ao cubo eh = %.2f", numero, numCubo);
		
		entrada.close();
	}

}
