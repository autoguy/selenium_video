<h1><u>Test Framework</u></h1>
<h2><b>Prerequisites:</b></h2>
  - Chromedriver.exe in path somewhere. 
      https://developer.chrome.com/docs/chromedriver/downloads
  - Chrome Version 131.0.6778.86 (Official Build) (64-bit)
  - Other driver needed for firefox, and edge
  - windows 11
  - python 3.12 download page: 
      https://www.python.org/downloads/release/python-3127/
  - setuptools pip
  - pycharm community edition. 

<h2>Installation:</h2>
1) install scoop  https://scoop.sh/
2) Use scoop to install allure
Open command prompt and run: 
  C:\>scoop install allure
more information if needed:
https://github.com/allure-framework/allure2/blob/2.32.0/README.md

3) Scoop installs the binary but you still need to install the
python library interface for it, which we do below
in the pip -r requirements.txt command.
4) Open command prompt and type command
5) C:\>pip install -r requirements.txt


<h2>Execution at Terminal</h2>

<h3><u>Run All The Tests and Produce Pytest Report</u></h3>
At the pycharm prompt:

<b>(venv) PS C:\selenium\selenium_video></b> pytest -v -rA | tee test_report.txt 

* tee outputs to console and file at same time.

<h3><u>Generate the Allure Report</u></h3>
opens the browser and displays reports in folder.
allure serve C:\selenium\selenium_video\allure-results


<h1>Project File Structure:</h1>
C:\selenium\selenium_video/<br>
├── allure-results    <--- generated allure server reports<br>
├── config/<br>
│   └── config.yaml    <--- test case global environment<br>
├── pages/<br>
│   ├── __init__.py<br>
│   ├── base_page.py    <--- setup/tear down <br>
│   ├── camera_single_view_page.py<br>
│   ├── cameras_page.py<br>
│   ├── login_page.py<br>
│   └── menu_page.py<br>
├── tests/<br>
│   ├── __init__.py<br>
│   ├── conftest.py<br>
│   ├── base_test.py<br>
│   ├── test_cameras_list_display.py<br>
│   ├── test_login_invalid_credentials.py<br>
│   ├── test_login_valid_credentials.py<br>
│   ├── test_runner.py<br>
│   ├── test_single_view_back_button.py<br>
│   ├── test_single_view_play_when_open.py<br>
│   └── test_login.py<br>
├── utils/<br>
│   ├── __init__.py<br>
│   ├── config_loader.py<br>
│   ├── driver_factory.py<br>
│   ├── table_helper.py<br>
│   └── logger.py<br>
├── pytest.ini            <---- config file for pytest<br>
├── README.md             <---- thie file<br>
├── testlog.log           <---- file for logging.logger<br>
└── requirements.txt      <---- python required libraries<br>

email: scottblackburn1@proton.me
Regards,
Scott Blackburn
