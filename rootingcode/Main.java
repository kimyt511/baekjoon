
// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
import java.util.*;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        for (int i = 0; i <= 1000000; i++) {
            gms(i);
            System.out.print("\n");
        }
        
    }

    static void gms(int num) {
        int N = num;

        int[] roadToN = new int[N + 1];

        Vector<Integer> geumminsu = new Vector<>();
        Queue<Integer> tempQ = new LinkedList<Integer>();
        geumminsu.add(4);
        geumminsu.add(7);
        tempQ.offer(4);
        tempQ.offer(7);
        int temp;
        while (true) {
            temp = tempQ.poll();
            if (temp > 100000)
                break;
            geumminsu.add(temp * 10 + 4);
            geumminsu.add(temp * 10 + 7);
            tempQ.offer(temp * 10 + 4);
            tempQ.offer(temp * 10 + 7);
        }

        // System.out.println(geumminsu.toString());

        bfs(roadToN, N, geumminsu);
        int index = 0;
        Stack<Integer> tempStack = new Stack<>();
        if (roadToN[0] == 0)
            System.out.print(-1);
        else {
            while (index < N) {
                tempStack.push(roadToN[index]);
                index = index + roadToN[index];
            }
            System.out.print(tempStack.pop());
            while (!tempStack.isEmpty()) {
                System.out.print(" ");
                System.out.print(tempStack.pop());
            }
        }
    }

    static void bfs(int[] roadToN, int N, Vector<Integer> geumminsu) {
        Queue<Integer> q = new LinkedList<Integer>();

        boolean[] visited = new boolean[N + 1];

        // for (int i=0;i<N;i++){
        // System.out.println(Arrays.toString(visited[i]));
        // }
        // System.out.println();

        visited[N] = true;
        q.offer(N);

        while (!q.isEmpty()) {
            Integer node = q.poll();

            for (int i : geumminsu) {
                int tempNode = node - i;
                if (tempNode >= 0 && !visited[tempNode]) {
                    visited[tempNode] = true;
                    roadToN[tempNode] = i;
                    q.offer(tempNode);
                }
            }

            if (visited[0])
                break;
        }
    }
}