# Prompt — reanudar

Se pega al empezar una sesión, sustituyendo lo que va entre corchetes.

---

Vas a continuar una obra literaria que se escribe como archivo. Antes de tocar nada, lee en este
orden y no escribas todavía:

1. `APUNTES.md`, empezando por §0 (punto de reanudación), y luego §2 (puntos abiertos), §3
   (registro de decisiones) y §4 (canon).
2. `ESTRUCTURA.md`.
3. `README.md`.
4. La última entrada de `BITACORA.md`.

Después ejecuta:

```
bin/nk estado
bin/nk contar
```

Y contéstame, en diez líneas como máximo: dónde estamos, qué está cerrado, qué está abierto, cuál
es el siguiente capítulo y cuál es el siguiente paso exacto. **No escribas en `MANUSCRITO/`** hasta
que yo lo diga.

Reglas que rigen toda la sesión:

- Si no está en el registro de decisiones de `APUNTES.md`, no está decidido. No lo inventes.
- No contradigas el canon (§4) sin anotarlo como precisión, con fecha.
- La desviación de palabras se anota, no se compensa.
- Antes de dar un capítulo por escrito: `bin/nk verificar --rubrica`.
- Al acabar: `bin/nk informe`, una entrada de tres líneas en `BITACORA.md` y un commit.
