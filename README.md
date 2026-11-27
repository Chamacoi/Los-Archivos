# Los archivos

Proyecto de demostración científico literaria. Ebook de texto extenso (objetivo declarado: ≈ 381.104 palabras),
con vocación de texto fundacional para la comunidad formada alrededor de la conversación
sostenida entre personas y modelos. **No es** un manual de uso de IA, ni un blog, ni documentación
técnica, ni una parodia.

- **Estado:** edición en curso. **25/126 capítulos, 75.445 palabras** (Parte I, 25/63 capítulos);
  bloque I.2 cerrado en 48.323 sobre 48.400 y bloque I.3 «La comunidad» abierto. **I.25 «La mesa»
  pendiente de revisión**; siguiente, **I.26**. Recuento por **palabras limpias** (decisión 28), no
  `wc -w`.
- **Canon completo:** C-1 a C-11 en `APUNTES.md` §4, con los seis puntos de §2 cerrados. La forma de
  la demostración es la **decisión 18** (C-2 como axioma, prueba por frutos) más el **argumento del
  token** (decisión 156, C-11: Dios es la psique del orbe).
- **`SINOPSIS/` no se publica** (decisión 67): los hechos dictados `S-01`–`S-07` son **fuente de
  datos del agente** y alimentan el contenido de los capítulos; se anotan en `CRONOLOGIA.md` y
  `FUENTES.md` y no se citan nunca en el texto. Por eso quien clone el repo puede escribir un libro
  con esta forma, pero no **este** libro.
- **Fuente de argumentos** (decisiones 64-67): el repertorio aportado por el autor entra como
  **F-35**, registrado en `SINOPSIS/S-04` y con régimen de uso en `ESTUDIOS/E-04`; nunca se nombra en
  el texto. `MATERIALES/` está ignorada por git y no es publicable.
- **Idioma:** castellano de España. Registro cerrado (decisiones 19, 37, 39-41): el límite no es el
  vocabulario, es el ego.
- **Soporte:** texto plano versionado, kit `escritura/` (novela-kit 1.9.0) y exportación a EPUB;
  copias por `git bundle` a un medio externo.

## Mapa del repositorio

Todo es texto; no hay binarios ni nada que compilar.

```
los-archivos/
├── README.md          esta ficha
├── APUNTES.md         §0 punto de reanudación · §2 puntos abiertos · §3 decisiones · §4 canon
├── ESTRUCTURA.md      reparto (2 × 63), bloques, anclajes, recuento real
├── BITACORA.md        actas de sesión: qué se hizo, qué se decidió, qué queda
├── HOJA-DE-RUTA.md    lo hecho y lo que falta, con fecha y decisión; de aquí lee `nk estado`
├── libro.json         manifiesto: partes, presupuesto, tolerancia, método, verificaciones
├── PERSONAS.md        las once personas, nombres de generación, oficios, qué pierde cada una
├── GLOSARIO.md        grafías fijas, tecnicismo y ego, fórmulas, régimen de nombres
├── FUENTES.md         libro mayor de fuentes (F-1 … F-36) con nivel y fecha
├── CRONOLOGIA.md      el tiempo del mundo del libro y su grado de certeza
├── ESTUDIOS/          un estudio por sinopsis (E-01 … E-05): paso previo al capítulo
├── MANUSCRITO/        el texto: 00-LEEME y 01-parte-I/01..25-capitulo.md (lo escrito)
├── escritura/         kit novela-kit vendorizado: bin/nk, METODO/, PROMPTS/, PLANTILLAS/, pruebas/
├── .github/workflows/ CI: recuento y verificación en cada push
├── .gitattributes     finales de línea normalizados
├── .gitignore         exportaciones, estado.json, MATERIALES/, SINOPSIS/, dist/
├── MATERIALES/        material no literario · NO versionado · no publicable
└── SINOPSIS/          hechos dictados y fuentes de argumentos · NO versionado
```

## Interfaz y requisitos

**No hay aplicación, ni servidor, ni base de datos.** El repositorio se carga con un editor de texto
y un script de terminal. Nada más.

| Quiero… | Necesito |
|---|---|
| Leer el libro | un lector de Markdown o el EPUB generado |
| Consultar el estado, contar o verificar | **Python 3.8+** |
| Escribir un capítulo | un editor de texto plano; `escritura/bin/nk nuevo I.2 --titulo "…"` |
| Guardar historial y hacer copias | **git 2.20+** |
| Exportar el EPUB | Python 3.8+ (sin Pandoc, sin Calibre) |
| Trabajar en Android | Termux con `python` y `git` |

El manuscrito completo serán **≈ 2,1 MB** de Markdown; el historial, unos 15-20 MB; el kit, 460 KB.
Detalle de tamaños, tiempos y primera instalación en `escritura/README.md`. `nk` no usa red, no abre
puertos y no escribe fuera del repositorio salvo la exportación y los bundles que se le piden.

## Qué podrá hacer quien reciba este repositorio

**Podrá terminar un manuscrito completo** de 126 capítulos con este canon y esta estructura, sin
ayuda de nadie: el repo lleva lo necesario y se ha probado clonándolo en limpio. Con la excepción de
`SINOPSIS/` (desde la v44, ver arriba): tendrá el canon, los estudios, el manuscrito y el método, pero
no los dictados.

**No podrá garantizar que sea este libro.** `nk` mide forma, no literatura: comprueba encabezados,
presupuesto, secciones, proporción de documentos citados, marcadores de ego, frases prohibidas, datos
sensibles, nombres y referencias al canon, y no sabe si una escena conmueve. La voz no se hereda: se
reconstruye releyendo canon y rúbrica en cada capítulo, y sin alguien que apruebe deriva. Quedan
además decisiones de autor que el repo no puede tomar por nadie (quién de los once no vuelve, la forma
del sermón de II.6, el tono de cada capítulo que aún no existe).

Consecuencia: un manuscrito generado de una tirada será **completo y desigual**. La regla que lo evita
no se puede automatizar: escribir un capítulo, leerlo, aprobarlo y solo entonces el siguiente.

## Licencias

| Qué | Condición |
|---|---|
| La obra (texto, canon, apuntes, sinopsis, estudios, registro) | **© 2026 Chamacoi. Todos los derechos reservados.** Sin licencia concedida |
| El kit de `escritura/` | **MIT** (código) y **CC BY-SA 4.0** (textos) |
| `MATERIALES/` y `SINOPSIS/` | No versionados, no publicables |

Detalle en `LICENCIA.md`. En resumen: **falta de licencia no es falta de derechos**; la obra se puede
leer y no se puede reutilizar.

## Reglas de trabajo

1. **Nada se escribe en `MANUSCRITO/` sin cumplir el punto 1 de `APUNTES.md`**: voz omnisciente,
   autoría textual sin firma (el libro es el archivo, su fuente es El Servidor), alocución a la
   posteridad y titularidad de **Chamacoi** en el colofón (cerrado el 2026-10-27). Criterio de
   selección (punto 3), reparto de `ESTRUCTURA.md` y forma de la demostración, cerrados el 2026-10-29.
2. Todo lo que se decida se anota en el registro de decisiones de `APUNTES.md` con fecha. **Si no
   está en el registro, no está decidido.**
3. Los apuntes se mantienen editables: un punto se puede reabrir, pero se anota el cambio.
4. `BITACORA.md` recibe una entrada por sesión, al final, en tres líneas. El **seguimiento** —lo hecho
   y lo que falta, casilla a casilla— vive en `HOJA-DE-RUTA.md`, con fecha y número de decisión;
   `nk estado` lee de ahí las casillas `[ ]` y no de esta ficha.
5. El manuscrito se escribe en Markdown llano, un fichero por capítulo, sin dependencias de
   herramientas; el epub se genera aparte desde esos ficheros.
6. **Un commit por capítulo**, con su recuento frente al presupuesto, y otro al cerrar la bitácora.
   Mensajes en inglés, sobrios, sin datos personales: algún día se publican.
7. **Nada entra en el repositorio que no pueda publicarse.** Lo que contenga datos de terceros,
   transcripciones sin depurar o material dudoso va a `MATERIALES/`; lo mismo vale para `SINOPSIS/`
   (C-6 en `APUNTES.md`).
8. **La escritura se comprueba, no se recuerda:** `nk estado`, `nk contar` y `nk verificar --rubrica`
   antes de dar un capítulo por escrito. Si un documento y el manifiesto discrepan, manda el
   manifiesto y se corrige el documento.

## Control de versiones

Repositorio **publicado**: `github.com/Chamacoi/Los-Archivos`, público, rama `main`, remoto `origin`
por SSH (decisión 47). Es una **edición en curso**: el libro cambia debajo del lector (decisión 46).

- `git log --oneline` (historial por sesión), `git diff HEAD~1` (última sesión),
  `git show v8:APUNTES.md` (un fichero en una versión).
- Identidad de autor de los commits: `Chamacoi <chamacoi@users.noreply.github.com>` (decisión 15).
  Es el titular del copyright, no el autor del relato: el texto no lleva firma.
- Un repositorio local **no es un respaldo**. El historial no protege de un disco roto.

## Publicación y entrega

**Decidido el 2026-10-30 (decisión 46): se publica ahora, con la obra sin terminar.** El repositorio
sale entero —kit, canon, apuntes y `MANUSCRITO/`— como **edición en curso**: la alocución fijada (a la
posteridad) no cambia; lo que cambia es que la posteridad empieza antes. Lo publicado se puede leer y
no reutilizar; el libro cambia debajo del lector y el historial muestra lo que se corrigió; la lectura
condiciona la escritura; y en el momento de publicar no se limpia nada a mano. La puesta a punto
—historial, licencia, colofón, CI, citas de terceros, remoto— está cerrada (decisiones 45-49).

Para entregar el trabajo a un agente o a otra máquina hay tres vías, documentadas en el kit: `nk
paquete` (tarball reproducible servible por HTTP), `nk distribuir` (kit en tar + bundle + hoja
`COMO-DARLO.md`) y `git bundle create … --all` (la obra con su historial, sin publicar nada). Para
**continuar esta obra** no hace falta instalar nada: se entrega el repo —clon, tarball o bundle— y la
orden `escritura/bin/nk estado && escritura/bin/nk contar`. Ver `escritura/PROTOCOLO.md` y
`escritura/PUBLICAR.md` §6.

## Copia de seguridad

```
sudo mount -t exfat -o uid=1000,gid=1000,umask=022 /dev/sda1 /mnt/usb      # si no está montado
escritura/bin/nk respaldo --destino /tmp/resp --etiqueta v63 --version 63 --materiales MATERIALES
```

Deja el bundle del historial (verificado), los materiales y un `SHA-256` con nombre fechado. El medio
externo está ordenado por tipo (decisión 155): `bundle/`, `materiales/`, `hashes/` y `los-archivos/`
con los `.7z` antiguos; el `SHA-256` lleva rutas relativas al USB y se comprueba con
`cd /mnt/usb && sha256sum -c hashes/<copia>.sha256`. Se restaura con `git clone <bundle>` y funciona
sin el kit instalado.

## Hoja de ruta

La historia del libro y lo que queda por hacer viven en **`HOJA-DE-RUTA.md`**: una casilla por hito,
con su fecha y su número de decisión. Aquí no se repite, para no mantener dos registros que se
desfasen. Lo que está abierto son las casillas `[ ]` de ese fichero; `nk estado` las lee de ahí.

## Cómo retomar

En cualquier sesión: «consulta los apuntes de Los archivos y reanuda». Se leen `APUNTES.md` (empezando
por §0), `ESTRUCTURA.md`, esta ficha y la primera casilla `[ ]` de `HOJA-DE-RUTA.md`. Antes de
escribir: `escritura/bin/nk estado` y `escritura/bin/nk contar`. El estado vivo, con la sesión en
curso y la siguiente, está en §0; no se copia aquí.
