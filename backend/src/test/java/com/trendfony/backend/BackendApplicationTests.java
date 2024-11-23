package com.trendfony.backend;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ActiveProfiles;

@SpringBootTest
@ActiveProfiles("test") // 테스트 환경 활성화
class BackendApplicationTests {

	@Test
	void contextLoads() {
		// 애플리케이션 컨텍스트 로딩 테스트
		System.out.println("Test context loads successfully!");
	}
}
