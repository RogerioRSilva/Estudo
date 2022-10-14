package fundamentos;

public class DesafioOperadoresLógicos {

	public static void main(String[] args) {
		
		boolean trabalho1 = false;
		boolean trabalho2 = !true;
		
		if (trabalho1 && trabalho2) {
			System.out.println("Vamos ao shopping comprar um TV de 50''. :) ");
			System.out.println("Vamos todos tomar sorvete juntos. :) ");
		}
		else if(trabalho1 || trabalho2) {
			System.out.println("Vamos ao shopping comprar um TV de 32''. :) ");
			System.out.println("Vamos todos tomar sorvete juntos. :) ");
		}
		else {
			System.out.println("Vamos todos ficar em casa. :( ");
		}
	}
	
}
