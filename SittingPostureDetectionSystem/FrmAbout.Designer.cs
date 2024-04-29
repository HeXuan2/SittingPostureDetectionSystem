namespace SittingPostureDetectionSystem
{
    partial class FrmAbout
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            panel1 = new Panel();
            label8 = new Label();
            label7 = new Label();
            label6 = new Label();
            label5 = new Label();
            label4 = new Label();
            label3 = new Label();
            label2 = new Label();
            label1 = new Label();
            panel1.SuspendLayout();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            panel1.Controls.Add(label8);
            panel1.Controls.Add(label7);
            panel1.Controls.Add(label6);
            panel1.Controls.Add(label5);
            panel1.Controls.Add(label4);
            panel1.Controls.Add(label3);
            panel1.Controls.Add(label2);
            panel1.Controls.Add(label1);
            panel1.Location = new Point(0, 0);
            panel1.Name = "panel1";
            panel1.Size = new Size(1447, 537);
            panel1.TabIndex = 0;
            // 
            // label8
            // 
            label8.AutoSize = true;
            label8.Font = new Font("新宋体", 12F, FontStyle.Regular, GraphicsUnit.Point);
            label8.Location = new Point(11, 409);
            label8.Name = "label8";
            label8.Size = new Size(526, 24);
            label8.TabIndex = 15;
            label8.Text = "版权所有 © 2022 SitWell Inc. 保留所有权利。";
            // 
            // label7
            // 
            label7.AutoSize = true;
            label7.Font = new Font("新宋体", 12F, FontStyle.Regular, GraphicsUnit.Point);
            label7.Location = new Point(11, 345);
            label7.Name = "label7";
            label7.Size = new Size(922, 24);
            label7.TabIndex = 14;
            label7.Text = "如果您遇到任何技术问题，可以联系我们的开发团队，邮箱：support@sitwell.com 。";
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Font = new Font("新宋体", 12F, FontStyle.Regular, GraphicsUnit.Point);
            label6.Location = new Point(11, 277);
            label6.Name = "label6";
            label6.Size = new Size(1354, 24);
            label6.TabIndex = 13;
            label6.Text = "该软件面向需要长时间坐下工作或学习的用户群体。我们希望通过这个软件，帮助用户减轻坐姿不良所带来的身体疲劳和疼痛。";
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Font = new Font("新宋体", 10F, FontStyle.Regular, GraphicsUnit.Point);
            label5.Location = new Point(48, 208);
            label5.Name = "label5";
            label5.Size = new Size(529, 20);
            label5.TabIndex = 12;
            label5.Text = "- 数据统计：分期记录用户坐姿状态，帮助用户发现问题。";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Font = new Font("新宋体", 10F, FontStyle.Regular, GraphicsUnit.Point);
            label4.Location = new Point(48, 174);
            label4.Name = "label4";
            label4.Size = new Size(649, 20);
            label4.TabIndex = 11;
            label4.Text = "- 提醒功能：定期提醒用户保持正确的坐姿；支持个性化设置提醒频次。";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("新宋体", 10F, FontStyle.Regular, GraphicsUnit.Point);
            label3.Location = new Point(48, 141);
            label3.Name = "label3";
            label3.Size = new Size(509, 20);
            label3.TabIndex = 10;
            label3.Text = "- 坐姿检测：通过摄像头对用户的坐姿进行检测和评估。";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("新宋体", 12F, FontStyle.Regular, GraphicsUnit.Point);
            label2.Location = new Point(11, 106);
            label2.Name = "label2";
            label2.Size = new Size(622, 24);
            label2.TabIndex = 9;
            label2.Text = "该应用程序目前仅支持Windows操作系统。主要功能包括：";
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("新宋体", 16F, FontStyle.Bold, GraphicsUnit.Point);
            label1.Location = new Point(11, 25);
            label1.Name = "label1";
            label1.Size = new Size(383, 33);
            label1.TabIndex = 8;
            label1.Text = "坐姿检测系统 v0.5 Bate";
            // 
            // FrmAbout
            // 
            AutoScaleDimensions = new SizeF(11F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1447, 537);
            Controls.Add(panel1);
            FormBorderStyle = FormBorderStyle.None;
            Name = "FrmAbout";
            Text = "FrmAbout";
            WindowState = FormWindowState.Maximized;
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private Panel panel1;
        private Label label8;
        private Label label7;
        private Label label6;
        private Label label5;
        private Label label4;
        private Label label3;
        private Label label2;
        private Label label1;
    }
}