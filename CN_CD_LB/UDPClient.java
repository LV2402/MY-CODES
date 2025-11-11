import java.net.*;
import java.util.Scanner;

public class UDPClient {
    public static void main(String[] args) {
        try {
            // Create a DatagramSocket
            DatagramSocket socket = new DatagramSocket();
            InetAddress serverAddress = InetAddress.getByName("localhost");
            int serverPort = 12345;

            byte[] sendData;
            byte[] receiveData = new byte[1024];

            Scanner scanner = new Scanner(System.in);

            System.out.println("UDP Client started. Type your messages (type 'exit' to quit):");

            while (true) {

                // Get user input
                System.out.print("Client (type your message): ");
                String message = scanner.nextLine();

                // Exit condition
                if (message.equalsIgnoreCase("exit")) {
                    socket.close();
                    System.out.println("Client closed.");
                    break;
                }

                // Send message to server
                sendData = message.getBytes();
                DatagramPacket sendPacket =
                        new DatagramPacket(sendData, sendData.length, serverAddress, serverPort);
                socket.send(sendPacket);

                // Receive response from server
                DatagramPacket receivePacket =
                        new DatagramPacket(receiveData, receiveData.length);
                socket.receive(receivePacket);

                String serverMessage =
                        new String(receivePacket.getData(), 0, receivePacket.getLength());
                System.out.println("Server: " + serverMessage);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
