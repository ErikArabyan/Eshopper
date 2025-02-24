@echo off

if exist "venv" (
    echo activating virtual envirement...

    call "venv\Scripts\activate.bat"

    start "django" powershell -NoExit -Command "cd .\django\; py ./manage.py runserver"

) else (
    echo creating and activating virtual envirement...

    powershell -Command "py -m venv venv"

    call .\venv\Scripts\activate.bat

    echo installing py packet manager...

    powershell -Command "py -m pip install --upgrade pip"

    echo installing django dependencyes...

    powershell -Command "pip install -r requirements.txt"

    start "django" powershell -NoExit -Command "cd .\django\; py ./manage.py runserver"
)

start chrome http://127.0.0.1:8000/

set /p answer="Do you want to open Visual Studio Code? (y/n): "
where code >nul 2>&1
if %errorlevel%==0 (
    if /i "%answer%"=="y" (
        code .
    )
)

exit