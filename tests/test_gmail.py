import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración de los detalles del correo
sender_email = "****@gmail.com"  # Tu dirección de correo
receiver_email = "****@gmail.com"  # Dirección de correo del destinatario
password = "**** **** **** ****"  # Contraseña de aplicación generada con la cuenta de Google
subject = "Prueba de Correo"
body = "Este es un mensaje de prueba enviado desde Python."

# Crear el mensaje de correo electrónico
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Enviar el correo
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Activar la seguridad
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()
    print("Correo enviado exitosamente")
except Exception as e:
    print(f"Error al enviar el correo: {e}")