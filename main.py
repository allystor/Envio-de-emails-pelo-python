#Fazendo a importação da blibioteca de envio te emails e o servidor do gmail

from email import message
from email.mime import text
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from typing import MutableSequence

#Aqui é o corpo do email onde está o texto de email que está sendo enviado

Mensagem = MIMEMultipart()
texto = "DIGITE AQUI A MENSAGEM"

#Aqui são onde você fornecerá as credenciais do assunto do email
#ATENÇÃO AS CREDENCIAIS E O TEXTO DEVEM SE ESCRITAS NO CORPO DO CÓDIGO SEM START

Mensagem['from'] = "alvarojoao17@gmail.com"
Senha = "alvaro123"
Mensagem['to'] = "alvarogeforce17@gmail.com"
Mensagem['subject'] = "ENVIANDO A MENSAGEM PELO PYTHON"

#Aqui é aonde acontece a conexão do email completo com o servidor do email

Mensagem.attach(MIMEText(texto, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', port=587)
server.starttls()
server.login(Mensagem['from'], Senha)
server.sendmail(Mensagem['from'],Mensagem['to'], Mensagem.as_string)
server.quit