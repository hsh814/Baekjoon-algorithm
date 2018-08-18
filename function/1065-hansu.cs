using System;

namespace BJpractive
{
    class Program
     { 
        static bool CheckNum(int i)
        {
            if(i < 100) { return true; }
            else
            {
                return CheckBigNum(i);
            }
        }
        static bool CheckBigNum(int i)
        {
            string str = i.ToString();
            int gap = (int.Parse(str[0].ToString()) - int.Parse(str[1].ToString()));
            int d = 0;
            for (int k = 1; k < str.Length - 1; k++)
            {
                d = (int.Parse(str[k].ToString()) - int.Parse(str[k + 1].ToString()));
                if (d == gap) { continue; }
                else { return false; }
            }
            return true;
        }
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int oneNum = 0;
            for (int i = 1; i <= n; i++)
            {
                if (CheckNum(i))
                {
                    oneNum++;
                }
            }
            Console.WriteLine(oneNum);
        }
    }
}
