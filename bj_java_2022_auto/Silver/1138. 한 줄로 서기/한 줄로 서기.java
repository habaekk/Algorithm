import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] lst = new int[n];
        int[] result = new int[n];

        for(int i = 0; i < n; i++) {
            lst[i] = sc.nextInt();
        }

        for(int i = 0; i < n; i++) {
            int cnt = 0;
            int l = lst[i];

            for(int j = 0; j < n; j++) {


                if(cnt == l && result[j] == 0) {
                    result[j] = i+1;
                    break;
                }
                if(result[j] == 0) {
                    cnt += 1;
                }
            }
        }

        for(int i = 0; i < n; i++) {
            System.out.print(result[i]);
            System.out.print(" ");
        }
    }
}
