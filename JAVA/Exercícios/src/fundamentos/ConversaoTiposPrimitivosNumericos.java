package fundamentos;



import javax.swing.JOptionPane;

public class ConversaoTiposPrimitivosNumericos {
	public static void main(String[] args) {
		// Convertendo numero em string
		Integer num1 = 100000;
		System.out.println(num1.toString());
		System.out.println(num1.toString().length());
		
		int num2 = 100000;
		System.out.println(Integer.toString(num2));
		System.out.println(Integer.toString(num2).length());
		
		// Convertendo string em numero
		String valor1 = JOptionPane.showInputDialog("Digite o Primeiro numero: ");
		String valor2 = JOptionPane.showInputDialog("Digite o Segundo numero: ");
		
		System.out.println(valor1);
		System.out.println(valor2);
		
		double n1 = Double.parseDouble(valor1);
		double n2 = Double.parseDouble(valor2);
		
		double soma = n1 + n2;
		
		System.out.printf("A soma de %f + %f = %.2f",n1, n2, soma );
		
		double media = (soma)/2;
		
		System.out.printf("\nA media total e : %.2f", media);
		
		
	}
}
