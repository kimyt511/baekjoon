// 787 Cheapest Flights Within K Stops
public class Solution
{
    public int FindCheapestPrice(int n, int[][] flights, int src, int dst, int k)
    {
        int[,] arr = new int[n, n];
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                arr[i, j] = 0;
            }
        }
        foreach (int[] i in flights)
        {
            arr[i[0], i[1]] = i[2];
        }
        Queue<int[]> queue = new Queue<int[]>();
        int[] dp = new int[n];
        int ans = -1;
        queue.Enqueue(new int[] { src, 0, -1 });
        while (queue.Count > 0)
        {
            int[] data = queue.Dequeue();
            if (data[2] > k) continue;
            if (data[0] == dst)
            {
                if (ans == -1) ans = data[1];
                else ans = Math.Min(ans, data[1]);
            }
            else
            {
                if (dp[data[0]] != 0 && dp[data[0]] < data[1]) continue;
                else if (dp[data[0]] == 0) dp[data[0]] = data[1];
                else dp[data[0]] = Math.Min(dp[data[0]], data[1]);

                for (int i = 0; i < n; i++)
                {
                    if (arr[data[0], i] != 0) queue.Enqueue(new int[] { i, data[1] + arr[data[0], i], data[2] + 1 });
                }
            }

        }
        return ans;
    }

}