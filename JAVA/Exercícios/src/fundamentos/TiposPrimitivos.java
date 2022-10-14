package fundamentos;

public class TiposPrimitivos {
	public static void main(String[] args) {
		/*
		 * TIPOS DE VARIAVEIS PRIMITIVAS
		 * 
		 * #NUMEROS INTEIROS: 
		 *  
		 *  > BYTE = 1 byte --> ( -128 até +127 )
		 *  > SHORT = dois bytes --> (+- 32.767)
		 *  > INT = 4 bytes --> ()
		 *  > LONG = 8 bytes 
		 *  
		 *  # NUMEROS REAIS
		 *  
		 *  > FLOAT = 4 bytes
		 *  > DOUBLE = 8 bytes
		 *  
		 *  # CARACTER
		 *  
		 *  > CHAR = um unico caracter --> 'A' ' ' (espaço pode ser um caracter)
		 *  
		 *  # BOLEANOS
		 *  
		 *  > BOOLEAN = FALSE ou TRUE (Verdadeiro ou Falso)
		 *   
		 */
		
		// Informações de um funcionário
		
		// Tipos Numéricos INTEIROS
		byte anosDeEmpresa = 23;
		short numeroDeVoos = 542;
		int id = 567;
		long pontosAcumulados = 3_234_845_223L; //com L na frente demonstra que ele é literal ou seja acima do valor de capacidade.
		
		// Tipos numéricos FLOAT
		float salario = 11_445.44F; // tem que ser colocado a letra F no final demonstra que ele é litral.
		double vendasAcumuladas = 2_991_797_103.01;
		
		// Tipos boleanos
		boolean estaDeFerias = false; //true
		
		// Tipos Caracter
		char status = 'A'; // Ativo  somente um caracter porem em listagem unicode pode ser feito assim '\u0010'
		
		System.out.println(anosDeEmpresa);		
		System.out.println(numeroDeVoos);
		System.out.println(id);	
		System.out.println(pontosAcumulados);	
		System.out.println(salario);
		System.out.println(vendasAcumuladas);
		System.out.println(estaDeFerias);
		System.out.println(status);	
		
	}
}
