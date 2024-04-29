namespace SittingPostureDetectionSystem
{
    partial class FrmSettings
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
            RecordManage = new GroupBox();
            labRoute = new Label();
            btnOpen = new Button();
            btnDelete = new Button();
            label3 = new Label();
            RemindControl = new GroupBox();
            btnApply = new Button();
            labRate = new Label();
            labVolume = new Label();
            tcbRate = new TrackBar();
            tcbVolume = new TrackBar();
            label7 = new Label();
            label5 = new Label();
            btnReset = new Button();
            label8 = new Label();
            tbxCrossLeg = new TextBox();
            labCLcnt = new Label();
            label6 = new Label();
            tbxHunch = new TextBox();
            labHcnt = new Label();
            label4 = new Label();
            tbxStreatNeck = new TextBox();
            labSNcnt = new Label();
            label2 = new Label();
            tbxWryNeck = new TextBox();
            labWNcnt = new Label();
            label1 = new Label();
            tbxLowHead = new TextBox();
            labLowHead = new Label();
            labText = new Label();
            panel1.SuspendLayout();
            RecordManage.SuspendLayout();
            RemindControl.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)tcbRate).BeginInit();
            ((System.ComponentModel.ISupportInitialize)tcbVolume).BeginInit();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            panel1.Controls.Add(RecordManage);
            panel1.Controls.Add(RemindControl);
            panel1.Location = new Point(0, 0);
            panel1.Name = "panel1";
            panel1.Size = new Size(1354, 799);
            panel1.TabIndex = 0;
            // 
            // RecordManage
            // 
            RecordManage.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right;
            RecordManage.Controls.Add(labRoute);
            RecordManage.Controls.Add(btnOpen);
            RecordManage.Controls.Add(btnDelete);
            RecordManage.Controls.Add(label3);
            RecordManage.Font = new Font("新宋体", 14F, FontStyle.Regular, GraphicsUnit.Point);
            RecordManage.Location = new Point(12, 401);
            RecordManage.Name = "RecordManage";
            RecordManage.Size = new Size(1330, 371);
            RecordManage.TabIndex = 1;
            RecordManage.TabStop = false;
            RecordManage.Text = "记录管理";
            // 
            // labRoute
            // 
            labRoute.AutoSize = true;
            labRoute.Location = new Point(294, 80);
            labRoute.Name = "labRoute";
            labRoute.Size = new Size(96, 28);
            labRoute.TabIndex = 17;
            labRoute.Text = "label9";
            // 
            // btnOpen
            // 
            btnOpen.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            btnOpen.Font = new Font("新宋体", 10.5F, FontStyle.Regular, GraphicsUnit.Point);
            btnOpen.Location = new Point(939, 303);
            btnOpen.Name = "btnOpen";
            btnOpen.Size = new Size(177, 52);
            btnOpen.TabIndex = 16;
            btnOpen.Text = "打开所在路径";
            btnOpen.UseVisualStyleBackColor = true;
            btnOpen.Click += btnOpen_Click;
            // 
            // btnDelete
            // 
            btnDelete.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            btnDelete.Font = new Font("新宋体", 10.5F, FontStyle.Regular, GraphicsUnit.Point);
            btnDelete.Location = new Point(1147, 303);
            btnDelete.Name = "btnDelete";
            btnDelete.Size = new Size(177, 52);
            btnDelete.TabIndex = 16;
            btnDelete.Text = "清除记录";
            btnDelete.UseVisualStyleBackColor = true;
            btnDelete.Click += btnDelete_Click;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(91, 80);
            label3.Name = "label3";
            label3.Size = new Size(208, 28);
            label3.TabIndex = 0;
            label3.Text = "记录存储路径：";
            // 
            // RemindControl
            // 
            RemindControl.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right;
            RemindControl.Controls.Add(btnApply);
            RemindControl.Controls.Add(labRate);
            RemindControl.Controls.Add(labVolume);
            RemindControl.Controls.Add(tcbRate);
            RemindControl.Controls.Add(tcbVolume);
            RemindControl.Controls.Add(label7);
            RemindControl.Controls.Add(label5);
            RemindControl.Controls.Add(btnReset);
            RemindControl.Controls.Add(label8);
            RemindControl.Controls.Add(tbxCrossLeg);
            RemindControl.Controls.Add(labCLcnt);
            RemindControl.Controls.Add(label6);
            RemindControl.Controls.Add(tbxHunch);
            RemindControl.Controls.Add(labHcnt);
            RemindControl.Controls.Add(label4);
            RemindControl.Controls.Add(tbxStreatNeck);
            RemindControl.Controls.Add(labSNcnt);
            RemindControl.Controls.Add(label2);
            RemindControl.Controls.Add(tbxWryNeck);
            RemindControl.Controls.Add(labWNcnt);
            RemindControl.Controls.Add(label1);
            RemindControl.Controls.Add(tbxLowHead);
            RemindControl.Controls.Add(labLowHead);
            RemindControl.Controls.Add(labText);
            RemindControl.Font = new Font("新宋体", 14F, FontStyle.Regular, GraphicsUnit.Point);
            RemindControl.Location = new Point(12, 12);
            RemindControl.Name = "RemindControl";
            RemindControl.Size = new Size(1330, 371);
            RemindControl.TabIndex = 0;
            RemindControl.TabStop = false;
            RemindControl.Text = "提醒控制";
            // 
            // btnApply
            // 
            btnApply.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            btnApply.Font = new Font("新宋体", 10.5F, FontStyle.Regular, GraphicsUnit.Point);
            btnApply.Location = new Point(1147, 301);
            btnApply.Name = "btnApply";
            btnApply.Size = new Size(177, 52);
            btnApply.TabIndex = 22;
            btnApply.Text = "应用";
            btnApply.UseVisualStyleBackColor = true;
            btnApply.Click += btnApply_Click;
            // 
            // labRate
            // 
            labRate.AutoSize = true;
            labRate.Location = new Point(1221, 185);
            labRate.Name = "labRate";
            labRate.Size = new Size(26, 28);
            labRate.TabIndex = 21;
            labRate.Text = "2";
            // 
            // labVolume
            // 
            labVolume.AutoSize = true;
            labVolume.Location = new Point(1221, 111);
            labVolume.Name = "labVolume";
            labVolume.Size = new Size(40, 28);
            labVolume.TabIndex = 20;
            labVolume.Text = "50";
            // 
            // tcbRate
            // 
            tcbRate.Location = new Point(982, 185);
            tcbRate.Name = "tcbRate";
            tcbRate.Size = new Size(235, 69);
            tcbRate.TabIndex = 19;
            tcbRate.Value = 2;
            tcbRate.Scroll += tcbRate_Scroll;
            // 
            // tcbVolume
            // 
            tcbVolume.Location = new Point(982, 108);
            tcbVolume.Maximum = 100;
            tcbVolume.Name = "tcbVolume";
            tcbVolume.Size = new Size(235, 69);
            tcbVolume.TabIndex = 18;
            tcbVolume.TickFrequency = 5;
            tcbVolume.Value = 50;
            tcbVolume.Scroll += tcbVolume_Scroll;
            // 
            // label7
            // 
            label7.AutoSize = true;
            label7.Location = new Point(880, 185);
            label7.Name = "label7";
            label7.Size = new Size(96, 28);
            label7.TabIndex = 17;
            label7.Text = "语速：";
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Location = new Point(880, 111);
            label5.Name = "label5";
            label5.Size = new Size(96, 28);
            label5.TabIndex = 16;
            label5.Text = "音量：";
            // 
            // btnReset
            // 
            btnReset.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            btnReset.Font = new Font("新宋体", 10.5F, FontStyle.Regular, GraphicsUnit.Point);
            btnReset.Location = new Point(939, 301);
            btnReset.Name = "btnReset";
            btnReset.Size = new Size(177, 52);
            btnReset.TabIndex = 3;
            btnReset.Text = "恢复默认";
            btnReset.UseVisualStyleBackColor = true;
            btnReset.Click += btnReset_Click;
            // 
            // label8
            // 
            label8.AutoSize = true;
            label8.Location = new Point(761, 184);
            label8.Name = "label8";
            label8.Size = new Size(40, 28);
            label8.TabIndex = 15;
            label8.Text = "次";
            // 
            // tbxCrossLeg
            // 
            tbxCrossLeg.Location = new Point(605, 179);
            tbxCrossLeg.Name = "tbxCrossLeg";
            tbxCrossLeg.Size = new Size(150, 39);
            tbxCrossLeg.TabIndex = 14;
            tbxCrossLeg.Text = "10";
            // 
            // labCLcnt
            // 
            labCLcnt.AutoSize = true;
            labCLcnt.Location = new Point(459, 185);
            labCLcnt.Name = "labCLcnt";
            labCLcnt.Size = new Size(152, 28);
            labCLcnt.TabIndex = 13;
            labCLcnt.Text = "翘二郎腿：";
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Location = new Point(761, 108);
            label6.Name = "label6";
            label6.Size = new Size(40, 28);
            label6.TabIndex = 12;
            label6.Text = "次";
            // 
            // tbxHunch
            // 
            tbxHunch.Location = new Point(605, 103);
            tbxHunch.Name = "tbxHunch";
            tbxHunch.Size = new Size(150, 39);
            tbxHunch.TabIndex = 11;
            tbxHunch.Text = "10";
            // 
            // labHcnt
            // 
            labHcnt.AutoSize = true;
            labHcnt.Location = new Point(459, 111);
            labHcnt.Name = "labHcnt";
            labHcnt.Size = new Size(96, 28);
            labHcnt.TabIndex = 10;
            labHcnt.Text = "塌腰：";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(331, 274);
            label4.Name = "label4";
            label4.Size = new Size(40, 28);
            label4.TabIndex = 9;
            label4.Text = "次";
            // 
            // tbxStreatNeck
            // 
            tbxStreatNeck.Location = new Point(175, 269);
            tbxStreatNeck.Name = "tbxStreatNeck";
            tbxStreatNeck.Size = new Size(150, 39);
            tbxStreatNeck.TabIndex = 8;
            tbxStreatNeck.Text = "10";
            // 
            // labSNcnt
            // 
            labSNcnt.AutoSize = true;
            labSNcnt.Location = new Point(84, 275);
            labSNcnt.Name = "labSNcnt";
            labSNcnt.Size = new Size(96, 28);
            labSNcnt.TabIndex = 7;
            labSNcnt.Text = "伸脖：";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(331, 190);
            label2.Name = "label2";
            label2.Size = new Size(40, 28);
            label2.TabIndex = 6;
            label2.Text = "次";
            // 
            // tbxWryNeck
            // 
            tbxWryNeck.Location = new Point(175, 185);
            tbxWryNeck.Name = "tbxWryNeck";
            tbxWryNeck.Size = new Size(150, 39);
            tbxWryNeck.TabIndex = 5;
            tbxWryNeck.Text = "10";
            // 
            // labWNcnt
            // 
            labWNcnt.AutoSize = true;
            labWNcnt.Location = new Point(84, 191);
            labWNcnt.Name = "labWNcnt";
            labWNcnt.Size = new Size(96, 28);
            labWNcnt.TabIndex = 4;
            labWNcnt.Text = "歪脖：";
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(331, 108);
            label1.Name = "label1";
            label1.Size = new Size(40, 28);
            label1.TabIndex = 3;
            label1.Text = "次";
            // 
            // tbxLowHead
            // 
            tbxLowHead.Location = new Point(175, 103);
            tbxLowHead.Name = "tbxLowHead";
            tbxLowHead.Size = new Size(150, 39);
            tbxLowHead.TabIndex = 2;
            tbxLowHead.Text = "10";
            // 
            // labLowHead
            // 
            labLowHead.AutoSize = true;
            labLowHead.Location = new Point(84, 109);
            labLowHead.Name = "labLowHead";
            labLowHead.Size = new Size(96, 28);
            labLowHead.TabIndex = 1;
            labLowHead.Text = "低头：";
            // 
            // labText
            // 
            labText.AutoSize = true;
            labText.Font = new Font("新宋体", 12F, FontStyle.Regular, GraphicsUnit.Point);
            labText.Location = new Point(41, 55);
            labText.Name = "labText";
            labText.Size = new Size(466, 24);
            labText.TabIndex = 0;
            labText.Text = "设置提醒频次（间隔多少次发出语音提醒）";
            // 
            // FrmSettings
            // 
            AutoScaleDimensions = new SizeF(11F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1354, 799);
            Controls.Add(panel1);
            FormBorderStyle = FormBorderStyle.None;
            Name = "FrmSettings";
            Text = "FrmSettings";
            WindowState = FormWindowState.Maximized;
            panel1.ResumeLayout(false);
            RecordManage.ResumeLayout(false);
            RecordManage.PerformLayout();
            RemindControl.ResumeLayout(false);
            RemindControl.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)tcbRate).EndInit();
            ((System.ComponentModel.ISupportInitialize)tcbVolume).EndInit();
            ResumeLayout(false);
        }

        #endregion

        private Panel panel1;
        private GroupBox RecordManage;
        private Button Apply;
        private GroupBox RemindControl;
        private Label labText;
        private Label label8;
        private TextBox tbxCrossLeg;
        private Label labCLcnt;
        private Label label6;
        private TextBox tbxHunch;
        private Label labHcnt;
        private Label label4;
        private TextBox tbxStreatNeck;
        private Label labSNcnt;
        private Label label2;
        private TextBox tbxWryNeck;
        private Label labWNcnt;
        private Label label1;
        private TextBox tbxLowHead;
        private Label labLowHead;
        private Button btnReset;
        private Label label3;
        private Button btnDelete;
        private Button btnOpen;
        private Label label7;
        private Label label5;
        private TrackBar tcbRate;
        private TrackBar tcbVolume;
        private Label labRate;
        private Label labVolume;
        private Button btnApply;
        private Label labRoute;
    }
}