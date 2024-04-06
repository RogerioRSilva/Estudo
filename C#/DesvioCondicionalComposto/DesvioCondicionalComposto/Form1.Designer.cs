namespace DesvioCondicionalComposto
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
            lblNota1 = new Label();
            lblNota2 = new Label();
            lblNota3 = new Label();
            lblNota4 = new Label();
            lblMedia = new Label();
            lblMediaCalculada = new Label();
            lblSituacao = new Label();
            lblSituacaoAluno = new Label();
            txtNota1 = new TextBox();
            txtNota2 = new TextBox();
            txtNota3 = new TextBox();
            txtNota4 = new TextBox();
            btnCalcularMedia = new Button();
            SuspendLayout();
            // 
            // lblNota1
            // 
            lblNota1.AutoSize = true;
            lblNota1.Location = new Point(42, 51);
            lblNota1.Name = "lblNota1";
            lblNota1.Size = new Size(53, 15);
            lblNota1.TabIndex = 0;
            lblNota1.Text = "1ª Nota: ";
            // 
            // lblNota2
            // 
            lblNota2.AutoSize = true;
            lblNota2.Location = new Point(209, 51);
            lblNota2.Name = "lblNota2";
            lblNota2.Size = new Size(53, 15);
            lblNota2.TabIndex = 1;
            lblNota2.Text = "2ª Nota: ";
            // 
            // lblNota3
            // 
            lblNota3.AutoSize = true;
            lblNota3.Location = new Point(381, 51);
            lblNota3.Name = "lblNota3";
            lblNota3.Size = new Size(53, 15);
            lblNota3.TabIndex = 2;
            lblNota3.Text = "3ª Nota: ";
            // 
            // lblNota4
            // 
            lblNota4.AutoSize = true;
            lblNota4.Location = new Point(550, 51);
            lblNota4.Name = "lblNota4";
            lblNota4.Size = new Size(53, 15);
            lblNota4.TabIndex = 3;
            lblNota4.Text = "4ª Nota: ";
            // 
            // lblMedia
            // 
            lblMedia.AutoSize = true;
            lblMedia.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point, 0);
            lblMedia.Location = new Point(42, 117);
            lblMedia.Name = "lblMedia";
            lblMedia.Size = new Size(66, 21);
            lblMedia.TabIndex = 4;
            lblMedia.Text = "Média: ";
            // 
            // lblMediaCalculada
            // 
            lblMediaCalculada.AutoSize = true;
            lblMediaCalculada.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point, 0);
            lblMediaCalculada.Location = new Point(114, 117);
            lblMediaCalculada.Name = "lblMediaCalculada";
            lblMediaCalculada.Size = new Size(0, 21);
            lblMediaCalculada.TabIndex = 5;
            // 
            // lblSituacao
            // 
            lblSituacao.AutoSize = true;
            lblSituacao.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point, 0);
            lblSituacao.Location = new Point(42, 188);
            lblSituacao.Name = "lblSituacao";
            lblSituacao.Size = new Size(134, 21);
            lblSituacao.TabIndex = 6;
            lblSituacao.Text = "Situação Aluno: ";
            // 
            // lblSituacaoAluno
            // 
            lblSituacaoAluno.AutoSize = true;
            lblSituacaoAluno.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point, 0);
            lblSituacaoAluno.Location = new Point(182, 188);
            lblSituacaoAluno.Name = "lblSituacaoAluno";
            lblSituacaoAluno.Size = new Size(0, 21);
            lblSituacaoAluno.TabIndex = 7;
            // 
            // txtNota1
            // 
            txtNota1.Location = new Point(101, 48);
            txtNota1.Name = "txtNota1";
            txtNota1.Size = new Size(60, 23);
            txtNota1.TabIndex = 8;
            // 
            // txtNota2
            // 
            txtNota2.Location = new Point(268, 48);
            txtNota2.Name = "txtNota2";
            txtNota2.Size = new Size(60, 23);
            txtNota2.TabIndex = 9;
            // 
            // txtNota3
            // 
            txtNota3.Location = new Point(440, 48);
            txtNota3.Name = "txtNota3";
            txtNota3.Size = new Size(60, 23);
            txtNota3.TabIndex = 10;
            // 
            // txtNota4
            // 
            txtNota4.Location = new Point(609, 48);
            txtNota4.Name = "txtNota4";
            txtNota4.Size = new Size(60, 23);
            txtNota4.TabIndex = 11;
            // 
            // btnCalcularMedia
            // 
            btnCalcularMedia.Location = new Point(42, 249);
            btnCalcularMedia.Name = "btnCalcularMedia";
            btnCalcularMedia.Size = new Size(119, 23);
            btnCalcularMedia.TabIndex = 12;
            btnCalcularMedia.Text = "Calcular Média";
            btnCalcularMedia.UseVisualStyleBackColor = true;
            btnCalcularMedia.Click += button1_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 319);
            Controls.Add(btnCalcularMedia);
            Controls.Add(txtNota4);
            Controls.Add(txtNota3);
            Controls.Add(txtNota2);
            Controls.Add(txtNota1);
            Controls.Add(lblSituacaoAluno);
            Controls.Add(lblSituacao);
            Controls.Add(lblMediaCalculada);
            Controls.Add(lblMedia);
            Controls.Add(lblNota4);
            Controls.Add(lblNota3);
            Controls.Add(lblNota2);
            Controls.Add(lblNota1);
            Name = "Form1";
            Text = "Calculo de Média";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label lblNota1;
        private Label lblNota2;
        private Label lblNota3;
        private Label lblNota4;
        private Label lblMedia;
        private Label lblMediaCalculada;
        private Label lblSituacao;
        private Label lblSituacaoAluno;
        private TextBox txtNota1;
        private TextBox txtNota2;
        private TextBox txtNota3;
        private TextBox txtNota4;
        private Button btnCalcularMedia;
    }
}
