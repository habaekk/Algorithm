import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        char[][] lst = new char[n][m];

        sc.nextLine();
        for(int i = 0; i < n; i++) {
            String nxt = sc.next();
            for(int j = 0; j < m; j++) {
                lst[i][j] = nxt.charAt(j);
            }
        }

        int cnt = 0;

        for (int i = n-1; i > -1; i--) {
            for (int j = m-1; j > -1; j--) {
                int coinAt = lst[i][j];
                if (coinAt == '1') {
                    cnt += 1;
                    for(int k = 0; k < i+1; k++) {
                        for(int l = 0; l < j+1; l++) {
                            if(lst[k][l] == '0') {
                                lst[k][l] = '1';
                            } else {
                                lst[k][l] = '0';
                            }
                        }
                    }
                }
            }
        }
        System.out.println(cnt);
    }
}