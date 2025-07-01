#kugoumusic/kugoumusic.py
import pyautogui
def kugoumusic(name,state,function):
    if name == 'end':
        pass
    else:
        print('正在播放：'%name)
    if state == 'play':
        pyautogui.hotkey('alt', '`')#播放
    elif state == 'pause':
        pyautogui.hotkey('alt', '`')#暂停
    elif state == 'next':
        pyautogui.hotkey('alt', 'right')#下一曲
    elif state == 'previous':
        pyautogui.hotkey('alt', 'left')#上一曲
    elif state == 'volumeup':
        pyautogui.hotkey('alt', 'up')#音量调高
    elif state == 'volumedown':
        pyautogui.hotkey('alt', 'down')#音量调低
    elif state == 'volumeno':
        pyautogui.hotkey('ctrl','alt', 's')#静音
    elif state == 'end':
        pass
    if function == 'F.F':
        pyautogui.hotkey('ctrl','shift', 'right')#快进
    elif function == 'F.R':
        pyautogui.hotkey('ctrl','shift', 'left')#快退
    elif function == 'D.L':
        pyautogui.hotkey('ctrl', 'alt', 'd')#显示歌词
    elif function == 'H.L':
        pyautogui.hotkey('ctrl', 'alt', 'd')#隐藏歌词
    elif function == 'L.L':
        pyautogui.hotkey('ctrl', 'alt', 'e')#锁定歌词
    elif function == 'U.L':
        pyautogui.hotkey('ctrl', 'alt', 'e')#解锁歌词
    elif function == 'download':
        pyautogui.hotkey('ctrl', 'alt', 'x')#下载
    elif function == 'collect':
        pyautogui.hotkey('ctrl', 'alt', 'l')#收藏
    elif function == 'hear.song.R.T':
        pyautogui.hotkey('shift', 'alt', 'z')#听歌识曲
    elif function == 'end':
        pass
    
    
