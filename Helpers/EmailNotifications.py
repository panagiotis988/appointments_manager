import codecs
import os
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailNotifications:
    @staticmethod
    def sendEmail(appointments, subject, template):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        template = os.path.join(base_path, "templates/" + template + ".html")

        for appointment in appointments:
            msg = MIMEMultipart()
            msg['From'] = 'apointmentmanager@yahoo.com'
            msg['To'] = appointment[10]
            msg['Subject'] = subject

            html_file = codecs.open(template, "r", "utf-8")

            html_format = html_file.read().format(first_name=appointment[6], last_name=appointment[7],
                                                  date=appointment[2], start_time=appointment[3])
            html_content = MIMEText(html_format, 'html')
            msg.attach(html_content)

            with smtplib.SMTP('smtp.mail.yahoo.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()

                smtp.login('apointmentmanager@yahoo.com', 'mihnphgrfwzbebby')

                smtp.send_message(msg)
                smtp.quit()
