#include <iostream>
#include <string>
#include <vector>
#include <string.h>

#define DIV 1000000007

using namespace std;

static int results[500009];

long bench_sum(int n, int start, long *save)
{
  long num = 0;
  long multiple = start * benchs[n - 1];
  *save = multiple;
  if
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int totalCase;
    cin >> totalCase;
    for(int repeat = 0; repeat < totalCase; repeat++)
    {
        cin >> n;
        results[repeat] = n;
    }
    long result = 
    cout << result;
    return 0;
}