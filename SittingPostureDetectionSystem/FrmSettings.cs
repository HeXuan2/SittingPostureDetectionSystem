using SittingPostureDetectionSystem.Common;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SittingPostureDetectionSystem
{
    public partial class FrmSettings : Form
    {
        static string route = AppDomain.CurrentDomain.BaseDirectory + "data\\";
        public Gaps gaps;
        //public int volume = 50, rate = 2;
        //public int gapLowHead = 10, gapWryNeck = 10, gapStreatNeck = 10, gapHunch = 10, gapCrossLeg = 10;
        public FrmSettings()
        {
            InitializeComponent();
            gaps = new Gaps();
            labRoute.Text = route;
            labRoute.MaximumSize = new(RecordManage.Width - 200, 0);
        }

        private void btnReset_Click(object sender, EventArgs e)
        {
            DialogResult res = MessageBox.Show("是否恢复默认？", "提示",
                MessageBoxButtons.OKCancel, MessageBoxIcon.Question);
            if (res == DialogResult.OK)
            {
                Reset();
            }

        }
        private void Reset()
        {
            Setting(50, 2, 10, 10, 10, 10, 10);

            //volume = 50;
            //rate = 2;
            //tcbVolume.Value = volume;
            //tcbRate.Value = rate;
            //VoiceAlerts.Setting(volume, rate);

            //gapLowHead = 10;
            //gapWryNeck = 10;
            //gapStreatNeck = 10;
            //gapHunch = 10;
            //gapCrossLeg = 10;

            //tbxLowHead.Text = gapLowHead.ToString();
            //tbxWryNeck.Text = gapWryNeck.ToString();
            //tbxStreatNeck.Text = gapStreatNeck.ToString();
            //tbxHunch.Text = gapHunch.ToString();
            //tbxCrossLeg.Text = gapCrossLeg.ToString();
        }

        private void btnApply_Click(object sender, EventArgs e)
        {
            DialogResult res = MessageBox.Show("是否保存并应用修改？", "提示",
                MessageBoxButtons.OKCancel, MessageBoxIcon.Question);
            if (res == DialogResult.OK)
            {
                Setting(tcbVolume.Value, tcbRate.Value,
                    int.Parse(tbxLowHead.Text),
                    int.Parse(tbxWryNeck.Text),
                    int.Parse(tbxStreatNeck.Text),
                    int.Parse(tbxHunch.Text),
                    int.Parse(tbxCrossLeg.Text));
            }
            else
            {
                Setting(gaps.volume, gaps.rate,
                    gaps.gapLowHead,
                    gaps.gapWryNeck,
                    gaps.gapStreatNeck,
                    gaps.gapHunch,
                    gaps.gapCrossLeg);
            }
        }

        private void btnOpen_Click(object sender, EventArgs e)
        {
            if (!Directory.Exists(route)) Directory.CreateDirectory(route);
            System.Diagnostics.Process.Start("explorer.exe", route);
        }

        private void btnDelete_Click(object sender, EventArgs e)
        {
            DialogResult res = MessageBox.Show("该操作不可逆，是否继续？", "警告",
                MessageBoxButtons.OKCancel, MessageBoxIcon.Warning);
            if (res == DialogResult.OK)
            {
                Directory.Delete(route, true);
            }
        }

        private void Setting(int volume, int rate, int gapLH, int gapWN, int gapSN, int gapH, int gapCL)
        {
            gaps.volume = volume;
            gaps.rate = rate;

            //this.volume = volume;
            //this.rate = rate;
            tcbVolume.Value = volume;
            tcbRate.Value = rate;
            labVolume.Text = volume.ToString();
            labRate.Text = rate.ToString();
            VoiceAlerts.Setting(volume, rate);

            gaps.gapLowHead = gapLH;
            gaps.gapWryNeck = gapWN;
            gaps.gapStreatNeck = gapSN;
            gaps.gapHunch = gapH;
            gaps.gapCrossLeg = gapCL;

            //gapLowHead = gapLH;
            //gapWryNeck = gapWN;
            //gapStreatNeck = gapSN;
            //gapHunch = gapH;
            //gapCrossLeg = gapCL;

            tbxLowHead.Text = gaps.gapLowHead.ToString();
            tbxWryNeck.Text = gaps.gapWryNeck.ToString();
            tbxStreatNeck.Text = gaps.gapStreatNeck.ToString();
            tbxHunch.Text = gaps.gapHunch.ToString();
            tbxCrossLeg.Text = gaps.gapCrossLeg.ToString();
        }

        public bool ComapreNowWithLast()
        {
            if (gaps.volume != tcbVolume.Value ||
                gaps.rate != tcbRate.Value ||
                gaps.gapLowHead != int.Parse(tbxLowHead.Text) ||
                gaps.gapWryNeck != int.Parse(tbxWryNeck.Text) ||
                gaps.gapStreatNeck != int.Parse(tbxStreatNeck.Text) ||
                gaps.gapHunch != int.Parse(tbxHunch.Text) ||
                gaps.gapCrossLeg != int.Parse(tbxCrossLeg.Text)) return true;
            return false;
        }

        public void ApplyModify()
        {
            Setting(tcbVolume.Value, tcbRate.Value,
                    int.Parse(tbxLowHead.Text),
                    int.Parse(tbxWryNeck.Text),
                    int.Parse(tbxStreatNeck.Text),
                    int.Parse(tbxHunch.Text),
                    int.Parse(tbxCrossLeg.Text));
        }
        public void ApplyLast()
        {
            Setting(gaps.volume, gaps.rate,
                    gaps.gapLowHead,
                    gaps.gapWryNeck,
                    gaps.gapStreatNeck,
                    gaps.gapHunch,
                    gaps.gapCrossLeg);
        }

        private void tcbVolume_Scroll(object sender, EventArgs e)
        {
            labVolume.Text = ((TrackBar)sender).Value.ToString();
        }

        private void tcbRate_Scroll(object sender, EventArgs e)
        {
            labRate.Text = ((TrackBar)sender).Value.ToString();
        }
    }
    public struct Gaps
    {
        public Gaps()
        {

        }

        public int volume = 50, rate = 2;
        public int gapLowHead = 10, gapWryNeck = 10, gapStreatNeck = 10, gapHunch = 10, gapCrossLeg = 10;
    }
}
