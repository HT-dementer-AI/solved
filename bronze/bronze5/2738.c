#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a, b;
    int arr1[100][100];
    int arr2[100][100];

    scanf("%d %d", &a, &b);

    for (int i = 0; i < a; i++)
    {
        for (int j = 0; j < b; j++)
        {
            scanf("%d", &arr1[i][j]);
        }
    }

    for (int i = 0; i < a; i++)
    {
        for (int j = 0; j < b; j++)
        {
            scanf("%d", &arr2[i][j]);
        }
    }

    for (int i = 0; i < a; i++)
    {
        for (int j = 0; j < b; j++)
        {
            printf("%d ", arr1[i][j] + arr2[i][j]);
        }
        printf("\n");
    }
}