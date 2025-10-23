# Instruções Didáticas: Enviando o Projeto para GitHub

Este documento fornece um guia passo a passo para compartilhar seu projeto Keylogger em um repositório público no GitHub.

---

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter:

- ✅ Conta no GitHub (crie em https://github.com/signup)
- ✅ Git instalado em seu computador (https://git-scm.com/downloads)
- ✅ Terminal ou Prompt de Comando aberto
- ✅ Projeto Keylogger pronto na pasta local

---

## 🔑 Passo 1: Configurar Git Localmente

### 1.1 Verificar Instalação do Git

```bash
git --version
```

Se aparecer a versão do Git, está instalado corretamente.

### 1.2 Configurar Identidade

Configure seu nome e e-mail (use os mesmos da conta GitHub):

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu_email@gmail.com"
```

Para verificar a configuração:

```bash
git config --global --list
```

---

## 📁 Passo 2: Inicializar Repositório Local

### 2.1 Navegar até a Pasta do Projeto

```bash
# Windows
cd C:\Users\seu_usuario\Keylogger

# Linux/macOS
cd ~/Keylogger
```

### 2.2 Inicializar Git

```bash
git init
```

**Resultado esperado:**

```
Initialized empty Git repository in /home/ubuntu/Keylogger/.git/
```

### 2.3 Verificar Status

```bash
git status
```

**Resultado esperado:**

```
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Keylogger.py
        Keylogger_Email.py
        Keylogger_Furtivo.py
        Medidas_de_Defesa_Keylogger.md
        README.md
        ...
```

---

## 📝 Passo 3: Adicionar Arquivos ao Git

### 3.1 Adicionar Todos os Arquivos

```bash
git add .
```

O ponto (`.`) significa "adicionar todos os arquivos da pasta atual".

### 3.2 Verificar Arquivos Adicionados

```bash
git status
```

**Resultado esperado:**

```
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   Keylogger.py
        new file:   Keylogger_Email.py
        new file:   Keylogger_Furtivo.py
        new file:   Medidas_de_Defesa_Keylogger.md
        new file:   README.md
        ...
```

### 3.3 Criar Arquivo .gitignore (Opcional)

Para evitar enviar arquivos desnecessários:

```bash
# Windows
echo __pycache__/ > .gitignore
echo *.pyc >> .gitignore
echo venv/ >> .gitignore
echo log*.txt >> .gitignore

# Linux/macOS
cat > .gitignore << EOF
__pycache__/
*.pyc
venv/
log*.txt
.DS_Store
EOF
```

---

## 💾 Passo 4: Fazer o Primeiro Commit

### 4.1 Criar Commit

Um commit é um "snapshot" do seu projeto em um momento específico.

```bash
git commit -m "Projeto inicial: Keylogger Simulado para fins educacionais"
```

**Resultado esperado:**

```
[master (root-commit) abc1234] Projeto inicial: Keylogger Simulado para fins educacionais
 6 files changed, 500 insertions(+)
 create mode 100644 Keylogger.py
 create mode 100644 Keylogger_Email.py
 ...
```

### 4.2 Verificar Histórico de Commits

```bash
git log
```

**Resultado esperado:**

```
commit abc1234567890abcdef1234567890abcdef123456 (HEAD -> master)
Author: Seu Nome <seu_email@gmail.com>
Date:   Wed Oct 22 14:30:45 2025 -0300

    Projeto inicial: Keylogger Simulado para fins educacionais
```

---

## 🌐 Passo 5: Criar Repositório no GitHub

### 5.1 Acessar GitHub

1. Vá para https://github.com
2. Faça login com sua conta
3. Clique no ícone "+" no canto superior direito
4. Selecione "New repository"

### 5.2 Configurar Repositório

Preencha os campos conforme indicado:

| Campo | Valor |
|-------|-------|
| **Repository name** | `Keylogger` |
| **Description** | `Projeto Educacional: Keylogger Simulado em Python` |
| **Visibility** | `Public` |
| **Initialize this repository with** | `Deixe vazio` |

### 5.3 Criar Repositório

Clique no botão "Create repository".

**Resultado:**

Você será redirecionado para a página do repositório vazio com instruções.

---

## 🔗 Passo 6: Conectar Repositório Remoto

### 6.1 Copiar URL do Repositório

Na página do GitHub, você verá uma URL como:

```
https://github.com/seu_usuario/Keylogger.git
```

Copie esta URL.

### 6.2 Adicionar Repositório Remoto

No terminal, execute:

```bash
git remote add origin https://github.com/seu_usuario/Keylogger.git
```

Substitua `seu_usuario` pelo seu nome de usuário do GitHub.

### 6.3 Verificar Conexão

```bash
git remote -v
```

**Resultado esperado:**

```
origin  https://github.com/seu_usuario/Keylogger.git (fetch)
origin  https://github.com/seu_usuario/Keylogger.git (push)
```

---

## 📤 Passo 7: Fazer Push (Enviar para GitHub)

### 7.1 Enviar Arquivos

```bash
git push -u origin master
```

Na primeira vez, você pode ser solicitado a autenticar. Use uma das opções:

**Opção 1: Token de Acesso Pessoal (Recomendado)**

1. Vá para https://github.com/settings/tokens
2. Clique em "Generate new token"
3. Selecione escopos: `repo`, `read:user`
4. Copie o token
5. Cole como senha quando solicitado

**Opção 2: Autenticação SSH**

1. Gere chave SSH: `ssh-keygen -t ed25519 -C "seu_email@gmail.com"`
2. Adicione a chave pública ao GitHub
3. Configure URL remota: `git remote set-url origin git@github.com:seu_usuario/Keylogger.git`

### 7.2 Verificar Push

**Resultado esperado:**

```
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 2.50 KiB | 2.50 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0)
To https://github.com/seu_usuario/Keylogger.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

---

## ✅ Passo 8: Verificar no GitHub

### 8.1 Acessar Repositório

1. Vá para https://github.com/seu_usuario/Keylogger
2. Verifique se todos os arquivos aparecem
3. Verifique se o README.md é exibido na página principal

### 8.2 Estrutura Esperada

```
Keylogger/
├── Keylogger.py
├── Keylogger_Email.py
├── Keylogger_Furtivo.py
├── Medidas_de_Defesa_Keylogger.md
├── README.md
├── Instrucoes_GitHub.md
├── Teste_ambiente/
├── log.txt
└── teste_demo.txt
```

---

## 🔄 Passo 9: Atualizações Futuras

Quando fizer mudanças no projeto:

### 9.1 Verificar Mudanças

```bash
git status
```

### 9.2 Adicionar Mudanças

```bash
git add .
```

### 9.3 Fazer Commit

```bash
git commit -m "Descrição das mudanças realizadas"
```

### 9.4 Fazer Push

```bash
git push origin master
```

---

## 📊 Exemplo Completo de Fluxo

```bash
# 1. Navegar até a pasta
cd ~/Keylogger

# 2. Inicializar Git
git init

# 3. Adicionar arquivos
git add .

# 4. Fazer commit
git commit -m "Projeto inicial: Keylogger Simulado"

# 5. Adicionar repositório remoto
git remote add origin https://github.com/seu_usuario/Keylogger.git

# 6. Fazer push
git push -u origin master

# 7. Verificar status
git status
# Resultado: "nothing to commit, working tree clean"
```

---

## 🆘 Solução de Problemas

### Problema: "fatal: not a git repository"

**Solução:**

```bash
git init
```

### Problema: "error: remote origin already exists"

**Solução:**

```bash
git remote remove origin
git remote add origin https://github.com/seu_usuario/Keylogger.git
```

### Problema: "Permission denied (publickey)"

**Solução:**

Use HTTPS em vez de SSH:

```bash
git remote set-url origin https://github.com/seu_usuario/Keylogger.git
```

### Problema: "fatal: could not read Username"

**Solução:**

Use um token de acesso pessoal em vez de senha:

1. Gere token em https://github.com/settings/tokens
2. Use o token como senha

### Problema: Arquivo grande não pode ser enviado

**Solução:**

Adicione o arquivo ao `.gitignore`:

```bash
echo "arquivo_grande.bin" >> .gitignore
git add .gitignore
git commit -m "Adicionar arquivo grande ao gitignore"
git push
```

---

## 🎯 Dicas e Boas Práticas

### Mensagens de Commit Efetivas

✅ **Bom:**
```
git commit -m "Adicionar funcionalidade de envio por e-mail"
```

❌ **Ruim:**
```
git commit -m "Mudanças"
```

### Commits Frequentes

Faça commits pequenos e frequentes:

```bash
git commit -m "Corrigir bug na captura de Enter"
git commit -m "Adicionar tratamento de erro"
git commit -m "Atualizar documentação"
```

### Branches para Desenvolvimento

Para trabalhos maiores, use branches:

```bash
git checkout -b feature/nova-funcionalidade
# Faça mudanças
git commit -m "Implementar nova funcionalidade"
git push origin feature/nova-funcionalidade
# Crie um Pull Request no GitHub
```

---

## 📚 Recursos Adicionais

- [Documentação do Git](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Git Cheat Sheet](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)
- [Markdown Guide](https://www.markdownguide.org/)

---

## ✨ Próximos Passos

Após enviar seu projeto:

1. **Adicionar Tópicos**: Vá para Settings > Topics e adicione tags como `python`, `keylogger`, `cybersecurity`, `educational`

2. **Criar Releases**: Vá para Releases e crie versões do seu projeto

3. **Adicionar Licença**: Crie um arquivo `LICENSE` com a licença MIT

4. **Ativar Discussions**: Vá para Settings e ative Discussions para comunidade

5. **Compartilhar**: Compartilhe o link do repositório com colegas e comunidade

---

## 🎓 Conclusão

Parabéns! Você enviou com sucesso seu projeto Keylogger para o GitHub. Agora seu trabalho está compartilhado com a comunidade de forma segura e profissional.

**Lembre-se:**
- Mantenha o repositório atualizado
- Responda a issues e pull requests
- Documente bem seu código
- Use o Git para controlar versões

Boa sorte com seu projeto de cibersegurança!

---

*Última atualização: 22 de outubro de 2025*

