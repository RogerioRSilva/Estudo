package exerciciosfundamentos;

import javax.swing.JOptionPane;

public class Exercicio01 {
	public static void main(String[] args) {
		
		// Conversão de Fahrenheit em garus Celsius.
		
		String temperaturaFahrenheit = JOptionPane.showInputDialog("Digite a temperaturam em Fahrenheit: ");
		
		double tempFah = Double.parseDouble(temperaturaFahrenheit);
		
		double convertCelsius = (tempFah - 32)/1.8;
		
		System.out.printf("A temperatura de %.2fF convertida em Celsius eh: %.2f", tempFah, convertCelsius);
		
	}
}
