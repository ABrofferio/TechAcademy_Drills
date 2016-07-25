using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Item44bExercises
{
    class Program
    {
        static void grade()
        {
            Console.WriteLine("Enter students quiz score as a number out of 100 with no % :");
            int quiz = int.Parse(Console.ReadLine());
            Console.WriteLine("Enter students midterm score as a number out of 100 with no % :");
            int midterm = int.Parse(Console.ReadLine());
            Console.WriteLine("Enter students final score as a number out of 100 with no % :");
            int final = int.Parse(Console.ReadLine());
            int finalgrade = (quiz + midterm + final) / (3);
            if (finalgrade >= 90)
            {
                Console.WriteLine("The student's final grade of {0}% gets them an A in the class.", finalgrade);
            }
            else if (finalgrade >= 80 && finalgrade < 90)
            {
                Console.WriteLine("The student's final grade of {0}% gets them a B in the class.", finalgrade);
            }
            else if (finalgrade >= 70 && finalgrade < 80)
            {
                Console.WriteLine("The student's final grade of {0}% gets them a C in the class.", finalgrade);
            }
            else if (finalgrade >= 60 && finalgrade < 70)
            {
                Console.WriteLine("The student's final grade of {0}% gets them a D in the class.", finalgrade);
            }
            else if (finalgrade < 60)
            {
                Console.WriteLine("Ouch, the student's final grade of {0}% gets them an F in the class.", finalgrade);
            }
        }
        static void Main(string[] args)
        {
            Program.grade();
        }
    }
}
