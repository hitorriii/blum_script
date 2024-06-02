from pyautogui import *
import pygetwindow as gw
import pyautogui
import time
import keyboard
import random
from pynput.mouse import Button, Controller
import colorama
from colorama import Fore

colorama.init(autoreset=True)

mouse = Controller()

def print_intro():
    print(r"""
                            _
                           ( )_
   ___  _ __  _   _  _ _   | ,_)   _
 /'___)( '__)( ) ( )( '_`\ | |   /'_`\
( (___ | |   | (_) || (_) )| |_ ( (_) )
`\____)(_)   `\__, || ,__/'`\__)`\___/'
             ( )_| || |
             `\___/'(_)
        _              _                            _             _
       (_ )  _        ( )                          ( )           ( )
   ___  | | (_)   ___ | |/')    __   _ __   ___    | |__   _   _ | |_
 /'___) | | | | /'___)| , <   /'__`\( '__)/',__)   |  _ `\( ) ( )| '_`\
( (___  | | | |( (___ | |\`\ (  ___/| |   \__, \   | | | || (_) || |_) )
`\____)(___)(_)`\____)(_) (_)`\____)(_)   (____/   (_) (_)`\___/'(_,__/'
                                                                        """)
    print(Fore.RED + "Crypto Clickers Hub - t.me/cryptoapps0")

def print_message(message):
    if "Play" in message:
        print(Fore.MAGENTA + message)
    else:
        print(message)

def click(x, y):
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)

def activate_window(window):
    try:
        if window.isMinimized:
            window.restore()
        window.activate()
        return True
    except Exception:
        return False

def click_play_button(is_first_time):
    try:
        if is_first_time:
            play_button_coords = (telegram_window.left + int(telegram_window.width * 0.75), telegram_window.top + int(telegram_window.height * 0.6))
        else:
            play_button_coords = (telegram_window.left + int(telegram_window.width * 0.5), telegram_window.top + int(telegram_window.height * 0.85) - 10)  # Сместили вверх
        if not activate_window(telegram_window):
            pass
        click(play_button_coords[0], play_button_coords[1])
        print_message('[🌙] | Кнопка Play нажата.')
        time.sleep(1)  # Уменьшена задержка после нажатия кнопки "Play"
    except Exception as e:
        pass

def find_and_click_bacteria():
    scrn = pyautogui.screenshot(region=(telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height))
    width, height = scrn.size

    bacteria_found = False

    for x in range(0, width, 20):
        for y in range(0, height, 20):
            r, g, b = scrn.getpixel((x, y))

            # Проверка на зеленые бактерии и избегание серых бомбочек
            if (b in range(0, 125)) and (r in range(102, 220)) and (g in range(200, 255)):
                is_bomb = False
                for bx in range(-5, 6):
                    for by in range(-5, 6):
                        if 0 <= x + bx < width and 0 <= y + by < height:
                            br, bg, bb = scrn.getpixel((x + bx, y + by))
                            if br in range(100, 160) and bg in range(100, 160) and bb in range(100, 160):
                                is_bomb = True
                                break
                    if is_bomb:
                        break

                if not is_bomb:
                    screen_x = telegram_window.left + x
                    screen_y = telegram_window.top + y
                    click(screen_x + 4, screen_y)
                    time.sleep(0.001)
                    bacteria_found = True

    return bacteria_found

def start_game():
    window_name = input('\n[⚡️] | Crypto Clickers Hub | Нажми 1 ')
    num_games = int(input('\n[☘️] | Введите количество игр, которые вы хотите сыграть: '))

    if window_name == '1':
        window_name = "TelegramDesktop"

    check = gw.getWindowsWithTitle(window_name)
    if not check:
        print(f"[❌] | Окно - {window_name} не найдено!")
        exit()

    print(f"[☘️] | Окно найдено - {window_name}\n[☘️] | Нажмите 'q' для паузы.")

    global telegram_window
    telegram_window = check[0]
    paused = False

    games_played = 0
    is_first_time = True

    while games_played < num_games:
        # Нажимаем кнопку "Play" в начале каждой игры
        click_play_button(is_first_time)
        is_first_time = False

        game_start_time = time.time()
        while time.time() - game_start_time < 31:  # Игра длится 30 секунд
            if keyboard.is_pressed('q'):
                paused = not paused
                if paused:
                    print('[🌙] | Пауза')
                else:
                    print('[🌙] | Возобновление работы')
                time.sleep(1)  # Небольшая задержка, чтобы избежать дребезга клавиши

            while paused:
                if keyboard.is_pressed('q'):
                    paused = False
                    print('[🌙] | Возобновление работы')
                    time.sleep(1)  # Небольшая задержка, чтобы избежать дребезга клавиши

            bacteria_found = find_and_click_bacteria()
            if not bacteria_found and not paused:
                time.sleep(0.1)  # Уменьшенная задержка между проверками

        games_played += 1
        print(f"[🌕] | Игра завершена. Игр сыграно: {games_played}")

        if games_played < num_games:
            is_first_time = False
            time.sleep(2)  # Небольшая задержка перед началом следующей игры

    print(f'[☘️] | {num_games} билетов потрачено, скрипт приостановлен.')

if __name__ == "__main__":
    print_intro()
    while True:
        start_game()
