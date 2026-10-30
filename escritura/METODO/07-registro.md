# 07. Registro: decisiones, bitácora y versiones

Un libro largo se pierde por lo que no se apuntó, no por lo que se escribió mal.

## `APUNTES.md`

Estructura mínima:

```
## 0. Punto de reanudación    ← lo primero que se lee al volver
## 1. Lo entendido
## 2. Puntos abiertos         ← numerados; no se cierran por defecto
## 3. Registro de decisiones  ← tabla con fecha; si no está aquí, no está decidido
## 4. Canon                   ← C-n
## 5. Cómo se consultan
```

### El registro de decisiones

| # | Punto | Decisión | Fecha | Notas |
|---|---|---|---|---|
| 1 | Voz | … | AAAA-MM-DD | … |

Reglas:

- **Si no está en la tabla, no está decidido.** No vale «lo hablamos».
- Cada fila lleva **fecha** y, si la decisión es parcial, la palabra **parcial** y qué falta.
- Las decisiones no se borran: se **precisan** en una fila nueva que cita la anterior.
- Una decisión puede reabrirse; se anota que se reabre y por qué. Reabrir no es fallar: es lo que
  evita que el libro herede un error de la sesión 3 durante 120 capítulos.
- Los números no se reciclan.

### El punto de reanudación

La primera sección de `APUNTES.md` responde, en una pantalla, a tres preguntas: dónde estamos, qué
se cerró, qué toca ahora. Se reescribe al cerrar cada sesión. Si alguien lee solo eso, debe poder
continuar.

## `BITACORA.md`

Una entrada por sesión, **al final**, de tres líneas:

1. qué se hizo;
2. qué se decidió (con el número de decisión);
3. qué queda para la próxima.

Nada de diario personal. La bitácora es el acta del trabajo, no del ánimo.

## `ESTRUCTURA.md`

Andamiaje y aritmética: partes, capítulos, bloques, anclajes, recuento real. La tabla de recuento la
escribe `nk contar --actualizar`; el resto se escribe a mano.

## Git

- Repositorio **local**, rama `main`, sin remoto mientras la obra no esté terminada.
- **Un commit por capítulo**, con el recuento real frente al presupuesto y la desviación.
- Otro commit al cerrar la sesión, con la entrada de la bitácora.
- Mensajes en inglés, sobrios, sin datos personales: algún día se publican.
- **Nada entra en el repositorio que no pueda publicarse.** Material de terceros, transcripciones
  sin depurar o datos sensibles van a una carpeta ignorada (`MATERIALES/`).
- Un repositorio local **no es un respaldo**. Copia fuera del disco, por sesión:

  ```
  bin/nk respaldo --destino /media/usb --etiqueta v29 --materiales MATERIALES
  ```

  Genera un bundle verificado, los materiales (si se piden) y un `SHA-256`, con nombre fechado.
  Se restaura con `git clone <bundle>` y no depende de ninguna herramienta del kit.

## Ficheros de apoyo

| Fichero | Qué guarda |
|---|---|
| `GLOSARIO.md` | Grafías fijas. `nk` lo usa para no marcar como nombre propio lo que ya está declarado. |
| `PERSONAS.md` | Fichas de quienes aparecen. Vacío hasta que el autor dé nombres. |
| `FUENTES.md` | Libro mayor: qué se consultó, para qué, con qué fecha y con qué nivel de fiabilidad. |
| `CRONOLOGIA.md` | El tiempo del mundo del libro, con grado de certeza. |
