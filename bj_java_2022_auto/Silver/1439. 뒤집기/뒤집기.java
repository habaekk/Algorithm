import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String str = new String("");

        str = sc.nextLine();
        int s = str.length();
        int cnt0 = 0;
        int cnt1 = 0;
        int prev = -1;

        for(int i = 0; i < s; i++) {
            char curr = str.charAt(i);
            
            if(prev != curr) {
                if(curr == '0') {
                    cnt0 += 1;
                } else {
                    cnt1 += 1;
                }
                prev = curr;
            }
        }

        System.out.println(Math.min(cnt0, cnt1));
    }
}