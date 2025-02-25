package demo1;

import java.io.File;

public class fileProperty {

	public static void main(String[] args) {
		String fname = args[0];
		
		File f = new File(fname);
		
		System.out.println("FileName: "+f.getName());
		System.out.println("path: "+f.getPath());
		System.out.println("Absolute path: "+f.getAbsolutePath());
		System.out.println("getParent: "+f.getParent());
		System.out.println("FileExists: "+f.exists());
		System.out.println("File canWrite: "+f.canWrite());
		
		if (f.exists()) {
			System.out.println("canWrite(): "+f.canWrite());
			System.out.println("canRead(): "+f.canRead());
			System.out.println("canExecute() "+f.canExecute());
			System.out.println("length: "+f.length());
		}
		
	}

}
