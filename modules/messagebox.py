#-*-coding:utf-8-*-

import win32api,win32con
import json

def run(**args):
    print "[*] In Message Module." 
    value = {"1":"OK","2":"CANCEL","3":"ABORT","4":"RETRY","5":"IGNORE","6":"YES","7":"NO"}
    result = []
    
    ans = value[str(win32api.MessageBox(0, "OK!Let's start!", "I LOVE U",win32con.MB_ICONASTERISK))]
    result.append(ans)
    ans = value[str(win32api.MessageBox(0, u"音乐好听吗？", "I LOVE U",win32con.MB_OK))]
    result.append(ans)
    ans = value[str(win32api.MessageBox(0, u"看你的桌面哦！", "I LOVE U",win32con.MB_OK))]
    result.append(ans)
    ans = value[str(win32api.MessageBox(0, u"如果变成了一大坨黑请联系蓝朋友……", "I LOVE U",win32con.MB_HELP))]
    result.append(ans)
    ans = value[str(win32api.MessageBox(0, u"点帮助没用哦，联系蓝朋友才有用", "I LOVE U",win32con.MB_OK))]
    result.append(ans)
    ans = value[str(win32api.MessageBox(0, u"不知道是不是高分屏呀？背景像素感人(ಥ _ ಥ)", "I LOVE U",win32con.MB_OK))]
    result.append(ans)
    ans = value[str(win32api.MessageBox(0, u"我在想要不要给你提供“否”这个选项啊", "I LOVE U",win32con.MB_OK))]
    result.append(ans)
    ans = value[str(win32api.MessageBox(0, u"但是你忍心拒绝我吗", "I LOVE U",win32con.MB_OK))]
    result.append(ans)
    ans = value[str(win32api.MessageBox(0, u"不忍心吧", "I LOVE U",win32con.MB_OK))]
    result.append(ans)
    ans = value[str(win32api.MessageBox(0, u"好吧我不是专制的银嘛，把“否”给你，一定要认真选哦", "I LOVE U",win32con.MB_YESNO))]
    result.append(ans)
    if ans == "NO":
        ans = value[str(win32api.MessageBox(0, u"你确定不认真选？", "I LOVE U",win32con.MB_ICONWARNING))]
        result.append("branch:" + ans)
    ans = value[str(win32api.MessageBox(0, u"喜欢这个礼物吗", "I LOVE U",win32con.MB_YESNO))]
    result.append("IMPORTANT:" + ans)
    ans = value[str(win32api.MessageBox(0, u"如果不喜欢让你点一百次喜欢我会不会有点过分呀", "I LOVE U",win32con.MB_OK))]
    result.append(ans)
    ans = value[str(win32api.MessageBox(0, u"虽然弹框很容易，但是人家可是忍着不和你说话对着屏幕打字呢", u"I LOVE U",win32con.MB_OK))]
    result.append(ans)
    ans = value[str(win32api.MessageBox(0, u"边打字边傻笑哈哈哈", "I LOVE U",win32con.MB_OK))]
    result.append(ans)
    ans = value[str(win32api.MessageBox(0, u"会烦我的弹框吗，'是'=烦,'否'=不烦", "I LOVE U",win32con.MB_YESNO))]
    result.append(ans)
    if ans == "YES":
        ans = value[str(win32api.MessageBox(0, u"啊啊啊！！！真的烦吗？？？", "U DONT LOVE THIS",win32con.MB_YESNO))]
        result.append("branch:" + ans)
        if ans == "YES":
            ans = value[str(win32api.MessageBox(0, u"委屈巴巴", "I LOVE U",win32con.MB_ICONERROR))]
            result.append("branch:" + ans)
            return result
    ans = value[str(win32api.MessageBox(0, u"不烦就好，前方高能预警哦", "I LOVE U",win32con.MB_ICONWARNING))]
    result.append(ans)
    ans = value[str(win32api.MessageBox(0, u"我系不系你的小宝贝？", "I LOVE U",win32con.MB_YESNO))]
    result.append(ans)
    if ans == "NO":
        for i in range(20):
            ans = value[str(win32api.MessageBox(0, u"记住！！！我就系你的小宝贝！！！", "I LOVE U",win32con.MB_ICONASTERISK))]
    ans = value[str(win32api.MessageBox(0, u"你要不要宠溺人家？", "I LOVE U",win32con.MB_YESNO))]
    result.append(ans)
    if ans == "NO":
        for i in range(20):
            ans = value[str(win32api.MessageBox(0, u"你果然不爱我了┭┮﹏┭┮", "I LOVE U",win32con.MB_ICONWARNING))]
    ans = value[str(win32api.MessageBox(0, u"好次的都给我次不啦", "I LOVE U",win32con.MB_YESNO))]
    result.append(ans)
    if ans == "NO":
        for i in range(20):
            ans = value[str(win32api.MessageBox(0, u"你都不愿意哄哄人家", "I LOVE U",win32con.MB_ICONWARNING))]
    ans = value[str(win32api.MessageBox(0, u"那好玩的都给我玩不", "I LOVE U",win32con.MB_YESNO))]
    result.append(ans)
    if ans == "NO":
        for i in range(20):
            ans = value[str(win32api.MessageBox(0, u"不和你玩了┭┮﹏┭┮", "I LOVE U",win32con.MB_ICONWARNING))]
    ans = value[str(win32api.MessageBox(0, u"我系不系膨胀了", "I LOVE U",win32con.MB_YESNO))]
    result.append(ans)
    if ans == "YES":
        for i in range(20):
            ans = value[str(win32api.MessageBox(0, u"被偏爱的有恃无恐嘛（天真脸）", "I LOVE U",win32con.MB_ICONWARNING))]
    ans = value[str(win32api.MessageBox(0, u"其实人家想说的是", "I LOVE U",win32con.MB_HELP))]
    result.append(ans)
    ans = value[str(win32api.MessageBox(0, u"I will be always love you!", "I LOVE U",win32con.MB_OK))]
    result.append(ans)
    
    return result

#result = run()
#print result