rem 显示unity日志

rem #初始#####################
set unity="D:\unity.exe"
set tail="C:\Program Files (x86)\Windows Resource Kits\Tools\tail.exe"
set project_path=""
set method=""
set logfile="f:\log.txt"
rem ##########################

start %unity% -batchmode -projectPath %project_path% -nographics -executeMethod %method% -logFile %log_path% -quit
::for test  start ping.exe www.baidu.com -n 100 > %logFile% 
%tail% -f %logFile%