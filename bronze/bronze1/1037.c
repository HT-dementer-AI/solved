#include <stdio.h>
#include <stdlib.h>

int max(int *arr, int arrSize)
{
    int maxNum;
    maxNum = arr[0];
    for (int i = 0; i < arrSize; i++)
    {
        if (maxNum < arr[i])
        {
            maxNum = arr[i];
        }
    }
    return maxNum;
}

int min(int *arr, int arrSize)
{
    int minNum;
    minNum = arr[0];
    for (int i = 0; i < arrSize; i++)
    {
        if (minNum > arr[i])
        {
            minNum = arr[i];
        }
    }
    return minNum;
}

int main()
{
    int n, result;
    scanf("%d", &n);
    int *array = (int *)malloc(sizeof(int) * n);

    for (int i = 0; i < n; i++)
    {
        scanf("%d", array + i);
    }

    // printf("%d %d\n", max(array, n), min(array, n));
    result = max(array, n) * min(array, n);
    printf("%d", result);
}