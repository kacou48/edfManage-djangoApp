from cgitb import html
import requests
import json
import re
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from time import sleep
#from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager

#se connecte au dashbord du client pour retourner sa clé primaire
"""
def get_api_key(id,passwd):
    options=Options()
    options.headless = True
    options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
    monExecutable = r'C:/geckodriver31/geckodriver.exe'
    with webdriver.Firefox(executable_path=monExecutable, options=options) as driver :
        #driver.set_page_load_timeout(30)
        print('proccessing...')
        driver.get('https://www.of.moncompteformation.gouv.fr/espace-prive/html/#/tableau-de-bord')
        
        #sleep(5)
        driver.maximize_window()
        sleep(11)
        
        cookies=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-bottom-sheet-container/mcf-cm-banner/div[2]/button[1]/span[1]')
        cookies.click()
        sleep(1)

        connexion=driver.find_element(By.XPATH,'/html/body/sl7-app/sl7-landing/main/div[1]/sl7-landing-task-section/section/div[2]/a')
        connexion.click()
        driver.maximize_window()
        sleep(15)
        
        driver.find_element(By.ID,'username').click()
        driver.find_element(By.ID,'username').send_keys(id)
        driver.find_element(By.ID,'password').click()
        driver.find_element(By.ID,'password').send_keys(passwd)
        sleep(2)
        driver.find_element(By.CSS_SELECTOR,'.btn-submit').click() 
        print(' connection avec succès...')
        driver.maximize_window()
        sleep(17)
        #print(driver.requests)

        for element in driver.requests:
            
            if type(element.headers["Authorization"])==str :
                bearer=element.headers["Authorization"]
            
        api_key=bearer
        print(' api key capturé avec succès...')
        return api_key
"""

url = "https://www.of.moncompteformation.gouv.fr/espace-prive/html/#/tableau-de-bord"

def get_api_key(id,passwd):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    with webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options) as driver :
        #driver.set_page_load_timeout(30)
        print('proccessing...')
        driver.get(url)
        
        #sleep(5)
        driver.maximize_window()
        sleep(11)
        
        cookies=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/mat-bottom-sheet-container/mcf-cm-banner/div[2]/button[1]/span[1]')
        cookies.click()
        sleep(1)

        connexion=driver.find_element(By.XPATH,'/html/body/sl7-app/sl7-landing/main/div[1]/sl7-landing-task-section/section/div[2]/a')
        connexion.click()
        driver.maximize_window()
        sleep(15)
        
        driver.find_element(By.ID,'username').click()
        driver.find_element(By.ID,'username').send_keys(id)
        driver.find_element(By.ID,'password').click()
        driver.find_element(By.ID,'password').send_keys(passwd)
        sleep(2)
        driver.find_element(By.CSS_SELECTOR,'.btn-submit').click() 
        print(' connection avec succès...')
        sleep(17)
        driver.maximize_window()
        #print(driver.requests)

        for element in driver.requests:
            
            if type(element.headers["Authorization"])==str :
                bearer=element.headers["Authorization"]
            
        api_key=bearer
        print(' api key capturé avec succès...')
        return api_key




#retourne une formation 
def get_file_online(ID_fiche,api_key):
    cookies = {
        'visid_incap_249257': '+4vJiyl2SQu1xpYFasFDDcsiYGIAAAAAQUIPAAAAAACHDd6tSN6hPdjiti5Lf0Wf',
        '_pk_id.14.2cba': '32693434edcc9df1.1652099649.',
        'mcf_cookie_consent_AT_INTERNET': '1',
        'mcf_cookie_consent_MATOMO': '1',
        'atuserid': '%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%222b9215b0-8421-4504-90ad-275403e7c9e7%22%2C%22options%22%3A%7B%22end%22%3A%222023-06-10T12%3A34%3A22.956Z%22%2C%22path%22%3A%22%2F%22%7D%7D',
        'atidvisitor': '%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-554395-%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D',
        '_pk_id.30.7ccd': 'bd50647a2ea28935.1652099664.',
        'incap_ses_393_249257': 'bCxIYUtip0rN1OWdCzh0Baszl2IAAAAA7xJEFeVjJVNGT3fKn6bLXA==',
        'nlbi_249257': 'Ha4bAVMyEkU2zonqsHLyrwAAAAAEjWPCT2YcPKJ9YL2ywGNL',
        'incap_ses_467_249257': 'ZIccLLpEdzmbkYOhqR57Bsszl2IAAAAATTQLXjduqFbQfjiUXyMSkA==',
        'incap_ses_391_249257': 'IL6DJrVNyRWGu+8WBR1tBcszl2IAAAAArdnYQw8+cwvxPiney0eC6w==',
        'incap_ses_390_249257': 'rnedJkuB1WfgDZe4lo9pBcszl2IAAAAAPe3EZmZbfH1C1UjXOtV1xw==',
        'incap_ses_392_249257': 'VeLFXKTWOHouUPafmKpwBcwzl2IAAAAAc7hdg6sW31b0cTNF65hwpg==',
        '_pk_ref.30.7ccd': '%5B%22%22%2C%22%22%2C1654076506%2C%22https%3A%2F%2F5euros.com%2F%22%5D',
        '_pk_ses.30.7ccd': '1',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Authorization': api_key,
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'visid_incap_249257=+4vJiyl2SQu1xpYFasFDDcsiYGIAAAAAQUIPAAAAAACHDd6tSN6hPdjiti5Lf0Wf; _pk_id.14.2cba=32693434edcc9df1.1652099649.; mcf_cookie_consent_AT_INTERNET=1; mcf_cookie_consent_MATOMO=1; atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%222b9215b0-8421-4504-90ad-275403e7c9e7%22%2C%22options%22%3A%7B%22end%22%3A%222023-06-10T12%3A34%3A22.956Z%22%2C%22path%22%3A%22%2F%22%7D%7D; atidvisitor=%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-554395-%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D; _pk_id.30.7ccd=bd50647a2ea28935.1652099664.; incap_ses_393_249257=bCxIYUtip0rN1OWdCzh0Baszl2IAAAAA7xJEFeVjJVNGT3fKn6bLXA==; nlbi_249257=Ha4bAVMyEkU2zonqsHLyrwAAAAAEjWPCT2YcPKJ9YL2ywGNL; incap_ses_467_249257=ZIccLLpEdzmbkYOhqR57Bsszl2IAAAAATTQLXjduqFbQfjiUXyMSkA==; incap_ses_391_249257=IL6DJrVNyRWGu+8WBR1tBcszl2IAAAAArdnYQw8+cwvxPiney0eC6w==; incap_ses_390_249257=rnedJkuB1WfgDZe4lo9pBcszl2IAAAAAPe3EZmZbfH1C1UjXOtV1xw==; incap_ses_392_249257=VeLFXKTWOHouUPafmKpwBcwzl2IAAAAAc7hdg6sW31b0cTNF65hwpg==; _pk_ref.30.7ccd=%5B%22%22%2C%22%22%2C1654076506%2C%22https%3A%2F%2F5euros.com%2F%22%5D; _pk_ses.30.7ccd=1',
        'Referer': 'https://www.of.moncompteformation.gouv.fr/espace-prive/html/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
        'X-ICDC-DGEFP-TOKEN': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTQwODYxMjAsImlhdCI6MTY1NDA3NjUyMCwiaXNzIjoidXJuOmNkYzpzb2NsZTpjb21tdW46aWRwIiwiYXVkIjoiMTk0NTc1MjYtZTA3Mi00ZTJjLWJjOTItZjA0MjdkNDM5YTgxIiwianRpIjoiNWI2ZTE2MDUtNWMwOS00MmNhLWE2YTctMDllOGNkNjM5ZDQwIiwidXJuOmNkYzpjbGFpbXM6dXNlcjpkb21haW5lIjoiQ1BGIiwiYXRfaGFzaCI6ImZUM01EZE9WMjNGeFhNclc1emxzbFEiLCJzdWIiOiJtYXJjLWVyaWNAbGVzZWR1Y2FjdGV1cnMuZnIiLCJ1cm46Y2RjOmNsYWltczphcHBsaWNhdGlvbkVudiI6IlgiLCJzdGF0ZSI6IjhIbXh3NnlXRjZTVV91ZzVmMEhMclhEXzFvT3hRV244bm9KWHVneW1yOFNpYyIsIm5vbmNlIjoiOEhteHc2eVdGNlNVX3VnNWYwSExyWERfMW9PeFFXbjhub0pYdWd5bXI4U2ljIiwiYXRfaGFzaF9pY2RjIjoiZlQzTURkT1YyM0Z4WE1yVzV6bHNsUSJ9.6zBky4-477490UZ-Vi-r2Z2Zv0rprG1gs5uOngwPylY',
        'X-ICDC-ORIGINE': 'SL7',
        'X-RequestID': 'd534a397-b7e9-ce6f-e087-6ffb377ef4d8',
        'X-SessionID': 'd7832e21-1174-6e6a-5c01-948bee44061e',
    }

    response = requests.get(f'https://www.of.moncompteformation.gouv.fr/edof-api/v1/api/private/trainings/{ID_fiche}',headers=headers)
    #data=response.json()
    try: 
        data = response.json()
        print('fichier reçu avec succès...')
    except:
        data = 'null pas reçu'
    return data




def get_all_formation(api_key):
    
    cookies = {
        'mcf_cookie_consent_MATOMO': '1',
        'mcf_cookie_consent_AT_INTERNET': '1',
        'atuserid': '%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%225d07f4be-4504-4691-86ba-f9662c1a2a00%22%2C%22options%22%3A%7B%22end%22%3A%222023-10-14T21%3A35%3A05.246Z%22%2C%22path%22%3A%22%2F%22%7D%7D',
        'atidvisitor': '%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-554395-%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D',
        '_pk_id.30.7ccd': 'b57c29966100ef03.1663018507.',
        '_pk_id.14.2cba': '3474fd9a6172bfbd.1663529721.',
        '_pk_ses.30.7ccd': '1',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.of.moncompteformation.gouv.fr/espace-prive/html/',
        'X-RequestID': '207be42d-5c87-b754-1783-ca51223e5426',
        'X-SessionID': 'f9fdd044-63de-34df-4728-2885664f1050',
        'X-ICDC-DGEFP-TOKEN': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjM5MzUyMjcsImlhdCI6MTY2MzkyNTYyNywiaXNzIjoidXJuOmNkYzpzb2NsZTpjb21tdW46aWRwIiwiYXVkIjoiMTk0NTc1MjYtZTA3Mi00ZTJjLWJjOTItZjA0MjdkNDM5YTgxIiwianRpIjoiZGI2OGQ3NjYtMTFjYi00ZGY4LWJlYjItOGQwZTA3YzUxNmM3IiwidXJuOmNkYzpjbGFpbXM6dXNlcjpkb21haW5lIjoiQ1BGIiwiYXRfaGFzaCI6IkhvTXlWaTVyY2hNWGxERHo0c05IRlEiLCJzdWIiOiJtYXJjLWVyaWNAbGVzZWR1Y2FjdGV1cnMuZnIiLCJ1cm46Y2RjOmNsYWltczphcHBsaWNhdGlvbkVudiI6IlgiLCJzdGF0ZSI6Im1aX2RmeXBoTWJOdlN5bXEtLVR1a1BtYTBEX3RscWYzZ2MwT19rMG80QkdwVSIsIm5vbmNlIjoibVpfZGZ5cGhNYk52U3ltcS0tVHVrUG1hMERfdGxxZjNnYzBPX2swbzRCR3BVIiwiYXRfaGFzaF9pY2RjIjoiSG9NeVZpNXJjaE1YbEREejRzTkhGUSJ9.IQIWTHsbAmDeRO2eHjFJaF7h2weAPMu_-Vs5gVmQXq0',
        'X-ICDC-ORIGINE': 'SL7',
        'Authorization': api_key,
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    params = (
        ('firstElementIndex', '1'),
        ('numberOfElements', '10'),
    )
    url = 'https://www.of.moncompteformation.gouv.fr/edof-api/v1/api/private/organisms/current/trainings'
    response = requests.get(url, headers=headers, params=params, cookies=cookies)
    #print(response.json())
    print('formations reçu avec succès...')
    try: 
        data = response.json()
    except:
        data = {'trainings': 'null pas reçu'}

    return data['trainings']






#permettra d'enregistrer la fiche modifier er retourn un message de confirm
def update_file_online(data,ID_fiche,api_key):
    cookies = {
        'visid_incap_249257': '+4vJiyl2SQu1xpYFasFDDcsiYGIAAAAAQUIPAAAAAACHDd6tSN6hPdjiti5Lf0Wf',
        'incap_ses_1559_249257': 'tBoCVxudBRgDf3olUK6iFTDXa2IAAAAAO2d/s/e0oO+JWt40paAvag==',
        'incap_ses_1523_249257': '2GIiOsPIuG8nL47ujsgiFTrXa2IAAAAALfWvM/OWuwSIQDfeIx5S1g==',
        'incap_ses_957_249257': 'r2OoWBvR5GR7vUT2F/NHDZXJbGIAAAAA+QV4dDw7mABbvMaXtdvHog==',
        'incap_ses_218_249257': 'CdowV6sfEWKqFq9T9H0GA1vMbGIAAAAArmgFLFFXLPSUk/tsSRh7aw==',
        'incap_ses_1564_249257': 'Nx55GFLwDhpDUWUKx3G0FWTMbGIAAAAA/c5Ti58ce0cpbSXoH6zSbQ==',
        'incap_ses_1562_249257': 'xZ7dLjtDiEi1zG0XxVatFeY2bWIAAAAACmSPHhjYQQZbodVXu613BA==',
        'incap_ses_966_249257': 'HJh4UCkKvREPqYF5dOxnDSWybmIAAAAAf/QWWKgdwXB/cRObaucQ9w==',
        'incap_ses_1557_249257': '0DYxcAQ5yzxHsRA7TpObFSmybmIAAAAAPpEvuAmgIH2jp8hdPswjQw==',
        'incap_ses_968_249257': '5ORGIVnNLUhYH3wVbQdvDSuybmIAAAAAUThwUWh+NHYBEQ1h2w07qg==',
        'incap_ses_1558_249257': 'LXz3FzAdiwL4jh3hzCCfFSuybmIAAAAAUowpL18jlk7hL/n5joRszw==',
        'incap_ses_219_249257': '36xOdL5HiWXCJBn2hwsKAyyybmIAAAAA6VAe4DGVyeLEDyprbIA7rA==',
        'incap_ses_1561_249257': 'nzQTdybggG+Dx7YeS8mpFSyybmIAAAAAdtSwBBD2NbAwSfJEJZUkXQ==',
        'incap_ses_1560_249257': 'MXUUSUd5VnvY42HSxzumFXyob2IAAAAA27hk803dLzDks4vovIw/1Q==',
        'incap_ses_960_249257': 'iC4vKxYqMChKRDdSgZtSDaC8b2IAAAAAT++mF4usZkaoecdWmujxHA==',
        'incap_ses_500_249257': 'nxMVTDRasiguWlrv51vwBpUHcWIAAAAAouoxii7ReWqaREGHQ2I8zA==',
        'nlbi_249257': 'MNQVTNU/CjmaOZ3IsHLyrwAAAADGaPUlMVYzW3Ch9Zq7ISgQ',
        'incap_ses_1565_249257': 'xOxZMPwUIHXj2PlRQ/+3FbVlc2IAAAAA1b1oqmJhiQIPnascifpLvw==',
        'incap_ses_963_249257': '6AdeGl0uenlv7EmZBkRdDbZlc2IAAAAAA/roM4z8RKECq6StVXXnqQ==',
        'incap_ses_967_249257': 'wCjyGFlQcmCh9HrL8HlrDbZlc2IAAAAAfDJgLNGyn9BOQjGsr94AFA==',
        'incap_ses_958_249257': 'asK7TglcdgiMsV+mloBLDbdlc2IAAAAAqLkmxdGaeyKpd2otdpGopQ==',
        'incap_ses_501_249257': 'dxQyEjvNs3KQCb0lcunzBrdlc2IAAAAAx9chc8N/DAkp0F+wo2zwkg==',
        'incap_ses_962_249257': 'V4CsWYj4VyHHRUiXk7ZZDbhlc2IAAAAAcDwmVhb8MtPtu5ZC/tUgmQ==',
        'incap_ses_1220_249257': 'bSNcXrAWdmijPuCWNVDuELhlc2IAAAAAPQadfA3SYbqyfxvCyb6OAQ==',
        'incap_ses_961_249257': '9ujhHJJ+iXTfEgurBClWDbllc2IAAAAAjMT1NuPjz2B8kwbXGDhP5w==',
        'incap_ses_944_249257': 'bmo3LgwnkFqWXYuhlMMZDbhlc2IAAAAAxAM6gF2CEycZ8EaIVw7pkw==',
        '_pk_id.14.2cba': '32693434edcc9df1.1652099649.',
        'mcf_cookie_consent_AT_INTERNET': '1',
        'mcf_cookie_consent_MATOMO': '1',
        'atuserid': '%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%222b9215b0-8421-4504-90ad-275403e7c9e7%22%2C%22options%22%3A%7B%22end%22%3A%222023-06-10T12%3A34%3A22.956Z%22%2C%22path%22%3A%22%2F%22%7D%7D',
        'atidvisitor': '%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-554395-%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D',
        '_pk_id.30.7ccd': 'bd50647a2ea28935.1652099664.',
        '_pk_ref.30.7ccd': '%5B%22%22%2C%22%22%2C1652803492%2C%22https%3A%2F%2F5euros.com%2F%22%5D',
        '_pk_ses.30.7ccd': '1',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Authorization': api_key,
        'Connection': 'keep-alive',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'visid_incap_249257=+4vJiyl2SQu1xpYFasFDDcsiYGIAAAAAQUIPAAAAAACHDd6tSN6hPdjiti5Lf0Wf; incap_ses_1559_249257=tBoCVxudBRgDf3olUK6iFTDXa2IAAAAAO2d/s/e0oO+JWt40paAvag==; incap_ses_1523_249257=2GIiOsPIuG8nL47ujsgiFTrXa2IAAAAALfWvM/OWuwSIQDfeIx5S1g==; incap_ses_957_249257=r2OoWBvR5GR7vUT2F/NHDZXJbGIAAAAA+QV4dDw7mABbvMaXtdvHog==; incap_ses_218_249257=CdowV6sfEWKqFq9T9H0GA1vMbGIAAAAArmgFLFFXLPSUk/tsSRh7aw==; incap_ses_1564_249257=Nx55GFLwDhpDUWUKx3G0FWTMbGIAAAAA/c5Ti58ce0cpbSXoH6zSbQ==; incap_ses_1562_249257=xZ7dLjtDiEi1zG0XxVatFeY2bWIAAAAACmSPHhjYQQZbodVXu613BA==; incap_ses_966_249257=HJh4UCkKvREPqYF5dOxnDSWybmIAAAAAf/QWWKgdwXB/cRObaucQ9w==; incap_ses_1557_249257=0DYxcAQ5yzxHsRA7TpObFSmybmIAAAAAPpEvuAmgIH2jp8hdPswjQw==; incap_ses_968_249257=5ORGIVnNLUhYH3wVbQdvDSuybmIAAAAAUThwUWh+NHYBEQ1h2w07qg==; incap_ses_1558_249257=LXz3FzAdiwL4jh3hzCCfFSuybmIAAAAAUowpL18jlk7hL/n5joRszw==; incap_ses_219_249257=36xOdL5HiWXCJBn2hwsKAyyybmIAAAAA6VAe4DGVyeLEDyprbIA7rA==; incap_ses_1561_249257=nzQTdybggG+Dx7YeS8mpFSyybmIAAAAAdtSwBBD2NbAwSfJEJZUkXQ==; incap_ses_1560_249257=MXUUSUd5VnvY42HSxzumFXyob2IAAAAA27hk803dLzDks4vovIw/1Q==; incap_ses_960_249257=iC4vKxYqMChKRDdSgZtSDaC8b2IAAAAAT++mF4usZkaoecdWmujxHA==; incap_ses_500_249257=nxMVTDRasiguWlrv51vwBpUHcWIAAAAAouoxii7ReWqaREGHQ2I8zA==; nlbi_249257=MNQVTNU/CjmaOZ3IsHLyrwAAAADGaPUlMVYzW3Ch9Zq7ISgQ; incap_ses_1565_249257=xOxZMPwUIHXj2PlRQ/+3FbVlc2IAAAAA1b1oqmJhiQIPnascifpLvw==; incap_ses_963_249257=6AdeGl0uenlv7EmZBkRdDbZlc2IAAAAAA/roM4z8RKECq6StVXXnqQ==; incap_ses_967_249257=wCjyGFlQcmCh9HrL8HlrDbZlc2IAAAAAfDJgLNGyn9BOQjGsr94AFA==; incap_ses_958_249257=asK7TglcdgiMsV+mloBLDbdlc2IAAAAAqLkmxdGaeyKpd2otdpGopQ==; incap_ses_501_249257=dxQyEjvNs3KQCb0lcunzBrdlc2IAAAAAx9chc8N/DAkp0F+wo2zwkg==; incap_ses_962_249257=V4CsWYj4VyHHRUiXk7ZZDbhlc2IAAAAAcDwmVhb8MtPtu5ZC/tUgmQ==; incap_ses_1220_249257=bSNcXrAWdmijPuCWNVDuELhlc2IAAAAAPQadfA3SYbqyfxvCyb6OAQ==; incap_ses_961_249257=9ujhHJJ+iXTfEgurBClWDbllc2IAAAAAjMT1NuPjz2B8kwbXGDhP5w==; incap_ses_944_249257=bmo3LgwnkFqWXYuhlMMZDbhlc2IAAAAAxAM6gF2CEycZ8EaIVw7pkw==; _pk_id.14.2cba=32693434edcc9df1.1652099649.; mcf_cookie_consent_AT_INTERNET=1; mcf_cookie_consent_MATOMO=1; atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%222b9215b0-8421-4504-90ad-275403e7c9e7%22%2C%22options%22%3A%7B%22end%22%3A%222023-06-10T12%3A34%3A22.956Z%22%2C%22path%22%3A%22%2F%22%7D%7D; atidvisitor=%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-554395-%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D; _pk_id.30.7ccd=bd50647a2ea28935.1652099664.; _pk_ref.30.7ccd=%5B%22%22%2C%22%22%2C1652803492%2C%22https%3A%2F%2F5euros.com%2F%22%5D; _pk_ses.30.7ccd=1',
        'Current-Siret': '84068088800012',
        'Origin': 'https://www.of.moncompteformation.gouv.fr',
        'Referer': 'https://www.of.moncompteformation.gouv.fr/espace-prive/html/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
        'X-ICDC-DGEFP-TOKEN': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTI4MTMxMDUsImlhdCI6MTY1MjgwMzUwNSwiaXNzIjoidXJuOmNkYzpzb2NsZTpjb21tdW46aWRwIiwiYXVkIjoiMTk0NTc1MjYtZTA3Mi00ZTJjLWJjOTItZjA0MjdkNDM5YTgxIiwianRpIjoiZWJmNWYxOWYtZTI4NS00MDhiLTk4NTAtZGMyNTlhMmZjZWE0IiwidXJuOmNkYzpjbGFpbXM6dXNlcjpkb21haW5lIjoiQ1BGIiwiYXRfaGFzaCI6Imo3U0FTVTd2VnRIdjdodXZvSFNtS1EiLCJzdWIiOiJtYXJjLWVyaWNAbGVzZWR1Y2FjdGV1cnMuZnIiLCJ1cm46Y2RjOmNsYWltczphcHBsaWNhdGlvbkVudiI6IlgiLCJzdGF0ZSI6InQxelpWUXlCM0Z3Q2EyME1PRjFFQTcyNDRMb2RaajRURXJqeWI2azZpSXprSyIsIm5vbmNlIjoidDF6WlZReUIzRndDYTIwTU9GMUVBNzI0NExvZFpqNFRFcmp5YjZrNmlJemtLIiwiYXRfaGFzaF9pY2RjIjoiajdTQVNVN3ZWdEh2N2h1dm9IU21LUSJ9.KDPq-hNltcoDKKlrhiGlfV1xwlwq7ksv9oZe9U8glVQ',
        'X-ICDC-ORIGINE': 'SL7',
        'X-RequestID': 'd86acd74-a4c8-3749-5355-0fe06d10118e',
        'X-SessionID': 'a82e5b7e-6632-12fb-027f-9432426bf6df',
    }

    params = {
        'wantedStatus': 'VALIDATED',
    }
    
    #url = "https://www.of.moncompteformation.gouv.fr/edof-api/v1/api/private/trainings/FormationTEST1?wantedStatus=VALIDATED"
    response = requests.put(f'https://www.of.moncompteformation.gouv.fr/edof-api/v1/api/private/trainings/{ID_fiche}', params=params, cookies=cookies, headers=headers, json=data)
    response=response.json()
    print("It work!!!!")
    try :
        erreur=response["message"]
        message=f"{erreur}\nLA FICHE {ID_fiche} N'AS PAS ETE MODIFIEE"
        statut="error"
    except:
        message=f"Fiche {ID_fiche} modifiée avec succès"
        statut="ok"
    return message,statut
