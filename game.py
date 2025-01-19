import os
import sys
import subprocess

# Configurações do repositório
REPO_URL = "https://raw.githubusercontent.com/Math14s/Teste/main/"
VERSION_FILE = "version.txt"
GAME_FILE = "game.py"

def get_remote_version():
    """Baixa a versão remota do arquivo."""
    os.system(f"wget -q -O remote_version.txt {REPO_URL}{VERSION_FILE}")
    if os.path.exists("remote_version.txt"):
        with open("remote_version.txt", "r") as file:
            return file.read().strip()
    return None

def update_game():
    """Baixa o código atualizado."""
    print("Atualização disponível! Baixando nova versão...")
    os.system(f"wget -q -O {GAME_FILE} {REPO_URL}{GAME_FILE}")
    print("Atualização concluída! Reiniciando o jogo...")
    # Reinicia o jogo após a atualização
    subprocess.run([sys.executable, GAME_FILE])
    sys.exit()

def main():
    """Função principal do jogo."""
    # Lê a versão local
    local_version = "1.0"  # Atualize manualmente com a versão do código
    if os.path.exists("version.txt"):
        with open("version.txt", "r") as file:
            local_version = file.read().strip()

    print(f"Versão local: {local_version}")

    # Verifica a versão remota
    remote_version = get_remote_version()
    if not remote_version:
        print("Não foi possível verificar atualizações.")
        return

    print(f"Versão remota: {remote_version}")

    # Compara versões
    if remote_version != local_version:
        update_game()
    else:
        print("O jogo já está na versão mais recente.")

    # Lógica principal do jogo
    print("Bem-vindo ao jogo!")
    # Coloque aqui o restante da lógica do seu jogo

if __name__ == "__main__":
    main()
