import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.h2.tools.Server;

import java.sql.SQLException;

@Configuration
public class H2ServerConfig {

	@Bean(initMethod = "start", destroyMethod = "stop")
	public Server H2DatabaseServer() throws SQLException {
		return Server.createTcpServer("-tcp", "-tcpAllowOthers", "-tcpPort", "9091");
	}
}