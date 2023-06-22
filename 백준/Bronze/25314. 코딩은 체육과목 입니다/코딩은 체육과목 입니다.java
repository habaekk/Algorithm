import java.util.*;
import java.io.*;

public class Main {
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int repeat = n / 4;
        for (int i = 0; i < repeat; i++) {
            System.out.print("long ");
        }
        System.out.println("int");
    }
}
