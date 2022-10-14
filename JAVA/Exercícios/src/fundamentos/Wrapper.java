package fundamentos;

public class Wrapper {
	
	public static void main(String[] args) {
		//Byte
		Byte b = 100;
		Short s = 1000;
		
		//Integer.parseInt(entrada.next()); conversão de string em numero
		Integer i = 10000; // int
		Long l = 100000L;
		
		System.out.println(b.byteValue());
		System.out.println(s.toString()); // convertendo numero para string
		System.out.println(i * 3);
		System.out.println(l / 3);
		
		Float f = 123.23F;
		System.out.println(f);
		
		Double d = 1234.5678;
		System.out.println(d);
		
		Boolean bo = Boolean.parseBoolean("true");
		System.out.println(bo);
		System.out.println(bo.toString().toUpperCase());
		
		Character c = '#';
		System.out.println(c.toString());
				
	}

}
