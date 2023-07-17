import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        String result = "";
        for (int i = 0; i < s.length(); i++) {
            if(Character.isUpperCase(s.charAt(i))) {
                result += Character.toLowerCase(s.charAt(i));
            } else {
                result += Character.toUpperCase(s.charAt(i));
            }
        }

        System.out.println(result);
    }
}
