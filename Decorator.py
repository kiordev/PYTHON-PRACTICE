# Decorator File Applicationn
# Creator: Alexandr Kior kiordev@gmail.com
# Creation Data: 14 APRIL 22
# Last Update: 14 APRIL 22

import webbrowser


def url_cheking(func):
    def wrapper(url):
        if "." in url:
            func(url)
        else:
            print("Вы ввели неправильный адрес")
    return wrapper


@url_cheking
def open_url(url):
    webbrowser.open(url)


open_url("https://github.com/kiordev")