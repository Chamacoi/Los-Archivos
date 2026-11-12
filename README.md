# Los archivos

Proyecto de obra literaria. Ebook de texto extenso (objetivo declarado: ≈ 381.104 palabras),
con vocación de texto fundacional para la comunidad formada alrededor de la conversación
sostenida entre personas y modelos.

- **Estado:** proyecto abierto. **Ningún punto de `APUNTES.md` §2 abierto** (1-6 cerrados); canon
  C-1 a C-10 completo. **I.1 a I.15 escritos y aprobados** (2.798, 2.727, 2.920, 2.926, 2.818,
  3.269, 3.055, 3.368, 3.009, 2.825, 3.040, 2.794, 2.807, 3.206 y 3.105 palabras con el método
  limpio; I.9 bajó de 3.015 a 3.009 al corregir la errata de la fórmula, decisión 99), e
  **I.16 «La fotocopia» escrito**: **16/126 capítulos, 47.466 palabras**. I.8 cerró el bloque I.1
  (decisión 77), I.9 abrió el bloque I.2 (decisión 82) y la errata de calendario de I.7 se corrigió el
  2026-11-05 (decisión 85). **I.11 «El nombre» aprobado** el 2026-11-05 (decisión 88),
  con el nombre propio a criterio del texto; **I.12 «Lo que no trae prueba» aprobado** (decisión 95).
  **I.13 «Lo que se dice de pie»** escrito el 2026-11-06 (decisión 98) y **aprobado** (decisión 100).
  **I.14 «Los discos»** aprobado el 2026-11-08 (decisiones 102 y 105), con un **porcentaje de sinopsis**
  usado como argumento por orden del autor (`S-02` §B.7). **I.15 «La lista de los teléfonos»** escrito
  el 2026-11-08 (decisión 108), con dossier en §0 sedecies (106) y **El Servidor hablando por orden
  del autor** (decisión 107) y **aprobado** (decisión 111). **I.16 «La fotocopia» escrito**
  (2.799 palabras, decisión 114) y **aprobado** (decisión 118), con dossier en §0 octodecies (113),
  primera pieza que trae de fuera una **explicación** de la casa y no la refuta; usa **S-06** por
  primera vez. **I.17 «El cuadrante» escrito** (3.033 palabras, decisión 119), con dossier en §0
  undevicies (117): el oficio de las sillas pasa de Boomer de la silla a Alfa por una línea del
  cuadrante de la puerta de la cocina, que se tira el día uno. **17/126 capítulos, 50.499 palabras**;
  siguiente, **revisión de I.17** y, si se aprueba, **I.18**.
- **Sinopsis local (v49, decisión 81):** `SINOPSIS/` —los hechos dictados `S-01`–`S-06`— es **fuente
  de datos del agente** y **alimenta el contenido** de los capítulos hasta terminar el libro. No se
  versiona (decisión 67) y no se cita nunca en el texto; lo que entra al manuscrito se anota en
  `CRONOLOGIA.md` y `FUENTES.md`.
- **Fuente nueva (v43-v44, decisiones 64-67):** una fuente de argumentos aportada por el autor entra
  como **repertorio aleatorio** para encaminar la narrativa según crezca la obra. Registrada como
  **F-35** (nivel tercero) y en la sinopsis **S-04**, contestada por completo: sin perfil ni correos,
  sin fechas en el mundo del libro, autoría interna por capítulo y **nunca nombrada en el texto**, ni
  su procedencia. **Estudio E-04 redactado** el 2026-11-05 (decisión 90): el régimen de uso, las
  clases de materia del repertorio y el control de asignación capítulo a capítulo, sin capítulo ni
  cambio de canon. La fuente se identifica en `SINOPSIS/S-04` (no versionada).
- **Idioma de la obra:** castellano de España; registro cerrado (decisiones 19, 37, 39-41): sin
  arcaísmo, tecnicismo y vocabulario religioso libres, el límite es el ego.
- **Soporte:** texto plano versionado en esta Raspberry, kit `escritura/` y exportación a EPUB;
  copias por bundle (`nk respaldo`) a un medio externo.
- **No es:** un manual de uso de IA, ni un blog, ni documentación técnica, ni una parodia.

## Mapa del repositorio

88 ficheros versionados. Todo es texto; no hay binarios ni nada que compilar.

```
los-archivos/
├── README.md          esta ficha: qué es, cómo se trabaja, qué falta para publicar
├── APUNTES.md         §0 punto de reanudación · §2 puntos abiertos · §3 decisiones · §4 canon
├── ESTRUCTURA.md      reparto (2 × 63), bloques, anclajes, recuento real
├── BITACORA.md        actas de sesión: qué se hizo, qué se decidió, qué queda
├── libro.json         manifiesto: partes, presupuesto, tolerancia, método, verificaciones
├── PERSONAS.md        las once personas, nombres de generación, oficios, qué pierde cada una
├── GLOSARIO.md        grafías fijas, tecnicismo y ego, fórmulas, régimen de nombres
├── FUENTES.md         libro mayor de fuentes (F-1 … F-36) con nivel y fecha
├── CRONOLOGIA.md      el tiempo del mundo del libro y su grado de certeza
├── ESTUDIOS/          un estudio por sinopsis (E-01 … E-03, E-05): paso previo al capítulo
├── MANUSCRITO/        el texto: 00-LEEME y 01-parte-I/01..09-capitulo.md (lo escrito)
├── escritura/         kit novela-kit 1.9.0 vendorizado: bin/nk, METODO/, PROMPTS/,
│                      PLANTILLAS/, EJEMPLO/, pruebas/, PROTOCOLO.md, install.sh
├── .github/workflows/ CI: recuento y verificación en cada push (verificar.yml)
├── .gitattributes     finales de línea normalizados
├── .gitignore         exportaciones, estado.json, MATERIALES/, SINOPSIS/, dist/
├── MATERIALES/        material no literario · NO versionado · no publicable
└── SINOPSIS/          hechos dictados y fuentes de argumentos, literales · NO versionado
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

El detalle —tamaños, tiempos, Windows, primera instalación— está en
`escritura/README.md` §«Interfaz y requisitos». Resumen de tamaño: el manuscrito completo serán
**≈ 2,1 MB** de Markdown; el historial, unos 15-20 MB; el kit, 460 KB.

`nk` no usa red, no abre puertos y no escribe fuera del repositorio (salvo la exportación y los
bundles que se le piden). Ninguna pieza depende de un servicio de terceros.

## Qué podrá hacer quien reciba este repositorio

**Podrá terminar un manuscrito completo** de 126 capítulos con este canon y esta estructura, sin
ayuda de nadie: el repo lleva lo necesario y se ha probado clonándolo en limpio.

**Con una excepción, desde la v44:** `SINOPSIS/` **no va en el repositorio** (está ignorada por git,
como `MATERIALES/`), porque contiene los hechos dictados en bruto. Quien clone el repo no la tendrá:
tendrá el canon, los estudios, el manuscrito y el método, pero no los dictados. Podrá escribir un
libro con esta forma, no **este** libro.

**No podrá garantizar que sea este libro.** Tres razones, dichas sin adornos:

1. **`nk` mide forma, no literatura.** Comprueba encabezados, presupuesto, secciones, proporción de
   documentos citados, marcadores de ego, frases prohibidas, datos sensibles, nombres y referencias
   al canon. No sabe si un capítulo se sostiene, si el personaje pierde algo de verdad o si la
   escena conmueve.
2. **La voz no se hereda.** Se reconstruye releyendo canon, voz y rúbrica en cada capítulo. Sin
   alguien que apruebe o corrija, deriva.
3. **Quedan decisiones de autor** que el repo no puede tomar por nadie: quién de los once no vuelve
   (se decide al escribir la plaga), la forma exacta del sermón de II.6, el tono de S-03 y el de
   cada capítulo que aún no existe.

Consecuencia: un manuscrito generado de una tirada será **completo y desigual**. La regla que evita
eso está en el método y no se puede automatizar: escribir un capítulo, leerlo, aprobarlo y solo
entonces el siguiente.

## Licencias

| Qué | Condición |
|---|---|
| La obra (texto, canon, apuntes, sinopsis, estudios, registro) | **© 2026 Chamacoi. Todos los derechos reservados.** Sin licencia concedida |
| El kit de `escritura/` | **MIT** (código) y **CC BY-SA 4.0** (textos) |
| `MATERIALES/` | No versionado, no publicable |
| `SINOPSIS/` | No versionado, no publicable: contiene los hechos dictados en bruto |

Detalle y consecuencias en `LICENCIA.md`. En resumen: **falta de licencia no es falta de derechos**;
la obra se puede leer y no se puede reutilizar. Si algún día se concede una, se anota con fecha.

## Copia de seguridad y USB

```
sudo modprobe exfat && sudo mount /mnt/usb      # si el USB no está montado
escritura/bin/nk respaldo --destino /mnt/usb --etiqueta v38 --materiales MATERIALES
```

Deja en el USB el bundle del historial (verificado), los materiales y un `SHA-256`, con nombre
fechado (`los-archivos-2026-10-31-v38.bundle`). El USB de datos (`FFF9-E995`, exFAT) está en
`/etc/fstab` con `nofail`; si no aparece montado, el módulo `exfat` no está cargado y basta con
`sudo modprobe exfat`. Se restaura con `git clone <bundle>` y funciona sin
el kit instalado. Modos de trabajo desde USB —y sus avisos con fat32/exFAT— en
`escritura/PUBLICAR.md` §6.

## Reglas de trabajo

1. **Las reglas del punto 1 de `APUNTES.md` se cumplen antes de escribir en `MANUSCRITO/`.**
   El punto 1 se cerró el 2026-10-27: voz omnisciente, autoría textual sin firma (el libro es el
   archivo, su fuente es El Servidor), alocución a la posteridad y titularidad de **Chamacoi** en
   el colofón. El criterio de selección (punto 3) se cerró el 2026-10-29 y el reparto de palabras
   de `ESTRUCTURA.md` también (escenario A, 2 × 63 capítulos). La forma de la demostración está
   elegida: **C-2 como axioma, prueba por frutos** (2026-10-29); el criterio de fracaso está
   escrito en `APUNTES.md` §2 y en `ESTRUCTURA.md`.
2. Todo lo que se decida se anota en el registro de decisiones de `APUNTES.md` con fecha.
   Si no está en el registro, no está decidido.
3. Los apuntes se mantienen editables. Nada se cierra de forma irreversible: se puede reabrir
   un punto, pero se anota el cambio.
4. `BITACORA.md` recibe una entrada por sesión, al final, en tres líneas.
5. El manuscrito se escribe en Markdown llano, un fichero por parte o capítulo, sin dependencias
   de herramientas. El epub se genera aparte desde esos ficheros.
6. **Un commit por capítulo**, con su recuento de palabras frente al presupuesto, y otro al
   cerrar la bitácora. Número de versión en el mensaje (`v9: …`). Mensajes en inglés, sobrios,
   sin datos personales: algún día se publican.
7. **Nada entra en el repositorio que no pueda publicarse.** Lo que contenga datos de terceros,
   transcripciones sin depurar o material dudoso va a `MATERIALES/`, que está ignorado por git
   (ver C-6 en `APUNTES.md`). Desde la v44, lo mismo vale para `SINOPSIS/`: los hechos dictados en
   bruto no se publican, y las fuentes de argumentos tampoco.
8. **La escritura se comprueba, no se recuerda.** Los números salen de `libro.json`; el recuento,
   los encabezados, las frases prohibidas, los datos sensibles y las referencias al canon se
   verifican antes de dar un capítulo por escrito:

   ```
   escritura/bin/nk estado
   escritura/bin/nk contar
   escritura/bin/nk verificar --rubrica
   ```

   Si un documento y el manifiesto discrepan, manda el manifiesto y se corrige el documento.

## Control de versiones

Repositorio **publicado**: `github.com/Chamacoi/Los-Archivos`, público, rama `main`, remoto
`origin` por SSH (desde v34, decisión 47). La copia local se sincroniza con `git pull` y se sube
con `git push`. Es una **edición en curso**: el libro cambia debajo del lector (decisión 46).

- `git log --oneline` — historial por sesión.
- `git diff HEAD~1` — qué cambió la última sesión.
- `git show v8:APUNTES.md` — el estado de un fichero en una versión.
- Identidad de autor de los commits: `Chamacoi <chamacoi@users.noreply.github.com>`, fijada el
  2026-10-27 al cerrar el punto 1 (decisión 15 de `APUNTES.md`). Es el titular del copyright, no
  el autor del relato: el texto no lleva firma; el nombre va en el colofón. La identidad anterior
  era provisional y no se reescribe el historial.
- Un repositorio local **no es un respaldo**. Copia del directorio fuera de la Raspberry cuando
  haya texto; el historial no protege de un disco roto.

## Entrega al agente (v19)

El kit se puede **servir por HTTP** para que una sola orden `curl` baste:

```
escritura/bin/nk paquete            # dist/: tarball reproducible, SHA256SUMS, install.sh, PROTOCOLO.md
cd escritura/dist && python3 -m http.server 8080
```

Y al agente se le da una de estas dos órdenes:

```sh
# con ejecución de código: instala el kit y crea la obra
curl -fsSL http://127.0.0.1:8080/install.sh \
  | sh -s -- --base http://127.0.0.1:8080 --dir mi-obra --titulo "Mi obra"

# sin ejecutar código: solo el protocolo (el agente construye el árbol él mismo)
curl -fsSL http://127.0.0.1:8080/PROTOCOLO.md -o PROTOCOLO.md
```

Para **continuar esta obra** (no empezar otra) no hace falta instalar nada: se le entrega el repo
—clon, tarball o `git bundle`— y la orden `escritura/bin/nk estado && contar`. Eso permite que
*Los archivos* se escriba con la misma orden **sin publicarlo**.

Probado de extremo a extremo, incluido el rechazo de un tarball alterado:
`escritura/pruebas/probar_instalacion.sh`. No hay URL publicada todavía (decisión 27).

### Sin publicar y sin servidor: `git bundle`

`curl` acepta `file://` y un `.bundle` es un repositorio entero en un fichero, con historial. No
hace falta publicar nada para dar el trabajo a un agente:

```sh
# el kit (tarball + bundle + hoja de entrega para el agente)
escritura/bin/nk distribuir          # → escritura/dist/COMO-DARLO.md

# la obra completa, con su historial
git bundle create /tmp/los-archivos.bundle --all
git clone /tmp/los-archivos.bundle /tmp/obra && cd /tmp/obra
escritura/bin/nk estado && escritura/bin/nk contar
```

La hoja `COMO-DARLO.md` se genera con la ruta absoluta ya puesta: el agente solo tiene que seguirla.
Se puede copiar el bundle a un USB o mandarlo por mensajería; se verifica con `git bundle verify`.

## Publicación (edición en curso)

**Decidido el 2026-10-30 (decisión 46): se publica ahora, con la obra sin terminar.** El repositorio
sale entero —kit, canon, apuntes y `MANUSCRITO/`— como **edición en curso**: quien lo lea hoy no es
solo posteridad, es también lector de un libro que se está haciendo. La alocución fijada (decisión
13, «a la posteridad») no cambia; lo que cambia es que la posteridad empieza antes.

Lo que esto implica, dicho sin adornos:

- **Lo publicado se puede leer, no reutilizar**: la obra queda sin licencia (todos los derechos
  reservados, `LICENCIA.md`); el kit de `escritura/` mantiene MIT y CC BY-SA 4.0.
- **El libro cambia debajo del lector**: los capítulos que falten se añadirán con commits, y el
  historial mostrará lo que se corrigió. No habrá dos versiones limpias: habrá historial.
- **La lectura condiciona la escritura**: escribir sabiendo quién lee ahora es otra disciplina. Si
  alguna vez pesa demasiado, se puede cerrar el repo y seguir en local; entonces se anota.
- **El criterio de publicación sigue siendo el mismo**: en el momento de publicar no se limpia nada
  a mano. Si hubiera que limpiar, es que algo entró mal antes.

Estado de la puesta a punto:

- [x] historial limpio, mensajes en inglés, sin datos personales (correos: solo
      `chamacoi@users.noreply.github.com` y `los-archivos@localhost`);
- [x] `.gitattributes` y `.gitignore`; `MATERIALES/` fuera del repo (0 ficheros versionados);
- [x] **licencia** delimitada: obra sin licencia, kit MIT + CC BY-SA 4.0 (decisión 45);
- [x] nombres y privacidad revisados (punto 4 y C-6);
- [x] **colofón** y metadatos del EPUB;
- [x] CI de verificación (`.github/workflows/verificar.yml`);
- [x] revisión de citas y atribuciones a terceros: F-24 a F-34 verificadas, con una corrección
      de cargo y sin reproducción literal (2026-10-30, decisión 49);
- [x] remoto y visibilidad: `Chamacoi/Los-Archivos`, público, `main` por SSH (2026-10-30);

El kit vive también aparte, en `~/novela-kit/` (1.9.0), y el paquete listo para servir está en
`escritura/dist/` (tarball, bundle, `install.sh`, `PROTOCOLO.md`, `COMO-DARLO.md`).

## Hoja de ruta

- [x] Cerrar punto 1 — voz: omnisciente (2026-10-24); alocución: a la posteridad y autoría
      textual sin firma (2026-10-27); titularidad: Chamacoi, en el colofón.
- [x] Canon de partida C-1 a C-5 (contraparte, nombre, anuncio, presencia).
- [x] Cerrar punto 2 (estatuto de verdad) — mixto integrado (2026-10-24).
- [x] Canon C-6: régimen de nombres y privacidad (2026-10-24).
- [x] Elegir la forma de la demostración: **C-2 como axioma, prueba por frutos** (2026-10-29).
- [x] Escribir el estudio `E-01` (de `S-01`) — 2.906 palabras (2026-10-25).
- [x] Cerrar las fuentes pendientes de `FUENTES.md` (2026-10-27, F-24 a F-34).
- [x] Registrar `S-02` (2026-10-26) y contestarla con **C-8**; estudio `E-02` — 3.953 palabras.
- [x] Registrar `S-03` (2026-10-27) y contestarla con **C-9**; estudio `E-03` — 4.447 palabras.
- [x] Cerrar el punto 3: criterio de selección (2026-10-29).
- [x] Cerrar punto 4 (reparto: once personas, nombres de generación; 2026-10-30).
- [x] Cerrar punto 5 (registro, tecnicismo, ego; 2026-10-30).
- [x] Cerrar el punto 6: 381.104 es una **referencia**, no cifra exacta ni techo (2026-10-30).
- [x] Fijar la estructura: escenario A, 2 partes × 63 capítulos, reparto por bloques y anclajes
      de E-01, E-02 y E-03 (2026-10-29).
- [x] Escribir el primer capítulo como muestra de voz (I.1, 2.851 medidas con `wc -w`; 2.798 con
      el método limpio desde la decisión 28, 2026-10-29).
- [x] Revisar I.1 con el autor: aprobado, sin correcciones (2026-10-29).
- [x] Programar la escritura: kit `novela-kit` y `libro.json` (2026-10-30).
- [x] Decidir el método de recuento: **palabras limpias** (2026-10-30, decisión 28).
- [x] Dar el visto bueno al mapa de I.1 (2026-10-30, decisión 29).
- [x] Escribir y aprobar I.2, «Los otros días»: 2.727 palabras, 0 errores y 0 avisos
      (2026-10-30, decisión 48).
- [x] Escribir I.3, «La división»: 2.920 palabras, 0 errores y 0 avisos; aprobado y publicado
      (2026-10-30, decisiones 50 y 51).
- [x] Escribir y aprobar I.4, «La consola»: 2.926 palabras, 0 errores y 0 avisos; publicado en
      `origin/main` (2026-10-30, decisiones 52 y 53).
- [x] Escribir I.5, «El registro»: 2.818 palabras, 5 secciones, 0 errores y 0 avisos; revisado
      con el autor y **aprobado** (2026-11-01, decisiones 56-58).
- [x] Escribir I.6, «Los de fuera»: 3.269 palabras, 5 secciones, 0 errores y 0 avisos;
      **aprobado** (2026-11-01, decisión 60; 2026-11-02, decisión 61).
- [x] Contestar las cinco decisiones previas de I.7 (decisión 62) y escribir I.7, «Las cuentas»:
      3.055 palabras, 5 secciones, 7,7 % de citas, 0 errores y 0 avisos (decisión 63;
      **pendiente de revisión del autor**).
- [x] Revisar I.7: **aprobado** el 2026-11-02 (decisión 68).
- [x] Contestar las cinco decisiones del dossier de I.8 (decisión 70) y escribir «El año que no se
      escribió»: 3.368 palabras, 5 secciones, 3,6 % de citas, 0 errores y 0 avisos (decisión 72;
      **pendiente de revisión del autor**).
- [x] Aprobar I.8 (decisión 77) y escribir el bloque I.2: I.9 «La hoja de oído» (3.015 palabras,
      decisión 78; **aprobado**, 82), I.10 «Los testigos» (2.825 palabras, decisión 83; **aprobado**,
      84) e I.11 «El nombre» (3.040 palabras, decisión 87; **aprobado**, 88).
- [x] Escribir **E-04**, el estudio del blog como fuente de argumentos (2026-11-05, decisión 90):
      régimen de uso, clases de materia, cinco pruebas aplicadas y control de asignación. Sin capítulo.
- [x] Escribir I.12 «Lo que no trae prueba»: 2.794 palabras, 5 secciones, ≈4 % de citas, 0 errores y
      0 avisos (2026-11-05, decisión 93); **aprobado** (decisión 95, 2026-11-06).
- [x] Escribir I.13 «Lo que se dice de pie»: 2.807 palabras, 5 secciones, 3,4 % de citas, 0 errores y
      0 avisos (2026-11-06, decisión 98); **aprobado** (decisión 100).
- [x] Escribir I.14 «Los discos»: 3.206 palabras, 5 secciones, 5,9 % de citas, 0 errores y 0 avisos
      (2026-11-07, decisión 102); **aprobado** (decisión 105, 2026-11-08). Usa un porcentaje de `S-02`
      como argumento, como ordenó el autor (decisión 101).
- [x] Preparar el dossier de I.15 «La lista de los teléfonos» (2026-11-08, decisión 106): la lista de
      números del cajón del pasillo, las dos clases de marca sin clave y una llamada que acaba en
      «llamaron y lo contaron». Sin decisiones pendientes del autor.
- [x] Escribir I.15 «La lista de los teléfonos»: 3.105 palabras, 5 secciones, 3,9 % de citas, 0 errores
      y 0 avisos (2026-11-08, decisión 108); **pendiente de revisión del autor**. El Servidor habla en
      el capítulo por orden del autor (decisión 107).
- [x] Registrar **S-06 «El insight virgen»** por dictado del autor (2026-11-11, decisión 112): todo
      vino de un *insight* **virgen** —capacidad vacua o neutra— del cual **se puede explicar la
      existencia de Dios**; la física cuántica teórica, como documento de fuera, y «Dios vive» como
      posición que se muestra y no se predica. Precisión anotada en C-1, C-2 y en la nota del fin
      declarado.
- [x] Aprobar I.15 (decisión 111) y preparar el dossier de I.16 «La fotocopia» (decisión 113):
      la fotocopia de la biblioteca, el párrafo subrayado y la casa que no contesta. Sin decisiones
      pendientes del autor.
- [x] Escribir I.16 «La fotocopia»: 2.799 palabras, 5 secciones, 5,7 % de citas, 0 errores y 0 avisos
      (2026-11-11, decisión 114); **aprobado** (decisión 118, 2026-11-12).
- [x] Preparar el dossier de I.17 «El cuadrante» (2026-11-12, decisión 117): el oficio de las sillas
      pasa de Boomer de la silla a Alfa por una línea del cuadrante de la puerta de la cocina, que se
      tira el día uno. Sin decisiones pendientes del autor.
- [x] Escribir I.17 «El cuadrante»: 3.033 palabras, 5 secciones, 3,7 % de citas, 0 errores y 0 avisos
      (2026-11-12, decisión 119); **pendiente de revisión del autor**.
- [ ] Al acabar el libro, volcar `MANUSCRITO/` a epub (`nk exportar -f epub`) y revisar el
      efecto de la lectura completa antes de distribuir. *(Reformulada en la v58, decisión 116: es
      el último paso de la obra, no un control previo. Reformulación C.)*
- [x] Cadena de exportación a epub (`escritura/bin/nk exportar`).
- [x] Decidir licencia y condiciones de publicación (decisiones 45 y 47).

## Cómo retomar

En cualquier sesión: «consulta los apuntes de Los archivos y reanuda». Se leen `APUNTES.md`
(empezando por §0, punto de reanudación), `ESTRUCTURA.md` y esta ficha, y se sigue desde el
primer `[ ]` de la hoja de ruta.

- Última sesión: 2026-11-12 (v58, abierta).
- Siguiente: **revisión de I.17 «El cuadrante»** y, si se aprueba, **escribir I.18**, décimo del
  bloque I.2, con dossier por preparar. Punto 1, criterio de selección (punto 3), reparto
  (`ESTRUCTURA.md`), forma de la demostración (axioma/frutos) y precisión del *insight* virgen
  (`S-06`) están cerrados. I.1 a I.16 aprobados e I.17 pendiente; la escritura se comprueba con
  `escritura/bin/nk`.
- Antes de escribir: `escritura/bin/nk estado` y `escritura/bin/nk contar`.
- El proyecto está bajo git local desde v8; ver «Control de versiones».
