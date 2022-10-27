package estruturadecontrole;

import java.util.Scanner;

public class DesafioWhile {
	
	public static void main(String[] args) {
		// Calcular a media da nota de uma turma. Vc não sabe a quantidade de alunos.
		// As notas são de 0 a 10. Quando for digitada a nota tem que somar todas as
		// notas
		// Contabilizar as notas digitadas. Encerra-se o programa quando o usuário
		// digitar -1

		Scanner entrada = new Scanner(System.in);

		int contaNota = 0;
		double nota = 0;
		double somaNota = 0;

		while (nota != -1) {
			System.out.print("Informe a nota: ");
			nota = entrada.nextDouble();

			if (nota >= 0 && nota <= 10) {
				contaNota++;
				somaNota += nota;

			}
		}

		double media = somaNota / contaNota;
		System.out.printf("Media = %.2f", media);

		entrada.close();
	}

}
