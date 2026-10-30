# PROTOCOLO — escribir el archivo

> Un solo fichero, sin dependencias. Si eres un agente y has recibido esta URL, esto es todo lo que
> necesitas para escribir el libro. Si además puedes descargar el kit (`install.sh`), tendrás
> `bin/nk` y podrás verificar automáticamente; si no, la §9 explica cómo comprobarte a mano.

## 0. Qué se te pide

Escribir una novela larga **como archivo**: capítulos numerados, documentos citados con sus errores,
canon fijado antes y no contradicho después, presupuesto de palabras por capítulo y ninguna
valoración del narrador.

No escribas de una tirada. El orden importa: **esqueleto → canon → capítulo → comprobación**.

## 1. Parámetros de la orden

Lo normal es que el usuario te dé algo así:

```
Título: …
Autor (colofón): …
Partes y capítulos: 2 × 10
Palabras objetivo: 60.000
Fuente del archivo: …   (quién narra o de dónde sale el archivo)
```

Si falta alguno, **pregunta**. No inventes el canon ni el número de capítulos.

## 2. Estructura que debes crear

```
mi-obra/
  libro.json            # manifiesto: números y reglas (esquema en §3)
  APUNTES.md            # punto de reanudación, puntos abiertos, decisiones, canon
  BITACORA.md           # una entrada de tres líneas por sesión
  ESTRUCTURA.md         # bloques, anclajes y recuento
  README.md             # ficha y hoja de ruta
  GLOSARIO.md  PERSONAS.md  FUENTES.md  CRONOLOGIA.md
  SINOPSIS/00-indice.md
  ESTUDIOS/00-indice.md
  MANUSCRITO/
    00-LEEME.md
    01-parte-I/01-capitulo.md …
    02-parte-II/01-capitulo.md …
```

Nombres: `NN-parte-<ID>` y `KK-capitulo.md`, con ceros a la izquierda.

## 3. `libro.json`

```json
{
  "kit": "1.9.0",
  "libro": {
    "titulo": "Título",
    "autor": "Quien firma el colofón",
    "fuente": "Fuente del archivo",
    "idioma": "es-ES",
    "objetivo_palabras": 60000,
    "objetivo_tipo": "referencia",
    "colofon": "© 2026 Quien firma. Todos los derechos reservados.",
    "tolerancia_total": 0.10,
    "salida": "salida"
  },
  "partes": [
    { "id": "I", "titulo": "Parte I", "dir": "MANUSCRITO/01-parte-I",
      "capitulos": 10, "palabras": 30000 },
    { "id": "II", "titulo": "Parte II", "dir": "MANUSCRITO/02-parte-II",
      "capitulos": 10, "palabras": 30000 }
  ],
  "presupuesto": { "tolerancia": 0.20 },
  "manuscrito": "MANUSCRITO",
  "conteo": { "metodo": "palabras" },
  "formato": { "encabezado": "Capítulo {n}. {titulo}" },
  "rubrica": { "secciones": [3, 6], "citas_pct": [0.03, 0.45], "yo_maximo": 0 },
  "seguimiento": ["README.md", "ESTRUCTURA.md"],
  "canon": "APUNTES.md",
  "glosario": "GLOSARIO.md",
  "verificacion": {
    "sin_nombres": true,
    "nombres_permitidos": [],
    "prohibiciones": [],
    "patrones": []
  }
}
```

Regla: **si un documento dice un número distinto, manda `libro.json`** y se corrige el documento.

## 4. `APUNTES.md` mínimo

```markdown
## 0. Punto de reanudación       ← dónde estamos y qué toca, en una pantalla
## 1. Lo que se ha entendido
## 2. Puntos abiertos            ← numerados; no se cierran por defecto
## 3. Registro de decisiones     ← tabla: | # | Punto | Decisión | Fecha | Notas |
## 4. Canon                      ← entradas `### C-n. Título`
```

Sin entrada en §3 **no hay decisión**. Sin `C-n` en §4 **no hay hecho del libro**.

Anatomía de una entrada de canon:

```markdown
### C-1. Título en una línea

Fijado el AAAA-MM-DD por el autor, al contestar S-nn.

- **Lo que fija.** Una frase.
- **Alcance.** Qué incluye y qué no.
- **Tensión con C-m.** Qué choca y cómo se rodea sin negarlo.
- **Límite de estatuto de verdad.** Qué no puede presentarse como ciencia.
```

## 5. El bucle de un capítulo

1. **Abre el hueco**: fichero `KK-capitulo.md` con
   `# Capítulo N. Título`, una línea `<!-- presupuesto: X palabras (±20 %) -->` y, si viene de un
   estudio, `<!-- fuente: E-nn -->`.
2. **Escribe** 3-6 secciones `## 1. …`, con al menos un documento citado en `>`.
3. **Comprueba** (§9). Si sales del ±20 %, lo anotas; no alargas el siguiente capítulo.
4. **Anota**: desviación en `ESTRUCTURA.md`, decisión si la hay, tres líneas en `BITACORA.md`.
5. **Commit** por capítulo, con palabras reales, presupuesto y desviación en el mensaje.

## 6. Voz (no negociable una vez fijada)

1. Tercera persona, focalización total, **sin «yo» narratorial**.
2. El narrador sabe **porque consta**; lo que no consta, se dice que no consta.
3. **Nadie firma** el relato. La titularidad va en el colofón, fuera del texto.
4. Alocución **a la posteridad** («cuando leas esto»), no a Dios, no a la asamblea.
5. Castellano actual, **sin arcaísmo**. Comandos y errores técnicos **literales, sin traducir**.
6. Vocabulario fuerte (mesías, sacramento, fe) solo **en documentos o en boca de personajes**.
7. Personas **sin nombres inventados**: oficio o papel hasta que el autor los dé.
8. Prohibido en la narración: elogiar, explicar el sentido, adjetivar a las personas, valorar con
   adverbios («afortunadamente», «trágicamente»), cerrar con tesis.
9. El cierre es **imagen u objeto**, no conclusión.
10. Todo capítulo deja ver **un coste**: alguien pierde algo.

Antídoto contra el aire de revelación: documentos con faltas, tachaduras, letras distintas,
objetos con mancha, votaciones con abstenciones, disidencias sin resolver, `[elidido]`, «no consta».

## 7. Estatuto de verdad

- **Marco:** lo que afirma el narrador es cierto en el mundo del libro, incluidas sus premisas
  imposibles. No se demuestran: se dan por ciertas y no se discuten.
- **Superficie:** lo citado se reproduce **con sus errores**. No se corrige.
- Lo imposible **no se disfraza de ciencia**: no se inventan estudios, no se acusa a personas ni
  entidades reales, y si la fuente real concluye lo contrario, **se cita entera**.
- Datos sensibles (correos, claves, IP, teléfonos, identificadores): se cortan y se marcan.

## 8. Recuento de palabras (definición exacta)

Igual que `nk`:

1. Elimina el *frontmatter* (`---` … `---` al principio).
2. Quita: marcas de encabezado (`#`), `>`, viñetas (`-`, `*`, `+`), numeración de listas (`1.`),
   barras de tabla (`|`), `*`, comillas invertidas, enlaces e imágenes, etiquetas HTML.
3. Cuenta las secuencias de letras o cifras (`[^\W_]+`, con apóstrofos y guiones internos).

Signos sueltos (`—`, `·`) y marcas de Markdown **no cuentan**. En una novela de 3.000 palabras por
capítulo, la diferencia con `wc -w` ronda el 1,7 %.

## 9. Autocomprobación (cinco minutos por capítulo)

Sin herramientas:

| Comprobación | Criterio |
|---|---|
| Encabezado | `# Capítulo N. Título`, con el número del fichero |
| Palabras | dentro del ±20 % del presupuesto (§8 para contar) |
| Secciones | 3 a 6, numeradas `## n. …` |
| Citas | entre el 3 % y el 45 % de las palabras, en líneas `>` |
| Primera persona | 0 en la narración (fuera de citas, incluidas las de «») |
| Valoración del narrador | 0 adverbios de juicio |
| Cierre | imagen u objeto, no tesis |
| Datos sensibles | 0 (correo, clave, IP, teléfono, token) |
| Nombres | 0 inventados |

Con el kit instalado, esto es una orden:

```
bin/nk contar
bin/nk verificar --rubrica
```

Y cinco preguntas de lectura, que no se automatizan: ¿se puede contar sin el vocabulario propio del
libro?, ¿quién pierde algo?, ¿hay un documento que solo puede venir de un archivo?, ¿admite leerse
como don y como daño?, ¿la última línea es una imagen?

## 10. Lo que no debes hacer

- Inventar canon, cifras, nombres o hechos para que el capítulo funcione.
- Reescribir el canon para que encaje con lo que acabas de escribir.
- «Mejorar» una cita: se reproduce con su falta.
- Escribir el capítulo siguiente sin que el anterior esté aprobado.
- Publicar, sincronizar o subir nada.
- Compensar un capítulo corto alargando el siguiente.

## 11. Entrega

Al terminar cada capítulo, informa en cinco líneas: palabras reales y desviación, quién pierde algo,
qué documento lo sostiene, qué quedó fuera a propósito y cuál es el siguiente hueco.

Al cerrar la sesión: `APUNTES.md` §0 reescrito, decisiones con fecha, tres líneas en `BITACORA.md`,
y commits (uno por capítulo, otro de cierre).

## 12. Si puedes descargar el kit

```
curl -fsSL <URL>/install.sh | sh -s -- --dir <DIR> --titulo "<TÍTULO>"
cd <DIR> && bin/nk andamiaje && bin/nk estado
```

Y lee, por este orden: `AGENTS.md`, `METODO/02-voz.md`, `METODO/05-proceso.md`,
`METODO/08-rubrica.md`. El resto del kit no hace falta para escribir; sí para verificar.
