import os
import time


def charge_animation():
    frames = [
        """
        =========
        |       |
        |  10%  |
        |       |
        =========
        """,
        """
        ===========
        ||       ||
        ||  50%  ||
        ||       ||
        ===========
        """,
        """
        =============
        |||       |||
        |||  90%  |||
        |||       |||
        ============= 

        """,
        """
        *************
        *           *
        *  CHARGED! *
        *           *
        *************
        """
    ]
    
    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Charge:")
        print(frame)
        time.sleep(0.5)

# Запускаем зарядку
charge_animation()