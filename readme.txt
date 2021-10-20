Download python 2.7
	https://www.python.org/downloads/release/python-2717/
Download webdriver( Put it in C:\Python27\Scripts)
	https://stackoverflow.max-everyday.com/2018/03/selenium-chrome-webdriver/
	https://sites.google.com/a/chromium.org/chromedriver/
Set Environment Variable
	Setx /M PATH $($Env:PATH + ';C:\Python27\Scripts')
	Setx /M PATH $($Env:PATH + ';C:\Python27')
Install Modules
	pip install selenium
	pip install nose
Run App
	.\init-robot.bat
