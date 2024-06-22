import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int numOfBottle = n;
        int buy = 0;
        int c = 0;


        while(true) {
            numOfBottle = n+buy;
            c = 0;

            while(true) {
                int q = numOfBottle / 2;
                int r = numOfBottle % 2;

                if (r == 1) {
                    c += 1;
                }

                if(q == 0) {
                    break;
                }

                numOfBottle /= 2;
            }

            if(c <= k) {
                break;
            }

            buy++;
        }

        System.out.println(buy);
    }
}