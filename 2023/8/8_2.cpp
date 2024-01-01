#include <iostream>
#include <vector>

using namespace std;
int count(int *arr, int num, int len)
{
    for (int i = len - 1; i >= 0; i--)
    {
        if (arr[i] >= num)
            return i + 1;
    }
    return 0;
}
int main()
{

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int num;
    cin >> num;
    int *arr = new int[num];
    int length = 0;
    int number;
    for (int i = 0; i < num; i++)
    {
        cin >> number;
        cout << count(arr, number, length) << " ";
        arr[length] = number;
        length++;
    }
}