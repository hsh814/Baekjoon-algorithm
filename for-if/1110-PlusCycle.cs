using System;

namespace BJpractive
{
    class Program
    {
        static int CycleFinder(int n, int prev, int cycle)
        {
            if (n == prev) { return cycle; }
            int sum = 0; 
            int present = 0;
            if (cycle == 0)
            {
                sum = (n % 10) + (n / 10);
                present = (n % 10) * 10 + (sum % 10);
            }
            else
            {
                sum = (prev % 10) + (prev / 10);
                present = (prev % 10) * 10 + (sum % 10);
            }
            cycle++;
            return CycleFinder(n, present, cycle);
        }
        static void Main(string[] args)
        {
            int n = Convert.ToInt32(Console.ReadLine());
            int cycle = CycleFinder(n, -1, 0);
            Console.WriteLine(cycle);
        }
    }
}
