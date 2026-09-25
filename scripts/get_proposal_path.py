import sys
import subprocess

def get_modified_proposal():
    try:
        # Obtener lista de archivos cambiados respecto a main
        result = subprocess.run(
            ["git", "diff", "--name-only", "origin/main...HEAD"],
            capture_output=True,
            text=True,
            check=True
        )
        files = result.stdout.strip().splitlines()
        proposals = [f for f in files if f.startswith("proposals/") and f.endswith(".json")]
        
        if not proposals:
            print("ERROR: No se encontró ningún archivo de propuesta en proposals/", file=sys.stderr)
            sys.exit(1)
            
        # Imprime la ruta del primer archivo de propuesta encontrado
        print(proposals[0])
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    get_modified_proposal()
