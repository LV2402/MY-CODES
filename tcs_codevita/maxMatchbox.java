import java.util.*;

public class maxMatchbox {
    public static void main(String[] args) {
        Scanner vamshi_sc = new Scanner(System.in);
        int vamshi_n = vamshi_sc.nextInt();
        double[] vamshi_x = new double[vamshi_n];
        double[] vamshi_y = new double[vamshi_n];

        for (int vamshi_i = 0; vamshi_i < vamshi_n; vamshi_i++) {
            vamshi_x[vamshi_i] = vamshi_sc.nextDouble();
            vamshi_y[vamshi_i] = vamshi_sc.nextDouble();
        }

        double vamshi_per = 0.0;
        double[] vamshi_len = new double[vamshi_n];

        for (int vamshi_i = 0; vamshi_i < vamshi_n; vamshi_i++) {
            int vamshi_j = (vamshi_i + 1) % vamshi_n;
            double vamshi_L = Math.abs(vamshi_x[vamshi_i] - vamshi_x[vamshi_j]) 
                             + Math.abs(vamshi_y[vamshi_i] - vamshi_y[vamshi_j]);
            vamshi_len[vamshi_i] = vamshi_L;
            vamshi_per += vamshi_L;
        }

        double vamshi_A0 = vamshi_area(vamshi_x, vamshi_y, vamshi_n);
        double vamshi_best = 0.0;

        for (int vamshi_k = 0; vamshi_k <= 1000; vamshi_k++) {
            double vamshi_H = vamshi_k / 10.0;
            boolean vamshi_bad = false;

            for (int vamshi_i = 0; vamshi_i < vamshi_n; vamshi_i++) {
                if (vamshi_len[vamshi_i] - 2 * vamshi_H < 0.1 - 1e-12) {
                    vamshi_bad = true;
                    break;
                }
            }
            if (vamshi_bad) break;

            double vamshi_A = vamshi_A0 - vamshi_per * vamshi_H + 4.0 * vamshi_H * vamshi_H;
            if (vamshi_A <= 0) break;

            double vamshi_V = vamshi_A * vamshi_H;
            if (vamshi_V > vamshi_best) vamshi_best = vamshi_V;
        }

        System.out.printf("%.2f", vamshi_best);
    }

    static double vamshi_area(double[] vamshi_x, double[] vamshi_y, int vamshi_n) {
        double vamshi_s = 0.0;
        for (int vamshi_i = 0; vamshi_i < vamshi_n; vamshi_i++) {
            int vamshi_j = (vamshi_i + 1) % vamshi_n;
            vamshi_s += vamshi_x[vamshi_i] * vamshi_y[vamshi_j] 
                       - vamshi_x[vamshi_j] * vamshi_y[vamshi_i];
        }
        return Math.abs(vamshi_s) / 2.0;
    }
}
