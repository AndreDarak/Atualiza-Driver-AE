Atualiza Driver AE

Este é um script em Python que automatiza o download e a instalação das versões mais recentes dos drivers chromedriver (para Google Chrome) e geckodriver (para Mozilla Firefox), compatíveis com as versões instaladas desses navegadores no sistema. Ele verifica os diretórios especificados, compara as versões dos drivers existentes com as versões dos navegadores e atualiza os drivers se necessário.

Funcionalidades
Faz o download do chromedriver a partir do repositório oficial do Chrome for Testing.
Faz o download do geckodriver a partir das releases do GitHub da Mozilla.
Renomeia os drivers para incluir a versão do navegador correspondente (ex.: CHROME123.exe ou FIREFOX123.exe).
Move os drivers para pastas específicas usadas pelo AutomationEdge (Process Studio e Agent).
Limpa arquivos temporários após o processo.
Requisitos
Python 3.6+
Bibliotecas Python:
httpx (para requisições HTTP)
platform, zipfile, os, winreg, shutil (bibliotecas padrão do Python)
Sistema operacional: Windows (o script usa o registro do Windows para verificar versões dos navegadores).
Google Chrome e/ou Mozilla Firefox instalados (opcional, mas necessário para determinar as versões corretas).
Instalação das dependências

pip install httpx

Como funciona

O script verifica as versões instaladas do Chrome e Firefox no registro do Windows.
Compara essas versões com os drivers já presentes nas pastas especificadas:

C:\AutomationEdge\process-studio\psplugins\web-gui\webui_drivers (Process Studio)
C:\AutomationEdge\Agent\ae-agent\psplugins\131_web-gui\webui_drivers (Agent)

Se a versão do navegador for mais recente que a do driver existente, ele:
Baixa a versão mais recente do chromedriver ou geckodriver.
Extrai, renomeia e move o driver para a pasta correspondente.
Remove arquivos temporários.

Uso
Certifique-se de que as pastas de destino existem no seu sistema ou ajuste os caminhos no código conforme necessário.

Execute o script:


python webdriver_downloader.py

O script atualizará automaticamente os drivers nas pastas especificadas, se necessário.
Estrutura do Código
get_chromedriver(destino): Faz o download e instala o chromedriver.
get_geckodriver(destino): Faz o download e instala o geckodriver.
Lógica principal: Verifica versões e decide quando atualizar os drivers.
Limitações
Funciona apenas em sistemas Windows devido ao uso do winreg.
Requer conexão com a internet para baixar os drivers.
Os caminhos das pastas são fixos e específicos para o AutomationEdge; adapte-os se necessário.