using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Text.Json;
using System.Diagnostics;

namespace SittingPostureDetectionSystem.DataStatistics.Common
{
    public class IO_Operations
    {
        static readonly string direct = AppDomain.CurrentDomain.BaseDirectory;
        public static async Task IOWrite<T>(string routeOrFileName, T obj)
        {
            await Task.Run(() =>
            {
                string route = direct + "data\\" + routeOrFileName;
                string file = route + "\\" + routeOrFileName + ".txt";

                if (!Directory.Exists(route)) Directory.CreateDirectory(route);
                if (!File.Exists(file)) File.Create(file).Dispose();

                FileStream fs = new(file, FileMode.Truncate, FileAccess.ReadWrite);
                //获得字节数组
                string info = JsonSerializer.Serialize(obj);
                byte[] data = Encoding.UTF8.GetBytes(info);
                //开始写入
                fs.Write(data, 0, data.Length); // 互斥访问
                //清空缓冲区、关闭流
                fs.Flush();
                fs.Close();
            });
        }

        public static async Task<T> IORead<T>(string routeOrFileName) where T : new()
        {
            T res = new();
            await Task.Run(() =>
            {
                string route = direct + "data\\" + routeOrFileName;
                string file = route + "\\" + routeOrFileName + ".txt";

                if (Directory.Exists(route) && File.Exists(file))
                {
                    byte[] buffer = File.ReadAllBytes(file);
                    // 使用下边方法把二进制字节数组转为字符串，我们才能看到真正的内容
                    // 下边Encoding后边是一个编码格式，默认使用UTF8即可
                    string info = Encoding.UTF8.GetString(buffer);
                    res = JsonSerializer.Deserialize<T>(info);
                }
            });
            return res;
        }
    }
}
