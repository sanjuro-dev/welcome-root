import os
from time import sleep
from random import choice
from colorama import Fore
import keyboard




def update(fps):
    sleep(1/fps)
    os.system('cls' if os.name == 'nt' else 'clear')


def summon_line(chars,lenght):
    line = ''

    for s in range(lenght):
        line += choice(chars)
    return line


ideograms = [
        'あ', 'い', 'う', 'え', 'お',  # Hiragana
        'か', 'き', 'く', 'け', 'こ',
        'さ', 'し', 'す', 'せ', 'そ',
        'た', 'ち', 'つ', 'て', 'と',
        'な', 'に', 'ぬ', 'ね', 'の',
        'は', 'ひ', 'ふ', 'へ', 'ほ',
        'ま', 'み', 'む', 'め', 'も',
        'や', 'ゆ', 'よ',
        'ら', 'り', 'る', 'れ', 'ろ',
        'わ', 'を', 'ん',  # Hiragana final
        'ア', 'イ', 'ウ', 'エ', 'オ',  # Katakana
        'カ', 'キ', 'ク', 'ケ', 'コ',
        'サ', 'シ', 'ス', 'セ', 'ソ',
        'タ', 'チ', 'ツ', 'テ', 'ト',
        'ナ', 'ニ', 'ヌ', 'ネ', 'ノ',
        'ハ', 'ヒ', 'フ', 'ヘ', 'ホ',
        'マ', 'ミ', 'ム', 'メ', 'モ',
        'ヤ', 'ユ', 'ヨ',
        'ラ', 'リ', 'ル', 'レ', 'ロ',
        'ワ', 'ヲ', 'ン',  # Katakana final
        '山'  # Ideograma
]

characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',  ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
widht = 80
height = 20
user = message = "Welcome Back, Master"
count = 0
print(Fore.RED)
while True:
    count += 1 / 30
    if 10 <= count < 10 +len(user):
        char = message[int(count - 10)]
        message = message.replace(char, summon_line(characters,1))
    elif count >= 10 + len(user):
        message = user
        count = 0

    for s in range(height):
        if s == 0 or s == height -1:
            print(summon_line(characters, widht+ 4))
        elif 0 < s < (height -1) and s != round(height/2):
            print(summon_line(characters,1)," "*widht,summon_line(characters,1))
        elif 0 < s < (height -1) and s == round(height/2):
            print(summon_line(characters,1)," " * round(widht/2),"", message, summon_line(ideograms,1)," " *( (round(widht / 4)) -6), summon_line(characters, 1))
    if keyboard.is_pressed('enter'):
        update(60)
        break
    update(60)