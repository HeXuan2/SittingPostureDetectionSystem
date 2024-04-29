using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SittingPostureDetectionSystem.DataStatistics.Models
{
    public class Types
    {
        public Types()
        {
            
        }
        public Types(Types t)
        {
           
            LowHeadCnt = t.LowHeadCnt;
            WryNeckCnt = t.WryNeckCnt;
            StretchNeckCnt = t.StretchNeckCnt;
            HunchCnt = t.HunchCnt;
            CrossLegCnt = t.CrossLegCnt;
        }
        public int LowHeadCnt { get; set; }
        public int WryNeckCnt { get; set; }
        public int StretchNeckCnt { get; set; }
        public int HunchCnt { get; set; }
        public int CrossLegCnt { get; set; }
    }
}
