import java.io.*;
import java.net.*;

public class ReceiverByte {
    public static void main(String[] args) throws IOException {
        
        // Opens a socket for connection
        ServerSocket servsock = new ServerSocket(45678);
        
        // Used to block until a client connects to the server
        Socket socket = servsock.accept();

        // Declaring I/O Streams
        DataInputStream dis = new DataInputStream(socket.getInputStream());
        DataOutputStream dos = new DataOutputStream(socket.getOutputStream());

        while (true) {
            String out = "";

            // Used to read the data sent by client
            String res = dis.readUTF();
            System.out.println("Message Received...Successfully!!!");
            System.out.println("The Stuffed Message is : " + res);

            for (int i = 1; i < res.length() - 1; i++) {
                if (res.charAt(i) == 'E') {

                    // Handle 'EE' -> 'E'
                    if (res.charAt(i + 1) == 'E') {
                        out = out + 'E';
                        i++; // Skip the next 'E'
                    }

                    // Handle 'EF' -> 'F'
                    else if (res.charAt(i + 1) == 'F') {
                        out = out + 'F';
                        i++; // Skip the next 'F'
                    }

                } else {
                    out = out + res.charAt(i);
                }
            }

            System.out.println("The Destuffed Message is : " + out);
            dos.writeUTF("success");

            String ch = dis.readUTF();
            if (ch.equals("bye")) {
                System.out.println("Messaging is over.....EXITING");
                break;
            }
        }

        // Closing all connections
        socket.close();
        dis.close();
        dos.close();
        servsock.close();
    }
}
