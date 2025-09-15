import sys
import re

# Variables de cookiecutter
project_slug = "{{ cookiecutter.project_slug }}"
author_name = "{{ cookiecutter.project_author_name }}"

# Validar que el slug no tenga caracteres raros
# (permitimos letras, números, guiones, guiones bajos y puntos)
if not re.match(r'^[a-zA-Z0-9_.-]+$', project_slug):
    print(f"ERROR: El nombre del proyecto '{project_slug}' contiene caracteres no permitidos.")
    print("Usa solo letras, números, puntos, guiones y guiones bajos (a-z, A-Z, 0-9, ., -, _).")
    sys.exit(1)

# Validar que el autor no esté vacío
if not author_name.strip():
    print("ERROR: El nombre del autor no puede estar vacío.")
    sys.exit(1)

print("✔ Validaciones previas completadas con éxito.")
