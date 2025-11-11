import java.util.Scanner;

public class DijkstraRouting {

    static final int INF = 9999; // large value representing infinity

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of nodes: ");
        int n = sc.nextInt();

        int[][] graph = new int[n][n];

        System.out.println("Enter adjacency matrix (0 means no direct link):");

        // Input adjacency matrix and convert 0 (no edge) to INF except diagonal
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                graph[i][j] = sc.nextInt();
                if (graph[i][j] == 0 && i != j) {
                    graph[i][j] = INF;
                }
            }
        }

        // Run Dijkstra for each node
        for (int src = 0; src < n; src++) {
            dijkstra(graph, n, src);
        }

        sc.close();
    }

    // Dijkstra's algorithm
    static void dijkstra(int[][] graph, int n, int src) {

        int[] dist = new int[n];
        boolean[] visited = new boolean[n];
        int[] parent = new int[n];

        // Initialization
        for (int i = 0; i < n; i++) {
            dist[i] = INF;
            visited[i] = false;
            parent[i] = -1;
        }

        dist[src] = 0;

        // Dijkstra main loop
        for (int count = 0; count < n - 1; count++) {

            int u = minDistance(dist, visited, n);

            if (u == -1)
                break; // no reachable node left

            visited[u] = true;

            // Update distances of neighbors
            for (int v = 0; v < n; v++) {
                if (!visited[v] && graph[u][v] != INF &&
                        dist[u] != INF &&
                        dist[u] + graph[u][v] < dist[v]) {

                    dist[v] = dist[u] + graph[u][v];
                    parent[v] = u;
                }
            }
        }

        // Print routing table for this source node
        printRoutingTable(src, n, dist, parent);
    }

    // Returns index of node with minimum distance
    static int minDistance(int[] dist, boolean[] visited, int n) {
        int min = INF;
        int minIndex = -1;

        for (int i = 0; i < n; i++) {
            if (!visited[i] && dist[i] < min) {
                min = dist[i];
                minIndex = i;
            }
        }
        return minIndex;
    }

    // Prints routing table
    static void printRoutingTable(int src, int n, int[] dist, int[] parent) {
        System.out.println("\nRouting Table for Node " + src);
        System.out.println("Destination\tNextHop\tDistance");

        for (int i = 0; i < n; i++) {

            if (i == src) continue;

            int nextHop = findNextHop(src, i, parent);

            String nh = (nextHop == -1) ? "-" : Integer.toString(nextHop);
            String d = (dist[i] == INF) ? "INF" : Integer.toString(dist[i]);

            System.out.println(i + "\t\t" + nh + "\t\t" + d);
        }
    }

    // Finds the next hop from src to destination using the parent array
    static int findNextHop(int src, int dest, int[] parent) {
        if (dest == src) return src;
        if (parent[dest] == -1) return -1; // unreachable

        int hop = dest;

        while (parent[hop] != -1 && parent[hop] != src) {
            hop = parent[hop];
        }

        if (parent[hop] == -1) return -1;

        return hop;
    }
}
