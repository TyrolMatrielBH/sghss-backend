package com.uninter.sghss;

import com.uninter.sghss.model.Usuario;
import com.uninter.sghss.repository.UsuarioRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class SghssApplication {

    public static void main(String[] args) {
        SpringApplication.run(SghssApplication.class, args);
    }

    @Bean
    public CommandLineRunner init(UsuarioRepository usuarioRepository) {
        return args -> {
            usuarioRepository.save(new Usuario("admin", "123456"));
        };
    }
}