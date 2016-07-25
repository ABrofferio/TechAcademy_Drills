using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace Drill33
{
    class Program
    {
        public static void OriginFiles(string pathA)
        {
            string[] homeArray = Directory.GetFiles(@"C:\Users\Owner\Desktop\Drill33A");
            string DestFolder = @"C:\Users\Owner\Desktop\Drill33B";
            DateTime now = DateTime.Now;
            DateTime epoch = new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc);
            var now1 = (now - epoch).TotalSeconds;
            var hours24 = now1 - 86400;
            Console.WriteLine("Files in FolderA are:");
            foreach (var item in homeArray)
            {
                FileInfo file = new FileInfo(item);
                var edited = file.LastWriteTime;
                var editedSec = (edited - epoch).TotalSeconds;
                var fileName = Path.GetFileName(file.FullName);
                var diff = now1 - editedSec;
                var toCopy = new List<string>();
                if (diff <= 86400)
                {
                    //toCopy.Add(fileName);
                    Console.WriteLine("{0}, {1}", fileName, edited);
                    var transferred = file.CopyTo(Path.Combine(DestFolder, fileName));
                    Console.WriteLine(transferred);
                }
                else
                {
                    Console.WriteLine("{0} not eligible for transfer", fileName);
                }
            }
        }
        static void Main(string[] args)
        {
            Program.OriginFiles(@"C:\Users\Owner\Desktop\Drill33A");
        }
    }
}
