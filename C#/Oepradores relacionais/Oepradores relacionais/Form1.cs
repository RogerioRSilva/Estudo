namespace Oepradores_relacionais
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnverificar_Click(object sender, EventArgs e)
        {
            double media;

            media = Convert.ToDouble(txtmedia.Text);

            if (media >= 7)
            {
                MessageBox.Show("Aluno aprovado!! M�dia: " + media);
            }
            else
            {
                MessageBox.Show("Aluno reprovado!! M�dia: " + media);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Form2.
        }
    }
}
