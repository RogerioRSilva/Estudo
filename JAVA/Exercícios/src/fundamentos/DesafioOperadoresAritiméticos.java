package fundamentos;

public class DesafioOperadoresAritiméticos {

	public static void main(String[] args) {
		
		/*
		 * Transforme essa formula em um programa utilizando variáveis. 
		 * 
		 * ([6*(3+2)]²/3*2 - ((1-5)*(2-7)/2)²)³/10³
		 * 
		 * */
		
		// Fracionei a formula em partes utilizando pequenas formulas e atribuindo as variáveis.
		
		
		var formulaElevada2 = Math.pow((6*(3+2)), 2); // elevei a formula1 ao quadrado
		
		var formula2 = formulaElevada2 / (3 * 2);
		
		var formula3Elevada2 = Math.pow(((1-5)*(2-7) / 2), 2); // elevei a formula3 ao quadrado
		
		double formulaCompleta = (Math.pow((formula2 - formula3Elevada2), 3 )) / Math.pow(10, 3); //Final
		
		int formulaCompleta2 = (int) formulaCompleta; // conversão de double para inteiro

		System.out.printf("O resultado da formula e: %d",formulaCompleta2);//saida
		
	}
	
}
