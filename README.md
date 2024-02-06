Example (main.py):

from notification_email import EmailNotification

EmailNotification(user='robot@domain.com', pwd='95*#D3&bBt*CVtdmwASVj@YvZu', smtp=['mail.domain.com', 25], receivers=['maxmustermann@gmail.com'], subject='Test E-Mail', body='E-Mail sent successfully.').send()
