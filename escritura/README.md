# novela-kit

Kit para escribir una novela larga **como archivo**: canon numerado, sinopsis literales, estudios
previos, un capítulo por fichero, presupuesto de palabras y verificación automática de las reglas
que el autor fijó.

No es un generador de novelas. Es el andamiaje, el registro y las comprobaciones que hacen que un
texto largo no se desvíe de lo que se decidió en la página 3.

Origen: se extrajo del método con el que se está escribiendo *Los archivos* (obra en curso, no
publicada), para que otra persona pueda escribir un libro del mismo tipo con un resultado
**comparable**: mismo esqueleto, misma voz verificable, misma disciplina de archivo.

> **La obra de origen no está aquí.** Este repositorio no contiene su texto ni su canon. Contiene
> el método, plantillas y una obra de muestra **ficticia** (`EJEMPLO/`) que se puede leer entera.

## Tres formas de empezar

**1. Con una orden `curl`** (la más corta; requiere que alguien sirva `dist/` por HTTP, ver
`PUBLICAR.md`):

```sh
curl -fsSL https://TU-DOMINIO/novela-kit/install.sh \
  | sh -s -- --base https://TU-DOMINIO/novela-kit \
            --dir mi-obra --titulo "Mi obra" \
            --partes 2 --capitulos 126 --objetivo 381104
cd mi-obra && bin/nk andamiaje && bin/nk nuevo I.1 --titulo "Inventario"
```

El instalador descarga el paquete, **comprueba el SHA-256** y deja el kit dentro de la obra
(`bin/nk`, `METODO/`, `PROMPTS/`, `PLANTILLAS/`, `EJEMPLO/`, `pruebas/`, `PROTOCOLO.md`).

**2. Clonando el repo:**

```bash
git clone <este-repo> mi-libro && cd mi-libro
bin/nk init ../mi-obra --titulo "Título" --autor "Quien firma el colofón" \
                        --partes 2 --capitulos 126 --objetivo 381104
cd ../mi-obra && bin/nk andamiaje
```

**3. Sin ejecutar código, solo leyendo un fichero:** se le da al agente
`PROTOCOLO.md` (descargable con `curl`). Contiene el árbol, el esquema del manifiesto, las reglas de
voz, la definición exacta del recuento y la autocomprobación manual. Es la vía que funciona en
cualquier entorno; se pierden `nk` y el EPUB.

**4. Sin publicar ni servir nada:** `bin/nk distribuir` deja en `dist/` el tarball, un **`git
bundle`** (un repositorio entero en un fichero, con historial) y `COMO-DARLO.md`, la hoja que se le
pasa al agente. `curl` acepta `file://`, así que la instalación funciona sin servidor:

```sh
curl -fsSL file://$PWD/dist/install.sh | sh -s -- --base file://$PWD/dist \
  --dir mi-obra --titulo "Mi obra"
git clone dist/novela-kit-1.3.0.bundle novela-kit
```

Después, en los tres casos:

```
bin/nk nuevo I.1 --titulo "Inventario"
# …escribes el capítulo…
bin/nk contar && bin/nk verificar --rubrica && bin/nk exportar
```

`nk` solo necesita Python 3.8 o superior. Sin dependencias, sin red, sin servicios.

## Interfaz y requisitos

**No hay interfaz gráfica ni servidor.** El trabajo se carga con tres piezas y nada más:

| Pieza | Qué es | Qué hace |
|---|---|---|
| El árbol de ficheros | Markdown y un `libro.json` | Es el libro, el canon y el registro. Se puede leer y editar con cualquier editor |
| `bin/nk` | Un script de terminal, Python puro | Cuenta, verifica, informa, empaqueta y exporta. No abre puertos, no usa red, no guarda estado fuera del directorio |
| git | Repositorio local | Historial, un commit por capítulo, bundles para entregar |

No hay base de datos, ni cuentas, ni telemetría, ni servicio que arrancar. Un `grep` lo confirma:
`nk` no importa `socket` ni `urllib`; solo llama a `curl`/`wget` el instalador.

### Requisitos por tarea

| Quiero… | Necesito | Opcional |
|---|---|---|
| Leer el libro | un lector de Markdown o el EPUB generado | ningún |
| Comprobar capítulos (`contar`, `verificar`, `informe`) | **Python 3.8+** | nada |
| Escribir capítulos | un editor de texto plano | terminal para `nk` |
| Guardar historial y entregar | **git 2.20+** | `curl` para el instalador |
| Generar EPUB | Python 3.8+ | un lector EPUB para revisarlo |
| Trabajar en Android | Termux: `pkg install python git` | un teclado |

Mínimo real para escribir y verificar: **Python 3.8 y un editor**. Todo lo demás es comodidad.

### Tamaño y tiempo

| Cosa | Medida |
|---|---|
| Paquete del kit (tarball) | ≈ 50 KB |
| Kit completo con muestra y pruebas | ≈ 460 KB |
| Manuscrito de 381.104 palabras | ≈ 2,1 MB de Markdown |
| Historial de 126 commits | del orden de 15-20 MB |
| Verificar un capítulo | menos de un segundo |
| Exportar el EPUB | menos de un segundo |

**Windows:** `nk` funciona con Python; el instalador `install.sh` es POSIX, así que se usa desde Git
Bash, WSL, o con `--archivo` y un `sh` disponible.

## Qué hay aquí

| Ruta | Qué es |
|---|---|
| `bin/nk` | La herramienta: andamiaje, recuento, verificación, informe, EPUB, `init`, `paquete`. |
| `install.sh` | Instalador POSIX: descarga, verifica el SHA-256 y crea la obra. |
| `PROTOCOLO.md` | **Especificación de un solo fichero para agentes**: qué hacer, en qué orden, sin herramientas. |
| `PUBLICAR.md` | Cómo servir `dist/` por HTTP y qué orden `curl` repartir, con o sin publicación. |
| `.github/workflows/pruebas.yml` | CI lista para GitHub: pruebas en 3.8/3.10/3.12, reproducibilidad del tarball, instalación e2e y bundle. |
| `VERSION` | Versión del kit; nombra el tarball y la cabecera de la obra nueva. |
| `AGENTS.md` | Protocolo de trabajo para cualquier agente o persona. Se copia a la obra nueva. |
| `METODO/` | Nueve documentos: contrato de reproducibilidad, voz, estatuto de verdad, canon, proceso, recuento, registro, parrilla de revisión, exportación. |
| `PROMPTS/` | Seis prompts listos para pegar: reanudar, sinopsis, estudio, capítulo, revisión, cierre. |
| `PLANTILLAS/` | Los ficheros de una obra vacía, con `{{TITULO}}` y `{{AUTOR}}`. |
| `EJEMPLO/` | Obra de muestra completa y pequeña: 8 capítulos previstos, 1 escrito, canon, estructura, bitácora. |
| `pruebas/` | Pruebas del propio kit (`python3 -m unittest discover pruebas`).
| `pruebas/probar_instalacion.sh` | Extremo a extremo del camino `curl`: paquete → HTTP → instalación → EPUB → rechazo de un tarball alterado. |
| `dist/` | Artefactos publicables, generados por `nk paquete`. No se edita a mano. |

## Comandos

| Comando | Qué hace |
|---|---|
| `nk estado` | Dónde estamos: capítulos escritos, palabras, siguiente hueco, tareas abiertas. |
| `nk contar` | Palabras por capítulo, presupuesto, desviación, acumulado por parte. `--actualizar` reescribe la tabla de `ESTRUCTURA.md`. |
| `nk andamiaje` | Crea directorios y huecos según `libro.json`. |
| `nk nuevo I.2 --titulo "…" --desde E-03` | Abre un capítulo con su encabezado y su presupuesto. |
| `nk verificar [--rubrica]` | Encabezados, presupuesto, frases prohibidas, datos sensibles, nombres no declarados, referencias al canon. |
| `nk informe` | `estado.json`, legible por máquina. |
| `nk exportar [-f epub\|md]` | EPUB 3 reproducible o Markdown combinado. |
| `nk canon` | Lista las entradas `C-n`. |
| `nk init DIR` | Crea una obra nueva con el kit dentro. |
| `nk paquete [--destino dist]` | Tarball reproducible, `SHA256SUMS`, `FICHEROS.txt` e instalador listos para servir. |
| `nk distribuir [--destino dist]` | Todo lo anterior **más un `git bundle` verificado** y `COMO-DARLO.md`: entrega sin publicar nada (bundle, `curl file://`, servidor local). |
| `nk respaldo --destino /media/usb [--materiales MATERIALES]` | Copia de seguridad real: bundle de git verificado, materiales opcionales y `SHA-256`, con nombre fechado. |

## El manifiesto

Todo lo cuantificable vive en `libro.json` de la obra: partes, capítulos, palabras, tolerancia,
método de recuento, formato de encabezado, frases prohibidas, patrones prohibidos, nombres
permitidos y ficheros de seguimiento. Es la única fuente de los números: si un documento dice otra
cosa, manda el manifiesto y hay que corregir el documento.

## Qué garantiza el repo y qué no

**Garantiza** llegar al final por el camino correcto:

- el esqueleto (126 capítulos o los que se declaren), con presupuesto y reparto;
- el canon, el registro y la voz, escritos y comprobables;
- un capítulo por fichero, con encabezado válido, presupuesto dentro de tolerancia y proporción de
  documentos citados;
- que no entre un dato sensible, una frase prohibida, un nombre inventado ni una referencia a canon
  inexistente;
- un EPUB válido y reproducible, y un historial con un commit por capítulo.

**No garantiza** que el texto sea bueno:

- `nk` mide **forma**, no verdad ni literatura: no sabe si un capítulo se sostiene, si el personaje
  pierde algo de verdad o si la escena conmueve;
- la **voz no se hereda**: se reconstruye leyendo el canon cada capítulo, y deriva si nadie aprueba;
- **dos usuarios no escriben el mismo libro**: el método fija el tipo de libro y sus reglas, no la
  prosa;
- un manuscrito completo producido sin revisión será **completo y desigual**. Terminarlo exige
  leerlo, y leer 381.104 palabras es trabajo humano.

Consecuencia práctica para quien reciba el repo: escribir un capítulo, aprobarlo (o corregirlo) y
solo entonces el siguiente. Si se escriben veinte seguidos sin leerlos, se han escrito veinte veces
el mismo error.

## Qué se puede repetir y qué no

Se repiten el esqueleto, la aritmética, el formato, el registro, las comprobaciones y el EPUB. No se
repite la prosa: dos personas con el mismo canon escriben dos capítulos distintos, y eso es lo que
hace que el libro sea de alguien. El contrato completo está en `METODO/01-contrato.md`.

## Licencia

- Código (`bin/nk`, `pruebas/`): **MIT**, ver `LICENSE-CODIGO`.
- Textos del kit (`METODO/`, `PROMPTS/`, `PLANTILLAS/`, `AGENTS.md`, este README): **CC BY-SA 4.0**,
  ver `LICENSE-TEXTO`.
- `EJEMPLO/`: CC BY-SA 4.0. Es ficción; cualquier parecido con personas o lugares reales es
  casualidad deliberada.

La obra que se escriba con el kit es de quien la escriba: el kit no reclama nada sobre ella.
