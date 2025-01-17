package demo1;
import java.io.File;
import java.io.IOException;

public class F1 {

	public static void main(String[] args) {
		try {
			File obj = new File("src/demo1/myfile.txt");
			if(obj.createNewFile()) {
				System.out.println("File created: "+obj.getName());
			}
			else {
				System.out.println("File already Exists");
			}
			
		}catch(IOException e) {
			System.out.println("An error has occured");
			e.printStackTrace();
		}
	}

}
