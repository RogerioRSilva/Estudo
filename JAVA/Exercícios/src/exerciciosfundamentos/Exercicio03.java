package exerciciosfundamentos;

import javax.swing.JOptionPane;

public class Exercicio03 {
	
	public static void main(String[] args) {
		// Criar um programa que leia o peso e a altura do usuário e imprima no console o IMC.
		
		String pesoEntra = JOptionPane.showInputDialog("Informe seu Peso: ");
		String alturaEntra = JOptionPane.showInputDialog("Informe sua Altura: ");
		
		double peso = Double.parseDouble(pesoEntra.replace(",", "."));
		double altura = Double.parseDouble(alturaEntra.replace(",", "."));
		
		double imc = peso / Math.pow(altura, 2);
		
		System.out.printf("O IMC do peso: %.2f e altura: %.2f é: %.2f", peso, altura, imc);
		
		if (imc < 18.5){
			System.out.printf("\nVc está com IMC %.2f e abaixo do peso ideal.", imc);
		}
		else if (imc >= 18.5 && imc < 25) {
			System.out.printf("\nVc está com IMC %.2f e no peso ideal.", imc);
		}
		else if (imc >= 25 && imc < 30) {
			System.out.printf("\nVc está com IMC %.2f e esta com sobrepeso.", imc);
		}
		else if (imc >= 30 && imc <= 40) {
			System.out.printf("\nVc está com IMC %.2f e esta com obesidade.", imc);
		}
		else{
			System.out.printf("\nVc está com IMC %.2f e esta com obesidade grave.", imc);
		}
	}

}
