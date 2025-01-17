package jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class JDBCExample {

	public static void main(String[] args) throws ClassNotFoundException, SQLException{
		//1.register the Driver
		Class.forName("com.mysql.cj.jdbc.Driver");
		
		//2.Establish the connection
		Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/employees", "root", "root");
		System.out.println("Connection created");

		
	}

}
