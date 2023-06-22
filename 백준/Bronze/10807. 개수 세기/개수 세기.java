import java.util.*;
import java.io.*;

public class Main {
    static int n, v;
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        int target = Integer.parseInt(st.nextToken());

        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] == target) {
                cnt ++;
            }
        }
        System.out.println(cnt);
    }
}
