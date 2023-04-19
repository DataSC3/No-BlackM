import os
from time import sleep

RESET ='\033[0m'
GREEN = '\033[32m'
RED ='\033[31m'
YELLOW = '\033[93m'

if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")

print(RED+'''█▄▄ █   █▀█ █▀▀ █▄▀ █▀▄▀█ █▀█ █ █'''+GREEN+'''
█▄█ █▄▄ █▀█ █▄▄ █ █ █ ▀ █ █▀█ █ █▄▄\n1.0.4'''+RESET+'\n')

print(f'{RED}[!] {YELLOW}Мы выпустили новую версию 1.0.5. {GREEN}Эта уже не актуально.{RESET}')
print(f'{RED}[+] {YELLOW}Ссылка на новую версию: {GREEN}https://github.com/DataSC3/noblack-mail.git{RESET}')
print(f'{RED}[+] {YELLOW}Ссылка на наш канал в телеграмме: {GREEN}https://t.me/noblack_channel{RESET}')
print(f'{RED}[#] {YELLOW}Cпасибо что вы с нами!!{RESET}\n\n')
sleep(6)
