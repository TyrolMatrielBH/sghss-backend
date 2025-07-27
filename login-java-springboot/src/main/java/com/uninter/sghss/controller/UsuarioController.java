package com.uninter.sghss.controller;

import com.uninter.sghss.dto.UsuarioRequest;
import com.uninter.sghss.model.Usuario;
import com.uninter.sghss.repository.UsuarioRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/usuarios")
public class UsuarioController {

    @Autowired
    private UsuarioRepository usuarioRepository;

    @PostMapping("/cadastrar")
    public ResponseEntity<String> cadastrarUsuario(@RequestBody UsuarioRequest usuarioRequest) {
        Usuario usuario = new Usuario();
        usuario.setLogin(usuarioRequest.getLogin());
        usuario.setSenha(usuarioRequest.getSenha());
        usuarioRepository.save(usuario);

        return ResponseEntity.ok("Usuário cadastrado com sucesso");
    }
}
