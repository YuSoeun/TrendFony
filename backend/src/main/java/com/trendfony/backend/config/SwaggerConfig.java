package com.trendfony.backend.product.config;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Info;
import io.swagger.v3.oas.models.servers.Server;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.List;

@Configuration
public class SwaggerConfig {

    @Bean
    public OpenAPI customOpenAPI() {
        return new OpenAPI()
                .info(new Info()
                        .title("TrendFony API Documentation")
                        .version("1.0.0")
                        .description("API documentation for TrendFony backend."))
                .servers(List.of(
                        new Server().url("http://localhost:8080").description("Local Server")
                ));
    }
}