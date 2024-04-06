namespace DesvioCondicionalComposto
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double nota1, nota2, nota3, nota4, media;

            nota1 = Convert.ToDouble(txtNota1.Text);
            nota2 = Convert.ToDouble(txtNota2.Text);
            nota3 = Convert.ToDouble(txtNota3.Text);
            nota4 = Convert.ToDouble(txtNota4.Text);

            media = (nota1 + nota2 + nota3 + nota4) / 4.0;

            if (media >= 7.0 && media <= 10.0)
            {
                lblMediaCalculada.Text = media.ToString();
                lblSituacaoAluno.Text = "Aluno Aprovado. Parabéns!!!";
                lblSituacaoAluno.ForeColor = Color.Green;

            }
            else if (media < 7.0 && media >= 5.0)
            {
                lblMediaCalculada.Text = media.ToString();
                lblSituacaoAluno.Text = "Aluno está de Recuperação."; 
                lblSituacaoAluno.ForeColor = Color.Blue;

            }
            else if (media < 5.0 && media >= 0.0)
            {
                lblMediaCalculada.Text = media.ToString();
                lblSituacaoAluno.Text = "Aluno Reprovado!!!";
                lblSituacaoAluno.ForeColor = Color.Red;
            }
            else
            {
                MessageBox.Show("Média Incorreta!!! Verifique se os valores estão entre 0 e 10.");
            }
        }
    }
}
