package jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class ReadOperation {

	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		String url = "jdbc:mysql://localhost:3306/employees";
		String username = "root";
		String password = "root";
		
		Class.forName("com.mysql.cj.jdbc.Driver");
		
		Connection con = DriverManager.getConnection(url, username, password);
		
		String query = "select * from employees"; 
		
		PreparedStatement pst = con.prepareStatement(query);
		
		ResultSet rs = pst.executeQuery();
		
		while(rs.next()) {
			String name = rs.getString("name");
			int age = rs.getInt("age");
			System.out.println("name: "+name+" age: "+age);
			
		}
		
		rs.close();
		pst.close();
		con.close();
	}

}
