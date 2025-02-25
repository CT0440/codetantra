package jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;


public class UpdateOperation {

	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		String url = "jdbc:mysql://localhost:3306/employees";
		String username = "root";
		String password = "root";
		
		Class.forName("com.mysql.cj.jdbc.Driver");
		
		Connection con = DriverManager.getConnection(url,username,password);
		
		String query = "update employees SET age = ? where name = ?";
		
		PreparedStatement pst = con.prepareStatement(query);
		
		pst.setInt(1, 56);
		pst.setString(2, "susruthi");
		
		int rowsEffected = pst.executeUpdate();
		System.out.println(rowsEffected+"row(s) updated");
		
		pst.close();
		con.close();

	}

}
