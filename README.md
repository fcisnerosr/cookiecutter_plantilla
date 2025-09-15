# Cookiecutter Plantilla General

Esta es una plantilla **genérica** basada en [Cookiecutter](https://cookiecutter.readthedocs.io/) para crear proyectos en **Python**.  
Sirve como punto de partida para proyectos de análisis de datos, APIs, chatbots, ETL, etc.

---

## 🚀 Características

- Estructura de directorios mínima y organizada:
  ```
  {{ cookiecutter.project_slug }}/
  ├── src/         # código fuente
  ├── tests/       # pruebas unitarias
  ├── notebooks/   # notebooks Jupyter
  ├── scripts/     # scripts auxiliares
  ├── README.md
  ├── LICENSE
  ├── requirements.txt
  └── pyproject.toml
  ```
- `cookiecutter.json` con variables configurables:
  - Nombre del proyecto
  - Slug (normalizado para carpetas/paquete)
  - Descripción
  - Autor y correo
  - Licencia
  - Versión inicial
- Hooks automáticos:
  - **`pre_gen_project.py`** → valida que el slug sea válido y que el autor no esté vacío.  
  - **`post_gen_project.py`** → crea carpetas mínimas (`src`, `tests`, `notebooks`, `scripts`) y muestra instrucciones para configurar entorno y Git.

---

## 🛠️ Requisitos

- Python 3.10+ (recomendado 3.12)
- [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html) instalado en tu entorno:

```bash
mamba create -n cookiecutter-env python=3.12 -y
mamba activate cookiecutter-env
pip install cookiecutter
```

---

## 📦 Uso

Generar un nuevo proyecto con esta plantilla:

```bash
cookiecutter gh:fcisnerosr/cookiecutter_plantilla
```

Esto te pedirá valores para cada campo definido en `cookiecutter.json`.

---

## ⚙️ Hooks

### 🔹 `pre_gen_project.py`
- Se ejecuta **antes** de crear el proyecto.
- Valida que:
  - `project_slug` solo contenga letras, números, guiones, guiones bajos o puntos.
  - `author_name` no esté vacío.
- Si falla la validación, se cancela la generación.

### 🔹 `post_gen_project.py`
- Se ejecuta **después** de crear el proyecto.
- Acciones:
  - Crea carpetas mínimas (`src/`, `tests/`, `notebooks/`, `scripts/`).
  - Imprime **instrucciones** para:
    - Inicializar Git (`git init`).
    - Crear entorno con conda/mamba.
    - Instalar dependencias (`requirements.txt`).
- ❌ No ejecuta comandos pesados automáticamente (para evitar errores).  
- ✅ Tú decides si inicializas Git o instalas dependencias.

---

## 📖 Siguientes pasos tras generar un proyecto

1. Entrar al directorio del proyecto generado:
   ```bash
   cd {{ cookiecutter.project_slug }}
   ```
2. Inicializar Git (opcional):
   ```bash
   git init && git add . && git commit -m "Initial commit"
   ```
3. Crear un entorno y activar:
   ```bash
   mamba env create -f environment.yml
   mamba activate {{ cookiecutter.project_slug }}
   ```
4. Instalar dependencias (alternativa con pip):
   ```bash
   pip install -r requirements.txt
   ```

---

## 📌 Notas

- Los hooks se ejecutan automáticamente; no necesitas llamarlos tú.
- Esta plantilla es **general** → puedes adaptarla para proyectos de chatbot, ETL, dashboards, etc.
- Para modificarla, edita:
  - `cookiecutter.json` → variables disponibles.
  - `hooks/*.py` → lógica previa y posterior.
  - Archivos de ejemplo en `{{ cookiecutter.project_slug }}/`.

---

## 📄 Licencia

Este proyecto de plantilla está bajo la licencia que elijas en `cookiecutter.json`.  
Ejemplo: MIT, Apache-2.0, GPL-3.0, etc.
