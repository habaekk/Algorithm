import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] info = br.readLine().split(" ");

        long[] arr = new long[Integer.parseInt(info[0])+1];

        for (int i = 1; i <= Integer.parseInt(info[0]); i++) {
            arr[i] = Long.parseLong(br.readLine());
        }

        SegmentTree st = new SegmentTree(Integer.parseInt(info[0]));
        st.init(arr, 1, 1, Integer.parseInt(info[0]));

        for (int i = 0; i < Integer.parseInt(info[1]) + Integer.parseInt(info[2]); i++) {
            String[] operation = br.readLine().split(" ");

            if(Integer.parseInt(operation[0]) == 1){

                long diff = Long.parseLong(operation[2]) - arr[Integer.parseInt(operation[1])];
                arr[Integer.parseInt(operation[1])] = Long.parseLong(operation[2]);
                st.update(1, 1, Integer.parseInt(info[0]), Integer.parseInt(operation[1]), diff );

                
         }else{
                
                long result = st.sum(1, 1, Integer.parseInt(info[0]), Integer.parseInt(operation[1]), Integer.parseInt(operation[2]));

                bw.write(String.valueOf(result));
                bw.newLine();
            }
        }

        br.close();
        bw.flush();
        bw.close();

    }

    static class SegmentTree{
        private long[] tree;

        SegmentTree(int n) {
            double treeHeight = Math.ceil(Math.log(n)/Math.log(2))+1;
            long treeNodeCount = Math.round(Math.pow(2, treeHeight));
            tree = new long[Math.toIntExact(treeNodeCount)];
        }

        long init(long[] arr, int node, int start, int end ){
            if (start == end) {
                return tree[node] = arr[start];
            }else{
                return tree[node] = init(arr, node*2, start, (start+end)/2)
                        + init(arr, node*2+1, (start+end)/2+1, end);
            }
        }

        long sum(int node, int start, int end, int left, int right) {
            if (end < left || right < start) {
                return 0;
            } else if (left <= start && end <= right) {
                return tree[node];
            } else {
                return sum(node*2, start, (start+end)/2, left, right)
                        + sum(node*2+1, (start+end)/2+1, end, left, right);
            }
        }

        void update(int node, int start, int end, int index, long diff) {
            if (index < start || end < index) {
                return;
            }else {
                tree[node] = tree[node] + diff;

                if (start != end) {
                    update(node*2, start, (start+end)/2, index, diff) ;
                    update(node*2+1, (start+end)/2+1, end, index, diff) ;
                }
            }
        }
    }
}