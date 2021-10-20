setlocal enabledelayedexpansion
for /f "tokens=1-4 delims=/-. " %%i in ('date /t') do (
        set v1=%%i& set v2=%%j& set v3=%%k
        if "%%i:~0,1%%" gtr "9" (set v1=%%j& set v2=%%k& set v3=%%l)
        for /f "skip=1 tokens=2-4 delims=(-)" %%m in ('echo.^|date') do (
            set %%m=!v1!& set %%n=!v2!& set %%o=!v3!
    )
)
:: Final set for language independency (English and Portuguese - maybe works for Spanish and French)
set TASK_DATE=%mm%/%dd%/%yy%%aa%
set TASK_DATE_2=%yy%%aa%/%mm%/%dd%
REM Auto enable Docker service
set /a MIN=%TIME:~3,2%+5
set /a HOUR=%TIME:~0,2%
IF %MIN% GEQ 60 (
	set /a MIN=1
	set /a HOUR+=1
	set /a HOUR%%=24
)
IF %MIN%  LEQ 9 set MIN=0%MIN%
IF %HOUR% LEQ 9 set HOUR=0%HOUR%
set TASK_TIME=%HOUR%:%MIN%
:: SCHTASKS /F /CREATE /TN "Enable_Docker_Service" /TR "C:\k\bootstrap.bat" /SD %TASK_DATE% /ST %TASK_TIME% /SC ONCE
:: SCHTASKS /F /CREATE /TN "Enable_Docker_Service" /TR "C:\k\bootstrap.bat" /SD %TASK_DATE_2% /ST %TASK_TIME% /SC ONCE
SCHTASKS /F /CREATE /TN "k8s_task" /TR "C:\\k\\init.bat" /SD %TASK_DATE% /ST %TASK_TIME% /SC ONCE
SCHTASKS /F /CREATE /TN "k8s_task" /TR "C:\\k\\init.bat" /SD %TASK_DATE_2% /ST %TASK_TIME% /SC ONCE
endlocal