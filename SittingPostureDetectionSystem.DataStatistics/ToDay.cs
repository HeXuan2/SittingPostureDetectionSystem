using Newtonsoft.Json;
using SittingPostureDetectionSystem.DataStatistics.Common;
using SittingPostureDetectionSystem.DataStatistics.Models;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Data;
using System.IO;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using static System.Formats.Asn1.AsnWriter;

namespace SittingPostureDetectionSystem.DataStatistics
{
    public static class ToDay
    {
        //static readonly string direct = AppDomain.CurrentDomain.BaseDirectory;

        public static async void Update(Types types, Status status)
        {
            DateTime lastTime = await ManageLastTime.ReadLastTime("toDayTime"), now = DateTime.Now.Date;
            if (DateJudge.IsInaDay(lastTime, now))
            {
                Types lastTypes = await IO_Operations.IORead<Types>("toDayTypes");
                types.LowHeadCnt += lastTypes.LowHeadCnt;
                types.WryNeckCnt += lastTypes.WryNeckCnt;
                types.StretchNeckCnt += lastTypes.StretchNeckCnt;
                types.HunchCnt += lastTypes.HunchCnt;
                types.CrossLegCnt += lastTypes.CrossLegCnt;

                Status lastStatus = await IO_Operations.IORead<Status>("toDayStatus");
                status.NormalTime += lastStatus.NormalTime;
                status.AbnormalTime += lastStatus.AbnormalTime;
            }

            await IO_Operations.IOWrite("toDayTypes", types);
            await IO_Operations.IOWrite("toDayStatus", status);

            await ManageLastTime.UpdateLastTime("toDayTime");
        }

        //private static bool IsInaDay(DateTime lastTime, DateTime now)
        //{
        //    if (lastTime != new DateTime(1999,1,1) && (lastTime.Year != now.Year || lastTime.Month != now.Month || lastTime.Day != now.Day))
        //        return false;
        //    return true;
        //}

        #region 已迁移到 Common 中
        //private static async Task IOWrite<T>(string routeOrFileName, T obj)
        //{
        //    await Task.Run(() =>
        //    {
        //        string route = direct + routeOrFileName;
        //        string file = route + "\\" + routeOrFileName + ".txt";

        //        if (!Directory.Exists(route)) Directory.CreateDirectory(route);
        //        if (!File.Exists(file)) File.Create(file).Dispose();

        //        FileStream fs = new(file, FileMode.Truncate, FileAccess.ReadWrite);
        //        //获得字节数组
        //        string info = System.Text.Json.JsonSerializer.Serialize(obj);
        //        byte[] data = Encoding.UTF8.GetBytes(info);
        //        //开始写入
        //        fs.Write(data, 0, data.Length); // 互斥访问
        //                                        //清空缓冲区、关闭流
        //        fs.Flush();
        //        fs.Close();
        //    });
        //}

        //public void IOWrite<T1, T2>(string routeOrFileName, List<T1> l1, List<T2> l2)
        //{

        //    //if (!Directory.Exists(route)) Directory.CreateDirectory(route);

        //    //if (!File.Exists(file)) File.Create(file).Dispose();

        //    //FileStream fs = new(file, FileMode.Truncate, FileAccess.ReadWrite);
        //    ////获得字节数组
        //    //var r1 = types.Zip(cnts, (type, cnt) => new { Type = type, Cnt = cnt });
        //    //string info = JsonConvert.SerializeObject(r1);
        //    //byte[] data = Encoding.UTF8.GetBytes(info);
        //    ////开始写入
        //    //fs.Write(data, 0, data.Length); // 互斥访问
        //    //fs.Write(data, 0, data.Length); // 互斥访问
        //    ////清空缓冲区、关闭流
        //    //fs.Flush();
        //    //fs.Close();

        //    //file = route + "/todayVal.txt";
        //    //if (!File.Exists(file)) File.Create(file).Dispose();
        //    //fs = new(file, FileMode.Truncate, FileAccess.ReadWrite);
        //    //var r2 = toDayStatus.Zip(toDayValues, (toDayStatu, toDayVal) => new { ToDayStatu = toDayStatu, ToDayVal = toDayVal });
        //    //info = JsonConvert.SerializeObject(r2);
        //    //data = Encoding.UTF8.GetBytes(info);
        //    ////开始写入
        //    //fs.Write(data, 0, data.Length); // 互斥访问
        //    ////清空缓冲区、关闭流
        //    //fs.Flush();
        //    //fs.Close();
        //}

        //public static async Task<T> IORead<T>(string routeOrFileName) where T : new()
        //{
        //    await Task.Run(() =>
        //    {
        //        string route = direct + routeOrFileName;
        //        string file = route + "\\" + routeOrFileName + ".txt";

        //        if (!Directory.Exists(route) || !File.Exists(file)) return new T();

        //        byte[] buffer = File.ReadAllBytes(file);
        //        // 使用下边方法把二进制字节数组转为字符串，我们才能看到真正的内容
        //        // 下边Encoding后边是一个编码格式，默认使用UTF8即可
        //        string info = Encoding.UTF8.GetString(buffer);
        //        T json = System.Text.Json.JsonSerializer.Deserialize<T>(info);
        //        return json;
        //    });
        //    return new T();
        //}
        #endregion

        #region 已废弃
        //public List<int>? IOReadOfCnts()
        //{
        //    if (!Directory.Exists(route) || !File.Exists(file)) return null;

        //    byte[] buffer = File.ReadAllBytes(direct + "/toDay/todayCnts.txt");
        //    // 使用下边方法把二进制字节数组转为字符串，我们才能看到真正的内容
        //    // 下边Encoding后边是一个编码格式，默认使用UTF8即可
        //    string info = Encoding.UTF8.GetString(buffer);
        //    dynamic json = System.Text.Json.JsonSerializer.Deserialize<dynamic>(info);
        //    for (int i = 0; json != null && i < json.Length; i++)
        //    {
        //        cnts[i] = int.Parse(json[i]);
        //    }

        //    return cnts;
        //}

        //public List<double>? IOReadOfTime()
        //{
        //    if (!Directory.Exists(route) || !File.Exists(file)) return null;

        //    byte[] buffer = File.ReadAllBytes(direct + "/toDay/todayVal.txt");
        //    // 使用下边方法把二进制字节数组转为字符串，我们才能看到真正的内容
        //    // 下边Encoding后边是一个编码格式，默认使用UTF8即可
        //    string info = Encoding.UTF8.GetString(buffer);
        //    dynamic json = System.Text.Json.JsonSerializer.Deserialize<dynamic>(info);
        //    for (int i = 0; json != null && i < json.Length; i++)
        //    {
        //        toDayValues[i] = double.Parse(json[i]);
        //    }

        //    return toDayValues;
        //}
        #endregion

        #region 已迁移到 Common.ManageLastTime
        //private async static void UpdateLastTime()
        //{
        //    await Task.Run(() =>
        //    {
        //        string route = direct + "toDay";
        //        string file = route + "\\" + "lastTime" + ".txt";

        //        if (!Directory.Exists(route)) Directory.CreateDirectory(route);
        //        if (!File.Exists(file)) File.Create(file).Dispose();

        //        FileStream fs = new(file, FileMode.Truncate, FileAccess.ReadWrite);
        //        //获得字节数组
        //        string info = DateTime.Now.Date.ToString();
        //        byte[] data = Encoding.UTF8.GetBytes(info);
        //        //开始写入
        //        fs.Write(data, 0, data.Length); // 互斥访问
        //        fs.Write(data, 0, data.Length); // 互斥访问
        //                                        //清空缓冲区、关闭流
        //        fs.Flush();
        //        fs.Close();
        //    });
        //}

        //private async static Task<DateTime> ReadLastTime()
        //{
        //    await Task.Run(() =>
        //    {
        //        string route = direct + "toDay";
        //        string file = route + "\\" + "lastTime" + ".txt";

        //        DateTime date = new(1999, 1, 1);
        //        if (!Directory.Exists(route) || !File.Exists(file)) return date;

        //        byte[] buffer = File.ReadAllBytes(file);
        //        // 使用下边方法把二进制字节数组转为字符串，我们才能看到真正的内容
        //        // 下边Encoding后边是一个编码格式，默认使用UTF8即可
        //        string info = Encoding.UTF8.GetString(buffer);
        //        date = DateTime.Parse(info);

        //        return date;
        //    });
        //    return new(1999, 1, 1);
        //}
        #endregion
    }
}
