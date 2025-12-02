import java.io.*;
import java.net.*;
import java.util.Scanner;

public class FtpClient {
    public static void main(String[] args) throws Exception {
        Socket socket = new Socket("localhost", 5000);
        System.out.println("Connected to FTP Server.");

        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("\nEnter command (UPLOAD filename / DOWNLOAD filename / EXIT): ");
            String command = scanner.nextLine();
            out.println(command);

            if (command.startsWith("UPLOAD")) {
                String fileName = command.split(" ")[1];
                File file = new File(fileName);

                if (!file.exists()) {
                    System.out.println("File not found.");
                    continue;
                }

                BufferedReader fr = new BufferedReader(new FileReader(file));
                String line;
                while ((line = fr.readLine()) != null) {
                    out.println(line);
                }
                fr.close();
                out.println("EOF");
                System.out.println(in.readLine()); // Server confirmation
            }

            else if (command.startsWith("DOWNLOAD")) {
                String fileName = command.split(" ")[1];
                String line = in.readLine();

                if (line.equals("NOT_FOUND")) {
                    System.out.println("File not found on server.");
                    continue;
                }

                FileOutputStream fos = new FileOutputStream("Downloaded_" + fileName);
                while (!line.equals("EOF")) {
                    fos.write((line + "\n").getBytes());
                    line = in.readLine();
                }
                fos.close();
                System.out.println("File downloaded.");
            }

            else if (command.equals("EXIT")) {
                break;
            }
        }

        socket.close();
        scanner.close();
    }
}