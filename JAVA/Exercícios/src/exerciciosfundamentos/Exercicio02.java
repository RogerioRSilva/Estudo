package exerciciosfundamentos;

import javax.swing.JOptionPane;

public class Exercicio02 {
	public static void main(String[] args) {
		
		// Conversão de Gaus Celsius em Fahrenheit
		
		String temperaturaCelsius = JOptionPane.showInputDialog("Digite a temperaturam em Celsius: ");
		
		double tempCel = Double.parseDouble(temperaturaCelsius);
		
		double convertFah = (tempCel * 1.8) + 32;
		
		System.out.printf("A temperatura de %.2fC convertida em Fahrenheit eh: %.2fF", tempCel, convertFah);
	}
}
