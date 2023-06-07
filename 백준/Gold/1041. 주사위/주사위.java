import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] dice = new int[6];

        for (int i = 0; i < 6; i++) {
            dice[i] = sc.nextInt();
        }


        long result = 0;

        if(n == 1) {
            int min5 = 301;
            int sum = 0;
            for (int i = 0; i < 6; i++) {
                sum += dice[i];
            }
            for (int i = 0; i < 6; i++) {
                int tmp = sum - dice[i];
                if(min5 > tmp) {
                    min5 = tmp;
                }
            }
            result = min5;

        } else {
            long min2 = 101;
            long min3 = 151;

            int[] lst = new int[12];
            // ab, ac, ad, ae
            // bc, ce, de, bd
            // bf, cf, df, ef

            // a - 0, b - 1, c - 2, d - 3, e - 4, f - 5
            lst[0] = dice[0] + dice[1];
            lst[1] = dice[0] + dice[2];
            lst[2] = dice[0] + dice[3];
            lst[3] = dice[0] + dice[4];

            lst[4] = dice[1] + dice[2];
            lst[5] = dice[2] + dice[4];
            lst[6] = dice[3] + dice[4];
            lst[7] = dice[1] + dice[3];

            lst[8] = dice[5] + dice[1];
            lst[9] = dice[5] + dice[2];
            lst[10] = dice[5] + dice[3];
            lst[11] = dice[5] + dice[4];

            for (int i = 0; i < 12; i++) {
                if(min2 > lst[i]) {
                    min2 = lst[i];
                }


            }

            // abc, ace, aed, abd
            // cbf, bdf, def, cef

            // a - 0, b - 1, c - 2, d - 3, e - 4, f - 5

            int[] lst2 = new int[8];

            lst2[0] = dice[0] + dice[1] + dice[2];
            lst2[1] = dice[0] + dice[2] + dice[4];
            lst2[2] = dice[0] + dice[3] + dice[4];
            lst2[3] = dice[0] + dice[1] + dice[3];

            lst2[4] = dice[5] + dice[1] + dice[2];
            lst2[5] = dice[5] + dice[1] + dice[3];
            lst2[6] = dice[5] + dice[3] + dice[4];
            lst2[7] = dice[5] + dice[2] + dice[4];

            for (int i = 0; i < 8; i++) {
                if (min3 > lst2[i]) {
                    min3 = lst2[i];
                }
            }

            if(n == 2) {
                result = min3 * 4 + min2 * 4;
            }


            if(n > 2) {
                
                long min1 = 51;
                for (int i = 0; i < 6; i++) {
                    if(min1 > dice[i]) {
                        min1 = dice[i];
                    }
                }
                long tmp2 = (long) Math.pow(n-2, 2);
                result = (min3 * 4) + (min2 * (n-2)*4) + (min1 * tmp2) + (((min2 * 4) + (min1 * (n-2)*4))*(n-1));
/*

        250,000,000,000,000
        50,000,552,894,464
                24 + 12 + 1 + (12 + 4) * 2

                3*4
                2*(i-2)*4
                1*(i-2)*2

                {
                    2*4
                    1*(i-2)*4
                } * (i-1)
*/
            }

        }


        System.out.println(result);

    }
}