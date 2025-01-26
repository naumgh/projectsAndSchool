
/* 
 * Naum Hoffman
 * Thompson Rivers University
 * COMP3411_ASSIGNMENT 5
 * producer consumer problem
 * 
 */
import java.util.*;
import java.util.Arrays;
import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class Main {
    public static void main(String[] args) {
        Random rand = new Random();
        // int buffer_size = rand.nextInt(13);
        int buffer_size = 5; // change this size if you want bigger/smaller buffer
        int[] buffer = new int[buffer_size];
        // System.out.println(buffer[4]);

        // we need to define 2 threads, a producer and consumer....

        try {
            produceConsume p = new produceConsume();
            Thread t1 = new Thread(new Runnable() {
                @Override
                public void run() {
                    try {
                        p.produce(buffer, buffer_size);

                    } catch (Error e) {
                        System.out.println("unable to call produce");
                    }
                }
            });
            Thread t2 = new Thread(new Runnable() {
                @Override
                public void run() {
                    try {
                        p.consume(buffer, buffer_size);
                    } catch (Error e) {
                        System.out.println("unable to call consume");
                    }
                }
            });

            t1.start();
            t2.start();

            t1.join();
            t2.join();

        } catch (Exception E) {
            System.out.println("error in creating thread(s)");
        }

    }

}

class produceConsume extends Main {
    private int[] buffer;
    int count = 0;
    private int buffer_size;

    public void produce(int[] buffer, int buffer_size) {
        int max = 100;
        Random rand = new Random();
        // System.out.println(buffer_size);
        while (true) {
            synchronized (this) {
                int rand_int = rand.nextInt(max);
                if (count != buffer_size) {
                    buffer[count] = rand_int;
                    count++;
                    System.out.println("produced: " + rand_int + " " + count);
                    try {
                        Thread.sleep(1000);
                    } catch (Exception e) {

                    }
                } else {
                    try {
                        notify();
                        wait();
                    } catch (Exception e) {
                        // put all under new while loop cause if not we ruin in troublew
                    }
                }

            }
        }

    }

    public void consume(int[] buffer, int buffer_size) {
        while (true) {
            int x = -2;
            Random y = new Random();
            int z = y.nextInt(buffer_size);
            // System.out.println(z + "this is z");
            if (z == 0) {
                z += 1;
            }
            synchronized (this) {
                if (count != 0) {
                    // System.out.println(count);
                    x = buffer[count - 1];
                    count--;

                    // System.out.println(count);
                    System.out.println("consumed: " + x);

                    try {

                        Thread.sleep(1000);

                    } catch (Exception e) {

                    }

                } else {
                    try {
                        notify();
                        wait();
                    } catch (Exception e) {

                    }

                }
            }

        }

    }
}
