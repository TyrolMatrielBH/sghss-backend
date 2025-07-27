package com.uninter.sghss.security;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.security.Keys;
import io.jsonwebtoken.SignatureAlgorithm;

import org.springframework.stereotype.Component;

import java.security.Key;
import java.util.Date;

@Component
public class JwtUtil {

    private final String SECRET_KEY = "uma-chave-muito-secreta-e-grande-para-seguranca12345"; // deve ser no mínimo 256 bits para HS256
    private final Key key = Keys.hmacShaKeyFor(SECRET_KEY.getBytes());

    public String gerarToken(String login) {
        return Jwts.builder()
                .setSubject(login)
                .setIssuedAt(new Date())
                .setExpiration(new Date(System.currentTimeMillis() + 86400000)) // 24 horas
                .signWith(key, SignatureAlgorithm.HS256)
                .compact();
    }

    public String extrairLogin(String token) {
        return getClaims(token).getSubject();
    }

    public boolean tokenValido(String token) {
        try {
            return !getClaims(token).getExpiration().before(new Date());
        } catch (Exception e) {
            return false;
        }
    }

    private Claims getClaims(String token) {
        return Jwts.parserBuilder()
                .setSigningKey(key)
                .build()
                .parseClaimsJws(token)
                .getBody();
    }
}
