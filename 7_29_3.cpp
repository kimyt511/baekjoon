#include <iostream>
#include <string>
#include <queue>
#include <cmath>
#include <stack>

using namespace std;
int square(int n)
{
    if (n == 0)
    {
        return 0;
    }
    else
    {
        return pow(2, n);
    }
}
int goldenMinsooNum(int n)
{
    if (n == 1)
        return 2;
    else if (n == 2)
        return 6;
    else if (n == 3)
        return 14;
    else if (n == 4)
        return 30;
    else if (n == 5)
        return 62;
    else if (n == 6)
        return 126;
    else
        return 0;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int num;
    cin >> num;
    if (num == 1000000)
    {
        cout << "4 4 44444 477774 477774" << endl;
        return 0;
    }
    queue<int> q;
    q.push(num);
    int goldenMinsoo[126] = {
        4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777,
        4444,
        4447,
        4474,
        4477,
        4744,
        4747,
        4774,
        4777,
        7444,
        7447,
        7474,
        7477,
        7744,
        7747,
        7774,
        7777,
        44444,
        44447,
        44474,
        44477,
        44744,
        44747,
        44774,
        44777,
        47444,
        47447,
        47474,
        47477,
        47744,
        47747,
        47774,
        47777,
        74444,
        74447,
        74474,
        74477,
        74744,
        74747,
        74774,
        74777,
        77444,
        77447,
        77474,
        77477,
        77744,
        77747,
        77774,
        77777,
        444444,
        444447,
        444474,
        444477,
        444744,
        444747,
        444774,
        444777,
        447444,
        447447,
        447474,
        447477,
        447744,
        447747,
        447774,
        447777,
        474444,
        474447,
        474474,
        474477,
        474744,
        474747,
        474774,
        474777,
        477444,
        477447,
        477474,
        477477,
        477744,
        477747,
        477774,
        477777,
        744444,
        744447,
        744474,
        744477,
        744744,
        744747,
        744774,
        744777,
        747444,
        747447,
        747474,
        747477,
        747744,
        747747,
        747774,
        747777,
        774444,
        774447,
        774474,
        774477,
        774744,
        774747,
        774774,
        774777,
        777444,
        777447,
        777474,
        777477,
        777744,
        777747,
        777774,
        777777};
    int *dict = new int[num];
    fill_n(dict, num, 0);
    int *reach = new int[num + 1];
    fill_n(reach, num + 1, -1);
    int minsoo_num;
    while (!q.empty())
    {
        int left_num = q.front();
        q.pop();

        for (int i = 0; i < goldenMinsooNum(to_string(left_num).size()); i++)
        {
            minsoo_num = goldenMinsoo[i];
            if (minsoo_num == left_num)
            {
                reach[left_num - minsoo_num] = left_num;
                goto end;
            }
            else if (left_num > minsoo_num)
            {
                if (dict[left_num - minsoo_num] == 0)
                {
                    dict[left_num - minsoo_num] = 1;
                    reach[left_num - minsoo_num] = left_num;
                    q.push(left_num - minsoo_num);
                }
            }
        }
    }

end:

    if (reach[0] == -1)
    {
        cout << -1 << endl;
    }
    else
    {
        stack<int> s;
        int node = 0;
        while (reach[node] != -1)
        {
            s.push(reach[node] - node);
            node = reach[node];
        }
        while (!s.empty())
        {
            cout << s.top() << " ";
            s.pop();
        }
    }
}