import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static class SegmentTree {
        long[] tree;
        SegmentTree(int n) {
            double treeHeight = Math.ceil(Math.log(n)/Math.log(2)) + 1;
            long treeNodes = Math.round(Math.pow(2, treeHeight));
            tree = new long[Math.toIntExact(treeNodes)];
        }

        long init(long[] arr, int node, int start, int end) {
            if (start == end) {
                return tree[node] = arr[start];
            } else {
                long a = init(arr, node*2, start, (start+end)/2);
                long b = init(arr, node*2+1, (start+end)/2+1, end);
                if (a > b) {
                    return tree[node] = b;
                } else {
                    return tree[node] = a;
                }
            }
        }

        long search(int node, int start, int end, int left, int right) {
            if (start > right || end < left) {
                return Long.MAX_VALUE;
            } else if (start >= left && end <= right) {
                return tree[node];
            } else {
                long a = search(node*2, start, (start+end)/2, left, right);
                long b = search(node*2+1, (start+end)/2+1, end, left, right);
                if (a > b) {
                    return b;
                } else {
                    return a;
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        long[] arr = new long[n+1];
        for (int i = 1; i < n+1; i++) {
            long a = Long.parseLong(br.readLine());
            arr[i] = a;
        }

        SegmentTree tree = new SegmentTree(n);
        tree.init(arr, 1, 1, n);

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            long c = tree.search(1, 1, n, a, b);
            System.out.println(c);
        }
    }
}
