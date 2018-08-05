import win32api, win32con, win32gui
import time

#5张每分钟一张循环
def run(**args):
    global username
    #username = 'shide'
    print "[*]  Changing desktop."
    # 打开指定注册表路径
    pic = ["1.png", "2.png","3.png","4.png","5.png"]
    for i in pic: 
        picpath = "C:\Users\%s\Pictures\SloveM%s" %(username, i)
        print picpath
        reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
        # 最后的参数:2拉伸,0居中,6适应,10填充,0平铺
        win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "6")
        # 最后的参数:1表示平铺,拉伸居中等都是0
        win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
        # 刷新桌面
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, picpath, win32con.SPIF_SENDWININICHANGE)
        time.sleep(60)
    
    return str("change desktop.")
