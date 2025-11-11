import java.net.*;
import java.io.*;

public class TcpServer {

    public static void main(String arg[]) {

        ServerSocket s = null;
        String line;
        DataInputStream is = null, is1 = null;
        PrintStream os = null;
        Socket c = null;

        try {
            s = new ServerSocket(9222);
            System.out.println("Server started on port 9222...");
        } catch (IOException e) {
            System.out.println(e);
        }

        try {
            c = s.accept();
            System.out.println("Client connected!");

            is = new DataInputStream(c.getInputStream());
            is1 = new DataInputStream(System.in);
            os = new PrintStream(c.getOutputStream());

            do {
                line = is.readLine();  // Deprecated but retained as in original code
                System.out.println("Client: " + line);

                System.out.print("Server: ");
                line = is1.readLine();
                os.println(line);

            } while (!line.equalsIgnoreCase("quit"));

            is.close();
            os.close();
            c.close();
            s.close();

        } catch (IOException e) {
            System.out.println(e);
        }
    }
}
