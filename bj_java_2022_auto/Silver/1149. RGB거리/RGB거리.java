import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] rA = new int[n][3];
        int[][] gA = new int[n][3];
        int[][] bA = new int[n][3];

        int[][] dp = new int[n][3];
        int[][] lst = new int[n][3];

        for(int i = 0; i < n; i ++) {

            lst[i][0] = sc.nextInt();
            lst[i][1] = sc.nextInt();
            lst[i][2] = sc.nextInt();

        }

        dp[0][0] = lst[0][0];
        dp[0][1] = lst[0][1];
        dp[0][2] = lst[0][2];

        for(int i = 1; i < n; i++) {
            dp[i][0] = Math.min(dp[i-1][1], dp[i-1][2]) + lst[i][0];
            dp[i][1] = Math.min(dp[i-1][0], dp[i-1][2]) + lst[i][1];
            dp[i][2] = Math.min(dp[i-1][0], dp[i-1][1]) + lst[i][2];
        }

        System.out.println(Math.min(Math.min(dp[n-1][0], dp[n-1][1]), dp[n-1][2]));


    }
}
