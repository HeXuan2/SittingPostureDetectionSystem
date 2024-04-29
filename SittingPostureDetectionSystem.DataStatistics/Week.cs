using Newtonsoft.Json;
using SittingPostureDetectionSystem.DataStatistics.Common;
using SittingPostureDetectionSystem.DataStatistics.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SittingPostureDetectionSystem.DataStatistics
{
    public static class Week
    {
        //static readonly string direct = AppDomain.CurrentDomain.BaseDirectory;
        public static async void Update(Types types, Status status)
        {
            DateTime lastTime = await ManageLastTime.ReadLastTime("weekTime"), now = DateTime.Now.Date;
            if (DateJudge.IsInaWeek(lastTime, now))
            {
                Types lastTypes = await IO_Operations.IORead<Types>("weekTypes");
                types.LowHeadCnt += lastTypes.LowHeadCnt;
                types.WryNeckCnt += lastTypes.WryNeckCnt;
                types.StretchNeckCnt += lastTypes.StretchNeckCnt;
                types.HunchCnt += lastTypes.HunchCnt;
                types.CrossLegCnt += lastTypes.CrossLegCnt;

                Status lastStatus = await IO_Operations.IORead<Status>("weekStatus");
                status.NormalTime += lastStatus.NormalTime;
                status.AbnormalTime += lastStatus.AbnormalTime;
            }

            await IO_Operations.IOWrite("weekTypes", types);
            await IO_Operations.IOWrite("weekStatus", status);

            await ManageLastTime.UpdateLastTime("weekTime");
        }

        //private static bool IsInaWeek(DateTime lastTime, DateTime now)
        //{
        //    if (lastTime == new DateTime(1999, 1, 1)) lastTime = now;
        //    // 确定一周的起始日期为星期一
        //    DayOfWeek firstDayOfWeek = DayOfWeek.Monday;
        //    // 计算出本周的起始日期
        //    DateTime startOfWeek = now.Date.AddDays(-(int)now.DayOfWeek + (int)firstDayOfWeek);

        //    if (lastTime < startOfWeek || lastTime >= startOfWeek.AddDays(7)) return false;
        //    return true;
        //}

        //private static async Task IOWrite<T1, T2>(string routeOrFileName, List<T1> l1, List<T2> l2)
        //{
        //    await Task.Run(() =>
        //    {
        //        string route = direct + routeOrFileName;
        //        string file = route + "\\" + routeOrFileName + ".txt";

        //        if (!Directory.Exists(route)) Directory.CreateDirectory(route);

        //        if (!File.Exists(file)) File.Create(file).Dispose();

        //        FileStream fs = new(file, FileMode.Truncate, FileAccess.ReadWrite);
        //        //获得字节数组
        //        var res = l1.Zip(l2, (key, value) => new { Key = key, Value = value });
        //        string info = JsonConvert.SerializeObject(res);
        //        byte[] data = Encoding.UTF8.GetBytes(info);
        //        //开始写入
        //        fs.Write(data, 0, data.Length); // 互斥访问
        //                                        //清空缓冲区、关闭流
        //        fs.Flush();
        //        fs.Close();
        //    });
        //}

        //public static async Task<List<T>> IORead<T>(string routeOrFileName)
        //{
        //    int len = routeOrFileName.Contains("Val") ? 2 : 5;
        //    T[] arr = new T[len];
        //    await Task.Run(() =>
        //    {
        //        string route = direct + routeOrFileName;
        //        string file = route + "\\" + routeOrFileName + ".txt";

        //        if (!Directory.Exists(route) || !File.Exists(file)) return arr.ToList();

        //        byte[] buffer = File.ReadAllBytes(file);
        //        // 使用下边方法把二进制字节数组转为字符串，我们才能看到真正的内容
        //        // 下边Encoding后边是一个编码格式，默认使用UTF8即可
        //        string info = Encoding.UTF8.GetString(buffer);
        //        dynamic? json = System.Text.Json.JsonSerializer.Deserialize<dynamic>(info);
        //        for (int i = 0; json != null && i < json.Length; i++)
        //        {
        //            arr[i] = (T)json[i];
        //        }
        //        return arr.ToList();
        //    });
        //    return arr.ToList();
        //}
    }
}
