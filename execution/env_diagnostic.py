import sys
import os
import platform
import psutil
import json

def run_diagnostic():
    diagnostic = {
        "system": {
            "os": platform.system(),
            "release": platform.release(),
            "architecture": platform.machine(),
        },
        "python": {
            "version": sys.version,
            "executable": sys.executable,
            "path": sys.path
        },
        "resources": {
            "total_ram_gb": round(psutil.virtual_memory().total / (1024**3), 2),
            "available_ram_gb": round(psutil.virtual_memory().available / (1024**3), 2),
            "cpu_count": psutil.cpu_count(logical=True)
        },
        "environment": {
            "cwd": os.getcwd(),
            "conda_env": os.environ.get('CONDA_DEFAULT_ENV', 'None'),
            "has_env_file": os.path.exists('.env')
        }
    }

    print(json.dumps(diagnostic, indent=4))

    # Verificación de permisos de escritura
    try:
        test_file = '.tmp/test_write.txt'
        os.makedirs('.tmp', exist_ok=True)
        with open(test_file, 'w') as f:
            f.write('test')
        os.remove(test_file)
        print("\n[SUCCESS] Permisos de escritura validados en .tmp/")
    except Exception as e:
        print(f"\n[ERROR] Fallo en permisos de escritura: {e}")

if __name__ == "__main__":
    run_diagnostic()