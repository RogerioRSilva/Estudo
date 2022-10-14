package fundamentos;

public class Converção_de_Graus {
	public static void main(String[] args) {
		double f = 98.6;
		final double N1 = 5.0/9.0;
		final double N2 = 32.0;
		
		double convert = (f - N2) * N1;
		
		System.out.println("A conversao de " + f +"F em Celsius eh: " + convert + "C" );
	}
}
