import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static int[][] graph;

    static class Node {
        int x;
        int y;
        int w;
        Node(int x, int y, int w) {
            this.x = x;
            this.y = y;
            this.w = w;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = 1;
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        PriorityQueue<Node> q = new PriorityQueue<Node>((o1, o2) -> Integer.compare(o1.w, o2.w)) ;

        while(true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());

            if (n == 0) {
                return;
            }
            graph = new int[n][n];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int[][] dist = new int[n][n];

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    dist[i][j] = Integer.MAX_VALUE;
                }
            }

            dist[0][0] = graph[0][0];
            q.add(new Node(0, 0, graph[0][0]));

            while(!q.isEmpty()) {
                Node curNode = q.poll();

                for (int i = 0; i < 4; i++) {
                    int nxtX = curNode.x+dx[i];
                    int nxtY = curNode.y+dy[i];

                    if(nxtX >= 0 && nxtX < n && nxtY >= 0 && nxtY < n) {
                        if (dist[nxtX][nxtY] > dist[curNode.x][curNode.y] + graph[nxtX][nxtY]) {
                            dist[nxtX][nxtY] = dist[curNode.x][curNode.y] + graph[nxtX][nxtY];
                            q.offer(new Node(nxtX, nxtY, dist[nxtX][nxtY]));
                        }
                    }
                }
            }

            // 5^6 2^12

            System.out.println("Problem " + num + ": " + dist[n-1][n-1]);

            num++;
        }
    }
}