import requests, json
import threading

def get_letter_words(letter, original):
    page_number = 1
    result = []
    while True:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                'X-Requested-With': 'XMLHttpRequest',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Referer': 'https://www.dictionary.com/e/word-finder/5-letter-words/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
            }

            params = {
                'page': f'{page_number}',
                'wordLength': '5',
                'letter': f'{letter.upper()}',
                'action': 'get_wf_widget_page',
                'pageType': '4',
                'nonce': 'eb40d9b58e',
            }
            response = requests.get('https://www.dictionary.com/e/crb-ajax/cached.php', params=params, headers=headers)
            result.extend(json.loads(response.text)['data']['words'])
            page_number+=1
        except:
            break
    original.extend(result)

def get_all_5_letter_words():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    threads = []
    all_words = []
    for i in alphabet:
        t = threading.Thread(target=get_letter_words, args=((i, all_words)))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
        
    return all_words
    
words = get_all_5_letter_words()
with open("words",'w') as f:
    f.write('\n'.join(words).lower())