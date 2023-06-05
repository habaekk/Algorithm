import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());

        ArrayList<Integer> lst = new ArrayList<Integer>(n);

        for(int i = 0; i < n; i++) {
            lst.add(Integer.parseInt(bf.readLine()));
        }

        Collections.sort(lst);

        for(int i = n-1; i > 1; i--) {

            if(lst.get(i) >= lst.get(i-1)+lst.get(i-2)) {
                continue;
            } else {
                System.out.println(lst.get(i) + lst.get(i-1) + lst.get(i-2));
                return;
            }
        }

        System.out.println(-1);
    }
}
