# 📬 sendmailpy

Uma ferramenta de linha de comando em Python para envio de e-mails via SMTP com suporte a **Gmail, Outlook, Hotmail e outros provedores personalizados**. Ideal para testes, automações ou aprendizado sobre envio de e-mails com segurança via SSL/STARTTLS.

---

## 📌 Tópicos

- [📖 Sobre o Projeto](#-sobre-o-projeto)
- [📸 Demonstração](#-demonstração)
- [🚀 Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [⚙️ Como Executar](#️-como-executar)
- [🛠️ Funcionalidades](#️-funcionalidades)
- [🧠 Explicação do Código](#-explicação-do-código)
- [📄 Licença](#-licença)
- [🤝 Contribuindo](#-contribuindo)

---

## 📖 Sobre o Projeto

Este script permite o envio de e-mails de forma simples e interativa diretamente pelo terminal. Ele detecta automaticamente o servidor SMTP com base no e-mail informado e usa conexões seguras via **SSL ou STARTTLS**. O usuário fornece os dados do e-mail e o conteúdo é enviado com segurança.

---

## 📸 Demonstração

```bash
--- Ferramenta de Envio de Email Simples ---

Seu email (remetente): seuexemplo@gmail.com
Email do destinatário: destino@dominio.com
Assunto do email: Teste automático
Corpo do email:
Olá! Este é um teste via Python.
Digite a senha ou 'Senha de App' para seuexemplo@gmail.com:
******
Conectando ao servidor smtp.gmail.com na porta 465...
Realizando login...
Enviando email...
Email enviado com sucesso!
--- Fim do programa ---
```

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- `smtplib`: Biblioteca padrão para envio de e-mails via SMTP.
- `ssl`: Para conexões seguras.
- `email.message.EmailMessage`: Para criar mensagens de e-mail.
- `getpass`: Para ocultar a senha ao digitar.
- `os`: Para capturar variáveis de ambiente opcionais.

---

## ⚙️ Como Executar

1. **Clone o repositório:**

```bash
git clone https://github.com/rafaelmoreirax/sendmailpy.git
cd sendmailpy
```

2. **Execute o script:**

```bash
python main.py
```

3. **Siga as instruções no terminal:**

- Digite o e-mail remetente e destinatário.
- Escreva o assunto e o corpo do e-mail.
- Informe a senha ou a senha de aplicativo.

✅ Dica: Você também pode definir as variáveis de ambiente `EMAIL_SENDER` e `EMAIL_RECEIVER` para evitar digitar esses dados sempre.

---

## 🛠️ Funcionalidades

- [x] Envio de e-mails via SSL (porta 465)
- [x] Suporte a STARTTLS (porta 587)
- [x] Detecção automática de provedores (Gmail, Outlook, Hotmail)
- [x] Suporte a outros provedores via entrada manual
- [x] Segurança via `getpass` (senha não fica visível)
- [ ] Anexo de arquivos (em planejamento)
- [ ] Suporte a HTML no corpo do e-mail (em planejamento)

---

## 🧠 Explicação do Código

### 🔐 Função `send_email(...)`

- **Parâmetros:** e-mails, senha, assunto e corpo da mensagem.
- **Funções:**
  - Detecta o servidor SMTP automaticamente com base no domínio do e-mail remetente.
  - Cria uma conexão segura com SSL ou STARTTLS.
  - Envia a mensagem usando `smtplib.SMTP_SSL` ou `smtplib.SMTP` com `starttls()`.
  - Lida com erros como autenticação, conexão ou falha no envio.

### 🧪 Bloco `if __name__ == "__main__":`

- Interage com o usuário via terminal para coletar:
  - Email remetente
  - Email destinatário
  - Assunto
  - Corpo do e-mail
  - Senha (com segurança)
- Valida os campos obrigatórios antes de enviar.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 🤝 Contribuindo

Contribuições são bem-vindas!

1. Faça um fork do projeto.
2. Crie uma branch com sua feature: `git checkout -b minha-feature`
3. Commit suas alterações: `git commit -m 'feat: nova funcionalidade'`
4. Push na sua branch: `git push origin minha-feature`
5. Abra um Pull Request.

---

## 👤 Autor

Feito com 💻 por [Rafael Moreira](https://github.com/rafaelmoreirax)
