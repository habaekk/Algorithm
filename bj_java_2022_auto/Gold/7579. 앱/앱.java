import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static int[] memory, cost;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        int ans = Integer.MAX_VALUE;

        memory = new int[n];
        cost = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            memory[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            cost[i] = Integer.parseInt(st.nextToken());
        }

        int[][] dp = new int[n][10001];

        for (int i = 0; i < n; i++) {
            int curCost = cost[i];
            int curMem = memory[i];

            for (int j = 0; j <= 10000; j++) {
                if(i == 0) {
                    if (j >= curCost) {
                        dp[i][j] = curMem;
                    }
                } else {
                    if (j >= curCost) {
                        dp[i][j] = Math.max(dp[i-1][j-curCost] + curMem, dp[i-1][j]);
                    } else {
                        dp[i][j] = dp[i-1][j];
                    }
                }
                if (dp[i][j] >= m) {
                    ans = Math.min(ans, j);
                }
            }
        }

        System.out.println(ans);
    }
}