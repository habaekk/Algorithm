import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static class SegmentTree {
        long[][] minMaxTree;


        SegmentTree(int n) {
            double treeHeight = Math.ceil(Math.log(n)/Math.log(2)) + 1;
            long treeNodes = Math.round(Math.pow(2, treeHeight));
            minMaxTree = new long[Math.toIntExact(treeNodes)][2];
        }

        long[] init(long[] arr, int node, int start, int end) {
            if (start == end) {
                minMaxTree[node][0] = arr[start]; minMaxTree[node][1] = arr[start];
                return minMaxTree[node];
            } else {
                long min, max;
                long[] a = init(arr, node*2, start, (start+end)/2);
                min = a[0]; max = a[1];
                long[] b = init(arr, node*2+1, (start+end)/2+1, end);
                if (min > b[0]) {
                    min = b[0];
                }
                if (max < b[1]) {
                    max = b[1];
                }
                minMaxTree[node][0] = min; minMaxTree[node][1] = max;
                return minMaxTree[node];
            }
        }

        long[] search(int node, int start, int end, int left, int right) {
            if (start > right || end < left) {
                long[] a = new long[2];
                a[0] = Long.MAX_VALUE; a[1] = Long.MIN_VALUE;
                return a;
            } else if (start >= left && end <= right) {
                long[] b = new long[2];
                b[0] = minMaxTree[node][0];
                b[1] = minMaxTree[node][1];
                return b;
            } else {
                long min, max;
                long[] c = search(node*2, start, (start+end)/2, left, right);
                min = c[0]; max = c[1];
                long[] d = search(node*2+1, (start+end)/2+1, end, left, right);
                if (min > d[0]) {
                    min = d[0];
                }
                if (max < d[1]) {
                    max = d[1];
                }
                long[] e = new long[2]; e[0] = min; e[1] = max;

                return e;
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
            arr[i] = Long.parseLong(br.readLine());
        }

        SegmentTree tree = new SegmentTree(n);
        tree.init(arr, 1, 1, n);


        long[] lst = new long[2];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int left = Integer.parseInt(st.nextToken());
            int right = Integer.parseInt(st.nextToken());
            lst = tree.search(1, 1, n, left, right);
            System.out.println(lst[0] + " " + lst[1]);
        }
    }
}

