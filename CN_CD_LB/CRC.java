import java.util.Scanner;

class CRC {

    public static void main(String args[]) {

        Scanner scan = new Scanner(System.in);

        // Accept input data bits
        System.out.println("Enter the size of the data:");
        int dataSize = scan.nextInt();

        int data[] = new int[dataSize];

        System.out.println("Enter the data bits (0 or 1):");
        for (int i = 0; i < dataSize; i++) {
            System.out.print("Enter bit number " + (i + 1) + ": ");
            data[i] = scan.nextInt();
        }

        // Accept divisor bits
        System.out.println("Enter the size of the divisor:");
        int divisorSize = scan.nextInt();

        int divisor[] = new int[divisorSize];

        System.out.println("Enter the divisor bits (0 or 1):");
        for (int i = 0; i < divisorSize; i++) {
            System.out.print("Enter bit number " + (i + 1) + ": ");
            divisor[i] = scan.nextInt();
        }

        // Perform division to get the remainder
        int[] remainder = divide(data, divisor);

        // Display the CRC code (data + remainder)
        System.out.println("\nThe CRC code generated is:");
        for (int i = 0; i < data.length; i++) {
            System.out.print(data[i]);
        }
        for (int i = 0; i < remainder.length - 1; i++) {
            System.out.print(remainder[i]);
        }
        System.out.println();

        // Create simulated sent data (data + CRC remainder)
        int[] sentData = new int[data.length + remainder.length - 1];

        System.arraycopy(data, 0, sentData, 0, data.length);
        System.arraycopy(remainder, 0, sentData, data.length, remainder.length - 1);

        System.out.println("Simulated sent data:");
        for (int i = 0; i < sentData.length; i++) {
            System.out.print(sentData[i]);
        }
        System.out.println();

        // Check received data for errors
        receive(sentData, divisor);

    }

    // Performs polynomial division (CRC generation and checking)
    static int[] divide(int[] oldData, int[] divisor) {

        int[] data = new int[oldData.length + divisor.length - 1];
        System.arraycopy(oldData, 0, data, 0, oldData.length);

        for (int i = 0; i < oldData.length; i++) {

            if (data[i] == 1) {
                for (int j = 0; j < divisor.length; j++) {
                    data[i + j] ^= divisor[j];  // XOR operation
                }
            }
        }

        int[] remainder = new int[divisor.length];

        System.arraycopy(
                data, 
                data.length - divisor.length + 1,
                remainder, 
                0, 
                divisor.length - 1
        );

        return remainder;
    }

    // Checks received data for errors
    static void receive(int[] data, int[] divisor) {

        int[] remainder = divide(data, divisor);

        // Check for errors
        boolean hasError = false;

        for (int bit : remainder) {
            if (bit != 0) {
                hasError = true;
                break;
            }
        }

        if (hasError) {
            System.out.println("There is an error in received data.");
        } else {
            System.out.println("Data was received without any error.");
        }
    }
}