import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int N, INF = 987654321, allMask;
	static int[][] arr, dp;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());

		allMask = (1 << N) - 1; // ex) 5개 도시 => 11111 => 1<<5 = 100000 여기서 -1 해주면 11111
		arr = new int[N][N];
		dp = new int[N][allMask];
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		System.out.println(tsp(0, 1));
	}

	static int tsp(int idx, int mask) {
		if (mask == allMask) {
			if (arr[idx][0] == 0) return INF;
			return arr[idx][0];
		}

		if (dp[idx][mask] != 0) return dp[idx][mask];

		dp[idx][mask] = INF;

		for (int i = 0; i < N; i++) {
			if (arr[idx][i] == 0 || (mask & (1 << i)) != 0)	continue;
			dp[idx][mask] = Math.min(dp[idx][mask], tsp(i, mask | (1 << i)) + arr[idx][i]);
		}

		return dp[idx][mask];
	}
}