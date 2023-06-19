import java.io.*;
import java.util.*;

public class Main {
    static int n, q, x, y, a;
    static long b;
    static long[] arr;


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
                return tree[node] = init(arr, node*2, start, (start+end)/2) + init(arr, node*2+1, (start+end)/2+1, end);
            }
        }

        long sum(int node, int start, int end, int left, int right) {
            if (start > right || end < left) {
                return 0;
            } else if (start >= left && end <= right) {
                return tree[node];
            } else {
                return sum(node*2, start, (start+end)/2, left, right) + sum(node*2+1, (start+end)/2+1, end, left, right);
            }
        }

        void update(int node, int start, int end, int idx, long diff) {
            if (start > idx || end < idx) {
                return;
            } else {
                tree[node] = tree[node] + diff;
            }

            if (start != end) {
                update(node*2, start, (start+end)/2, idx, diff);
                update(node*2+1, (start+end)/2+1, end, idx, diff);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        q = Integer.parseInt(st.nextToken());

        arr = new long[n+1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < n+1; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }

        SegmentTree t = new SegmentTree(n);
        t.init(arr, 1, 1, n);

        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());
            if (x > y) {
                int tmp = y;
                y = x;
                x = tmp;
            }
            a = Integer.parseInt(st.nextToken());
            b = Long.parseLong(st.nextToken());
            System.out.println(t.sum(1, 1, n, x, y));
            long diff = - arr[a] + b;
            arr[a] = b;
            t.update(1, 1, n, a, diff);
        }
    }
}