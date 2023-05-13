#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a, b, n;
    int result; // 결과를 받을변수

    scanf("%d %d %d", &a, &b, &n);

    for (int i = 0; i < n; i++)
    {
        a %= b;
        a *= 10;
        result = a / b;
    }

    printf("%d", result);

    return 0;
}