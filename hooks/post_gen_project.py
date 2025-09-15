import os

# Colores para mensajes bonitos
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Proyecto creado exitosamente. Ejecutando pasos posteriores...{RESET_ALL}")

# -------------------------------------------------
# 1. Crear carpetas mínimas necesarias
# -------------------------------------------------
print(f"{MESSAGE_COLOR}Creando carpetas mínimas...{RESET_ALL}")
folders = ['src', 'tests', 'notebooks', 'scripts']
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"{MESSAGE_COLOR}Carpeta creada: {folder}{RESET_ALL}")

# -------------------------------------------------
# 2. Instrucciones útiles (sin forzar acciones)
# -------------------------------------------------
print(f"{MESSAGE_COLOR}Siguientes pasos recomendados:{RESET_ALL}")
print("- Inicializar git manualmente si este proyecto no está en un repo:")
print("    git init && git add . && git commit -m 'Initial commit'")
print("- Crear y activar tu entorno con conda o mamba:")
print("    mamba env create -f environment.yml && mamba activate <nombre_env>")
print("- Instalar dependencias con pip si lo prefieres:")
print("    pip install -r requirements.txt")

# -------------------------------------------------
# 3. Mensaje final
# -------------------------------------------------
print(f"{MESSAGE_COLOR}Proyecto listo. ¡A trabajar! 🚀{RESET_ALL}")
