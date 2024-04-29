namespace SittingPostureDetectionSystem
{
    partial class MainForm
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
            TreeNode treeNode1 = new TreeNode("主界面");
            TreeNode treeNode2 = new TreeNode("数据统计");
            TreeNode treeNode3 = new TreeNode("设置");
            TreeNode treeNode4 = new TreeNode("关于");
            TreeNode treeNode5 = new TreeNode("帮助");
            splitContainer1 = new SplitContainer();
            trvMenu = new TreeView();
            ((System.ComponentModel.ISupportInitialize)splitContainer1).BeginInit();
            splitContainer1.Panel1.SuspendLayout();
            splitContainer1.SuspendLayout();
            SuspendLayout();
            // 
            // splitContainer1
            // 
            splitContainer1.Dock = DockStyle.Fill;
            splitContainer1.Location = new Point(0, 0);
            splitContainer1.Name = "splitContainer1";
            // 
            // splitContainer1.Panel1
            // 
            splitContainer1.Panel1.Controls.Add(trvMenu);
            // 
            // splitContainer1.Panel2
            // 
            splitContainer1.Panel2.Resize += splitContainer1_Panel2_Resize;
            splitContainer1.Size = new Size(1851, 1150);
            splitContainer1.SplitterDistance = 259;
            splitContainer1.TabIndex = 0;
            // 
            // trvMenu
            // 
            trvMenu.Dock = DockStyle.Fill;
            trvMenu.Font = new Font("微软雅黑", 12F, FontStyle.Regular, GraphicsUnit.Point);
            trvMenu.FullRowSelect = true;
            trvMenu.ItemHeight = 80;
            trvMenu.Location = new Point(0, 0);
            trvMenu.Name = "trvMenu";
            treeNode1.Name = "tnVedio";
            treeNode1.Tag = "FrmVideo";
            treeNode1.Text = "主界面";
            treeNode2.Name = "tnDataStatistics";
            treeNode2.Tag = "FrmDataStatistics";
            treeNode2.Text = "数据统计";
            treeNode3.Name = "tnSetting";
            treeNode3.Tag = "FrmSettings";
            treeNode3.Text = "设置";
            treeNode4.Name = "tnAbout";
            treeNode4.Tag = "FrmAbout";
            treeNode4.Text = "关于";
            treeNode5.Name = "tnHelper";
            treeNode5.Tag = "FrmHelper";
            treeNode5.Text = "帮助";
            trvMenu.Nodes.AddRange(new TreeNode[] { treeNode1, treeNode2, treeNode3, treeNode4, treeNode5 });
            trvMenu.ShowLines = false;
            trvMenu.Size = new Size(259, 1150);
            trvMenu.TabIndex = 0;
            trvMenu.BeforeSelect += trvMenu_BeforeSelect;
            trvMenu.AfterSelect += treeView1_AfterSelect;
            // 
            // MainForm
            // 
            AutoScaleDimensions = new SizeF(11F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1851, 1150);
            Controls.Add(splitContainer1);
            IsMdiContainer = true;
            MinimumSize = new Size(1763, 1140);
            Name = "MainForm";
            Text = "MainForm";
            FormClosing += MainForm_FormClosing;
            FormClosed += MainForm_FormClosed;
            Load += MainForm_Load;
            splitContainer1.Panel1.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)splitContainer1).EndInit();
            splitContainer1.ResumeLayout(false);
            ResumeLayout(false);
        }

        #endregion

        private SplitContainer splitContainer1;
        private TreeView trvMenu;
    }
}