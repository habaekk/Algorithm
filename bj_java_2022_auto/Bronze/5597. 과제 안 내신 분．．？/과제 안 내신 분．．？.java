import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int[] attendence;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        attendence = new int[28];
        for (int i = 0; i < 28; i++) {
            attendence[i] = Integer.parseInt(br.readLine());
        }
        int no1 = 0;
        int no2 = 0;
        for (int i = 0; i < 31; i++) {
            for (int j = 0; j < 28; j++) {
                if (attendence[j] == i) {
                    break;
                }
                if (j == 27) {
                    if (no1 == 0) {
                        no1 = i;
                    } else {
                        no2 = i;
                    }
                }
            }
        }

        System.out.println(no1);
        System.out.println(no2);
    }
}