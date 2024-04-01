namespace HelloWord
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
            Clique = new Button();
            label1 = new Label();
            textBox1 = new TextBox();
            SuspendLayout();
            // 
            // Clique
            // 
            Clique.BackColor = Color.LightGray;
            Clique.FlatAppearance.BorderColor = Color.Black;
            Clique.FlatAppearance.BorderSize = 2;
            Clique.FlatStyle = FlatStyle.System;
            Clique.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point, 0);
            Clique.Location = new Point(35, 122);
            Clique.Name = "Clique";
            Clique.Size = new Size(111, 23);
            Clique.TabIndex = 0;
            Clique.Text = "Clique Aqui";
            Clique.UseVisualStyleBackColor = false;
            Clique.Click += button1_Click;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(35, 87);
            label1.Name = "label1";
            label1.Size = new Size(40, 15);
            label1.TabIndex = 1;
            label1.Text = "Nome";
            label1.Click += label1_Click;
            // 
            // textBox1
            // 
            textBox1.BorderStyle = BorderStyle.FixedSingle;
            textBox1.Location = new Point(81, 84);
            textBox1.Name = "textBox1";
            textBox1.PlaceholderText = " Digite seu nome aqui";
            textBox1.Size = new Size(290, 23);
            textBox1.TabIndex = 2;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(758, 450);
            Controls.Add(textBox1);
            Controls.Add(label1);
            Controls.Add(Clique);
            FormBorderStyle = FormBorderStyle.Fixed3D;
            Name = "Form1";
            Text = "Form1";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button Clique;
        private Label label1;
        private TextBox textBox1;
    }
}
