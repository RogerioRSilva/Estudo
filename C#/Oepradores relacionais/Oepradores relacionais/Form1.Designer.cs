namespace Oepradores_relacionais
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
            lblmedia = new Label();
            txtmedia = new TextBox();
            btnverificar = new Button();
            SuspendLayout();
            // 
            // lblmedia
            // 
            lblmedia.AutoSize = true;
            lblmedia.Location = new Point(43, 61);
            lblmedia.Name = "lblmedia";
            lblmedia.Size = new Size(40, 15);
            lblmedia.TabIndex = 0;
            lblmedia.Text = "Média";
            // 
            // txtmedia
            // 
            txtmedia.Location = new Point(89, 58);
            txtmedia.Name = "txtmedia";
            txtmedia.Size = new Size(100, 23);
            txtmedia.TabIndex = 1;
            // 
            // btnverificar
            // 
            btnverificar.Location = new Point(43, 104);
            btnverificar.Name = "btnverificar";
            btnverificar.Size = new Size(75, 23);
            btnverificar.TabIndex = 2;
            btnverificar.Text = "Verificar";
            btnverificar.UseVisualStyleBackColor = true;
            btnverificar.Click += btnverificar_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(375, 239);
            Controls.Add(btnverificar);
            Controls.Add(txtmedia);
            Controls.Add(lblmedia);
            Name = "Form1";
            Text = "Média";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label lblmedia;
        private TextBox txtmedia;
        private Button btnverificar;
    }
}
