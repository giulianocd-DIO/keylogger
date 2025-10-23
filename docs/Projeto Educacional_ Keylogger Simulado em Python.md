# Projeto Educacional: Keylogger Simulado em Python

## 📋 Visão Geral

Este projeto apresenta uma implementação educacional de um keylogger em Python, desenvolvido em um **ambiente controlado de estudo** para fins de aprendizado em cibersegurança. O projeto demonstra como keyloggers funcionam, implementa técnicas de captura de teclas, ocultação e envio remoto de dados, além de documentar medidas de defesa contra essas ameaças.

**⚠️ AVISO IMPORTANTE**: Este projeto é exclusivamente para fins educacionais em ambientes controlados. O uso de keyloggers em sistemas sem autorização explícita é **ILEGAL** na maioria das jurisdições.

---

## 🎯 Objetivos do Projeto

- Compreender o funcionamento técnico de keyloggers
- Implementar captura de teclas usando a biblioteca `pynput`
- Desenvolver técnicas de ocultação e furtividade
- Implementar envio automático de dados por e-mail
- Documentar medidas de defesa e prevenção
- Aprender sobre segurança defensiva em cibersegurança

---

## 📁 Estrutura do Projeto

```
Keylogger/
├── Keylogger.py                    # Script básico de captura de teclas
├── Keylogger_Furtivo.py            # Script com técnicas de ocultação
├── Keylogger_Email.py              # Script com envio por e-mail
├── Medidas_de_Defesa_Keylogger.md  # Documentação de defesa
├── README.md                        # Este arquivo
├── Teste_ambiente/                 # Pasta para testes
├── log.txt                         # Arquivo de log de exemplo
└── teste_demo.txt                  # Arquivo de demonstração
```

---

## 🔧 Requisitos do Sistema

### Dependências de Software

- **Python 3.7+**: Linguagem de programação
- **pip**: Gerenciador de pacotes Python
- **pynput**: Biblioteca para captura de teclado
- **secure-smtplib**: Biblioteca para envio seguro de e-mail

### Sistemas Operacionais Suportados

- ✅ Windows 10/11
- ✅ Linux (Ubuntu, Debian, Fedora, etc.)
- ✅ macOS

### Requisitos de Hardware

- Mínimo: 512 MB de RAM
- Processador: Qualquer processador moderno
- Espaço em disco: 50 MB

---

## 📦 Instalação

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu_usuario/Keylogger.git
cd Keylogger
```

### 2. Criar Ambiente Virtual (Recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

Ou instale manualmente:

```bash
pip install pynput secure-smtplib
```

### 4. Verificar Instalação

```bash
python -c "import pynput; print('pynput instalado com sucesso')"
```

---

## 🚀 Como Usar

### Script 1: Keylogger Básico

O script `Keylogger.py` implementa a captura básica de teclas e as salva em um arquivo de log.

**Uso:**

```bash
python Keylogger.py
```

**Funcionalidades:**

- Captura todas as teclas pressionadas
- Registra em arquivo `log.txt`
- Ignora teclas modificadoras (Shift, Ctrl, Alt)
- Registra teclas especiais (Enter, Tab, Backspace, Esc)
- Parada com Ctrl+C

**Exemplo de Saída:**

```
[*] Keylogger iniciado...
[*] Registrando teclas em: Keylogger/log.txt
[*] Pressione Ctrl+C para parar

usuario123 [SPACE] senha_secreta [ENTER]
```

### Script 2: Keylogger Furtivo

O script `Keylogger_Furtivo.py` implementa técnicas de ocultação e execução em background.

**Uso:**

```bash
python Keylogger_Furtivo.py
```

**Funcionalidades:**

- Ocultação de console (Windows)
- Execução em thread de background
- Envio periódico de dados (simulado)
- Arquivo de log oculto (Windows)
- Técnicas de persistência (documentadas)

**Técnicas Implementadas:**

- Minimização de janela do console
- Execução em thread daemon
- Arquivo de log com atributo oculto
- Simulação de envio remoto periódico

### Script 3: Keylogger com Envio por E-mail

O script `Keylogger_Email.py` implementa captura de teclas com envio automático por e-mail.

**Configuração:**

Edite o arquivo `Keylogger_Email.py` e configure as credenciais:

```python
EMAIL_ORIGEM = "seu_email@gmail.com"
SENHA_EMAIL = "sua_senha_app"
EMAIL_DESTINO = "destino@gmail.com"
```

**Para Gmail:**

1. Ativar autenticação de dois fatores
2. Gerar senha de app: https://support.google.com/accounts/answer/185833
3. Usar a senha de app no script

**Uso:**

```bash
python Keylogger_Email.py
```

**Funcionalidades:**

- Captura de teclas contínua
- Envio automático por e-mail a cada 60 segundos
- Formatação HTML das mensagens
- Tratamento de erros de conexão
- Envio de dados restantes ao finalizar

**Exemplo de E-mail Enviado:**

```
Assunto: Dados Capturados - 2025-10-22 14:30:45

Dados Capturados pelo Keylogger
Data/Hora: 2025-10-22 14:30:45
Quantidade de Teclas: 245

Conteúdo Capturado:
usuario123
senha_secreta
Email: usuario@empresa.com
...
```

---

## 📊 Arquivos de Log

Os scripts geram arquivos de log contendo as teclas capturadas:

| Arquivo | Script | Conteúdo |
|---------|--------|----------|
| `log.txt` | Keylogger.py | Teclas capturadas básicas |
| `log_furtivo.txt` | Keylogger_Furtivo.py | Teclas capturadas furtivas |
| `log_email.txt` | Keylogger_Email.py | Teclas capturadas com e-mail |

**Formato do Log:**

```
=== KEYLOGGER - Iniciado em 2025-10-22 14:30:45.123456 ===
usuario123
senha_secreta
Email: usuario@empresa.com
Telefone: (11) 98765-4321
```

---

## 🛡️ Medidas de Defesa

Para informações detalhadas sobre como se defender contra keyloggers, consulte o arquivo `Medidas_de_Defesa_Keylogger.md`.

### Resumo das Defesas

| Camada | Medida | Descrição |
|--------|--------|-----------|
| **Prevenção** | Antivírus | Detecta keyloggers conhecidos |
| **Prevenção** | Firewall | Bloqueia comunicações suspeitas |
| **Detecção** | EDR | Monitora comportamento anômalo |
| **Resposta** | Isolamento | Desconecta sistema da rede |
| **Recuperação** | Backups | Restaura dados não comprometidos |

### Boas Práticas

- ✅ Manter antivírus e firewall ativados
- ✅ Instalar atualizações de segurança regularmente
- ✅ Usar senhas fortes e únicas
- ✅ Ativar autenticação multifator
- ✅ Desconfiar de e-mails suspeitos
- ✅ Usar teclado virtual para dados sensíveis
- ✅ Monitorar atividade de rede

---

## 🔍 Análise Técnica

### Funcionamento do Keylogger

```
┌─────────────────────────────────────────────────┐
│  1. Listener de Teclado (pynput)               │
│     - Monitora eventos de teclado              │
│     - Captura cada tecla pressionada           │
└─────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────┐
│  2. Processamento de Tecla                     │
│     - Identifica tipo de tecla                 │
│     - Filtra teclas modificadoras              │
│     - Formata teclas especiais                 │
└─────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────┐
│  3. Armazenamento                              │
│     - Escreve em arquivo local                 │
│     - Ou envia para servidor remoto            │
└─────────────────────────────────────────────────┘
```

### Bibliotecas Utilizadas

**pynput**

A biblioteca `pynput` fornece controle de mouse e teclado em Python. Funciona em Windows, Linux e macOS.

```python
from pynput import keyboard

def on_press(key):
    print(f'Tecla pressionada: {key}')

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
```

**secure-smtplib**

Extensão segura da biblioteca `smtplib` para envio de e-mails com suporte a TLS/SSL.

```python
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, senha)
server.send_message(msg)
```

---

## 🧪 Testes e Validação

### Teste 1: Captura Básica

```bash
python Keylogger.py
# Digite: "teste123"
# Verifique log.txt
```

**Resultado Esperado:**

```
teste123
```

### Teste 2: Teclas Especiais

```bash
python Keylogger.py
# Digite: "senha" + Enter + Tab
# Verifique log.txt
```

**Resultado Esperado:**

```
senha
 [ENTER] 
 [TAB] 
```

### Teste 3: Envio por E-mail

```bash
python Keylogger_Email.py
# Digite algumas teclas
# Aguarde 60 segundos
# Verifique e-mail de destino
```

**Resultado Esperado:**

E-mail recebido com os dados capturados.

---

## 📚 Recursos Educacionais

### Conceitos Relacionados

- **Keyloggers**: Ferramentas que capturam entrada de teclado
- **Spyware**: Software que monitora atividade do usuário
- **Malware**: Software malicioso com múltiplas funcionalidades
- **Engenharia Social**: Técnicas para enganar usuários
- **Defesa em Profundidade**: Múltiplas camadas de segurança

### Leitura Recomendada

- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Microsoft Security Best Practices](https://docs.microsoft.com/en-us/security/)
- [Linux Security Hardening](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_basic_system_settings/using-selinux_configuring-basic-system-settings)

---

## ⚖️ Considerações Legais e Éticas

### Aviso Legal

Este projeto é fornecido **exclusivamente para fins educacionais** em ambientes controlados. O desenvolvedor e os contribuidores **não são responsáveis** pelo uso indevido deste código.

**É ILEGAL:**

- ❌ Usar keyloggers em sistemas sem autorização explícita
- ❌ Capturar dados pessoais ou financeiros de terceiros
- ❌ Violar privacidade de outras pessoas
- ❌ Usar para fins criminosos

**Uso Permitido:**

- ✅ Pesquisa em ambientes controlados
- ✅ Educação em cibersegurança
- ✅ Testes de segurança com permissão
- ✅ Análise forense autorizada

### Conformidade

Este projeto respeita as seguintes regulamentações:

- **GDPR**: Proteção de dados pessoais
- **LGPD**: Lei Geral de Proteção de Dados (Brasil)
- **HIPAA**: Proteção de dados de saúde
- **PCI DSS**: Proteção de dados de cartão

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo `LICENSE` para detalhes.

---

## 👨‍💻 Autor

**Seu Nome** - Projeto de Cibersegurança Educacional

---

## 🔗 Links Úteis

- [Documentação do pynput](https://pynput.readthedocs.io/)
- [Documentação do smtplib](https://docs.python.org/3/library/smtplib.html)
- [GitHub do Projeto](https://github.com/seu_usuario/Keylogger)
- [Issues e Discussões](https://github.com/seu_usuario/Keylogger/issues)

---

## 📞 Suporte

Para dúvidas ou problemas:

1. Verifique a seção de [Issues](https://github.com/seu_usuario/Keylogger/issues)
2. Consulte a documentação em `Medidas_de_Defesa_Keylogger.md`
3. Abra uma nova issue com descrição detalhada

---

## 🎓 Conclusão

Este projeto fornece uma compreensão prática de como keyloggers funcionam e como se defender contra eles. A educação em cibersegurança é fundamental para criar um ambiente digital mais seguro. Use este conhecimento de forma responsável e ética.

**Lembre-se: Com grande poder vem grande responsabilidade!**

---

*Última atualização: 22 de outubro de 2025*

