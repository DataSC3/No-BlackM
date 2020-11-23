import os

RESET ='\033[0m'
GREEN = '\033[32m'
RED ='\033[31m'

def banner():
    print(RED+'''█▄▄ █   █▀█ █▀▀ █▄▀ █▀▄▀█ █▀█ █ █'''+GREEN+'''
█▄█ █▄▄ █▀█ █▄▄ █ █ █ ▀ █ █▀█ █ █▄▄
                           '''+RESET+RED+'V: 0.0.0\n')
def clear():
    if os.sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


clear()
print(banner())

print(f'Мы закрыты!, чтобы узнать больше о проблеме, напишите нам в Telegram: {GREEN}FELIX4{RESET}')
print(f'Для большего кол-во данных воспользуйтесь нашим Telegram Ботом: {GREEN}https://t.me/No_BlackMail_bot{RESET}\n')

print(f'{RED}+{GREEN} Пробив по номеру\n{RED}+{GREEN} Номер по ФИО\n{RED}+{GREEN} Объявления/Авито\n{RED}+{GREEN} Пробив авто/UA\n{RED}+{GREEN} Пробив авто/RU (Фото)\n{RED}+{GREEN} Поиск по ФИО/RU\n{RED}+{GREEN} Поиск по VK{RESET}')
print('\nCпасибо что вы с нами!!')
