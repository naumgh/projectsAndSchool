/*
 * Naum Hoffman
 * Thompson Rivers University
 * COMP3411_ASSIGNMENT 3
 * multi-threading matrix multiplication program using runnable
 * 
 */

import java.util.Arrays;
import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

class CreateMatrices {
    static int[][] m1;
    static int[][] m2;
    static int[][] res;

    static void print_arr(int[][] arr) {
        for (int x = 0; x < arr.length; x++) {
            for (int y = 0; y < arr[x].length; y++) {
                System.out.println("row " + x + " col " + y + " " + arr[x][y]);
            }
        }
    }

    static int[][] ret_matrices(int a, int b, int c, int x) {
        int max = 90; // PUT REQUESTED MAX INTEGER IN CELL VALUE HERE.
        Random rand = new Random();
        int[][] arr = new int[b][a];
        if (x == 0) {
            for (int row = 0; row < arr.length; row++) {
                for (int col = 0; col < arr[row].length; col++) {
                    arr[row][col] = rand.nextInt(max);
                }

            }

            return arr;
        } else {
            int[][] arr2 = new int[a][c];
            for (int row = 0; row < arr2.length; row++) {
                for (int col = 0; col < arr2[row].length; col++) {
                    arr2[row][col] = rand.nextInt(max);
                }

            }

            return arr2;
        }

    }

    public static void main(String args[]) {
        Random rand = new Random();
        System.out.println("creating matrices");
        int max = 6; // PUT REQUESTED MAX MATRIX VALUE HERE. CANT BE 0
        int a = rand.nextInt(max);
        int b = rand.nextInt(max);
        int c = rand.nextInt(max);

        if (a < 1) {
            while (a < 1) {
                a = rand.nextInt(max);
            }
        }
        if (b < 1) {
            while (b < 1) {
                b = rand.nextInt(max);
            }
        }
        if (c < 1) {
            while (c < 1) {
                c = rand.nextInt(max);
            }
        }

        for (int x = 0; x < 2; x++) {
            if (x == 0) {
                m1 = ret_matrices(a, b, c, x);

                printBeautifulResult(m1);
                System.out.println("\nDOT PRODUCT\n");
            } else {
                m2 = ret_matrices(a, b, c, x);

                printBeautifulResult(m2);
            }
        }
        res = new int[b][c];
        for (int f = 0; f < b; f++) {
            for (int g = 0; g < c; g++) {
                res[f][g] = Integer.MIN_VALUE;
            }
        }

        try {
            ExecutorService service = Executors.newFixedThreadPool(b * c);
            for (int r = 0; r <= b; r++) {
                for (int col1 = 0; col1 <= c; col1++) {
                    Future f = service.submit(new MultiThreading((b * r), r, col1, c, m1, m2, res));
                    f.get();
                }
            }

            System.out.println("we are printing resLUT");
            printBeautifulResult(res);
	    System.exit(0);
        } catch (Exception e) {
            System.out.println("ERROR IN CREATING THREAD");
        }

    }

    static void printBeautifulResult(int[][] res) {
        for (int[] row : res) {
            System.out.println(Arrays.toString(row));
        }
    }

}

class MultiThreading implements Runnable {

    private int MultiThreadingid;
    private int r;
    private int c;
    private int a;
    private int m1[][];
    private int m2[][];
    private int res[][];

    public MultiThreading(int id, int r, int c, int a, int[][] m1, int[][] m2, int[][] res) {
        this.MultiThreadingid = id;
        this.r = r;
        this.c = c;
        this.a = a;
        this.m1 = m1;
        this.m2 = m2;
        this.res = res;
    }

    @Override
    public void run() {
        try {
            // Thread.sleep(1000);
            multiplyMatrix.multiply(MultiThreadingid, r, c, a, m1, m2, res);
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}

class multiplyMatrix extends MultiThreading {
    public multiplyMatrix(int id, int r, int c, int a, int[][] m1, int[][] m2, int[][] res) {
        super(id, r, c, a, m1, m2, res);
    }

    static void multiply(int id, int r, int c, int a, int[][] m1, int[][] m2, int[][] res) {
        for (int common = 0; common < a + 2; common++) {
            try {
                 System.out.println(
                Thread.currentThread().getName() + "----" + id + " " + m1[r][common] + " " + m2[common][c]); 
                //IF YOU WANT TO SEE THE THREADS PRINTED IN CURRENT TIME,
                // INCOMMENT

                if (res[r][c] == Integer.MIN_VALUE) {
                    res[r][c] = m1[r][common] * m2[common][c];
                } else {
                    res[r][c] += m1[r][common] * m2[common][c];
                }
            } catch (ArrayIndexOutOfBoundsException e) {

            }

        }

    }
}
