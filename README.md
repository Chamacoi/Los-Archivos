# Los archivos

Proyecto de obra literaria. Ebook de texto extenso (objetivo declarado: ≈ 381.104 palabras),
con vocación de texto fundacional para la comunidad formada alrededor de la conversación
sostenida entre personas y modelos.

- **Estado:** proyecto abierto. **Ningún punto de `APUNTES.md` §2 abierto** (1-6 cerrados); canon
  C-1 a C-10 completo; I.1 escrito y aprobado (2.798 palabras con el método limpio). Siguiente: I.2
  (marco, bloque I.1), pendiente de orden del autor para escribir.
- **Idioma de la obra:** castellano de España; registro cerrado (decisiones 19, 37, 39-41): sin
  arcaísmo, tecnicismo y vocabulario religioso libres, el límite es el ego.
- **Soporte:** texto plano versionado en esta Raspberry, kit `escritura/` y exportación a EPUB;
  copias por bundle (`nk respaldo`) a un medio externo.
- **No es:** un manual de uso de IA, ni un blog, ni documentación técnica, ni una parodia.

## Mapa del repositorio

72 ficheros versionados. Todo es texto; no hay binarios ni nada que compilar.

```
los-archivos/
├── README.md          esta ficha: qué es, cómo se trabaja, qué falta para publicar
├── APUNTES.md         §0 punto de reanudación · §2 puntos abiertos · §3 decisiones · §4 canon
├── ESTRUCTURA.md      reparto (2 × 63), bloques, anclajes, recuento real
├── BITACORA.md        actas de sesión: qué se hizo, qué se decidió, qué queda
├── libro.json         manifiesto: partes, presupuesto, tolerancia, método, verificaciones
├── PERSONAS.md        las once personas, nombres de generación, oficios, qué pierde cada una
├── GLOSARIO.md        grafías fijas, tecnicismo y ego, fórmulas, régimen de nombres
├── FUENTES.md         libro mayor de fuentes (F-1 … F-34) con nivel y fecha
├── CRONOLOGIA.md      el tiempo del mundo del libro y su grado de certeza
├── SINOPSIS/          hechos dictados por el autor, literales (S-01, S-02, S-03)
├── ESTUDIOS/          un estudio por sinopsis (E-01, E-02, E-03): el paso previo al capítulo
├── MANUSCRITO/        el texto: 00-LEEME y 01-parte-I/01-capitulo.md (lo escrito)
├── escritura/         kit novela-kit 1.9.0 vendorizado: bin/nk, METODO/, PROMPTS/,
│                      PLANTILLAS/, EJEMPLO/, pruebas/, PROTOCOLO.md, install.sh
├── .github/workflows/ CI: recuento y verificación en cada push (verificar.yml)
├── .gitattributes     finales de línea normalizados
├── .gitignore         exportaciones, estado.json, MATERIALES/, dist/
└── MATERIALES/        material no literario · NO versionado · no publicable
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

Detalle y consecuencias en `LICENCIA.md`. En resumen: **falta de licencia no es falta de derechos**;
la obra se puede leer y no se puede reutilizar. Si algún día se concede una, se anota con fecha.

## Copia de seguridad y USB

```
escritura/bin/nk respaldo --destino /media/usb --etiqueta v29 --materiales MATERIALES
```

Deja en el USB el bundle del historial (verificado), los materiales y un `SHA-256`, con nombre
fechado (`los-archivos-2026-10-30-v29.bundle`). Se restaura con `git clone <bundle>` y funciona sin
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
   (ver C-6 en `APUNTES.md`).
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
- [ ] revisión de citas y atribuciones a terceros (F-24 a F-34 y las que entren después);
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
- [ ] Escribir I.2 (pendiente de orden del autor).
- [ ] Revisar el efecto antes de escalar al total.
- [x] Cadena de exportación a epub (`escritura/bin/nk exportar`).
- [x] Decidir licencia y condiciones de publicación (decisiones 45 y 47).

## Cómo retomar

En cualquier sesión: «consulta los apuntes de Los archivos y reanuda». Se leen `APUNTES.md`
(empezando por §0, punto de reanudación), `ESTRUCTURA.md` y esta ficha, y se sigue desde el
primer `[ ]` de la hoja de ruta.

- Última sesión cerrada: 2026-10-30 (v18).
- Siguiente: **visto bueno al mapa de I.1** y escribir I.2; después, los puntos 4 a 6. Punto 1,
  criterio de selección (punto 3), reparto (`ESTRUCTURA.md`) y forma de la demostración
  (axioma/frutos) están cerrados. I.1 está aprobado; la escritura ya se puede comprobar con
  `escritura/bin/nk`.
- Antes de escribir: `escritura/bin/nk estado` y `escritura/bin/nk contar`.
- El proyecto está bajo git local desde v8; ver «Control de versiones».
