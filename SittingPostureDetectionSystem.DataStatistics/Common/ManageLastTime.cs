using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SittingPostureDetectionSystem.DataStatistics.Common
{
    public class ManageLastTime
    {
        static readonly string direct = AppDomain.CurrentDomain.BaseDirectory;
        public async static Task UpdateLastTime(string routeOrFileName)
        {
            await Task.Run(() =>
            {
                string route = direct + "data\\" + routeOrFileName;
                string file = route + "\\" + routeOrFileName + ".txt";

                if (!Directory.Exists(route)) Directory.CreateDirectory(route);
                if (!File.Exists(file)) File.Create(file).Dispose();

                FileStream fs = new(file, FileMode.Truncate, FileAccess.ReadWrite);
                //获得字节数组
                string info = DateTime.Now.Date.ToString();
                byte[] data = Encoding.UTF8.GetBytes(info);
                //开始写入
                fs.Write(data, 0, data.Length); // 互斥访问
                //清空缓冲区、关闭流
                fs.Flush();
                fs.Close(); 
            });
        }

        public async static Task<DateTime> ReadLastTime(string routeOrFileName)
        {
            DateTime date = DateTime.Now;
            await Task.Run(() =>
            {
                string route = direct + "data\\" + routeOrFileName;
                string file = route + "\\" + routeOrFileName + ".txt";

                //DateTime date = DateTime.Now;
                if (Directory.Exists(route) && File.Exists(file))
                {

                    byte[] buffer = File.ReadAllBytes(file);
                    // 使用下边方法把二进制字节数组转为字符串，我们才能看到真正的内容
                    // 下边Encoding后边是一个编码格式，默认使用UTF8即可
                    string info = Encoding.UTF8.GetString(buffer);
                    date = DateTime.Parse(info);
                }
            });
            return date;
        }
    }
}
