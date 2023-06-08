import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = 99;

        int[][] dp = new int[n+1][k+1];
        int[] w = new int[n+1];
        int[] v = new int[n+1];


        for (int i = 0; i < n; i++) {
            w[i+1] = sc.nextInt();
        }

        for (int i = 0; i < n; i++) {
            v[i+1] = sc.nextInt();
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= k; j++) {
                if (w[i] <= j) {
                    dp[i][j] = Math.max(dp[i-1][j-w[i]]+v[i], dp[i-1][j]);
                } else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        System.out.println(dp[n][k]);
    }
}
