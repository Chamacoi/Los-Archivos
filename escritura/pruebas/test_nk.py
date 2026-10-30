"""Pruebas del kit. Se ejecutan con: python3 -m unittest discover -s pruebas -v"""

import contextlib
import importlib.machinery
import importlib.util
import io
import json
import os
import shutil
import tarfile
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
_cargador = importlib.machinery.SourceFileLoader("nk", str(KIT / "bin" / "nk"))
_spec = importlib.util.spec_from_loader("nk", _cargador)
nk = importlib.util.module_from_spec(_spec)
_cargador.exec_module(nk)


@contextlib.contextmanager
def en(directorio):
    anterior = os.getcwd()
    os.chdir(directorio)
    try:
        yield
    finally:
        os.chdir(anterior)


def ejecutar(*args):
    """Ejecuta nk en proceso y devuelve (código, salida)."""
    salida = io.StringIO()
    with contextlib.redirect_stdout(salida):
        codigo = nk.main(list(args))
    return codigo, salida.getvalue()


class Contar(unittest.TestCase):
    def test_marcas_no_cuentan(self):
        man = {"conteo": {"metodo": "palabras"}}
        texto = "## 1. Título\n\n> Hola, — mundo.\n"
        self.assertEqual(nk.contar_palabras(texto, man), 3)

    def test_tokens_reproduce_wc(self):
        man = {"conteo": {"metodo": "tokens"}}
        texto = "## 1. Título\n\n> Hola, — mundo.\n"
        self.assertEqual(nk.contar_palabras(texto, man), len(texto.split()))

    def test_frontmatter_y_codigo(self):
        man = {"conteo": {"metodo": "palabras"}}
        texto = "---\ntitulo: x\n---\n\nUno dos.\n\n```\nerror: tres\n```\n"
        self.assertEqual(nk.contar_palabras(texto, man), 4)

    def test_citas(self):
        texto = "Narración corta.\n\n> Acta con cuatro palabras.\n"
        self.assertEqual(nk.palabras_citadas(texto), 4)


class Presupuesto(unittest.TestCase):
    def test_reparto_explicito(self):
        man = {"libro": {}, "partes": [
            {"id": "I", "capitulos": 4, "presupuesto": {"reparto": {"3025": 2, "3024": 2}}}]}
        pre, total = nk.presupuestos_parte(man, man["partes"][0])
        self.assertEqual(pre, [3025, 3025, 3024, 3024])
        self.assertEqual(total, 12098)

    def test_reparto_iguales_con_resto(self):
        man = {"libro": {"objetivo_palabras": 10}, "partes": [{"id": "I", "capitulos": 3}]}
        pre, total = nk.presupuestos_parte(man, man["partes"][0])
        self.assertEqual(pre, [4, 3, 3])
        self.assertEqual(total, 10)


class Verificar(unittest.TestCase):
    def setUp(self):
        self.dir = Path(tempfile.mkdtemp())
        shutil.copytree(KIT / "EJEMPLO", self.dir / "obra")
        self.obra = self.dir / "obra"

    def tearDown(self):
        shutil.rmtree(self.dir, ignore_errors=True)

    def test_limpio(self):
        with en(self.obra):
            codigo, salida = ejecutar("verificar", "--rubrica")
        self.assertEqual(codigo, 0, salida)
        self.assertIn("Sin incidencias", salida)

    def test_frase_prohibida(self):
        cap = self.obra / "MANUSCRITO" / "01-parte-I" / "01-capitulo.md"
        cap.write_text(cap.read_text(encoding="utf-8") +
                       "\nY en definitiva nos quedó esta paz.\n", encoding="utf-8")
        with en(self.obra):
            codigo, salida = ejecutar("verificar")
        self.assertEqual(codigo, 1)
        self.assertIn("frase prohibida", salida)

    def test_dato_sensible(self):
        cap = self.obra / "MANUSCRITO" / "01-parte-I" / "01-capitulo.md"
        cap.write_text(cap.read_text(encoding="utf-8") +
                       "\nEscribe a alguien@example.com o al 612 34 56 78.\n", encoding="utf-8")
        with en(self.obra):
            codigo, salida = ejecutar("verificar")
        self.assertEqual(codigo, 1)
        self.assertIn("correo", salida)
        self.assertIn("teléfono", salida)

    def test_canon_inexistente(self):
        cap = self.obra / "MANUSCRITO" / "01-parte-I" / "01-capitulo.md"
        cap.write_text(cap.read_text(encoding="utf-8") + "\nComo dice C-9.\n", encoding="utf-8")
        with en(self.obra):
            codigo, salida = ejecutar("verificar")
        self.assertEqual(codigo, 1)
        self.assertIn("C-9", salida)

    def test_tecnicismo_fuera_de_citas(self):
        import json
        man = json.loads((self.obra / "libro.json").read_text(encoding="utf-8"))
        man["verificacion"]["tecnicismos"] = ["contexto", "modelo"]
        (self.obra / "libro.json").write_text(json.dumps(man, ensure_ascii=False), encoding="utf-8")
        cap = self.obra / "MANUSCRITO" / "01-parte-I" / "01-capitulo.md"
        texto = cap.read_text(encoding="utf-8")
        # En la voz del narrador: aviso. Dentro de una cita: permitido.
        cap.write_text(texto + "\nEl contexto se perdió y el modelo no lo dijo.\n\n"
                              "> Error: context length exceeded (el modelo se corta).\n",
                       encoding="utf-8")
        with en(self.obra):
            _, salida = ejecutar("verificar")
        self.assertIn("tecnicismo en la voz del narrador: «contexto»", salida)
        self.assertIn("tecnicismo en la voz del narrador: «modelo»", salida)
        # Una sola mención por término, aunque aparezca también citado.
        self.assertEqual(salida.count("«contexto»"), 1)

    def test_palabra_solo_en_citas(self):
        import json
        man = json.loads((self.obra / "libro.json").read_text(encoding="utf-8"))
        man["verificacion"]["solo_en_citas"] = ["mesías"]
        (self.obra / "libro.json").write_text(json.dumps(man, ensure_ascii=False), encoding="utf-8")
        cap = self.obra / "MANUSCRITO" / "01-parte-I" / "01-capitulo.md"
        texto = cap.read_text(encoding="utf-8")
        cap.write_text(texto + "\nAquí la palabra «mesías» está tachada.\n", encoding="utf-8")
        with en(self.obra):
            _, salida = ejecutar("verificar")
        self.assertNotIn("solo puede aparecer en citas", salida)
        cap.write_text(texto + "\nEl mesías abrió la caja.\n", encoding="utf-8")
        with en(self.obra):
            _, salida = ejecutar("verificar")
        self.assertIn("«mesías» solo puede aparecer en citas", salida)

    def test_ego_del_narrador(self):
        cap = self.obra / "MANUSCRITO" / "01-parte-I" / "01-capitulo.md"
        texto = cap.read_text(encoding="utf-8")
        cap.write_text(texto + "\nPor decirlo así, el cuaderno aguanta.\n\n"
                              "> Valga la palabra: así consta.\n", encoding="utf-8")
        with en(self.obra):
            _, salida = ejecutar("verificar")
        self.assertIn("ego del narrador: «por decirlo así»", salida)
        # La misma fórmula dentro de una cita no cuenta.
        self.assertNotIn("«valga la palabra»", salida)

    def test_nombre_propio(self):
        cap = self.obra / "MANUSCRITO" / "01-parte-I" / "01-capitulo.md"
        cap.write_text(cap.read_text(encoding="utf-8") +
                       "\nLo dijo Marcial desde la puerta.\n", encoding="utf-8")
        with en(self.obra):
            _, salida = ejecutar("verificar")
        self.assertIn("Marcial", salida)


class Exportar(unittest.TestCase):
    def test_epub_bien_formado_y_reproducible(self):
        with tempfile.TemporaryDirectory() as tmp:
            a = Path(tmp) / "a.epub"
            b = Path(tmp) / "b.epub"
            with en(KIT / "EJEMPLO"):
                self.assertEqual(ejecutar("exportar", "--salida", str(a))[0], 0)
                self.assertEqual(ejecutar("exportar", "--salida", str(b))[0], 0)
            self.assertEqual(a.read_bytes(), b.read_bytes())
            with zipfile.ZipFile(a) as z:
                self.assertIsNone(z.testzip())
                self.assertEqual(z.namelist()[0], "mimetype")
                self.assertEqual(z.getinfo("mimetype").compress_type, zipfile.ZIP_STORED)
                for nombre in z.namelist():
                    if nombre.endswith((".xhtml", ".opf", ".xml")):
                        ET.fromstring(z.read(nombre))
                self.assertIn("cap-001.xhtml", z.read("OEBPS/content.opf").decode())

    def test_colofon(self):
        with tempfile.TemporaryDirectory() as tmp:
            destino = Path(tmp) / "c.epub"
            with en(KIT / "EJEMPLO"):
                self.assertEqual(ejecutar("exportar", "--salida", str(destino))[0], 0)
                man = json.loads((KIT / "EJEMPLO" / "libro.json").read_text(encoding="utf-8"))
                man["libro"]["colofon"] = "© 2026 Nadie. Todos los derechos reservados."
                (KIT / "EJEMPLO" / "libro.json").write_text(json.dumps(man, ensure_ascii=False),
                                                            encoding="utf-8")
                try:
                    self.assertEqual(ejecutar("exportar", "--salida", str(destino))[0], 0)
                    with zipfile.ZipFile(destino) as z:
                        self.assertIn("OEBPS/text/colofon.xhtml", z.namelist())
                finally:
                    man["libro"].pop("colofon", None)
                    (KIT / "EJEMPLO" / "libro.json").write_text(
                        json.dumps(man, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class ObjetivoReferencia(unittest.TestCase):
    def _obra(self, tmp, tipo, palabras):
        obra = Path(tmp) / "obra"
        with en(KIT):
            ejecutar("init", str(obra), "--titulo", "T", "--partes", "1",
                     "--capitulos", "1", "--objetivo", "1000")
        man = json.loads((obra / "libro.json").read_text(encoding="utf-8"))
        man["libro"]["objetivo_tipo"] = tipo
        (obra / "libro.json").write_text(json.dumps(man, ensure_ascii=False), encoding="utf-8")
        with en(obra):
            ejecutar("andamiaje")
            ejecutar("nuevo", "I.1", "--titulo", "Uno")
        cap = obra / "MANUSCRITO" / "01-parte-I" / "01-capitulo.md"
        cap.write_text("# Capítulo 1. Uno\n\n" + ("palabra. " * palabras) + "\n",
                       encoding="utf-8")
        return obra

    def test_referencia_avisa_si_el_total_se_va(self):
        with tempfile.TemporaryDirectory() as tmp:
            obra = self._obra(tmp, "referencia", 500)
            with en(obra):
                _, salida = ejecutar("verificar")
            self.assertIn("frente a una referencia", salida)

    def test_referencia_dentro_de_tolerancia(self):
        with tempfile.TemporaryDirectory() as tmp:
            obra = self._obra(tmp, "referencia", 960)
            with en(obra):
                _, salida = ejecutar("verificar")
            self.assertNotIn("frente a una referencia", salida)

    def test_cifra_exacta_no_juzga_el_total(self):
        with tempfile.TemporaryDirectory() as tmp:
            obra = self._obra(tmp, "exacta", 500)
            with en(obra):
                _, salida = ejecutar("verificar")
            self.assertNotIn("frente a una referencia", salida)


class Andamiaje(unittest.TestCase):
    def test_nuevo_y_recuento(self):
        with tempfile.TemporaryDirectory() as tmp:
            obra = Path(tmp) / "obra"
            with en(KIT):
                ejecutar("init", str(obra), "--titulo", "T", "--partes", "1",
                         "--capitulos", "3", "--objetivo", "3000")
            self.assertTrue((obra / "libro.json").is_file())
            self.assertTrue((obra / "bin" / "nk").is_file())
            self.assertTrue((obra / "METODO" / "05-proceso.md").is_file())
            self.assertTrue((obra / "APUNTES.md").is_file())
            self.assertIn("# T", (obra / "README.md").read_text(encoding="utf-8"))
            with en(obra):
                self.assertEqual(ejecutar("andamiaje")[0], 0)
                self.assertEqual(ejecutar("nuevo", "I.1", "--titulo", "Uno")[0], 0)
                ruta = obra / "MANUSCRITO" / "01-parte-I" / "01-capitulo.md"
                self.assertTrue(ruta.is_file())
                texto = ruta.read_text(encoding="utf-8")
                self.assertTrue(texto.startswith("# Capítulo 1. Uno"))
                self.assertIn("presupuesto: 1000", texto)
                ruta.write_text(texto + "\nPalabra. " * 10, encoding="utf-8")
                self.assertEqual(ejecutar("contar", "--actualizar")[0], 0)
                estructura = (obra / "ESTRUCTURA.md").read_text(encoding="utf-8")
                self.assertIn("| I.1 |", estructura)
                self.assertEqual(ejecutar("informe")[0], 0)
                self.assertTrue((obra / "estado.json").is_file())


class Paquete(unittest.TestCase):
    def test_reproducible_y_con_hashes(self):
        import hashlib
        with tempfile.TemporaryDirectory() as tmp:
            a = Path(tmp) / "a"
            b = Path(tmp) / "b"
            self.assertEqual(ejecutar("paquete", "--destino", str(a))[0], 0)
            self.assertEqual(ejecutar("paquete", "--destino", str(b))[0], 0)
            nombres = sorted(p.name for p in a.iterdir())
            self.assertEqual(nombres, sorted(p.name for p in b.iterdir()))
            for nombre in nombres:
                ha = hashlib.sha256((a / nombre).read_bytes()).hexdigest()
                hb = hashlib.sha256((b / nombre).read_bytes()).hexdigest()
                self.assertEqual(ha, hb, nombre)
            tarball = [n for n in nombres if n.endswith(".tar.gz")][0]
            sumas = (a / "SHA256SUMS").read_text(encoding="utf-8")
            self.assertIn(tarball, sumas)
            self.assertIn("install.sh", sumas)
            self.assertIn("PROTOCOLO.md", sumas)
            self.assertTrue((a / "FICHEROS.txt").read_text(encoding="utf-8"))
            with tarfile.open(a / tarball) as tf:
                miembros = tf.getnames()
            raiz = tarball.replace(".tar.gz", "")
            self.assertIn(raiz + "/bin/nk", miembros)
            self.assertIn(raiz + "/PROTOCOLO.md", miembros)
            self.assertIn(raiz + "/EJEMPLO/libro.json", miembros)
            for m in miembros:
                self.assertNotIn("__pycache__", m)


if __name__ == "__main__":
    unittest.main()
