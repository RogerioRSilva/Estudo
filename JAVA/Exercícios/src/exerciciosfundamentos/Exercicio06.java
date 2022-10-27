package exerciciosfundamentos;

public class Exercicio06 {
	public static void main(String[] args) {
		/*
		 * Criar um programa que resolve equações do segundo grau 
		 * (ax2 + bx + c = 0) utilizando a fórmula de Bhaskara. 
		 * Use como exemplo a = 1, b = 12 e c = -13. Encontre o delta
		 * */
		
		var a = 1;
		var b = 12;
		var c = -13;
		
		double delta = Math.pow(b, 2)- (4 * a * c);
		
		double xln = (-b +(Math.sqrt(delta))/(2*a));
		
		double x2ln = (-b -(Math.sqrt(delta))/(2*a));
		
		System.out.printf("Resultado X linha = %.2f \nResultado X 2linhas = %.2f",xln,x2ln);
		
		
	}
}
