namespace SittingPostureDetectionSystem
{
    partial class FrmVideo
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
            components = new System.ComponentModel.Container();
            panel1 = new Panel();
            splitContainer1 = new SplitContainer();
            groupBox1 = new GroupBox();
            labNoneObject = new Label();
            labNormalTime = new Label();
            labCrossLegCnt = new Label();
            labHunchCnt = new Label();
            labStretchNeckCnt = new Label();
            labWryNeckCnt = new Label();
            labLowHeadCnt = new Label();
            labCrossLeg = new Label();
            labHunch = new Label();
            labStreatNeck = new Label();
            labWryNect = new Label();
            labLowHead = new Label();
            labNormal = new Label();
            labShowTotalTime = new Label();
            btnStop = new Button();
            btnStart = new Button();
            cbxCameras = new ComboBox();
            labSelectCamera = new Label();
            normalRuntime = new System.Windows.Forms.Timer(components);
            totalRuntime = new System.Windows.Forms.Timer(components);
            panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)splitContainer1).BeginInit();
            splitContainer1.Panel2.SuspendLayout();
            splitContainer1.SuspendLayout();
            groupBox1.SuspendLayout();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            panel1.Controls.Add(splitContainer1);
            panel1.Controls.Add(cbxCameras);
            panel1.Controls.Add(labSelectCamera);
            panel1.Location = new Point(0, 0);
            panel1.Name = "panel1";
            panel1.Size = new Size(1496, 964);
            panel1.TabIndex = 0;
            // 
            // splitContainer1
            // 
            splitContainer1.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            splitContainer1.FixedPanel = FixedPanel.Panel2;
            splitContainer1.Location = new Point(0, 70);
            splitContainer1.Name = "splitContainer1";
            // 
            // splitContainer1.Panel1
            // 
            splitContainer1.Panel1.SizeChanged += splitContainer1_Panel1_SizeChanged;
            splitContainer1.Panel1MinSize = 0;
            // 
            // splitContainer1.Panel2
            // 
            splitContainer1.Panel2.Controls.Add(groupBox1);
            splitContainer1.Panel2.Controls.Add(labShowTotalTime);
            splitContainer1.Panel2.Controls.Add(btnStop);
            splitContainer1.Panel2.Controls.Add(btnStart);
            splitContainer1.Panel2MinSize = 0;
            splitContainer1.Size = new Size(1496, 893);
            splitContainer1.SplitterDistance = 1096;
            splitContainer1.SplitterWidth = 6;
            splitContainer1.TabIndex = 3;
            // 
            // groupBox1
            // 
            groupBox1.Controls.Add(labNoneObject);
            groupBox1.Controls.Add(labNormalTime);
            groupBox1.Controls.Add(labCrossLegCnt);
            groupBox1.Controls.Add(labHunchCnt);
            groupBox1.Controls.Add(labStretchNeckCnt);
            groupBox1.Controls.Add(labWryNeckCnt);
            groupBox1.Controls.Add(labLowHeadCnt);
            groupBox1.Controls.Add(labCrossLeg);
            groupBox1.Controls.Add(labHunch);
            groupBox1.Controls.Add(labStreatNeck);
            groupBox1.Controls.Add(labWryNect);
            groupBox1.Controls.Add(labLowHead);
            groupBox1.Controls.Add(labNormal);
            groupBox1.Location = new Point(16, 238);
            groupBox1.Name = "groupBox1";
            groupBox1.Size = new Size(373, 643);
            groupBox1.TabIndex = 3;
            groupBox1.TabStop = false;
            groupBox1.Text = "当前状态";
            // 
            // labNoneObject
            // 
            labNoneObject.AutoSize = true;
            labNoneObject.Font = new Font("微软雅黑", 16F, FontStyle.Regular, GraphicsUnit.Point);
            labNoneObject.ForeColor = Color.DarkGray;
            labNoneObject.Location = new Point(38, 54);
            labNoneObject.Name = "labNoneObject";
            labNoneObject.Size = new Size(274, 41);
            labNoneObject.TabIndex = 12;
            labNoneObject.Text = "未检测到有效目标";
            // 
            // labNormalTime
            // 
            labNormalTime.AutoSize = true;
            labNormalTime.Location = new Point(243, 139);
            labNormalTime.Name = "labNormalTime";
            labNormalTime.Size = new Size(88, 25);
            labNormalTime.TabIndex = 11;
            labNormalTime.Text = "00:00:00";
            // 
            // labCrossLegCnt
            // 
            labCrossLegCnt.AutoSize = true;
            labCrossLegCnt.Font = new Font("微软雅黑", 10.5F, FontStyle.Regular, GraphicsUnit.Point);
            labCrossLegCnt.Location = new Point(276, 528);
            labCrossLegCnt.Name = "labCrossLegCnt";
            labCrossLegCnt.Size = new Size(51, 28);
            labCrossLegCnt.TabIndex = 10;
            labCrossLegCnt.Text = "0 次";
            // 
            // labHunchCnt
            // 
            labHunchCnt.AutoSize = true;
            labHunchCnt.Font = new Font("微软雅黑", 10.5F, FontStyle.Regular, GraphicsUnit.Point);
            labHunchCnt.Location = new Point(276, 451);
            labHunchCnt.Name = "labHunchCnt";
            labHunchCnt.Size = new Size(51, 28);
            labHunchCnt.TabIndex = 9;
            labHunchCnt.Text = "0 次";
            // 
            // labStretchNeckCnt
            // 
            labStretchNeckCnt.AutoSize = true;
            labStretchNeckCnt.Font = new Font("微软雅黑", 10.5F, FontStyle.Regular, GraphicsUnit.Point);
            labStretchNeckCnt.Location = new Point(276, 372);
            labStretchNeckCnt.Name = "labStretchNeckCnt";
            labStretchNeckCnt.Size = new Size(51, 28);
            labStretchNeckCnt.TabIndex = 8;
            labStretchNeckCnt.Text = "0 次";
            // 
            // labWryNeckCnt
            // 
            labWryNeckCnt.AutoSize = true;
            labWryNeckCnt.Font = new Font("微软雅黑", 10.5F, FontStyle.Regular, GraphicsUnit.Point);
            labWryNeckCnt.Location = new Point(276, 293);
            labWryNeckCnt.Name = "labWryNeckCnt";
            labWryNeckCnt.Size = new Size(51, 28);
            labWryNeckCnt.TabIndex = 7;
            labWryNeckCnt.Text = "0 次";
            // 
            // labLowHeadCnt
            // 
            labLowHeadCnt.AutoSize = true;
            labLowHeadCnt.Font = new Font("微软雅黑", 10.5F, FontStyle.Regular, GraphicsUnit.Point);
            labLowHeadCnt.Location = new Point(276, 214);
            labLowHeadCnt.Name = "labLowHeadCnt";
            labLowHeadCnt.Size = new Size(51, 28);
            labLowHeadCnt.TabIndex = 6;
            labLowHeadCnt.Text = "0 次";
            // 
            // labCrossLeg
            // 
            labCrossLeg.AutoSize = true;
            labCrossLeg.Font = new Font("微软雅黑", 16F, FontStyle.Regular, GraphicsUnit.Point);
            labCrossLeg.ForeColor = Color.DarkGray;
            labCrossLeg.Location = new Point(38, 514);
            labCrossLeg.Name = "labCrossLeg";
            labCrossLeg.Size = new Size(146, 41);
            labCrossLeg.TabIndex = 5;
            labCrossLeg.Text = "翘二郎腿";
            // 
            // labHunch
            // 
            labHunch.AutoSize = true;
            labHunch.Font = new Font("微软雅黑", 16F, FontStyle.Regular, GraphicsUnit.Point);
            labHunch.ForeColor = Color.DarkGray;
            labHunch.Location = new Point(38, 439);
            labHunch.Name = "labHunch";
            labHunch.Size = new Size(82, 41);
            labHunch.TabIndex = 4;
            labHunch.Text = "塌腰";
            // 
            // labStreatNeck
            // 
            labStreatNeck.AutoSize = true;
            labStreatNeck.Font = new Font("微软雅黑", 16F, FontStyle.Regular, GraphicsUnit.Point);
            labStreatNeck.ForeColor = Color.DarkGray;
            labStreatNeck.Location = new Point(38, 361);
            labStreatNeck.Name = "labStreatNeck";
            labStreatNeck.Size = new Size(82, 41);
            labStreatNeck.TabIndex = 3;
            labStreatNeck.Text = "伸脖";
            // 
            // labWryNect
            // 
            labWryNect.AutoSize = true;
            labWryNect.Font = new Font("微软雅黑", 16F, FontStyle.Regular, GraphicsUnit.Point);
            labWryNect.ForeColor = Color.DarkGray;
            labWryNect.Location = new Point(38, 283);
            labWryNect.Name = "labWryNect";
            labWryNect.Size = new Size(82, 41);
            labWryNect.TabIndex = 2;
            labWryNect.Text = "歪脖";
            // 
            // labLowHead
            // 
            labLowHead.AutoSize = true;
            labLowHead.Font = new Font("微软雅黑", 16F, FontStyle.Regular, GraphicsUnit.Point);
            labLowHead.ForeColor = Color.DarkGray;
            labLowHead.Location = new Point(38, 204);
            labLowHead.Name = "labLowHead";
            labLowHead.Size = new Size(146, 41);
            labLowHead.TabIndex = 1;
            labLowHead.Text = "头部过低";
            // 
            // labNormal
            // 
            labNormal.AutoSize = true;
            labNormal.Font = new Font("微软雅黑", 16F, FontStyle.Regular, GraphicsUnit.Point);
            labNormal.ForeColor = Color.DarkGray;
            labNormal.Location = new Point(38, 128);
            labNormal.Name = "labNormal";
            labNormal.Size = new Size(146, 41);
            labNormal.TabIndex = 0;
            labNormal.Text = "坐姿正常";
            // 
            // labShowTotalTime
            // 
            labShowTotalTime.AutoSize = true;
            labShowTotalTime.Font = new Font("微软雅黑", 26F, FontStyle.Bold, GraphicsUnit.Point);
            labShowTotalTime.Location = new Point(77, 49);
            labShowTotalTime.Name = "labShowTotalTime";
            labShowTotalTime.Size = new Size(252, 69);
            labShowTotalTime.TabIndex = 2;
            labShowTotalTime.Text = "00:00:00";
            // 
            // btnStop
            // 
            btnStop.Location = new Point(223, 166);
            btnStop.Name = "btnStop";
            btnStop.Size = new Size(121, 49);
            btnStop.TabIndex = 1;
            btnStop.Text = "停止";
            btnStop.UseVisualStyleBackColor = true;
            btnStop.Click += btnStop_Click;
            // 
            // btnStart
            // 
            btnStart.Location = new Point(55, 166);
            btnStart.Name = "btnStart";
            btnStart.Size = new Size(121, 49);
            btnStart.TabIndex = 0;
            btnStart.Text = "启动";
            btnStart.UseVisualStyleBackColor = true;
            btnStart.Click += btnStart_Click;
            // 
            // cbxCameras
            // 
            cbxCameras.DropDownStyle = ComboBoxStyle.DropDownList;
            cbxCameras.FormattingEnabled = true;
            cbxCameras.Location = new Point(162, 20);
            cbxCameras.Name = "cbxCameras";
            cbxCameras.Size = new Size(839, 33);
            cbxCameras.TabIndex = 4;
            // 
            // labSelectCamera
            // 
            labSelectCamera.AutoSize = true;
            labSelectCamera.Location = new Point(30, 22);
            labSelectCamera.Name = "labSelectCamera";
            labSelectCamera.Size = new Size(126, 25);
            labSelectCamera.TabIndex = 5;
            labSelectCamera.Text = "选择摄像头：";
            // 
            // normalRuntime
            // 
            normalRuntime.Interval = 1000;
            normalRuntime.Tick += normalRuntime_Tick;
            // 
            // totalRuntime
            // 
            totalRuntime.Interval = 1000;
            totalRuntime.Tick += totalRuntime_Tick;
            // 
            // FrmVideo
            // 
            AutoScaleDimensions = new SizeF(11F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1495, 964);
            Controls.Add(panel1);
            FormBorderStyle = FormBorderStyle.None;
            Name = "FrmVideo";
            Text = "FrmVideo";
            WindowState = FormWindowState.Maximized;
            SizeChanged += FrmVedio_SizeChanged;
            Resize += FrmVideo_Resize;
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            splitContainer1.Panel2.ResumeLayout(false);
            splitContainer1.Panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)splitContainer1).EndInit();
            splitContainer1.ResumeLayout(false);
            groupBox1.ResumeLayout(false);
            groupBox1.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private Panel panel1;
        private SplitContainer splitContainer1;
        private GroupBox groupBox1;
        private Label labNoneObject;
        private Label labNormalTime;
        private Label labCrossLegCnt;
        private Label labHunchCnt;
        private Label labStretchNeckCnt;
        private Label labWryNeckCnt;
        private Label labLowHeadCnt;
        private Label labCrossLeg;
        private Label labHunch;
        private Label labStreatNeck;
        private Label labWryNect;
        private Label labLowHead;
        private Label labNormal;
        private Label labShowTotalTime;
        private Button btnStop;
        private Button btnStart;
        private ComboBox cbxCameras;
        private Label labSelectCamera;
        private System.Windows.Forms.Timer normalRuntime;
        private System.Windows.Forms.Timer totalRuntime;
    }
}