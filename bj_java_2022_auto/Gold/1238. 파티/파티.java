import java.util.*;
import java.io.*;

public class Main {
    static int n, m, x;
    static ArrayList<ArrayList<Node>> graph;

    static class Node {
        int idx, cost;

        Node(int idx, int cost) {
            this.idx = idx;
            this.cost = cost;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        graph = new ArrayList<ArrayList<Node>>();

        for (int i = 0; i < n + 1; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph.get(s).add(new Node(e, w));
        }

        int[] timeTravel = new int[n+1];

        for (int i = 1; i < n+1; i++) {
            int[] dist = new int[n + 1];
            int start = i;

            for (int j = 0; j < n + 1; j++) {
                dist[j] = Integer.MAX_VALUE;
            }
            dist[start] = 0;

            PriorityQueue<Node> q = new PriorityQueue<>((o1, o2) -> Integer.compare(o1.cost, o2.cost));
            q.offer(new Node(start, 0));


            while(!q.isEmpty()) {
                Node curNode = q.poll();
                if (start != x) {
                    if (curNode.idx == x) {
                        break;
                    }
                }

                if (dist[curNode.idx] < curNode.cost) {
                    continue;
                }

                for (int j = 0; j < graph.get(curNode.idx).size(); j++) {
                    Node nxtNode = graph.get(curNode.idx).get(j);

                    if (dist[nxtNode.idx] > curNode.cost + nxtNode.cost) {
                        dist[nxtNode.idx] = curNode.cost + nxtNode.cost;
                        q.offer(new Node(nxtNode.idx, dist[nxtNode.idx]));
                    }
                }
            }

            timeTravel[i] += dist[x];

            if (i == x) {
                for (int j = 1; j < n + 1; j++) {
                    timeTravel[j] += dist[j];
                }
            }
        }

        int result = 0;
        for (int i = 1; i < n+1; i++) {
            if (result < timeTravel[i]) {
                result = timeTravel[i];
            }
        }

        System.out.println(result);
    }
}