#include <stdio.h>
int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        int a, b;
        scanf("%d %d", &a, &b);
        int num = a;
        for (int j = 1; j < b; j++)
        {
            num = num * a % 10;
        }
        if (num % 10 == 0)
            printf("%d\n", 10);
        else
            printf("%d\n", num % 10);
    }
}