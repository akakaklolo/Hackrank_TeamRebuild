#include <stdio.h>
#include <math.h>

int main()
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
        int n;
        scanf("%d", &n);
        if ((n % 10 >= 3) && (n % 10 <= 4) && (n >= 40))
        {
            n += 5 - (n % 10);
        }
        else if ((n % 10 >= 8) && (n % 10 <= 9) && (n >= 38))
        {
            n += 10 - (n % 10);
        }
        printf("%d", n);
        printf("\n");
    }
}