# conftest.py → pytest lo carga automáticamente
import sys, os

# Añade la raíz del proyecto a sys.path (para que se pueda hacer import app, import src, etc.)
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
