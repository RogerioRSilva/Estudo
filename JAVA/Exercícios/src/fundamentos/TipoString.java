package fundamentos;

public class TipoString {

	public static void main(String[] args) {
		System.out.println("Ola pessoal".charAt(5));

		String s = "Boa tarde";
		System.out.println(s.concat("!!!"));
		System.out.println(s.startsWith("Boa")); // começa com uma letra ou palavra específica
		System.out.println(s.startsWith("boa"));
		System.out.println(s.endsWith("tarde")); // termina com uma letra ou palavra específica
		System.out.println(s.length()); // conta a quantidade de caracter que tem na string levando em consideração o
										// espaço
		System.out.println(s.equals(s)); // Verifica se a string é igual a outra
		System.out.println(s.equalsIgnoreCase("boa tarde")); // Nesse caso o equals faz a verificação ignorando a
																// diferença de tamanho de letras

		var nome = "Pedro";
		System.out.println(nome);
		var sobrenome = "Silva";
		var idade = 33;
		var salario = 12345.987;
		// String formatada ou template

		System.out.printf("\nO %s %s eh muito feliz. Ele tem %d anos e ganha R$%.2f de salário", nome, sobrenome, idade,
				salario);

	}
}
