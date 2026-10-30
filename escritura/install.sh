#!/bin/sh
# novela-kit — instalador.
#
# Crea una obra nueva a partir del kit publicado en una URL:
#
#   curl -fsSL https://TU-DOMINIO/install.sh | sh -s -- --dir mi-obra --titulo "Mi obra"
#
# O con el fichero ya descargado:
#
#   sh install.sh --base https://TU-DOMINIO --dir mi-obra --titulo "Mi obra"
#
# Qué hace: descarga el paquete, comprueba su SHA-256, lo extrae en un directorio
# temporal y ejecuta `nk init`, que deja la obra con el kit dentro (bin/, METODO/,
# PROMPTS/, PLANTILLAS/, EJEMPLO/, pruebas/) y su libro.json.
#
# No necesita root, ni git, ni red más allá de la descarga. Solo python3 y tar.

set -eu

VERSION_POR_DEFECTO="1.9.0"
BASE="${NOVELA_KIT_BASE:-}"
VERSION="${NOVELA_KIT_VERSION:-auto}"
DIR=""
TITULO=""
AUTOR=""
FUENTE=""
PARTES="2"
CAPITULOS="20"
OBJETIVO="60000"
TARBALL_LOCAL=""
VERIFICAR="si"
PYTHON="${PYTHON:-python3}"

morir() {
    printf 'novela-kit: %s\n' "$1" >&2
    exit "${2:-1}"
}

ayuda() {
    cat <<'FIN'
novela-kit — instalador

Uso:
  sh install.sh --base URL --dir DIR --titulo TEXTO [opciones]

Opciones:
  --base URL          URL donde están install.sh, SHA256SUMS y el .tar.gz
                      (o variable NOVELA_KIT_BASE, o --archivo para uso local)
  --dir DIR           Directorio de la obra nueva (obligatorio)
  --titulo TEXTO      Título de la obra (obligatorio)
  --autor TEXTO       Titularidad del colofón (no es la autoría del relato)
  --fuente TEXTO      Fuente del archivo (una línea)
  --partes N          Número de partes (por defecto 2)
  --capitulos N       Capítulos totales (por defecto 20)
  --objetivo N        Palabras objetivo (por defecto 60000)
  --version X.Y.Z     Versión del paquete (por defecto: la que anuncie BASE/VERSION)
  --archivo RUTA      Instalar desde un .tar.gz local (sin red)
  --sin-verificar     No comprobar el SHA-256 (no recomendado)
  --ayuda             Esta ayuda

Ejemplo:
  curl -fsSL https://ejemplo.org/novela-kit/install.sh \
    | sh -s -- --dir novelas/mi-obra --titulo "Mi obra" --autor "Yo"
FIN
}

while [ "$#" -gt 0 ]; do
    case "$1" in
        --base) [ "$#" -ge 2 ] || morir "--base necesita un valor"; BASE="$2"; shift 2 ;;
        --dir) [ "$#" -ge 2 ] || morir "--dir necesita un valor"; DIR="$2"; shift 2 ;;
        --titulo) [ "$#" -ge 2 ] || morir "--titulo necesita un valor"; TITULO="$2"; shift 2 ;;
        --autor) [ "$#" -ge 2 ] || morir "--autor necesita un valor"; AUTOR="$2"; shift 2 ;;
        --fuente) [ "$#" -ge 2 ] || morir "--fuente necesita un valor"; FUENTE="$2"; shift 2 ;;
        --partes) [ "$#" -ge 2 ] || morir "--partes necesita un valor"; PARTES="$2"; shift 2 ;;
        --capitulos) [ "$#" -ge 2 ] || morir "--capitulos necesita un valor"; CAPITULOS="$2"; shift 2 ;;
        --objetivo) [ "$#" -ge 2 ] || morir "--objetivo necesita un valor"; OBJETIVO="$2"; shift 2 ;;
        --version) [ "$#" -ge 2 ] || morir "--version necesita un valor"; VERSION="$2"; shift 2 ;;
        --archivo) [ "$#" -ge 2 ] || morir "--archivo necesita un valor"; TARBALL_LOCAL="$2"; shift 2 ;;
        --sin-verificar) VERIFICAR="no"; shift ;;
        -h|--ayuda) ayuda; exit 0 ;;
        *) morir "opción desconocida: $1 (usa --ayuda)" 2 ;;
    esac
done

[ -n "$DIR" ] || morir "falta --dir (usa --ayuda)"
[ -n "$TITULO" ] || morir "falta --titulo (usa --ayuda)"
[ -n "$BASE" ] || [ -n "$TARBALL_LOCAL" ] || morir "falta --base o --archivo (usa --ayuda)"

command -v tar >/dev/null 2>&1 || morir "hace falta tar"

"$PYTHON" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)' \
    || morir "hace falta python3 3.8 o superior"

TMP="$(mktemp -d 2>/dev/null || mktemp -d -t novela-kit)" || morir "no se puede crear un temporal"
trap 'rm -rf "$TMP"' EXIT INT TERM


descargar() {
    # descargar URL DESTINO
    if command -v curl >/dev/null 2>&1; then
        curl -fsSL "$1" -o "$2" && return 0
    fi
    if command -v wget >/dev/null 2>&1; then
        wget -qO "$2" "$1" && return 0
    fi
    return 1
}

sha256() {
    if command -v sha256sum >/dev/null 2>&1; then
        sha256sum "$1" | awk '{print $1}'
    elif command -v shasum >/dev/null 2>&1; then
        shasum -a 256 "$1" | awk '{print $1}'
    else
        "$PYTHON" - "$1" <<'FIN'
import hashlib, sys
h = hashlib.sha256()
with open(sys.argv[1], "rb") as fh:
    for trozo in iter(lambda: fh.read(65536), b""):
        h.update(trozo)
print(h.hexdigest())
FIN
    fi
}

# Versión: si no se pidió una concreta, se anuncia en BASE/VERSION; si no, la de reserva.
if [ "$VERSION" = "auto" ]; then
    VERSION="$VERSION_POR_DEFECTO"
    if [ -n "$BASE" ] && descargar "${BASE%/}/VERSION" "$TMP/VERSION" 2>/dev/null; then
        anunciada="$(tr -d ' \t\r\n' < "$TMP/VERSION")"
        [ -n "$anunciada" ] && VERSION="$anunciada"
    fi
fi

NOMBRE="novela-kit-$VERSION"
TARBALL="$NOMBRE.tar.gz"

if [ -n "$TARBALL_LOCAL" ]; then
    [ -f "$TARBALL_LOCAL" ] || morir "no existe el fichero $TARBALL_LOCAL"
    cp "$TARBALL_LOCAL" "$TMP/$TARBALL"
    printf 'Paquete local: %s\n' "$TARBALL_LOCAL"
else
    BASE="${BASE%/}"
    printf 'Descargando %s/...\n' "$BASE"
    descargar "$BASE/$TARBALL" "$TMP/$TARBALL" || morir "no se puede descargar $BASE/$TARBALL"
fi

if [ "$VERIFICAR" = "si" ]; then
    if [ -n "$BASE" ] && descargar "$BASE/SHA256SUMS" "$TMP/SHA256SUMS" 2>/dev/null; then
        esperado="$(awk -v n="$TARBALL" '$2 == n {print $1}' "$TMP/SHA256SUMS")"
        if [ -n "$esperado" ]; then
            obtenido="$(sha256 "$TMP/$TARBALL")"
            [ "$esperado" = "$obtenido" ] || morir "el SHA-256 no coincide: paquete alterado o incompleto"
            printf 'SHA-256 verificado.\n'
        else
            printf 'Aviso: SHA256SUMS no incluye %s; sigo sin verificar.\n' "$TARBALL" >&2
        fi
    else
        if [ -n "$TARBALL_LOCAL" ]; then
            printf 'Aviso: instalación local sin SHA256SUMS.\n' >&2
        else
            morir "no se puede descargar $BASE/SHA256SUMS (usa --sin-verificar para omitir)"
        fi
    fi
fi

(
    umask 022
    mkdir -p "$TMP/kit"
    tar -xzf "$TMP/$TARBALL" -C "$TMP/kit"
) || morir "no se puede extraer el paquete"

KIT="$TMP/kit/$NOMBRE"
[ -f "$KIT/bin/nk" ] || morir "el paquete no contiene bin/nk"

printf 'Creando obra en %s\n' "$DIR"
"$PYTHON" "$KIT/bin/nk" init "$DIR" \
    --titulo "$TITULO" \
    --autor "$AUTOR" \
    --fuente "$FUENTE" \
    --partes "$PARTES" \
    --capitulos "$CAPITULOS" \
    --objetivo "$OBJETIVO" || morir "falló la creación de la obra"

cat <<FIN

Listo. Obra creada en: $DIR

Siguiente:
  cd "$DIR"
  bin/nk andamiaje
  bin/nk nuevo I.1 --titulo "Primer capítulo"
  bin/nk estado
  bin/nk verificar --rubrica

Antes de escribir, lee:
  PROTOCOLO.md   (si trabajas con un agente: qué hacer, en qué orden)
  AGENTS.md      (reglas duras)
  METODO/02-voz.md y METODO/08-rubrica.md

El kit no escribe por ti: fija el esqueleto, la voz verificable y las comprobaciones.
FIN
