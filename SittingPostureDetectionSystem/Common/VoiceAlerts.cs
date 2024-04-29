using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Speech.Synthesis;

namespace SittingPostureDetectionSystem.Common
{
    public class VoiceAlerts
    {
        private static SpeechSynthesizer synth = new();
        public VoiceAlerts()
        {
            synth.SetOutputToDefaultAudioDevice(); // 设置语音输出设备为默认音频设备
        }
        public async static Task Alert(string msg)
        {
            await Task.Run(() => { synth.Speak(msg); });
            // 朗读文本内容
        }
        public static void Setting(int volume, int rate)
        {
            synth.Volume = volume; // 音量
            synth.Rate = rate; // 语速
        }
    }
}
