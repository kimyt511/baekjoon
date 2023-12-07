#include <iostream>
#include <vector>

using namespace std;

int n, num, segtree[400000], ans[100000];

void update(int start, int end, int node, int idx, int val)
{
    if (start > idx || end < idx)
        return;
    if (start == end)
    {
        if (start == idx)
        {
            segtree[node] += val;
            return;
        }
    }
    if (start <= idx && idx <= end)
    {
        segtree[node] += val;
        int mid = (start + end) / 2;
        update(start, mid, node * 2, idx, val);
        update(mid + 1, end, node * 2 + 1, idx, val);
    }
}

int get(int start, int end, int node, int left, int right)
{
    if (end < left || start > right)
        return 0;
    if (left <= start && end <= right)
        return segtree[node];
    int mid = (start + end) / 2;
    return get(start, mid, node * 2, left, right) + get(mid + 1, end, node * 2 + 1, left, right);
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(NULL);
    int left, right;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> num;
        left = 0;
        right = n - 1;
        while (left <= right)
        {
            int mid = (left + right) / 2;
            if (mid - get(0, n - 1, 1, 0, mid) < num)
            {
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
        }
        ans[left] = i;
        update(0, n - 1, 1, left, 1);
    }

    for (int i = 0; i < n; i++)
    {
        printf("%d\n", ans[i]);
    }
}
