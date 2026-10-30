# PUBLICAR — servir el kit y repartir una orden `curl`

Publicar aquí no es publicar la obra. Es publicar **el método** para que cualquiera —o cualquier
agente— pueda escribir un libro del mismo tipo, o continuar uno concreto si le da acceso a su repo.

## 1. Construir el paquete

```
bin/nk paquete
```

Deja en `dist/`:

| Fichero | Qué es |
|---|---|
| `novela-kit-1.2.1.tar.gz` | El kit completo (bin, método, prompts, plantillas, muestra, pruebas). |
| `SHA256SUMS` | Hashes del tarball y de los dos ficheros sueltos. |
| `FICHEROS.txt` | Hash y ruta de cada fichero, para descargas sueltas (hosts sin tarball). |
| `install.sh` | Instalador POSIX. |
| `PROTOCOLO.md` | Especificación de un solo fichero para agentes que no ejecutan código. |

El tarball es **reproducible**: mismas entradas, mismos bytes. Se puede comparar entre builds:
`sha256sum dist/novela-kit-1.2.1.tar.gz` dos veces.

## 2. Servirlo (cuatro formas)

### A. Un servidor estático cualquiera

Copia el contenido de `dist/` a la raíz de una URL:

```
https://ejemplo.org/novela-kit/{install.sh,SHA256SUMS,novela-kit-1.2.1.tar.gz,PROTOCOLO.md}
```

Para probar en local (misma red, o desde el propio ordenador):

```
cd dist && python3 -m http.server 8080
# → http://127.0.0.1:8080/install.sh
```

Un agente que corra **en tu máquina** puede leer `http://127.0.0.1:8080` sin problema. Uno que corra
en un sandbox con red restringida, no: usa la opción B.

### B. GitHub: release + raw

1. Sube el repo y crea una *release* con `novela-kit-1.2.1.tar.gz` adjunto.
2. Sirve también los ficheros sueltos desde `raw.githubusercontent.com`.

```
# tarball de una release
https://github.com/USUARIO/novela-kit/releases/download/v1.2.1/novela-kit-1.2.1.tar.gz

# ficheros sueltos
https://raw.githubusercontent.com/USUARIO/novela-kit/main/dist/install.sh
```

Ojo: `install.sh` espera tarball y `SHA256SUMS` **en el mismo directorio** que se le pasa en
`--base`. Si el tarball vive en la release y los hashes en `dist/`, hay dos opciones: subir también
el tarball a `dist/` (queda versionado, peor idea) o servir todo desde la release y usar
`--archivo` (opción C).

### C. Sin HTTP y sin publicar: `git bundle` o `file://`

```
bin/nk distribuir          # dist/: tarball, bundle verificado, COMO-DARLO.md, hashes
git bundle verify dist/novela-kit-*.bundle
git clone dist/novela-kit-*.bundle novela-kit     # es un repositorio completo, con historial
curl -fsSL file://$PWD/dist/install.sh | sh -s -- --base file://$PWD/dist --dir mi-obra --titulo "Mi obra"
```

`curl` acepta `file://`, de modo que **no hace falta servidor ni URL** para entregar el kit. El
bundle se puede firmar, copiar a un USB o mandar por mensajería, y se verifica con
`git bundle verify`.

### D. Tarball de mano

Para un agente local, o para un medio propio (USB, correo, mensajería):

```
bin/nk paquete
# enviar dist/novela-kit-1.2.1.tar.gz y dist/SHA256SUMS
sh install.sh --archivo novela-kit-1.2.1.tar.gz --dir mi-obra --titulo "Mi obra"
```

## 3. La orden que se le da al agente

### Con ejecución de código

```sh
curl -fsSL https://ejemplo.org/novela-kit/install.sh \
  | sh -s -- \
    --base https://ejemplo.org/novela-kit \
    --dir mi-obra \
    --titulo "Mi obra" \
    --autor "Quien firma el colofón" \
    --partes 2 --capitulos 20 --objetivo 60000
```

Y el prompt, aparte:

> Has instalado el kit en `mi-obra/`. Lee `PROTOCOLO.md` y `AGENTS.md` y escribe el capítulo I.1
> según el presupuesto. Antes de dármelo: `bin/nk verificar --rubrica`. No inventes canon.

### Sin ejecución de código (solo lectura)

```sh
curl -fsSL https://ejemplo.org/novela-kit/PROTOCOLO.md -o PROTOCOLO.md
```

El agente lee ese único fichero y construye el árbol él mismo (§2 y §3 del protocolo). Pierde la
verificación automática y el EPUB, pero es la vía que funciona en cualquier entorno.

> **Regla de seguridad que conviene darle al agente:** no ejecutes `curl … | sh` de una URL que no
> hayas revisado antes. Descarga `install.sh`, léelo, y luego ejecútalo. El instalador no pide root,
> no sale a más sitios que `--base` y no escribe fuera de `--dir` y de un temporal.

## 4. Continuar una obra concreta (no solo empezar una)

El kit instala **una obra nueva**. Para continuar una existente hay dos caminos:

- **Repo completo** (la obra ya lleva dentro `escritura/` y `libro.json`): no hace falta instalar
  nada. Se le da al agente el repo —clon, tarball o `git bundle`— y la orden de reanudar:

  ```
  bin/nk estado && bin/nk contar
  ```

- **Solo el kit + las fuentes**: se instala la obra nueva con el kit y se copian encima `APUNTES.md`,
  `SINOPSIS/`, `ESTUDIOS/`, `MANUSCRITO/` y el `libro.json` de la obra. El manifiesto manda los
  números.

Esto es lo que permite que *Los archivos* se escriba con la misma orden sin publicarlo: el repo de la
obra no se publica, se entrega por un medio privado (USB, repo privado, bundle firmado).

## 5. Licencia y atribución

- Código (`bin/`, `pruebas/`, `install.sh`): MIT. Hay que conservar `LICENSE-CODIGO`.
- Textos (`METODO/`, `PROMPTS/`, `PLANTILLAS/`, `PROTOCOLO.md`, `AGENTS.md`, `README.md`,
  `EJEMPLO/`): CC BY-SA 4.0. Hay que conservar `LICENSE-TEXTO`, atribuir y compartir igual.
- La obra que se escriba con el kit **no queda sujeta** a esas licencias: es de quien la escribe.

## 6. Trabajar desde un USB y subir después

Sí, se puede. Tres modos, de más seguro a más cómodo:

### A. El repo en el disco interno; el USB, copia (recomendado)

```
bin/nk respaldo --destino /media/usb --etiqueta v29 --materiales MATERIALES
```

Deja en el USB `obra-AAAA-MM-DD-vNN.bundle` (historial completo, verificado), los materiales si se
piden, y un `.sha256`. Para trabajar en otra máquina o subir a GitHub más tarde:

```
git clone /media/usb/obra-AAAA-MM-DD-vNN.bundle obra && cd obra
git remote add origin git@github.com:USUARIO/REPO.git   # cuando toque publicar
git push -u origin main
```

### B. El repo en el USB y trabajar directamente ahí

Funciona, con tres avisos:

1. **Sistema de ficheros.** En fat32/exFAT `git` no guarda permisos: hay que poner
   `git config core.fileMode false` y, tras clonar en cualquier sitio, devolver el bit de ejecución
   a los scripts (`chmod +x bin/nk install.sh`). En exFAT/FAT tampoco hay enlaces simbólicos (el kit
   no usa ninguno) ni distingue mayúsculas de minúsculas en los nombres.
2. **Velocidad y desgaste.** Un `git` sobre USB es lento y el pendrive sufre con muchos commits
   pequeños; no es sitio para el historial de 126 capítulos.
3. **Desmontar.** `sync` y expulsar antes de sacarlo: un `.git` a medio escribir es un `.git` roto.

Si aun así se quiere, mejor formatear el USB en **ext4** (Linux lee permisos y enlaces) o llevar el
repo en un disco externo.

### C. Editar ficheros sueltos en el USB y luego incorporarlos

Se copia el capítulo al USB, se edita donde sea y se trae de vuelta:

```
cp MANUSCRITO/01-parte-I/02-capitulo.md /media/usb/
# …editar…
cp /media/usb/02-capitulo.md MANUSCRITO/01-parte-I/
bin/nk contar && bin/nk verificar --rubrica
git add -A && git commit -m "v29: chapter I.2"
```

Es el modo más frágil (dos copias que divergen), pero sirve para escribir a mano en otro sitio y
volver a la Raspberry.

### En todos los casos: antes de subir

```
bin/nk verificar --rubrica     # 0 errores
git status --short             # árbol limpio
git bundle verify <el bundle>  # la copia del USB es buena
```

`nk respaldo` comprueba de paso que el bundle verifica y que queda espacio: si el USB está a punto de
llenarse, para. Ninguna copia se da por buena sin su `SHA-256`.

## 7. Antes de dar la URL por buena

```
bin/nk paquete
cd dist && python3 -m http.server 8080 &
# en otra consola:
sh install.sh --base http://127.0.0.1:8080 --dir /tmp/prueba --titulo "Prueba"
cd /tmp/prueba && bin/nk estado && bin/nk verificar --rubrica && bin/nk exportar
```

Si eso funciona, la orden `curl` funciona. Está probado en `pruebas/probar_instalacion.sh`.
