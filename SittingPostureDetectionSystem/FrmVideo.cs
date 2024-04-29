using SittingPostureDetectionSystem.Common;
using SittingPostureDetectionSystem.DataStatistics;
using SittingPostureDetectionSystem.DataStatistics.Models;
using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Linq;
using System.Management;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SittingPostureDetectionSystem
{
    public partial class FrmVideo : Form
    {
        List<string> allCameras;

        public FrmVideo()
        {
            InitializeComponent();
            allCameras = new List<string>();
            cbxCameras.DataSource = GetAllCameras();
            cbxCameras.DisplayMember = "Name";
            CheckForIllegalCrossThreadCalls = false;
            frmSettings = (FrmSettings)FormFactory.CreateForm("FrmSettings");

            // 禁止用户调整 SplitContainer 的面板大小
            splitContainer1.IsSplitterFixed = true;
        }

        private async void btnStart_Click(object sender, EventArgs e)
        {
            btnStart.Enabled = false;
            btnStop.Enabled = false;
            if (allCameras.Count == 0) MessageBox.Show("未检测到可用摄像头，请检查连接情况！");
            else
            {
                SetWindow.EmbedExternalWindow();
                bool findRes = await SetWindow.FindWindow("frame");
                if (findRes == true)
                {
                    ColorRestore();
                    CntRestore();
                    totRuntime = 0;
                    nalRuntime = 0;
                    SetWindow.SetParent(splitContainer1.Panel1.Handle);
                    totalRuntime.Start();
                    normalRuntime.Start();
                    //await ChangeStatus();

                    _cancellationTokenSource = new CancellationTokenSource();
                    // 使用Task.Run开启一个新的线程来执行状态检查和UI更新的任务。
                    var tasks = new[] {
                        Task.Run(() => RunStatusCheckAsync(_cancellationTokenSource.Token)),
                        Task.Run(() => UpdateUIAsync(_cancellationTokenSource.Token))
                    };
                }
            }
            btnStop.Enabled = true;
        }

        public void SetParent()
        {
            SetWindow.SetParent(splitContainer1.Panel1.Handle);
        }

        private void btnStop_Click(object sender, EventArgs e)
        {
            btnStop.Enabled = false;

            totalRuntime.Stop();
            normalRuntime.Stop();
            StopChangeStatus();
            // 统计数据
            Types types = StatisticsOfCnt();
            Status status = StatisticsOfTime();
            ToDay.Update(new(types), new(status));
            Week.Update(new(types), new(status));
            Month.Update(new(types), new(status));
            All.Update(new(types), new(status));

            ColorRestore();
            this.status = -2;
            SetWindow.Form_FormClosing();

            btnStart.Enabled = true;
            btnStop.Enabled = true;
        }

        private void FrmVedio_SizeChanged(object sender, EventArgs e)
        {
            SetWindow.MaxWindow();
        }

        int totRuntime, nalRuntime;
        private void totalRuntime_Tick(object sender, EventArgs e)
        {
            totRuntime++;
            int hours = totRuntime / 3600;
            int minutes = (totRuntime % 3600) / 60;
            int seconds = totRuntime % 60;

            labShowTotalTime.Text = string.Format("{0:D2}:{1:D2}:{2:D2}", hours, minutes, seconds);
        }
        private void normalRuntime_Tick(object sender, EventArgs e)
        {
            if (status == 0)
            {
                nalRuntime++;
                int hours = nalRuntime / 3600;
                int minutes = (nalRuntime % 3600) / 60;
                int seconds = nalRuntime % 60;

                labNormalTime.Text = string.Format("{0:D2}:{1:D2}:{2:D2}", hours, minutes, seconds);
            }
        }

        private List<string> GetAllCameras()
        {
            var searcher = new ManagementObjectSearcher("SELECT * FROM Win32_PnPEntity WHERE (PNPClass = 'Image' OR PNPClass = 'Camera')");

            foreach (var device in searcher.Get())
            {
                //var deviceId = device["DeviceID"].ToString();
                //var index = deviceId.LastIndexOf('\\');
                string name = device["Name"].ToString();
                allCameras.Add(name);
            }

            return allCameras;
        }

        int status = -2;
        private CancellationTokenSource _cancellationTokenSource;
        private BlockingCollection<int> _statusBuffer = new BlockingCollection<int>();
        private async Task RunStatusCheckAsync(CancellationToken cancellationToken)
        {
            while (!cancellationToken.IsCancellationRequested)
            {
                int nextStatus = SetWindow.Status; // 读取Python进程的输出流

                if (status != nextStatus)
                {
                    status = nextStatus;

                    // 将状态添加到缓冲区
                    _statusBuffer.Add(status);
                }

                // 等待一段时间再进行下一次循环，以避免占用过多CPU资源。
                await Task.Delay(100, cancellationToken);
            }
        }

        int idxLowHead = 0, idxWryNeck = 0, idxStretchNeck = 0, idxHunch = 0, idxCrossLeg = 0;
        FrmSettings frmSettings;
        private async Task UpdateUIAsync(CancellationToken cancellationToken)
        {
            while (!cancellationToken.IsCancellationRequested)
            {
                try
                {
                    int status = _statusBuffer.Take(cancellationToken); // 获取缓冲区中的最新状态

                    this.Invoke((MethodInvoker)async delegate
                    {
                        if (!cancellationToken.IsCancellationRequested)
                        {
                            if (status == -1)
                            {
                                ColorRestore();
                                labNoneObject.ForeColor = Color.Red;
                                labShowTotalTime.ForeColor = Color.Red;
                                totalRuntime.Stop();
                                normalRuntime.Stop();
                            }
                            else if (status == 0)
                            {
                                ColorRestore();
                                labNormal.ForeColor = Color.DarkGreen;
                                totalRuntime.Start();
                                normalRuntime.Start();
                            }
                            else if (status == 1)
                            {
                                idxLowHead++;
                                int g = frmSettings.gaps.gapLowHead;
                                if (idxLowHead == g)
                                {
                                    await VoiceAlerts.Alert("低头次数过多，请及时调整");
                                    idxLowHead = 0;
                                }
                                var v = labLowHeadCnt.Text[..(labLowHeadCnt.Text.Length - 1)];
                                labLowHeadCnt.Text = (int.Parse(labLowHeadCnt.Text[..(labLowHeadCnt.Text.Length - 1)]) + 1).ToString() + " 次";
                                ColorRestore();
                                labLowHead.ForeColor = Color.Red;
                                totalRuntime.Start();
                                normalRuntime.Stop();
                                //Thread.Sleep(500);
                            }
                            else if (status == 2)
                            {
                                idxWryNeck++;
                                int g = frmSettings.gaps.gapWryNeck;
                                if (idxWryNeck == g)
                                {
                                    await VoiceAlerts.Alert("歪脖次数过多，请摆正姿态");
                                    idxWryNeck = 0;
                                }
                                labWryNeckCnt.Text = (int.Parse(labWryNeckCnt.Text[..(labWryNeckCnt.Text.Length - 1)]) + 1).ToString() + " 次";
                                ColorRestore();
                                labWryNect.ForeColor = Color.Red;
                                totalRuntime.Start();
                                normalRuntime.Stop();
                                //Thread.Sleep(500);
                            }
                            else if (status == 3)
                            {
                                idxStretchNeck++;
                                int g = frmSettings.gaps.gapStreatNeck;
                                if (idxStretchNeck == g)
                                {
                                    await VoiceAlerts.Alert("伸脖次数过多，请摆正姿态");
                                    idxStretchNeck = 0;
                                }
                                labStretchNeckCnt.Text = (int.Parse(labStretchNeckCnt.Text[..(labStretchNeckCnt.Text.Length - 1)]) + 1).ToString() + " 次";
                                ColorRestore();
                                labStreatNeck.ForeColor = Color.Red;
                                totalRuntime.Start();
                                normalRuntime.Stop();
                                //Thread.Sleep(500);
                            }
                            else if (status == 4)
                            {
                                idxHunch++;
                                int g = frmSettings.gaps.gapHunch;
                                if (idxHunch == g)
                                {
                                    await VoiceAlerts.Alert("塌腰次数过多，请及时调整");
                                    idxHunch = 0;
                                }
                                labHunchCnt.Text = (int.Parse(labHunchCnt.Text[..(labHunchCnt.Text.Length - 1)]) + 1).ToString() + " 次";
                                ColorRestore();
                                labHunch.ForeColor = Color.Red;
                                totalRuntime.Start();
                                normalRuntime.Stop();
                                //Thread.Sleep(500);
                            }
                            else if (status == 5)
                            {
                                idxCrossLeg++;
                                int g = frmSettings.gaps.gapCrossLeg;
                                if (idxCrossLeg == g)
                                {
                                    await VoiceAlerts.Alert("翘腿次数过多，请及时调整");
                                    idxCrossLeg = 0;
                                }
                                labCrossLegCnt.Text = (int.Parse(labCrossLegCnt.Text[..(labCrossLegCnt.Text.Length - 1)]) + 1).ToString() + " 次";
                                ColorRestore();
                                labCrossLeg.ForeColor = Color.Red;
                                totalRuntime.Start();
                                normalRuntime.Stop();
                                //Thread.Sleep(500);
                            }
                        }
                    });
                }
                catch (Exception) { }
                // 等待一段时间再进行下一次循环，以避免占用过多CPU资源。
                await Task.Delay(500, cancellationToken);
            }
        }

        //private CancellationTokenSource _cancellationTokenSource;
        //private Task ChangeStatus()
        //{
        //    _cancellationTokenSource = new CancellationTokenSource();
        //    return Task.Run(() =>
        //    {
        //        while (!_cancellationTokenSource.Token.IsCancellationRequested)
        //        {
        //            this.Invoke((MethodInvoker)delegate
        //            {
        //                try
        //                {
        //                    int nextStatus = SetWindow.Status; // 读取Python进程的输出流

        //                    if (status != nextStatus && !_cancellationTokenSource.Token.IsCancellationRequested)
        //                    {
        //                        status = nextStatus;

        //                        if (status == -1)
        //                        {
        //                            ColorRestore();
        //                            labNoneObject.ForeColor = Color.Red;
        //                            labShowTotalTime.ForeColor = Color.Red;
        //                            totalRuntime.Stop();
        //                            normalRuntime.Stop();
        //                        }
        //                        else if (status == 0)
        //                        {
        //                            ColorRestore();
        //                            labNormal.ForeColor = Color.DarkGreen;
        //                            totalRuntime.Start();
        //                            normalRuntime.Start();
        //                        }
        //                        else if (status == 1)
        //                        {
        //                            var v = labLowHeadCnt.Text[..(labLowHeadCnt.Text.Length - 1)];
        //                            labLowHeadCnt.Text = (int.Parse(labLowHeadCnt.Text[..(labLowHeadCnt.Text.Length - 1)]) + 1).ToString() + " 次";
        //                            ColorRestore();
        //                            labLowHead.ForeColor = Color.Red;
        //                            totalRuntime.Start();
        //                            normalRuntime.Stop();
        //                            Thread.Sleep(500);
        //                        }
        //                        else if (status == 2)
        //                        {
        //                            labWryNeckCnt.Text = (int.Parse(labWryNeckCnt.Text[..(labWryNeckCnt.Text.Length - 1)]) + 1).ToString() + " 次";
        //                            ColorRestore();
        //                            labWryNect.ForeColor = Color.Red;
        //                            totalRuntime.Start();
        //                            normalRuntime.Stop();
        //                            Thread.Sleep(500);
        //                        }
        //                        else if (status == 3)
        //                        {
        //                            labStretchNeckCnt.Text = (int.Parse(labStretchNeckCnt.Text[..(labStretchNeckCnt.Text.Length - 1)]) + 1).ToString() + " 次";
        //                            ColorRestore();
        //                            labStreatNeck.ForeColor = Color.Red;
        //                            totalRuntime.Start();
        //                            normalRuntime.Stop();
        //                            Thread.Sleep(500);
        //                        }
        //                        else if (status == 4)
        //                        {
        //                            labHunchCnt.Text = (int.Parse(labHunchCnt.Text[..(labHunchCnt.Text.Length - 1)]) + 1).ToString() + " 次";
        //                            ColorRestore();
        //                            labHunch.ForeColor = Color.Red;
        //                            totalRuntime.Start();
        //                            normalRuntime.Stop();
        //                            Thread.Sleep(500);
        //                        }
        //                        else if (status == 5)
        //                        {
        //                            labCrossLegCnt.Text = (int.Parse(labCrossLegCnt.Text[..(labCrossLegCnt.Text.Length - 1)]) + 1).ToString() + " 次";
        //                            ColorRestore();
        //                            labCrossLeg.ForeColor = Color.Red;
        //                            totalRuntime.Start();
        //                            normalRuntime.Stop();
        //                            Thread.Sleep(500);
        //                        }
        //                    }
        //                }
        //                catch (Exception) { }
        //            });
        //        }
        //    });
        //}
        private void StopChangeStatus()
        {
            _cancellationTokenSource?.Cancel();
        }

        private void ColorRestore()
        {
            labShowTotalTime.ForeColor = Color.Black;

            labNoneObject.ForeColor = Color.DarkGray;

            labNormal.ForeColor = Color.DarkGray;
            labLowHead.ForeColor = Color.DarkGray;
            labWryNect.ForeColor = Color.DarkGray;
            labStreatNeck.ForeColor = Color.DarkGray;
            labHunch.ForeColor = Color.DarkGray;
            labCrossLeg.ForeColor = Color.DarkGray;
        }

        static readonly Font font = new("微软雅黑", 10.5f, FontStyle.Regular);
        private void CntRestore()
        {
            labShowTotalTime.Text = "00:00:00";

            labNormalTime.Text = "00:00:00";

            labLowHeadCnt.Text = "0 次";
            labLowHeadCnt.Font = font;

            labWryNeckCnt.Text = "0 次";
            labWryNeckCnt.Font = font;

            labStretchNeckCnt.Text = "0 次";
            labStretchNeckCnt.Font = font;

            labHunchCnt.Text = "0 次";
            labHunchCnt.Font = font;

            labCrossLegCnt.Text = "0 次";
            labCrossLegCnt.Font = font;
        }

        private Types StatisticsOfCnt()
        {
            Types types = new()
            {
                LowHeadCnt = int.Parse(labLowHeadCnt.Text[..(labLowHeadCnt.Text.Length - 1)]),
                WryNeckCnt = int.Parse(labWryNeckCnt.Text[..(labWryNeckCnt.Text.Length - 1)]),
                StretchNeckCnt = int.Parse(labStretchNeckCnt.Text[..(labStretchNeckCnt.Text.Length - 1)]),
                HunchCnt = int.Parse(labHunchCnt.Text[..(labHunchCnt.Text.Length - 1)]),
                CrossLegCnt = int.Parse(labCrossLegCnt.Text[..(labCrossLegCnt.Text.Length - 1)]),
            };
            return types;
        }

        private Status StatisticsOfTime()
        {
            double normalTime = TimeSpan.Parse(labNormalTime.Text).TotalMinutes;
            string nt = normalTime.ToString("0.00");

            double abNormalTime = TimeSpan.Parse(labShowTotalTime.Text).TotalMinutes - TimeSpan.Parse(labNormalTime.Text).TotalMinutes;
            string ant = abNormalTime.ToString("0.00");

            Status status = new()
            {
                NormalTime = decimal.Parse(nt),
                AbnormalTime = decimal.Parse(ant),
            };
            return status;
        }

        private void splitContainer1_Panel1_SizeChanged(object sender, EventArgs e)
        {
            SetWindow.ResizeWindow();
        }

        private void labCrossLegCnt_Click(object sender, EventArgs e)
        {

        }

        private void FrmVideo_Resize(object sender, EventArgs e)
        {
            panel1.Size = this.Size;
            splitContainer1.Width = this.Width;
            splitContainer1.Height = this.Height - 70;
            splitContainer1.SplitterDistance = this.Width - 400;
        }
    }
}