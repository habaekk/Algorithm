import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static int[] gas, distance;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        gas = new int[n];
        distance = new int[n-1];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n-1; i++) {
            distance[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            gas[i] = Integer.parseInt(st.nextToken());
        }


        int result = 0;
        int currentGas = gas[0];

        for (int i = 0; i < n-1; i++) {
            int gasL = gas[i];
            int dist = distance[i];
            if (currentGas < gas[i]) {
                result += distance[i] * currentGas;
            } else {
                currentGas = gas[i];
                result += distance[i] * currentGas;
            }
        }

        System.out.println(result);
    }
}
