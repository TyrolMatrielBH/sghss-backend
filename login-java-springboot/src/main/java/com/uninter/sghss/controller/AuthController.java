package com.uninter.sghss.controller;

import com.uninter.sghss.dto.LoginRequest;
import com.uninter.sghss.dto.TokenResponse;
import com.uninter.sghss.model.Usuario;
import com.uninter.sghss.repository.UsuarioRepository;
import com.uninter.sghss.security.JwtUtil;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
@RequestMapping("/auth")
public class AuthController {

    @Autowired
    private UsuarioRepository usuarioRepository;

    @Autowired
    private JwtUtil jwtUtil;

    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestBody LoginRequest loginRequest) {
        Optional<Usuario> usuarioOpt = usuarioRepository.findByLogin(loginRequest.getLogin());

        if (usuarioOpt.isEmpty() || !usuarioOpt.get().getSenha().equals(loginRequest.getSenha())) {
            return ResponseEntity.status(401).body("Credenciais inválidas");
        }

        Usuario usuario = usuarioOpt.get();
        String token = jwtUtil.gerarToken(usuario.getLogin());

        return ResponseEntity.ok(new TokenResponse(token));
    }
}
