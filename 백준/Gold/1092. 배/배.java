import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        ArrayList<Integer> crane = new ArrayList<Integer>();

        for (int i = 0; i < n; i++) {
            crane.add(sc.nextInt());
        }

        int m = sc.nextInt();
        ArrayList<Integer> box = new ArrayList<Integer>();

        for (int i = 0; i < m; i++) {
            box.add(sc.nextInt());
        }

        Collections.sort(crane, Collections.reverseOrder());
        Collections.sort(box, Collections.reverseOrder());



        if(crane.get(0) < box.get(0)) {
            System.out.println(-1);
            return;
        }

        int time = 0;

        while(!box.isEmpty()) {
            int idx = 0;
            for (int i = 0; i < n;) {
                if (idx == box.size()) {
                    break;
                } else if (crane.get(i) >= box.get(idx)) {
                    box.remove(idx);
                    i++;
                } else {
                    idx++;
                }
            }
            time++;
        }
        System.out.println(time);
    }
}