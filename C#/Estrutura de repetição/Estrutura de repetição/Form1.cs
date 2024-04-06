namespace Estrutura_de_repetição
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void lblSemana_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            String diaSemana;

            diaSemana = txtDiaSemana.Text;

            switch (diaSemana)
            {
                case "1":
                    lblSemana.Text = "Domingo";
                    lblSemana.ForeColor = Color.Red;
                    break;

                case "2":
                    lblSemana.Text = "Segunda-Feira";
                    lblSemana.ForeColor = Color.Blue;
                    break;

                case "3":
                    lblSemana.Text = "Terça-Feira";
                    lblSemana.ForeColor = Color.Blue;
                    break;

                case "4":
                    lblSemana.Text = "Quarta-Feira";
                    lblSemana.ForeColor = Color.Blue;
                    break;
                
                case "5":
                    lblSemana.Text = "Quinta-Feira";
                    lblSemana.ForeColor = Color.Blue;
                    break;

                case "6":
                    lblSemana.Text = "Sexta-Feita";
                    lblSemana.ForeColor = Color.Blue;
                    break;

                case "7":
                    lblSemana.Text = "Sábado";
                    lblSemana.ForeColor = Color.Red;
                    break;

                default:
                    lblSemana.Text = "Semana inválida!!!";
                    lblSemana.ForeColor = Color.Red;
                    break;
            }
        }
    }
}
