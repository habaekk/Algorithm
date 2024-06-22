import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int l = sc.nextInt();

        ArrayList<Integer> leakLst = new ArrayList<Integer>();
        for(int i = 0; i < n; i++) {
            leakLst.add(sc.nextInt());
        }

        Collections.sort(leakLst);

        int taped = 0;
        int cnt = 0;
        for(int i = 0; i < n; i++) {
            int leak = leakLst.get(i);
            if(taped < leak) {
                taped = leak+l-1;
                cnt++;
            }
        }

        System.out.println(cnt);
    }
}
