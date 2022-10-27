package exerciciosfundamentos;

import java.util.Scanner;

public class Exercicio05 {
	public static void main(String[] args) {
		/*
		 * Criar um programa que leia o valor da base e 
		 * da altura de um triângulo e calcule a área.
		 * */
		
		Scanner entrada = new Scanner(System.in);
		
		System.out.print("Informe o valor da base do triangulo: ");
		double base = entrada.nextDouble();
		
		System.out.print("\nInforme o valor da altura do triangulo: ");
		double altura = entrada.nextDouble();
		
		double areaTriangulo = (base * altura) / 2;
		
		System.out.printf("\nBase Triangulo: %.2f  \nAltura Triangulo: %.2f  \nArea: %.2f",base, altura, areaTriangulo);
		
		entrada.close();
	}
}
