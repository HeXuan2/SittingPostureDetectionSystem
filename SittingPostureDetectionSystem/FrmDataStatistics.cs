using SittingPostureDetectionSystem.Common;
using SittingPostureDetectionSystem.DataStatistics;
using SittingPostureDetectionSystem.DataStatistics.Common;
using SittingPostureDetectionSystem.DataStatistics.Models;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;

namespace SittingPostureDetectionSystem
{
    public partial class FrmDataStatistics : Form
    {
        public FrmDataStatistics()
        {
            InitializeComponent();
        }

        public void Reload()
        {
            LoadPage1PieChart();
            LoadPage1BarChart();

            LoadPage2PieChart();
            LoadPage2BarChart();

            LoadPage3PieChart();
            LoadPage3BarChart();

            LoadPage4PieChart();
            LoadPage4BarChart();
        }

        private void FrmDataStatistics_Load(object sender, EventArgs e)
        {
            //LoadPageBarChart(0, "toDayTypes");
            //LoadPagePieChart(0, "toDayStatus");

            //LoadPageBarChart(1, "weekTypes");
            //LoadPagePieChart(1, "weekStatus");

            //LoadPageBarChart(2, "monthTypes");
            //LoadPagePieChart(2, "monthStatus");

            //LoadPageBarChart(3, "allTypes");
            //LoadPagePieChart(3, "allStatus");

            LoadPage1PieChart();
            LoadPage1BarChart();

            LoadPage2PieChart();
            LoadPage2BarChart();

            LoadPage3PieChart();
            LoadPage3BarChart();

            LoadPage4PieChart();
            LoadPage4BarChart();
        }

        #region 已废弃
        //private async void LoadPageBarChart(int idx, string routeOrFileName)
        //{
        //    List<string> types = new() { "低头", "歪脖", "伸脖", "塌腰", "翘二郎腿" };
        //    Types typesCnt = await IO_Operations.IORead<Types>(routeOrFileName);
        //    List<int> cnt = new()
        //    {
        //        typesCnt.LowHeadCnt,
        //        typesCnt.WryNeckCnt,
        //        typesCnt.StretchNeckCnt,
        //        typesCnt.HunchCnt,
        //        typesCnt.CrossLegCnt,
        //    };

        //    Chart abnomalBar = (Chart)tabControl1.TabPages[idx].Controls.Find("AbnormalBar" + (idx + 1), true)[0];
        //    abnomalBar.Series[0].Points.DataBindXY(types, cnt);
        //    abnomalBar.Series[0].IsValueShownAsLabel = true;
        //    abnomalBar.Series[0].Font = new Font("Arial", 14, FontStyle.Bold);
        //}

        //private async void LoadPagePieChart(int idx, string routeOrFileName)
        //{
        //    List<string> status = new() { "正确", "异常" };
        //    Status statusCnt = await IO_Operations.IORead<Status>(routeOrFileName);
        //    List<double> val = new()
        //    {
        //        statusCnt.NormalTime,
        //        statusCnt.AbnormalTime
        //    };

        //    Chart nromalRatio = (Chart)tabControl1.TabPages[idx].Controls.Find("NormalRatio" + (idx + 1), true)[0];
        //    nromalRatio.Series[0].Points.DataBindXY(status, val);
        //    nromalRatio.Series[0].IsValueShownAsLabel = true;
        //    nromalRatio.Series[0].Font = new Font("Arial", 14, FontStyle.Bold);

        //    nromalRatio.Series[0].Label = "#VALY" + " 分钟";
        //    nromalRatio.Series[0].LegendText = "#AXISLABEL (#VALY" + "分钟)";
        //}
        #endregion

        #region 今日
        private async void LoadPage1BarChart()
        {
            List<string> types = new() { "低头", "歪脖", "伸脖", "塌腰", "翘二郎腿" };
            DateTime lastTime = await ManageLastTime.ReadLastTime("toDayTime"), now = DateTime.Now.Date;
            List<int> cnt = new() { 0, 0, 0, 0, 0 };
            if (DateJudge.IsInaDay(lastTime, now))
            {
                Types typesCnt = await IO_Operations.IORead<Types>("toDayTypes");
                cnt = new()
                {
                    typesCnt.LowHeadCnt,
                    typesCnt.WryNeckCnt,
                    typesCnt.StretchNeckCnt,
                    typesCnt.HunchCnt,
                    typesCnt.CrossLegCnt,
                };
            }

            Chart abnomalBar = (Chart)tabControl1.TabPages[0].Controls.Find("AbnormalBar1", true)[0];
            abnomalBar.Series[0].Points.DataBindXY(types, cnt);
            abnomalBar.Series[0].IsValueShownAsLabel = true;
            abnomalBar.Series[0].Font = new Font("Arial", 14, FontStyle.Bold);
        }

        private async void LoadPage1PieChart()
        {
            List<string> status = new() { "正确", "异常" };
            DateTime lastTime = await ManageLastTime.ReadLastTime("toDayTime"), now = DateTime.Now.Date;
            List<decimal> val = new() { 0, 0 };
            if (DateJudge.IsInaDay(lastTime, now))
            {
                Status statusCnt = await IO_Operations.IORead<Status>("toDayStatus");
                val = new()
                {
                    statusCnt.NormalTime,
                    statusCnt.AbnormalTime
                };
            }

            Chart nromalRatio = (Chart)tabControl1.TabPages[0].Controls.Find("NormalRatio1", true)[0];
            nromalRatio.Series[0].Points.DataBindXY(status, val);
            nromalRatio.Series[0].IsValueShownAsLabel = true;
            nromalRatio.Series[0].Font = new Font("Arial", 14, FontStyle.Bold);

            nromalRatio.Series[0].Label = "#VALY" + " 分钟";
            nromalRatio.Series[0].LegendText = "#AXISLABEL (#VALY" + "分钟)";
        }
        #endregion

        #region 本周
        private async void LoadPage2BarChart()
        {
            List<string> types = new() { "低头", "歪脖", "伸脖", "塌腰", "翘二郎腿" };
            DateTime lastTime = await ManageLastTime.ReadLastTime("weekTime"), now = DateTime.Now.Date;
            List<int> cnt = new() { 0, 0, 0, 0, 0 };
            if (DateJudge.IsInaWeek(lastTime, now))
            {
                Types typesCnt = await IO_Operations.IORead<Types>("weekTypes");
                cnt = new()
                {
                    typesCnt.LowHeadCnt,
                    typesCnt.WryNeckCnt,
                    typesCnt.StretchNeckCnt,
                    typesCnt.HunchCnt,
                    typesCnt.CrossLegCnt,
                };
            }

            Chart abnomalBar = (Chart)tabControl1.TabPages[1].Controls.Find("AbnormalBar2", true)[0];
            abnomalBar.Series[0].Points.DataBindXY(types, cnt);
            abnomalBar.Series[0].IsValueShownAsLabel = true;
            abnomalBar.Series[0].Font = new Font("Arial", 14, FontStyle.Bold);
        }

        private async void LoadPage2PieChart()
        {
            List<string> status = new() { "正确", "异常" };
            DateTime lastTime = await ManageLastTime.ReadLastTime("weekTime"), now = DateTime.Now.Date;
            List<decimal> val = new() { 0, 0 };
            if (DateJudge.IsInaWeek(lastTime, now))
            {
                Status statusCnt = await IO_Operations.IORead<Status>("weekStatus");
                val = new()
                {
                    statusCnt.NormalTime,
                    statusCnt.AbnormalTime
                };
            }

            Chart nromalRatio = (Chart)tabControl1.TabPages[1].Controls.Find("NormalRatio2", true)[0];
            nromalRatio.Series[0].Points.DataBindXY(status, val);
            nromalRatio.Series[0].IsValueShownAsLabel = true;
            nromalRatio.Series[0].Font = new Font("Arial", 14, FontStyle.Bold);

            nromalRatio.Series[0].Label = "#VALY" + " 分钟";
            nromalRatio.Series[0].LegendText = "#AXISLABEL (#VALY" + "分钟)";
        }
        #endregion

        #region 本月
        private async void LoadPage3BarChart()
        {
            List<string> types = new() { "低头", "歪脖", "伸脖", "塌腰", "翘二郎腿" };
            DateTime lastTime = await ManageLastTime.ReadLastTime("monthTime"), now = DateTime.Now.Date;
            List<int> cnt = new() { 0, 0, 0, 0, 0 };
            if (DateJudge.IsInaMonth(lastTime, now))
            {
                Types typesCnt = await IO_Operations.IORead<Types>("monthTypes");
                cnt = new()
                {
                    typesCnt.LowHeadCnt,
                    typesCnt.WryNeckCnt,
                    typesCnt.StretchNeckCnt,
                    typesCnt.HunchCnt,
                    typesCnt.CrossLegCnt,
                };
            }

            Chart abnomalBar = (Chart)tabControl1.TabPages[2].Controls.Find("AbnormalBar3", true)[0];
            abnomalBar.Series[0].Points.DataBindXY(types, cnt);
            abnomalBar.Series[0].IsValueShownAsLabel = true;
            abnomalBar.Series[0].Font = new Font("Arial", 14, FontStyle.Bold);
        }

        private async void LoadPage3PieChart()
        {
            List<string> status = new() { "正确", "异常" };
            DateTime lastTime = await ManageLastTime.ReadLastTime("monthTime"), now = DateTime.Now.Date;
            List<decimal> val = new() { 0, 0 };
            if (DateJudge.IsInaMonth(lastTime, now))
            {
                Status statusCnt = await IO_Operations.IORead<Status>("monthStatus");
                val = new()
                {
                    statusCnt.NormalTime,
                    statusCnt.AbnormalTime
                };
            }

            Chart nromalRatio = (Chart)tabControl1.TabPages[2].Controls.Find("NormalRatio3", true)[0];
            nromalRatio.Series[0].Points.DataBindXY(status, val);
            nromalRatio.Series[0].IsValueShownAsLabel = true;
            nromalRatio.Series[0].Font = new Font("Arial", 14, FontStyle.Bold);

            nromalRatio.Series[0].Label = "#VALY" + " 分钟";
            nromalRatio.Series[0].LegendText = "#AXISLABEL (#VALY" + "分钟)";
        }
        #endregion

        #region 全部
        private async void LoadPage4BarChart()
        {
            List<string> types = new() { "低头", "歪脖", "伸脖", "塌腰", "翘二郎腿" };
            DateTime lastTime = await ManageLastTime.ReadLastTime("allTime");
            List<int> cnt = new() { 0, 0, 0, 0, 0 };
            if (lastTime != new DateTime(1999, 1, 1))
            {
                Types typesCnt = await IO_Operations.IORead<Types>("allTypes");
                cnt = new()
                {
                    typesCnt.LowHeadCnt,
                    typesCnt.WryNeckCnt,
                    typesCnt.StretchNeckCnt,
                    typesCnt.HunchCnt,
                    typesCnt.CrossLegCnt,
                };
            }

            Chart abnomalBar = (Chart)tabControl1.TabPages[3].Controls.Find("AbnormalBar4", true)[0];
            abnomalBar.Series[0].Points.DataBindXY(types, cnt);
            abnomalBar.Series[0].IsValueShownAsLabel = true;
            abnomalBar.Series[0].Font = new Font("Arial", 14, FontStyle.Bold);
        }

        private async void LoadPage4PieChart()
        {
            List<string> status = new() { "正确", "异常" };
            DateTime lastTime = await ManageLastTime.ReadLastTime("allTime");
            List<decimal> val = new() { 0, 0 };
            if (lastTime != new DateTime(1999, 1, 1))
            {
                Status statusCnt = await IO_Operations.IORead<Status>("allStatus");
                val = new()
                {
                    statusCnt.NormalTime,
                    statusCnt.AbnormalTime
                };
            }

            Chart nromalRatio = (Chart)tabControl1.TabPages[3].Controls.Find("NormalRatio4", true)[0];
            nromalRatio.Series[0].Points.DataBindXY(status, val);
            nromalRatio.Series[0].IsValueShownAsLabel = true;
            nromalRatio.Series[0].Font = new Font("Arial", 14, FontStyle.Bold);

            nromalRatio.Series[0].Label = "#VALY" + " 分钟";
            nromalRatio.Series[0].LegendText = "#AXISLABEL (#VALY" + "分钟)";
        }
        #endregion
    }
}
