import java.util.*;
import java.io.*;

public class Main {
    static int N, M, start, end;
    static ArrayList<ArrayList<Node>> graph;

    static class Node {
        int idx, c, cnt;
        String trace;
        Node(int idx, int c, int cnt, String trace) {
            this.idx = idx;
            this.c = c;
            this.cnt = cnt;
            this.trace = trace;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        graph = new ArrayList<ArrayList<Node>>();
        for (int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            graph.get(s).add(new Node(e, c, 1, Integer.toString(s)));
        }

        int[] dist = new int[N+1];
        for (int i = 0; i < N + 1; i++) {
            dist[i] = Integer.MAX_VALUE;
        }

        st = new StringTokenizer(br.readLine());
        start = Integer.parseInt(st.nextToken());
        end = Integer.parseInt(st.nextToken());

        PriorityQueue<Node> q = new PriorityQueue<>((o1, o2) -> Integer.compare(o1.c, o2.c));
        q.offer(new Node(start, 0, 1, Integer.toString(start)));

        while(!q.isEmpty()) {
            Node curNode = q.poll();

            if(curNode.idx == end) {
                System.out.println(curNode.c);
                System.out.println(curNode.cnt);
                st = new StringTokenizer(curNode.trace);
                while (st.hasMoreTokens()) {
                    System.out.print(st.nextToken() + " ");
                }

                return;
            }

            if(dist[curNode.idx] < curNode.c) {
                continue;
            }

            for (int i = 0; i < graph.get(curNode.idx).size(); i++) {
                Node nxtNode = graph.get(curNode.idx).get(i);
                if (dist[nxtNode.idx] > curNode.c + nxtNode.c) {
                    dist[nxtNode.idx] = curNode.c + nxtNode.c;
                    q.offer(new Node(nxtNode.idx, dist[nxtNode.idx], curNode.cnt + 1, curNode.trace + " " + Integer.toString(nxtNode.idx)));
                }
            }
        }
    }
}
