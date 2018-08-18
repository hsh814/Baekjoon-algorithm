using System;

namespace BJpractive
{
    class Month
    {
        string[] day = { "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT" };
        int[] month = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        int n = 0;
        public Month(int m, int d)
        {
            for (int k = 0; k < m - 1; k++)
            {
                n += month[k];
            }
            n += d;
        }   
        public string WhatDay()
        {
            return day[(n % 7)];
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            string[] days = Console.ReadLine().Split(' ');
            int[] md = { int.Parse(days[0]), int.Parse(days[1]) };
            Month m = new Month(md[0], md[1]);
            Console.WriteLine(m.WhatDay());
        }
    }
}
