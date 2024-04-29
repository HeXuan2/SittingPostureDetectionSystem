using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SittingPostureDetectionSystem.DataStatistics.Common
{
    public class DateJudge
    {
        public static bool IsInaDay(DateTime lastTime, DateTime now)
        {
            if (lastTime != new DateTime(1999, 1, 1) && (lastTime.Year != now.Year || lastTime.Month != now.Month || lastTime.Day != now.Day))
                return false;
            return true;
        }
        public static bool IsInaWeek(DateTime lastTime, DateTime now)
        {
            if (lastTime == new DateTime(1999, 1, 1)) lastTime = now;
            // 确定一周的起始日期为星期一
            DayOfWeek firstDayOfWeek = DayOfWeek.Sunday;
            // 计算出本周的起始日期
            DateTime startOfWeek = now.Date.AddDays(-(int)now.DayOfWeek + (int)firstDayOfWeek);

            if (lastTime < startOfWeek || lastTime >= startOfWeek.AddDays(7)) return false;
            return true;
        }
        public static bool IsInaMonth(DateTime lastTime, DateTime now)
        {
            if (lastTime != new DateTime(1999, 1, 1) && (lastTime.Year != now.Year || lastTime.Month != now.Month))
                return false;
            return true;
        }

    }
}
