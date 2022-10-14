package fundamentos;

public class Logicos {
	
	public static void main(String[] args) {
		
		boolean condicao1 = true;
		boolean condicao2 = false;
		
		System.out.println(condicao1);
		System.out.println(condicao2);
		
		System.out.printf("\n %b", (condicao1 && condicao2));
		System.out.printf("\n %b", (condicao1 || condicao2));
		System.out.printf("\n %b", (condicao1 ^ condicao2)); // ou esclusivo 
		System.out.printf("\n %b", (!condicao2)); // negação
		System.out.printf("\n %b", (!condicao1)); // negação
		
		System.out.println("\n\nTabela verdade OU exclusivo(XOR)");
		System.out.println(true ^ true); // falso
		System.out.println(true ^ false); // verdade
		System.out.println(false ^ true); // verdade
		System.out.println(false ^ false); // falso
		
		
	}
	
}
