import os
import sys
import time
import shutil
import subprocess

def is_process_running(exe_name):
    import psutil
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] and proc.info['name'].lower() == exe_name.lower():
                return True
        except Exception:
            continue
    return False

def main():
    if len(sys.argv) != 3:
        print("Uso: updater.exe <nuevo_exe> <exe_principal>")
        sys.exit(1)

    nuevo_exe = sys.argv[1]
    exe_principal = sys.argv[2]

    # Esperar a que el exe principal termine
    while is_process_running(exe_principal):
        time.sleep(1)

    # Eliminar el exe principal si existe
    if os.path.exists(exe_principal):
        try:
            os.remove(exe_principal)
        except Exception as e:
            print(f"No se pudo eliminar {exe_principal}: {e}")
            sys.exit(2)

    # Renombrar el nuevo exe
    try:
        os.rename(nuevo_exe, exe_principal)
    except Exception as e:
        print(f"No se pudo renombrar {nuevo_exe} a {exe_principal}: {e}")
        sys.exit(3)

    # Relanzar el exe principal
    try:
        subprocess.Popen([exe_principal], shell=True)
    except Exception as e:
        print(f"Error al relanzar la aplicación: {e}")
        sys.exit(4)

if __name__ == "__main__":
    main()