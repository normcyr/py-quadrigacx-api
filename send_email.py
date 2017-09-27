import yaml, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def load_config(config_file):

    with open(config_file, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    username = cfg['login']['username']
    password = cfg['login']['password']
    smtp_server = cfg['server']

    return(username, password, smtp_server)

def build_message(announcement):

    from_address = 'normand.cyr@gmail.com'
    to_address = 'normand.cyr@gmail.com'

    msg = MIMEMultipart()
    msg['Subject'] = 'Test message'
    msg['From'] = from_address
    msg['To'] = to_address

    body = announcement
    msg.attach(MIMEText(body, 'plain'))

    return(msg, from_address, to_address)

def send_message(username, password, smtp_server, msg, from_address, to_address):

    server = smtplib.SMTP(smtp_server, 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    send_mail_status = server.sendmail(from_address, to_address, msg.as_string())

    if send_mail_status != {}:
        print('There was a problem sending an email. Error: {}.'.format(send_mail_status))

    server.quit()

def main(eth_profit, btc_profit):

    config_file = 'config.yml'

    eth_positive = 'You are profitable with ethereum!'
    btc_positive = 'You are profitable with bitcoin!'

    if eth_profit == True:
        username, password, smtp_server = load_config(config_file)
        msg, from_address, to_address = build_message(eth_positive)
        send_message(username, password, smtp_server, msg, from_address, to_address)

    if btc_profit == True:
        username, password, smtp_server = load_config(config_file)
        msg, from_address, to_address = build_message(btc_positive)
        send_message(username, password, smtp_server, msg, from_address, to_address)

if __name__ == '__main__':
    main(eth_profit, btc_profit)
