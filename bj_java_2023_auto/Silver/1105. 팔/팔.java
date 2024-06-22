import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String l = sc.next();
        String r = sc.next();

        int cnt = 0;

        if(l.length() == r.length()) {
            for(int i = 0; i < l.length(); i++) {
                if (l.charAt(i) != r.charAt(i)) {
                    break;
                }

                if (l.charAt(i) == '8' && r.charAt(i) == '8') {
                    cnt += 1;
                }
            }
        }

        System.out.println(cnt);
    }
}