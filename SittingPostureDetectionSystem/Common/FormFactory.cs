using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;

namespace SittingPostureDetectionSystem.Common
{
    public class FormFactory
    {
        // static 一旦被赋值，会永远保持，不会因为运行、做操作或再次实例化而被修改，保持静态全局唯一性 => 单例
        //private static FrmUserManager frmUserManager; 
        //private static FrmBaseManager frmBaseManager;
        //private static FrmNone frmNone;
        //private static Form form;
        private static List<Form> forms = new(); // 库存，其中放的窗体一定是实例化后的
        //public static Form CreateForm(int idx) // 为了创造出窗体，返回给上端
        //{
        //    HideFormAll();
        //    // 简单工厂
        //    switch (idx) // 多次实例化会导致窗体闪烁 => 因此，对于展示多个窗体，遵循“单例”原则
        //    {
        //        case 0:
        //            if (frmUserManager == null)
        //            {
        //                frmUserManager = new FrmUserManager();
        //                forms.Add(frmUserManager);
        //            }
        //            form = frmUserManager;
        //            break;
        //        case 1:
        //            if (frmBaseManager == null)
        //            {
        //                frmBaseManager = new FrmBaseManager();
        //                forms.Add(frmBaseManager);
        //            }
        //            form = frmBaseManager;
        //            break;
        //        default:
        //            if (frmNone == null)
        //            {
        //                frmNone = new FrmNone();
        //                forms.Add(frmNone);
        //            }
        //            form = frmNone;
        //            break;
        //    }
        //    return form;
        //}

        // 缓存，避免反复进行反射，以提高性能高
        public static List<Type> types;
        static FormFactory() // 在程序运行时，同一个对象（包括同一个泛型类型）的构造只会运行一次
        {
            Assembly ass = Assembly.Load("SittingPostureDetectionSystem");
            types = ass.GetTypes().ToList();
        }

        /// <summary>
        /// 利用反射获取程序集中的窗体
        /// </summary>
        /// <param name="formName">窗体名称</param>
        public static Form CreateForm(string formName)
        {
            //string path = AppDomain.CurrentDomain.BaseDirectory; // 获取程序所在的根目录
            //Assembly ass = Assembly.LoadFile(path + "Appraisal_System");
            //Assembly ass = Assembly.LoadFrom("Appraisal_System.exe"); // 只需要程序名称，后缀名不可省略

            HideFormAll();
            Form? form = forms.Find(m => m.Name == formName);
            Type type = types.Find(m => m.Name == formName);
            if (form == null)
            {
                form = (Form)Activator.CreateInstance(type);
                forms.Add(form);
            }
            return form;
        }

        public static void HideFormAll()
        {
            foreach (var form in forms)
            {
                form.Hide();
            }
        }

        public static Form GetForm(string formName)
        {
            Form form = forms.Find(m => m.Name == formName);
            return form;
        }
    }
}
