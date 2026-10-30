#!/bin/sh
# Prueba de extremo a extremo del camino `curl`:
#   paquete → servidor estático → install.sh → obra → nk → EPUB
#
# Uso: sh pruebas/probar_instalacion.sh
# No necesita red externa: levanta un servidor en 127.0.0.1.

set -eu

KIT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d 2>/dev/null || mktemp -d -t nk-e2e)"
PUERTO="${PUERTO:-8765}"

limpiar() {
    [ -n "${SERVIDOR:-}" ] && kill "$SERVIDOR" 2>/dev/null || true
    rm -rf "$TMP"
}
trap limpiar EXIT INT TERM

paso() { printf '\n== %s\n' "$1"; }
bien() { printf '   ok: %s\n' "$1"; }
fallo() { printf '   FALLO: %s\n' "$1" >&2; exit 1; }

paso "Construir el paquete"
"$KIT/bin/nk" paquete --destino "$KIT/dist" >/dev/null || fallo "nk paquete"
[ -f "$KIT/dist/install.sh" ] || fallo "falta dist/install.sh"
[ -f "$KIT/dist/SHA256SUMS" ] || fallo "falta dist/SHA256SUMS"
bien "dist/ generado"

paso "Servir dist/ por HTTP"
(cd "$KIT/dist" && exec python3 -m http.server "$PUERTO" >/dev/null 2>&1) &
SERVIDOR=$!
i=0
until curl -fsS "http://127.0.0.1:$PUERTO/SHA256SUMS" >/dev/null 2>&1; do
    i=$((i + 1))
    [ "$i" -gt 50 ] && fallo "el servidor no responde"
    sleep 0.1
done
bien "http://127.0.0.1:$PUERTO/"

paso "Instalar con la orden del README"
curl -fsSL "http://127.0.0.1:$PUERTO/install.sh" \
    | sh -s -- \
        --base "http://127.0.0.1:$PUERTO" \
        --dir "$TMP/obra" \
        --titulo "Obra de prueba" \
        --autor "Nadie" \
        --partes 2 --capitulos 4 --objetivo 4800 >"$TMP/install.log" 2>&1 \
    || { cat "$TMP/install.log"; fallo "install.sh"; }
grep -q "SHA-256 verificado" "$TMP/install.log" || fallo "no se verificó el hash"
bien "instalación y SHA-256"

paso "Comprobar la obra instalada"
cd "$TMP/obra"
[ -f libro.json ] || fallo "sin libro.json"
[ -x bin/nk ] || fallo "sin bin/nk ejecutable"
[ -f PROTOCOLO.md ] || fallo "sin PROTOCOLO.md"
[ -f AGENTS.md ] || fallo "sin AGENTS.md"
[ -d METODO ] || fallo "sin METODO/"
bien "árbol completo (kit + protocolo + manifiesto)"

bin/nk estado >/dev/null || fallo "nk estado"
bin/nk andamiaje >/dev/null || fallo "nk andamiaje"
bin/nk nuevo I.1 --titulo "Uno" >/dev/null || fallo "nk nuevo"
printf '\n Palabra. Palabra. Palabra. Palabra. Palabra. Palabra. Palabra. Palabra. Palabra. Palabra.\n' \
    >> MANUSCRITO/01-parte-I/01-capitulo.md
bin/nk contar >/dev/null || fallo "nk contar"
# Un capítulo de 13 palabras no puede pasar: la verificación debe detectarlo.
if bin/nk verificar --rubrica >"$TMP/verificar.log" 2>&1; then
    fallo "la verificación acepta un capítulo de 13 palabras"
fi
grep -q "palabras" "$TMP/verificar.log" || fallo "no avisa del presupuesto"
grep -q "secciones" "$TMP/verificar.log" || fallo "no avisa de las secciones"
bien "capítulo abierto, contado y la verificación detecta el hueco"

paso "Exportar"
bin/nk exportar >/dev/null || fallo "nk exportar"
python3 - "$TMP/obra/salida.epub" <<'FIN' || fallo "EPUB inválido"
import sys, zipfile
z = zipfile.ZipFile(sys.argv[1])
assert z.testzip() is None
assert z.namelist()[0] == "mimetype"
FIN
bien "EPUB válido"

paso "Pruebas del kit instalado"
(cd "$TMP/obra" && python3 -m unittest discover -s pruebas >/dev/null 2>&1) \
    && bien "pruebas del kit instalado, todas verdes" \
    || fallo "pruebas del kit instalado"

paso "Sustitución de paquete alterado"
TARBALL="$(ls "$KIT"/dist/novela-kit-*.tar.gz | head -1)"
printf 'x' >> "$TARBALL"
if curl -fsSL "http://127.0.0.1:$PUERTO/install.sh" \
        | sh -s -- --base "http://127.0.0.1:$PUERTO" --dir "$TMP/malo" \
                  --titulo "Mala" >"$TMP/malo.log" 2>&1; then
    fallo "se instaló un paquete con hash incorrecto"
fi
grep -q "SHA-256 no coincide" "$TMP/malo.log" || fallo "el error no explica el hash"
bien "un tarball alterado se rechaza"

printf '\nTODO OK\n'
