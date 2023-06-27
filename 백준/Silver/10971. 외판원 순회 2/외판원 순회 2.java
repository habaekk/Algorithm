import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int[][] dp, w;
    static final int INF = 16000000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        N = Integer.parseInt(br.readLine());
        dp = new int[N][(1 << N) - 1];
        w = new int[N][N];
        for (int i = 0; i < N; i++) {
            String[] input = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                w[i][j] = Integer.parseInt(input[j]);
            }
        }
        for (int i = 0; i < N; i++) {
            Arrays.fill(dp[i], INF);
        }

        bw.write(dfs(0, 1) + "\n");
        bw.flush();

    }

    public static int dfs(int node, int visit) {
        if (visit == (1 << N) - 1) {
            if (w[node][0] == 0) {
                return INF;
            } else {
                return w[node][0];
            }
        }

        if (dp[node][visit] != INF) {
            return dp[node][visit];
        }

        for (int i = 0; i < N; i++) {
            if ((visit & (1 << i)) == 0 && w[node][i] != 0) {
                dp[node][visit] = Math.min(dp[node][visit], dfs(i, visit | (1 << i)) + w[node][i]);
            }
        }

        return dp[node][visit];

    }
}
