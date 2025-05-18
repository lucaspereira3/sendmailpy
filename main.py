import smtplib
import ssl
from email.message import EmailMessage
import getpass # To securely get password
import os

def send_email(sender_email, sender_password, receiver_email, subject, body):
    """Envia um email usando SMTP com SSL."""
    
    # Tenta detectar configurações comuns de SMTP (Gmail, Outlook)
    smtp_server = ""
    smtp_port = 465 # Porta padrão para SMTPS (SSL)
    
    if "@gmail.com" in sender_email:
        smtp_server = "smtp.gmail.com"
    elif "@outlook.com" in sender_email or "@hotmail.com" in sender_email:
        smtp_server = "smtp.office365.com"
        smtp_port = 587 # Outlook/Office365 geralmente usa STARTTLS na porta 587
    else:
        # Pede ao usuário se não for um provedor comum
        smtp_server = input(f"Digite o endereço do servidor SMTP para {sender_email}: ")
        try:
            smtp_port_input = input(f"Digite a porta SMTP (padrão {smtp_port} para SSL, 587 para STARTTLS): ")
            if smtp_port_input:
                smtp_port = int(smtp_port_input)
        except ValueError:
            print(f"Porta inválida, usando porta padrão {smtp_port}.")

    if not smtp_server:
        print("Erro: Servidor SMTP não especificado.")
        return False

    # Cria a mensagem de email
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(body)

    # Cria contexto SSL seguro
    context = ssl.create_default_context()

    try:
        print(f"Conectando ao servidor {smtp_server} na porta {smtp_port}...")
        if smtp_port == 465:
            # Conexão SMTPS (SSL direto)
            with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
                print("Realizando login...")
                server.login(sender_email, sender_password)
                print("Enviando email...")
                server.send_message(msg)
                print("Email enviado com sucesso!")
        elif smtp_port == 587:
            # Conexão STARTTLS
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                print("Iniciando conexão e STARTTLS...")
                server.starttls(context=context)
                print("Realizando login...")
                server.login(sender_email, sender_password)
                print("Enviando email...")
                server.send_message(msg)
                print("Email enviado com sucesso!")
        else:
             # Tenta conexão padrão (pode não ser segura)
             print(f"Aviso: Tentando conexão na porta {smtp_port} sem garantia de SSL/TLS.")
             with smtplib.SMTP(smtp_server, smtp_port) as server:
                # Tenta STARTTLS se disponível, mas sem garantia
                try: 
                    server.starttls(context=context)
                    print("STARTTLS iniciado.")
                except smtplib.SMTPNotSupportedError:
                    print("STARTTLS não suportado pelo servidor nesta porta.")
                
                print("Realizando login...")
                server.login(sender_email, sender_password)
                print("Enviando email...")
                server.send_message(msg)
                print("Email enviado com sucesso!")
                
        return True
    except smtplib.SMTPAuthenticationError:
        print("Erro de autenticação: Verifique seu email e senha/senha de aplicativo.")
        print("Para Gmail/Outlook, pode ser necessário usar uma 'Senha de App'.")
    except smtplib.SMTPServerDisconnected:
        print("Erro: Servidor desconectado inesperadamente.")
    except smtplib.SMTPException as e:
        print(f"Erro de SMTP: {e}")
    except OSError as e:
        print(f"Erro de conexão (verifique o servidor/porta e sua conexão): {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    
    return False

if __name__ == "__main__":
    print("--- Ferramenta de Envio de Email Simples ---")
    
    # Tenta obter email dos argumentos ou variáveis de ambiente
    sender = os.getenv("EMAIL_SENDER") or input("Seu email (remetente): ")
    receiver = os.getenv("EMAIL_RECEIVER") or input("Email do destinatário: ")
    subj = input("Assunto do email: ")
    mail_body = input("Corpo do email: \n")
    
    # Pede a senha de forma segura
    print(f"Digite a senha ou 'Senha de App' para {sender}: ")
    password = getpass.getpass()

    if not all([sender, receiver, subj, mail_body, password]):
        print("Erro: Todos os campos (remetente, destinatário, assunto, corpo, senha) são obrigatórios.")
    else:
        send_email(sender, password, receiver, subj, mail_body)

    print("--- Fim do programa ---")
