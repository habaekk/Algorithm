import java.util.*;
import java.io.*;

public class Main {
    static int n;

    static class SegmentTree {
        long[] tree;

        SegmentTree() {
            double treeHeight = Math.ceil(Math.log(1000000)/Math.log(2)) + 1;
            long treeNodes = Math.round(Math.pow(2, treeHeight));
            tree = new long[Math.toIntExact(treeNodes)];
        }

        void update(int node, int start, int end, int taste, int num) {
            if (start > taste || end < taste) {
                return;
            } else {
                tree[node] += num;
            }
            if (start != end) {
                update(node*2, start, (start+end)/2, taste, num);
                update(node*2+1, (start+end)/2+1, end, taste, num);
            }
        }

        void find(int node, int start, int end, long nthTaste) {
            tree[node] -= 1;
            if (start == end) {
                System.out.println(start);
                return;
            }

            if (tree[node*2] >= nthTaste) {
                find(node*2, start, (start+end)/2, nthTaste);
            } else {
                find(node*2+1, (start+end)/2+1, end, nthTaste - tree[node*2]);
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        SegmentTree t = new SegmentTree();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.MAX_VALUE;
            if (st.hasMoreTokens()) {
                c = Integer.parseInt(st.nextToken());
            }

            if (a == 1) {
                t.find(1, 1, 1000000, (long)b);

            }

            if (a == 2) {
                t.update(1, 1, 1000000, b, c);
            }
        }
    }
}