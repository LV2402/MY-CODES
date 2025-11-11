import java.net.*;
import java.util.Scanner;

public class UDPServer {
    public static void main(String[] args) {
        try {
            // Create a DatagramSocket to listen on port 12345
            DatagramSocket socket = new DatagramSocket(12345);

            byte[] receiveData = new byte[1024];
            byte[] sendData;

            Scanner scanner = new Scanner(System.in);

            System.out.println("UDP Server started. Waiting for client messages...");

            while (true) {

                // Receive packet from client
                DatagramPacket receivePacket =
                        new DatagramPacket(receiveData, receiveData.length);
                socket.receive(receivePacket);

                // Get the client's message
                String clientMessage =
                        new String(receivePacket.getData(), 0, receivePacket.getLength());

                System.out.println("Client: " + clientMessage);

                // Exit condition for server
                if (clientMessage.equalsIgnoreCase("exit")) {
                    System.out.println("Client closed connection. Server shutting down...");
                    break;
                }

                // Get server response from console
                System.out.print("Server (type your message): ");
                String serverMessage = scanner.nextLine();

                // Prepare response packet
                sendData = serverMessage.getBytes();
                InetAddress clientAddress = receivePacket.getAddress();
                int clientPort = receivePacket.getPort();

                DatagramPacket sendPacket =
                        new DatagramPacket(sendData, sendData.length, clientAddress, clientPort);

                // Send response to client
                socket.send(sendPacket);
            }

            socket.close();
            System.out.println("Server closed.");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
