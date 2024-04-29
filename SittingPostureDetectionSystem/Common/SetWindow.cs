using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace SittingPostureDetectionSystem.Common
{
    public static class SetWindow
    {
        private static IntPtr intPtr;         //第三方应用窗口的句柄
        private static Process p;
        public static int Status;

        static string workDirect = AppDomain.CurrentDomain.BaseDirectory;

        /// <summary>
        /// 调整第三方应用窗体大小
        /// </summary>
        public static void ResizeWindow()
        {
            _ = ShowWindow(intPtr, 0);  //先将窗口隐藏
            _ = ShowWindow(intPtr, 3);  //再将窗口最大化，可以让第三方窗口自适应容器的大小
        }

        public static void MaxWindow()
        {
            _ = ShowWindow(intPtr, 3);
        }

        /// <summary>
        /// 循环查找第三方窗体
        /// </summary>
        /// <returns></returns>
        public async static Task<bool> FindWindow(string formName)
        {
            return await Task.Run(() =>
            {
                for (int i = 0; i < 10000; i++)
                {
                    //按照窗口标题查找Python窗口
                    IntPtr vHandle = FindWindow(null, formName);
                    if (vHandle == IntPtr.Zero)
                    {
                        Thread.Sleep(100);  //每100ms查找一次，直到找到，最多查找10s
                        continue;
                    }
                    else      //找到返回True
                    {
                        intPtr = vHandle;
                        return true;
                    }
                }
                intPtr = IntPtr.Zero;
                return false;
            });
        }

        /// <summary>
        /// 将第三方窗体嵌入到容器内
        /// </summary>
        /// <param name="hWndNewParent">父容器句柄</param>
        /// <param name="windowName">窗体名</param>
        public static void SetParent(IntPtr hWndNewParent)
        {
            _ = ShowWindow(intPtr, 0);                 //先将窗体隐藏，防止出现闪烁
            SetParent(intPtr, hWndNewParent);      //将第三方窗体嵌入父容器                    
            Thread.Sleep(100);                      //略加延时
            _ = ShowWindow(intPtr, 3);                 //让第三方窗体在容器中最大化显示
            RemoveWindowTitle(intPtr);              // 去除窗体标题
        }

        /// <summary>
        /// 去除窗体标题
        /// </summary>
        /// <param name="vHandle">窗口句柄</param>
        public static void RemoveWindowTitle(IntPtr vHandle)
        {
            long style = GetWindowLong(vHandle, -16);
            style &= ~0x00C00000;
            SetWindowLong(vHandle, -16, style);
        }

        /// <summary>
        /// 运行第三方窗体
        /// </summary>
        /// <param name="scriptPath">调试命令</param>
        public static void EmbedExternalWindow()
        {
            // 确保 UI 线程不会被阻塞
            Task.Run(() =>
            {
                p = new();
                p.StartInfo.FileName = "C:\\Users\\14020\\.conda\\envs\\PyTorch2\\python.exe";
                p.StartInfo.Arguments = workDirect + "Sittingpose\\videoPredicSitPose.py";
                //p.StartInfo.Arguments = @"D:\ProgramDemos\VisualStudioDemos\C#\SittingPostureDetectionSystem\Sittingpose\videoPredicSitPose.py";
                //p.StartInfo.Arguments = @"D:\ProgramDemos\VisualStudioDemos\C#\SittingPostureDetectionSystem\SittingPostureDetectionSystem\bin\Debug\net6.0-windows\Python\main.py";
                p.StartInfo.WorkingDirectory = workDirect + "Sittingpose";
                p.StartInfo.UseShellExecute = false;
                p.StartInfo.RedirectStandardOutput = true;
                //p.StartInfo.RedirectStandardInput = true;
                //p.StartInfo.RedirectStandardError = true;
                p.StartInfo.CreateNoWindow = true;
                //p.StartInfo.EnvironmentVariables["PYTHONPATH"] = "C:\\Python311\\Lib";
                // 设置输出流编码
                //p.StartInfo.StandardOutputEncoding = Encoding.UTF8;
                p.Start();
                p.BeginOutputReadLine();//在应用程序的重定向 StandardOutput 流上开始进行异步读取操作。
                p.OutputDataReceived += new DataReceivedEventHandler(p_OutputDataReceived);
                p.WaitForExit();
            });
        }
        private async static void p_OutputDataReceived(object sender, DataReceivedEventArgs e)//这里将方法给出了，然后也就在这里执行
        {
            await Task.Run(() =>
            {
                if (!string.IsNullOrEmpty(e.Data))//如果字符串存在
                {
                    string result = e.Data + Environment.NewLine;
                    Status = int.Parse(result);
                    Debug.WriteLine(Status);
                }
            });
        }

        /// <summary>
        /// 关闭窗体时发生的事件
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        public static void Form_FormClosing(object? sender = default, FormClosingEventArgs? e = default)
        {
            try
            {
                if (p != null && !p.HasExited)
                {
                    p.Kill();
                    p.Dispose();
                }
            }
            catch (Exception) { }
        }


        #region API 需要using System.Runtime.InteropServices;

        [DllImport("user32.dll ", EntryPoint = "SetParent")]
        private static extern IntPtr SetParent(IntPtr hWndChild, IntPtr hWndNewParent);   //将外部窗体嵌入程序

        [DllImport("user32.dll")]
        private static extern IntPtr FindWindow(string? lpszClass, string lpszWindow);      //按照窗体类名或窗体标题查找窗体

        [DllImport("user32.dll", EntryPoint = "ShowWindow", CharSet = CharSet.Auto)]
        private static extern int ShowWindow(IntPtr hwnd, int nCmdShow);                  //设置窗体属性

        [DllImport("user32.dll", EntryPoint = "SetWindowLong", CharSet = CharSet.Auto)]
        public static extern IntPtr SetWindowLong(IntPtr hWnd, int nIndex, long dwNewLong);

        [DllImport("user32.dll", EntryPoint = "GetWindowLong", CharSet = CharSet.Auto)]
        public static extern long GetWindowLong(IntPtr hWnd, int nIndex);

        #endregion
    }
}
