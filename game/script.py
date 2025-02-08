import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
from pynput.keyboard import Controller, Key
import time
def get_game_window_position(window_title):
    """根据窗口标题获取窗口位置"""
    window = gw.getWindowsWithTitle(window_title)
    if window:
        win = window[0]
        return (win.left, win.top), (win.right, win.bottom)
    else:
        raise None

def capture_screen(top_left, bottom_right):
    """截取屏幕特定区域"""
    screenshot = pyautogui.screenshot(region=(*top_left, bottom_right[0]-top_left[0], bottom_right[1]-top_left[1]))
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

def find_template(screen, template_path):
    """在屏幕中查找模板图像的位置"""
    template = cv2.imread(template_path, 0)
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    return max_loc if max_val > 0.95 else None

keyboard = Controller()
def move_left():
    keyboard.press('a')
    time.sleep(0.1)
    keyboard.release('a')
def move_right():
    keyboard.press('d')
    time.sleep(0.1)
    keyboard.release('d')
def jump():
    keyboard.press('k')
    keyboard.release('k')
def skill_y():
    keyboard.press('y')
    time.sleep(0.1)
    keyboard.release('y')
def attack_l():
    keyboard.press('l')
    time.sleep(0.1)
    keyboard.release('l')
def refresh(left_top,right_bottom):
    screen = capture_screen(left_top, right_bottom)
    pos = find_template(screen, 'imgs/f5.png')
    pyautogui.click(pos[0] + left_top[0], pos[1] + left_top[1])
    while True:
        screen = capture_screen(left_top, right_bottom)
        pos = find_template(screen, 'imgs/game_start.png')
        if pos is not None:
            pyautogui.click(pos[0] + left_top[0], pos[1] + left_top[1])
            break
    while True:
        screen = capture_screen(left_top, right_bottom)
        time.sleep(1)
        pos = find_template(screen, 'imgs/wukong.png')
        if pos is not None:
            pyautogui.click(pos[0] + left_top[0], pos[1] + left_top[1])
            break
    while True:
        screen = capture_screen(left_top, right_bottom)
        pos = find_template(screen, 'imgs/buzhoushan.png')
        if pos is not None:
            time.sleep(1)
            pyautogui.click(pos[0] + left_top[0], pos[1] + left_top[1])
            break
    time.sleep(10)
def game_end(left_top,right_bottom):
    screen = capture_screen(left_top, right_bottom)
    pos = find_template(screen, 'imgs/game_end.png')
    pos1=find_template(screen, 'imgs/lose.png')
    if pos1 is not None or pos is not None:
        return True
    return False
def checkout():
    if get_game_window_position('造梦西游4') == None:
        exit(0)
def wushuanghefuzi(left_top,right_bottom):
    screen = capture_screen(left_top, right_bottom)
    pos = find_template(screen, 'imgs/juexianjian.png')
    if pos is not None:
        keyboard.press('h')
        time.sleep(0.1)
        keyboard.release('h')
        keyboard.press(Key.space)
        time.sleep(0.1)
        keyboard.release(Key.space)




if __name__ == "__main__":

    left_top,right_bottom=get_game_window_position('造梦西游4')
    for i in range(10000):

        flag=False
        refresh(left_top,right_bottom)
        for i in range(8):
            move_right()
        for i in range(8):
            move_left()
        while True:


            checkout()
            for i in range(5):
                skill_y()
                checkout()
            for i in range(5):
                checkout()
                wushuanghefuzi(left_top,right_bottom)
                if game_end(left_top,right_bottom)==True:
                    flag=True
                    break
                attack_l()
                time.sleep(1.5)

            if flag:
                break

        screen = capture_screen(left_top, right_bottom)
        pos = find_template(screen, 'imgs/settings.png')
        if pos is None:
            continue
        pyautogui.click(pos[0] + left_top[0], pos[1] + left_top[1])
        time.sleep(1)
        screen = capture_screen(left_top, right_bottom)
        pos = find_template(screen, 'imgs/backtomap.png')
        if pos is None:
            continue
        pyautogui.click(pos[0] + left_top[0], pos[1] + left_top[1])
        time.sleep(3)

