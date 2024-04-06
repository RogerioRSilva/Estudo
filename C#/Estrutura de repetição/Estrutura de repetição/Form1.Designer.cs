namespace Estrutura_de_repetição
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
            lblDiaSemana = new Label();
            txtDiaSemana = new TextBox();
            lblValidaDia = new Button();
            lblSemana = new Label();
            SuspendLayout();
            // 
            // lblDiaSemana
            // 
            lblDiaSemana.AutoSize = true;
            lblDiaSemana.Location = new Point(23, 51);
            lblDiaSemana.Name = "lblDiaSemana";
            lblDiaSemana.Size = new Size(153, 15);
            lblDiaSemana.TabIndex = 0;
            lblDiaSemana.Text = "Digite um numero de 1 à 7: ";
            lblDiaSemana.Click += label1_Click;
            // 
            // txtDiaSemana
            // 
            txtDiaSemana.Location = new Point(182, 48);
            txtDiaSemana.Name = "txtDiaSemana";
            txtDiaSemana.PlaceholderText = "Digite um número";
            txtDiaSemana.Size = new Size(112, 23);
            txtDiaSemana.TabIndex = 1;
            // 
            // lblValidaDia
            // 
            lblValidaDia.Location = new Point(117, 92);
            lblValidaDia.Name = "lblValidaDia";
            lblValidaDia.Size = new Size(128, 23);
            lblValidaDia.TabIndex = 2;
            lblValidaDia.Text = "Validar Dia Semana";
            lblValidaDia.UseVisualStyleBackColor = true;
            lblValidaDia.Click += button1_Click;
            // 
            // lblSemana
            // 
            lblSemana.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            lblSemana.AutoSize = true;
            lblSemana.Font = new Font("Segoe UI Semibold", 18F, FontStyle.Bold | FontStyle.Italic, GraphicsUnit.Point, 0);
            lblSemana.Location = new Point(63, 163);
            lblSemana.Name = "lblSemana";
            lblSemana.Size = new Size(0, 32);
            lblSemana.TabIndex = 3;
            lblSemana.TextAlign = ContentAlignment.MiddleCenter;
            lblSemana.Click += lblSemana_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(395, 292);
            Controls.Add(lblSemana);
            Controls.Add(lblValidaDia);
            Controls.Add(txtDiaSemana);
            Controls.Add(lblDiaSemana);
            Name = "Form1";
            Text = "Mostra dia da Semana";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label lblDiaSemana;
        private TextBox txtDiaSemana;
        private Button lblValidaDia;
        private Label lblSemana;
    }
}
