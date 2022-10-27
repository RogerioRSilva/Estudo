package estruturadecontrole;

import javax.swing.JOptionPane;

public class DesafioIf {
	public static void main(String[] args) {
		// Identifique se um numero é par ou impar.
		
		String valor = JOptionPane.showInputDialog("Informe o um numero: ");
		
		int numero = Integer.parseInt(valor);
		
		if((numero % 2) == 0) {
			System.out.printf("O numero %d e par", numero);
		}else {
			System.out.printf("O numero %d e impar", numero);
		}
	}
}
