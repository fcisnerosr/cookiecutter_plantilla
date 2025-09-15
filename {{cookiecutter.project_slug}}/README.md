# {{ cookiecutter.project_title }}

📦 Versión: `{{ cookiecutter.project_version }}`  
👤 Autor: [{{ cookiecutter.project_author_name }}](mailto:{{ cookiecutter.project_author_email }})  
⚖️ Licencia: {{ cookiecutter.project_license }}

---

## ✨ Descripción

{{ cookiecutter.project_description }}

Este proyecto fue generado automáticamente con [Cookiecutter](https://cookiecutter.readthedocs.io/), siguiendo buenas prácticas de estructura y organización en Python.

---

## 🚀 Requisitos

- Python {{ cookiecutter.python_version }}+
- [Mamba](https://mamba.readthedocs.io/) o [Conda](https://docs.conda.io/)
- Pip (si prefieres usarlo para dependencias)

---

## 📦 Instalación

Clona el repositorio y crea el entorno:

```bash
mamba env create -f environment.yml
mamba activate {{ cookiecutter.project_slug }}
```

O bien con `pip`:

```bash
pip install -r requirements.txt
```

---

## 📂 Estructura del proyecto

```
{{ cookiecutter.project_slug }}/
├── src/             # código fuente principal
├── tests/           # pruebas unitarias
├── notebooks/       # notebooks de exploración
├── scripts/         # scripts auxiliares
├── README.md        # este archivo
├── LICENSE
├── requirements.txt
├── environment.yml
└── pyproject.toml
```

---

## 🛠️ Uso

Ejemplo de cómo ejecutar el proyecto (ajusta según tu caso):

```bash
python scripts/run_project.py
```

O, si usas notebooks:

```bash
jupyter lab
```

---

## 🤝 Contribución

1. Haz un **fork** del repositorio.  
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).  
3. Haz tus cambios y confirma (`git commit -m "Add: nueva funcionalidad"`).  
4. Envía un **pull request** 🚀.  

---

## 📄 Licencia

Este proyecto está bajo la licencia **{{ cookiecutter.project_license }}**.  
Consulta el archivo `LICENSE` para más detalles.
