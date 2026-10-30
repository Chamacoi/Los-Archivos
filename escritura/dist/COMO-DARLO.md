# Cómo entregar esto a un agente (sin publicar nada)

Generado por `nk distribuir`. Versión 1.9.0. Directorio: `/mnt/usb/los-archivos-repo/escritura/dist`.

Este paquete **no se ha subido a ninguna parte**: no hay remoto, ni URL pública, ni release. Todo se
entrega por fichero local, que es lo que permite dárselo a un agente hoy y publicarlo cuando se
quiera.

## A. Solo lectura: un fichero

El agente lee `PROTOCOLO.md` y construye el árbol él mismo. No ejecuta código.

```
curl -fsSL file:///mnt/usb/los-archivos-repo/escritura/dist/PROTOCOLO.md -o PROTOCOLO.md
```

Si el agente no puede leer rutas locales, se le pega el contenido (`cat PROTOCOLO.md`) o se le pasa
el fichero por el canal que uses.

## B. Instalación por `curl` local (sin servidor)

`curl` acepta `file://`, así que no hace falta levantar nada:

```
curl -fsSL file:///mnt/usb/los-archivos-repo/escritura/dist/install.sh | sh -s --   --base file:///mnt/usb/los-archivos-repo/escritura/dist   --dir mi-obra --titulo "Mi obra" --autor "Quien firma"   --partes 2 --capitulos 20 --objetivo 60000
```

Comprueba el SHA-256 y deja la obra con el kit dentro. Si el agente corre en otra máquina o en un
sandbox sin acceso a tu disco, usa C o D.

## C. Repositorio completo por bundle (historial incluido)

Un `.bundle` **es un repositorio**: se clona como si estuviera en un servidor, sin subirlo a
ninguno.

```
git clone /mnt/usb/los-archivos-repo/escritura/dist/(sin bundle: este directorio no es un repositorio git) novela-kit
cd novela-kit
git log --oneline          # historial completo
git bundle verify /mnt/usb/los-archivos-repo/escritura/dist/(sin bundle: este directorio no es un repositorio git)
bin/nk --version
```

Y desde ahí, la obra:

```
bin/nk init ../mi-obra --titulo "Mi obra" --partes 2 --capitulos 20 --objetivo 60000
```

Ventaja frente al tarball: el agente ve el historial, las decisiones y las pruebas; puede comparar y
revertir. Se puede firmar y verificar con GPG si hace falta.

## D. Servidor local (para otro ordenador o un sandbox con red)

```
cd /mnt/usb/los-archivos-repo/escritura/dist && python3 -m http.server 8080
```

Y en el otro lado, la orden de B cambiando `file://$(d)s` por `http://IP-DEL-ORDENADOR:8080`.

## E. Cuando sí se quiera publicar (más adelante)

El repo ya está preparado: `.gitignore`, `.gitattributes`, `LICENSE-CODIGO`, `LICENSE-TEXTO`,
`.github/workflows/pruebas.yml`. Sin nada que limpiar a mano.

```
gh repo create novela-kit --public --source . --push   # requiere decidirlo antes
```

O, sin `gh`: crear el repo vacío en la web, `git remote add origin …` y `git push -u origin main`.
Un repositorio local **no es un respaldo**: el bundle sí sirve como copia.

## F. Si lo que se entrega es una obra que ya existe

No hace falta instalar nada: la obra lleva el kit dentro (`escritura/`). Se empaqueta su historial y
se clona igual:

```
cd /ruta/a/la-obra && git bundle create /tmp/obra.bundle --all
git clone /tmp/obra.bundle /tmp/obra
cd /tmp/obra && escritura/bin/nk estado && escritura/bin/nk contar
```

Y si la obra aún no lleva el kit, se instala uno nuevo y se copian encima `APUNTES.md`, `SINOPSIS/`,
`ESTUDIOS/`, `MANUSCRITO/` y `libro.json`: el manifiesto manda los números.

## Qué pegarle al agente

> Tienes el kit en `/mnt/usb/los-archivos-repo/escritura/dist` (o clonado de `(sin bundle: este directorio no es un repositorio git)`). Lee `PROTOCOLO.md` y `AGENTS.md`.
> Instala la obra con la orden de `COMO-DARLO.md` apartado B, o construye el árbol siguiendo
> `PROTOCOLO.md` §2-§3 si no puedes ejecutar código.
> Después: `bin/nk andamiaje`, `bin/nk nuevo I.1 --titulo "Primer capítulo"` y escribe el capítulo
> según el presupuesto. Antes de dármelo: `bin/nk verificar --rubrica`.
> No inventes canon, ni nombres, ni cifras. No publiques nada.

## Aviso

`novela-kit-1.9.0.tar.gz` es reproducible: dos `nk paquete` seguidos dan el mismo SHA-256. Cualquier cambio en el
paquete se ve en `SHA256SUMS`. Un agente debe revisar `install.sh` antes de ejecutarlo, aunque sea
local.
