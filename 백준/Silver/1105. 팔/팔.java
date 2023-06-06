import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String l = sc.next();
        String r = sc.next();

        int cnt = 0;

        for(int i = 0; i < l.length(); i++) {
            if(l.length() == r.length()) {

                if (l.charAt(i) != r.charAt(i)) {
                    break;
                }
                if (l.charAt(i) == '8' && r.charAt(i) == '8') {
                    cnt += 1;
                }
            } else {
                System.out.println(0);
                return;
            }
        }

        System.out.println(cnt);
    }
}