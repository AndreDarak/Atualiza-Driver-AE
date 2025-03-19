import httpx
import platform
import zipfile
import os
import winreg
import shutil
import time


def get_chromedriver(destino:str):
    url="https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json"
    version = httpx.get(url).json()["channels"]["Stable"]["version"]
    system = platform.system().lower()
    arch="win64" if system == "windows" else "linux64"
    download_url = f"https://storage.googleapis.com/chrome-for-testing-public/{version}/{arch}/chromedriver-{arch}.zip"
    filename = f"REPO/chromedriver_{version}.zip"
    short_version = str(version).split(".")[0]
    name_version = f"CHROME{short_version}.exe"

    response = httpx.get(download_url)
    if response.status_code != 200:
        return False
    
    with open(filename,"wb") as file:
        for chunk in response.iter_bytes(chunk_size=1024):
            file.write(chunk)
    
    with zipfile.ZipFile(filename,"r") as zip_ref:
        zip_ref.extractall(path='REPO')
    os.remove(filename)
    os.rename('REPO/chromedriver-win64/chromedriver.exe',name_version)
    shutil.move(name_version, f'{destino}/{name_version}')

    for arquivo in os.listdir('REPO'):
        caminho_completo = os.path.join('REPO',arquivo)
        shutil.rmtree(caminho_completo)
    return True

def get_geckodriver(destino:str):
    url = 'https://api.github.com/repos/mozilla/geckodriver/releases/latest'
    version = httpx.get(url).json()["tag_name"]
    data = httpx.get(url).json()["assets"]
    asset_name = f"geckodriver-{version}-win64.zip"
    download_url = f'https://github.com/mozilla/geckodriver/releases/download/{version}/{asset_name}'
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Mozilla\Mozilla Firefox") as key:
                firefox_version, _ = winreg.QueryValueEx(key, "CurrentVersion")
    
    nome_arquivo = firefox_version.split('.')[0]
    name_version=f'FIREFOX{nome_arquivo}.exe'


    response = httpx.get(download_url, follow_redirects= True)
    if response.status_code != 200:
        return False
    
    filename = f'REPO/{asset_name}'
    with open(filename,"wb") as file:
        for chunk in response.iter_bytes(chunk_size=1024):
            file.write(chunk)

    with zipfile.ZipFile(filename,"r") as zip_ref:
        zip_ref.extractall(path='REPO')
    os.remove(filename)
    os.rename('REPO/geckodriver.exe',name_version)
    shutil.move(name_version, f'{destino}/{name_version}')

    for arquivo in os.listdir('REPO'):
        caminho_completo = os.path.join('REPO',arquivo)
        shutil.rmtree(caminho_completo)
    return True

pasta_studio = r'C:\AutomationEdge\process-studio\psplugins\web-gui\webui_drivers'
pasta_studio_2 = r'C:\AutomationEdge\Studio\process-studio\psplugins\web-gui\webui_drivers'
mv_chrome_s = -1
amv_chrome_s = ''
mv_firefox_s = -1
amv_firefox_s = ''

pasta_agent = r'C:\AutomationEdge\Agent\ae-agent\psplugins\131_web-gui\webui_drivers'
mv_chrome_a = -1
amv_chrome_a = ''
mv_firefox_a = -1
amv_firefox_a = ''

try:
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Mozilla\Mozilla Firefox") as key:
                firefox_atual, _ = winreg.QueryValueEx(key, "CurrentVersion")
                firefox_version = int(firefox_atual.split('.')[0])

except FileNotFoundError:
     firefox_version = -1


try:     
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Google\Chrome\BLBeacon") as key:
        chrome_atual, _ = winreg.QueryValueEx(key, "version")
        chrome_version = int(chrome_atual.split('.')[0])

except FileNotFoundError:
     chrome_version = -1


if os.path.exists(pasta_studio):
     arquivos = os.listdir(pasta_studio)
     chrome = list(filter(lambda x: 'CHROME' in x, arquivos))
     firefox = list(filter(lambda x: 'FIREFOX' in x, arquivos))
     for arquivo in chrome:
          versao_str = ''.join(filter(str.isdigit, arquivo))
          if int(versao_str) > mv_chrome_s:
               mv_chrome_s = int(versao_str)
               amv_chrome_s = arquivo
    
     if chrome_version > mv_chrome_s:
        get_chromedriver(pasta_studio)

     for arquivo in firefox:
          versao_str = ''.join(filter(str.isdigit, arquivo))
          if int(versao_str) > mv_firefox_s:
               mv_firefox_s = int(versao_str)
               amv_firefox_s = arquivo

     if firefox_version > mv_firefox_s:
          get_geckodriver(pasta_studio)

elif os.path.exists(pasta_studio_2):
        arquivos = os.listdir(pasta_studio_2)
        chrome = list(filter(lambda x: 'CHROME' in x, arquivos))
        firefox = list(filter(lambda x: 'FIREFOX' in x, arquivos))
        for arquivo in chrome:
          versao_str = ''.join(filter(str.isdigit, arquivo))
          if int(versao_str) > mv_chrome_s:
               mv_chrome_s = int(versao_str)
               amv_chrome_s = arquivo
    
        if chrome_version > mv_chrome_s:
            get_chromedriver(pasta_studio_2)

        for arquivo in firefox:
          versao_str = ''.join(filter(str.isdigit, arquivo))
          if int(versao_str) > mv_firefox_s:
               mv_firefox_s = int(versao_str)
               amv_firefox_s = arquivo

        if firefox_version > mv_firefox_s:
          get_geckodriver(pasta_studio_2)
     


if os.path.exists(pasta_agent):
     arquivos = os.listdir(pasta_agent)
     chrome = list(filter(lambda x: 'CHROME' in x, arquivos))
     firefox = list(filter(lambda x: 'FIREFOX' in x, arquivos))
     for arquivo in chrome:
        versao_str = ''.join(filter(str.isdigit, arquivo))
        if int(versao_str) > mv_chrome_a:
            mv_chrome_a = int(versao_str)
            amv_chrome_a = arquivo

     if chrome_version > mv_chrome_a:
        get_chromedriver(pasta_agent)

     for arquivo in firefox:
        versao_str = ''.join(filter(str.isdigit, arquivo))
        if int(versao_str) > mv_firefox_a:
               mv_firefox_a = int(versao_str)
               amv_firefox_a = arquivo

     if firefox_version > mv_firefox_a:
          get_geckodriver(pasta_agent)
