using SittingPostureDetectionSystem.Common;
using System;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace SittingPostureDetectionSystem
{
    public partial class MainForm : Form
    {
        Form? form;
        public MainForm()
        {
            InitializeComponent();
            //SetWindow.EmbedExternalWindow(sp);
            //bool findRes = SetWindow.FindWindow("frame");
            //if (findRes == true)
            //{
            //    SetWindow.SetParent(vedioPanel.Handle);
            //}
        }

        private void MainForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            SetWindow.Form_FormClosing();
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            form = FormFactory.CreateForm("FrmVideo");
            form.MdiParent = this;
            form.Parent = splitContainer1.Panel2;
            form.Show();
        }

        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {
            // 均可获取当前选中的结点对象
            //((TreeView)sender).SelectedNode;
            //e.Node;
            //trvMenu.SelectedNode;
            foreach (TreeNode node in trvMenu.Nodes)
            {
                node.BackColor = Color.White;
                node.ForeColor = Color.Black;
            }
            e.Node.BackColor = SystemColors.Highlight;
            e.Node.ForeColor = Color.White;

            form = FormFactory.CreateForm(e.Node.Tag.ToString());
            form.MdiParent = this;
            form.Parent = splitContainer1.Panel2;
            splitContainer1_Panel2_Resize(sender, e);
            form.Show();

            if (e.Node.Tag.ToString() == "FrmVideo")
            {
                FrmVideo form = (FrmVideo)FormFactory.GetForm("FrmVideo");
                form.SetParent();
            }

            if (e.Node.Tag.ToString() == "FrmDataStatistics")
            {
                FrmDataStatistics form = (FrmDataStatistics)FormFactory.GetForm("FrmDataStatistics");
                if (form != null) form.Reload();
            }
        }

        private void splitContainer1_Panel2_Resize(object sender, EventArgs e)
        {
            if (form != null)
            {
                form.WindowState = FormWindowState.Normal;
                form.Size = splitContainer1.Panel2.ClientSize;
                form.WindowState = FormWindowState.Maximized;
                form.Show();
            }
        }

        private void MainForm_FormClosed(object sender, FormClosedEventArgs e)
        {
            SetWindow.Form_FormClosing();
        }

        FrmSettings formSettings;
        private bool IsModified()
        {
            formSettings = (FrmSettings)FormFactory.GetForm("FrmSettings");
            if (formSettings == null) return false;
            return formSettings.ComapreNowWithLast();
        }

        private void trvMenu_BeforeSelect(object sender, TreeViewCancelEventArgs e)
        {
            if (IsModified())
            {
                DialogResult res = MessageBox.Show("当前修改未保存，是否保存并应用修改？", "提示",
                MessageBoxButtons.OKCancel, MessageBoxIcon.Question);
                if (res == DialogResult.OK)
                {
                    formSettings.ApplyModify();
                }
                else
                {
                    formSettings.ApplyLast();
                }
            }
        }
    }
}