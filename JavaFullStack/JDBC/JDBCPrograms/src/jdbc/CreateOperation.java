package jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class CreateOperation {

	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		// TODO Auto-generated method stub
		String url = "jdbc:mysql://localhost:3306/employees";
		String username = "root";
		String password = "root";
		
		//1.Load ClassName
		Class.forName("com.mysql.cj.jdbc.Driver");
		
		//2.Establish the COnnection
		Connection con = DriverManager.getConnection(url, username, password);
		
		//3.create a query
		String query = "insert into employees (name, age) values (?, ?)";
		
		//4.Create a preparedStatement
		PreparedStatement pst = con.prepareStatement(query);
		pst.setString(1, "Gangadhar");
		pst.setInt(2, 21);
		
		//5.Execute the update
		int rowsEffected = pst.executeUpdate();
		System.out.print(rowsEffected+"row(s) inserted");
		
		pst.close();
		con.close();

	}

}
