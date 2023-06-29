import java.util.*;
import java.io.*;

public class Main {
    static int n, k;
    static int[][]  items, dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());


        items = new int[n][2];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            items[i][0] = Integer.parseInt(st.nextToken());
            items[i][1] = Integer.parseInt(st.nextToken());
        }

        dp = new int[n+1][k+1];

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= k; j++) {
                int w = items[i-1][0];
                int v = items[i-1][1];
                if (j >= w) {
                    dp[i][j] = Math.max(dp[i-1][j - w] + v, dp[i-1][j]);
                } else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }

        System.out.println(dp[n][k]);
    }
}