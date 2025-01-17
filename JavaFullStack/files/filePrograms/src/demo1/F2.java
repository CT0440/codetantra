package demo1;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class F2 {

    public static void main(String[] args) {
        // Declare the file object here to make it accessible throughout the method
        File obj = new File("myfile1.txt");

        try {
            // Attempt to create the file
            if (obj.createNewFile()) {
                System.out.println("File created: " + obj.getName());
            } else {
                System.out.println("File already exists.");
            }

            // Write to the file
            try (FileWriter writer = new FileWriter(obj)) {
                writer.write("This is a write file.");
                System.out.println("Successfully written to the file.");
            }

            // Read the file
            try (Scanner reader = new Scanner(obj)) {
                System.out.println("File contents:");
                while (reader.hasNextLine()) {
                    System.out.println(reader.nextLine());
                }
            }

        } catch (IOException e) {
            System.out.println("An error occurred: " + e.getMessage());
            e.printStackTrace();
        }

        // Delete the file
        if (obj.exists() && obj.delete()) {
            System.out.println("The deleted file is: " + obj.getName());
        } else {
            System.out.println("Failed to delete the file.");
        }
    }
}
