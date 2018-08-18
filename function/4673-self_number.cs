using System;
using System.Collections.Generic;

namespace BJpractive
{
    class Program
     { 
        static int GetD(int i)
        {
            string str = i.ToString();
            int d = i;
            foreach (char c in str)
            {
                d += int.Parse(c.ToString());
            }
            return d;
        }
        static void Main(string[] args)
        {
            int len = 10000;
            List<int> nonSelfNums = new List<int>();
            for(int i = 1; i <= len; i++)
            {
                nonSelfNums.Add(GetD(i));
            }
            for (int n = 1; n < len; n++)
            {
                if (nonSelfNums.Contains(n) != true)
                {
                    Console.WriteLine(n);
                }
            }

        }
    }
}
