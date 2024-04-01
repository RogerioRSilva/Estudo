namespace UsandoVariaveis
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

        private void button2_Click(object sender, EventArgs e)
        {
            double a, b;

            a = Convert.ToDouble(txt_a.Text);
            b = double.Parse(txt_b.Text);

            txtVariaveis.Text = ("Variavel A: " + a.ToString() + " Variavel B: " + b.ToString());
        }

        private void btnVariaveis_Click(object sender, EventArgs e)
        {
            int a, b;

            /* entrada de dados */
            a = Int32.Parse(txt_a.Text);
            b = Int32.Parse(txt_b.Text);

            /*saida de dados*/
            txtVariaveis.Text = ("Variavel A: " + a.ToString() + "   Variavel B: " + b.ToString() + 
                "      Tipo: Inteiro");
        }

        private void btnSomar_Click(object sender, EventArgs e)
        {
            int a, b, soma;

            /* entrada de dados */
            a = Int32.Parse(txt_a.Text);
            b = Int32.Parse(txt_b.Text);

            /* processamento */
            soma = a + b;

            /*saida de dados*/
            txtResultado.Text = soma.ToString();
        }


    }
}
