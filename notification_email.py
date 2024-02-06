#!/usr/bin/env python3

# Lukas Stuffer
# IG: _lukasstuffer_


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailNotification:

	def __init__(self, user: str, pwd: str, receivers: str, smtp=['smtp.domain.com', 587], subject='Test E-Mail', body='E-Mail sent successfully.'):

		self.user 		= user
		self.pwd 		= pwd
		self.smtp		= smtp
		self.receivers 	= receivers
		self.subject 	= subject
		self.body 		= body


	def send(self):

		try:

			for receiver in self.receivers:

				message 			= MIMEMultipart()
				message["From"] 	= self.user
				message["To"] 		= receiver
				message["Subject"] 	= self.subject

				# Add body to the email
				message.attach(MIMEText(self.body, "plain"))

				# Establish a connection to the SMTP server
				with smtplib.SMTP(self.smtp[0], self.smtp[1]) as server:

					server.starttls() # Use TLS for security
					server.login(self.user, self.pwd)

					# Send the email
					server.sendmail(self.user, receiver, message.as_string())


			print("E-Mail send successfully")

		except:

			print("E-Mail send failed!")