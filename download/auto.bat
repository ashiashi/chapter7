@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit
:begin
REM
@echo msgbox "À¶ÅóÓÑÔÚÕâÀï£¡£¨¤Å£þ3£þ£©¤Å¨q">msg.vbs 
@msg.vbs
@del msg.vbs
pause