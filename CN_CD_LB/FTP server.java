import java.io.*;
import java.net.*;

public class FtpServer {
    public static void main(String[] args) throws Exception {
        ServerSocket server = new ServerSocket(5000);
        System.out.println("FTP Server started...");

        Socket socket = server.accept();
        System.out.println("Client connected!");

        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

        while (true) {
            String command = in.readLine();
            if (command == null) continue;

            if (command.startsWith("UPLOAD")) {
                String fileName = command.split(" ")[1];
                System.out.println("Receiving: " + fileName);

                FileOutputStream fos = new FileOutputStream(fileName);
                String line;
                while (!(line = in.readLine()).equals("EOF")) {
                    fos.write((line + "\n").getBytes());
                }
                fos.close();
                System.out.println("File saved.");
                out.println("UPLOAD DONE");
            }

            else if (command.startsWith("DOWNLOAD")) {
                String fileName = command.split(" ")[1];
                File file = new File(fileName);

                if (!file.exists()) {
                    out.println("NOT_FOUND");
                    continue;
                }

                BufferedReader fr = new BufferedReader(new FileReader(file));
                String line;
                while ((line = fr.readLine()) != null) {
                    out.println(line);
                }
                fr.close();
                out.println("EOF");
                System.out.println("File sent.");
            }

            else if (command.equals("EXIT")) {
                System.out.println("Client disconnected.");
                break;
            }
        }

        socket.close();
        server.close();
    }
}