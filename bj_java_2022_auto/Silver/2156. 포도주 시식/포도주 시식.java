import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static int[] podo;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        podo = new int[n+1];
        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            podo[i] = Integer.parseInt(st.nextToken());
        }

        int[] dp = new int[n+1];
        dp[1] = podo[1];
        if (n > 1) {
            dp[2] = podo[1]+podo[2];
        }
        for (int i = 3; i <= n; i++) {
            dp[i] = Math.max(dp[i - 1], Math.max(dp[i - 2] + podo[i], dp[i-3] + podo[i-1] + podo[i]));
        }
        System.out.println(dp[n]);

    }
}
