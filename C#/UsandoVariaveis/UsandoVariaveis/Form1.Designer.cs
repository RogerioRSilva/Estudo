namespace UsandoVariaveis
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            lbl_a = new Label();
            lbl_b = new Label();
            txt_a = new TextBox();
            txt_b = new TextBox();
            txtResultado = new TextBox();
            lblResultado = new Label();
            lblVariaveis = new Button();
            btnSomar = new Button();
            label1 = new Label();
            lblExibir = new Label();
            txtVariaveis = new TextBox();
            SuspendLayout();
            // 
            // lbl_a
            // 
            lbl_a.AutoSize = true;
            lbl_a.Location = new Point(57, 57);
            lbl_a.Name = "lbl_a";
            lbl_a.Size = new Size(15, 15);
            lbl_a.TabIndex = 0;
            lbl_a.Text = "A";
            lbl_a.Click += label1_Click;
            // 
            // lbl_b
            // 
            lbl_b.AutoSize = true;
            lbl_b.Location = new Point(61, 107);
            lbl_b.Name = "lbl_b";
            lbl_b.Size = new Size(14, 15);
            lbl_b.TabIndex = 1;
            lbl_b.Text = "B";
            // 
            // txt_a
            // 
            txt_a.BorderStyle = BorderStyle.FixedSingle;
            txt_a.Location = new Point(78, 54);
            txt_a.Name = "txt_a";
            txt_a.Size = new Size(100, 23);
            txt_a.TabIndex = 2;
            // 
            // txt_b
            // 
            txt_b.BorderStyle = BorderStyle.FixedSingle;
            txt_b.Location = new Point(81, 104);
            txt_b.Name = "txt_b";
            txt_b.Size = new Size(100, 23);
            txt_b.TabIndex = 3;
            // 
            // txtResultado
            // 
            txtResultado.BorderStyle = BorderStyle.FixedSingle;
            txtResultado.Location = new Point(81, 156);
            txtResultado.Name = "txtResultado";
            txtResultado.ReadOnly = true;
            txtResultado.Size = new Size(100, 23);
            txtResultado.TabIndex = 4;
            // 
            // lblResultado
            // 
            lblResultado.AutoSize = true;
            lblResultado.Location = new Point(16, 159);
            lblResultado.Name = "lblResultado";
            lblResultado.Size = new Size(59, 15);
            lblResultado.TabIndex = 5;
            lblResultado.Text = "Resultado";
            // 
            // lblVariaveis
            // 
            lblVariaveis.Location = new Point(238, 54);
            lblVariaveis.Name = "lblVariaveis";
            lblVariaveis.Size = new Size(75, 23);
            lblVariaveis.TabIndex = 6;
            lblVariaveis.Text = "Variáveis";
            lblVariaveis.UseVisualStyleBackColor = true;
            lblVariaveis.Click += btnVariaveis_Click;
            // 
            // btnSomar
            // 
            btnSomar.Location = new Point(238, 156);
            btnSomar.Name = "btnSomar";
            btnSomar.Size = new Size(75, 23);
            btnSomar.TabIndex = 8;
            btnSomar.Text = "Somar";
            btnSomar.UseVisualStyleBackColor = true;
            btnSomar.Click += btnSomar_Click;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(0, 0);
            label1.Name = "label1";
            label1.Size = new Size(38, 15);
            label1.TabIndex = 9;
            label1.Text = "label1";
            // 
            // lblExibir
            // 
            lblExibir.AutoSize = true;
            lblExibir.Location = new Point(16, 219);
            lblExibir.Name = "lblExibir";
            lblExibir.Size = new Size(90, 15);
            lblExibir.TabIndex = 10;
            lblExibir.Text = "Exibir Variaveis: ";
            // 
            // txtVariaveis
            // 
            txtVariaveis.BorderStyle = BorderStyle.None;
            txtVariaveis.Location = new Point(112, 222);
            txtVariaveis.Multiline = true;
            txtVariaveis.Name = "txtVariaveis";
            txtVariaveis.ReadOnly = true;
            txtVariaveis.Size = new Size(176, 65);
            txtVariaveis.TabIndex = 11;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(352, 299);
            Controls.Add(txtVariaveis);
            Controls.Add(lblExibir);
            Controls.Add(label1);
            Controls.Add(btnSomar);
            Controls.Add(lblVariaveis);
            Controls.Add(lblResultado);
            Controls.Add(txtResultado);
            Controls.Add(txt_b);
            Controls.Add(txt_a);
            Controls.Add(lbl_b);
            Controls.Add(lbl_a);
            Name = "Form1";
            Text = "Usando Variáveis";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label lbl_a;
        private Label lbl_b;
        private TextBox txt_a;
        private TextBox txt_b;
        private TextBox txtResultado;
        private Label lblResultado;
        private Button lblVariaveis;
        private Button btnSomar;
        private Label label1;
        private Label lblExibir;
        private TextBox txtVariaveis;
        private Button btnReais;
    }
}
