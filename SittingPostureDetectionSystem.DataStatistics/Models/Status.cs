using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SittingPostureDetectionSystem.DataStatistics.Models
{
    public class Status
    {
        public Status()
        {
            
        }
        public Status(Status s)
        {
           
            NormalTime = s.NormalTime;
            AbnormalTime = s.AbnormalTime;
        }
        public decimal NormalTime { get; set; }
        public decimal AbnormalTime { get; set; }
    }
}
