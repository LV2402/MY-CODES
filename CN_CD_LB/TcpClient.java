import java.net.*;
import java.io.*;

public class TcpClient {

    public static void main(String arg[]) {

        Socket c = null;
        String line;
        DataInputStream is, is1;
        PrintStream os;

        try {
            c = new Socket("127.0.0.1", 9222);
            System.out.println("Connected to server!");
        } 
        catch (IOException e) {
            System.out.println(e);
        }

        try {
            os = new PrintStream(c.getOutputStream());
            is = new DataInputStream(System.in);
            is1 = new DataInputStream(c.getInputStream());

            do {
                System.out.println("Client:");
                line = is.readLine();  // deprecated but used as in original code

                os.println(line);

                System.out.println("Server: " + is1.readLine());

            } while (!line.equalsIgnoreCase("quit"));

            is1.close();
            os.close();
            c.close();

        } catch (IOException e) {
            System.out.println("Socket Closed! Message Passing is over");
        }
    }
}
