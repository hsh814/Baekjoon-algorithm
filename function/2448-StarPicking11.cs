using System;

namespace BJpractive
{
    class Program
     {
        static string InputStar(int n, int i)
        {
            string[] stars = { "  *  ", " * * ", "*****" };
            if (n == 3)
            {
                return stars[i];
            }
            else if(i < n/2)
            {
                return new string(' ', n / 2 ) + InputStar(n / 2, i) + new string(' ', n / 2);
            }
            else
            {
                return InputStar(n / 2, i - n/2) + " " + InputStar(n / 2, i - n/2);
            }
        }
        static void WriteStar(int n, string[] allStar)
        {
            foreach(string star in allStar)
            {
                Console.WriteLine(star + " ");
            }
        }
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            string[] allStar = new string[n];
            for (int i = 0; i < n; i++)
            {
                allStar[i] = InputStar(n, i);
            }
            WriteStar(n, allStar);
        }
    }
}
