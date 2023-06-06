import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        char[][] mtrx1 = new char[n][m];
        char[][] mtrx2 = new char[n][m];

        for(int i = 0; i < n; i++){
            String nxt = sc.next();
            for(int j = 0; j < m; j++) {
                mtrx1[i][j] = nxt.charAt(j);
            }
        }

        for(int i = 0; i < n; i++){
            String nxt = sc.next();
            for(int j = 0; j < m; j++) {
                mtrx2[i][j] = nxt.charAt(j);
            }
        }

        int cnt = 0;

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(mtrx1[i][j] != mtrx2[i][j]) {
                    cnt += 1;
                    if ((i+2 < n) && (j+2 < m)) {
                        for (int k = 0; k < 3; k++) {
                            for (int l = 0; l < 3; l++) {
                                if (mtrx1[i+k][j+l] == '0') {
                                    mtrx1[i+k][j+l] = '1';
                                } else {
                                    mtrx1[i+k][j+l] = '0';
                                }
                            }
                        }
                    } else {
                        System.out.println(-1);
                        return;
                    }
                }
            }
        }

        System.out.println(cnt);
    }
}