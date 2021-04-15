import requests,json,random,string
from gtts import gTTS

def random_string(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))
rand = random_string(9)
class facebook:
  def __init__(self, url):
    self.url = url

  def dl(url):
      headers = {
                'authority': 'yt1s.com',
                'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                'accept': '*/*',
                'x-requested-with': 'XMLHttpRequest',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://yt1s.com',
                'ec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://yt1s.com/facebook-downloader',
                'accept-language': 'en-US,en;q=0.9',
                'cookie': '__cfduid=d439cdfb738517f0266928797b0d1930e1617294868; _ga=GA1.2.964011950.1617294870; _gid=GA1.2.1293958132.1617294870; __atssc=google%3B1; __atuvc=4%7C13; _PN_SBSCRBR_FALLBACK_DENIED=1617296845563'
      }
      data = {
          'q': url,
          'vt': 'facebook'
      }
      return requests.post('https://yt1s.com/api/ajaxSearch/facebook', headers=headers,
                           data=data).text

class youtube:
    def __init__(self,url):
        self.url = url

    def dl(url):
        headers = {
            'authority': 'api.savemedia.website',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://api.savemedia.website',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://api.savemedia.website/button2/?url={}'.format(url),
            'accept-language': 'en-US,en;q=0.9',
            'cookie': '_gid=GA1.2.944958180.1616888565; PHPSESSID=sl53k3sbchs185uktt7doc5g4b; _gat_gtag_UA_116356283_5=1; _ga_BF2VV4EHKN=GS1.1.1616888587.1.1.1616889273.0; _ga=GA1.1.1780847063.1616888565',
        }

        data = {
            'url': url,
            'convert': 'gogogo'
        }

        response = requests.post('https://api.savemedia.website/convert/', headers=headers, data=data)
        token = json.loads(response.text)["jobid"]
        return ("https://api.savemedia.website/convert/?jobid={}".format(token))

class youtube1:
    def __init__(self,url):
        self.url = url

    def Req1(url):
        headers = {
            'authority': 'yt1s.com',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'accept': '*/*',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://yt1s.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://yt1s.com/en3',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': 'cfduid=d439cdfb738517f0266928797b0d1930e1617294868; _ga=GA1.2.964011950.1617294870; _gid=GA1.2.1293958132.1617294870; atssc=google%3B1; _PN_SBSCRBR_FALLBACK_DENIED=1617294969081; atuvc=3%7C13; atuvs=6065f62587a4998b002; _gat_gtag_UA_173445049_1=1',
        }

        data = {
            'q': url,
            'vt': 'home'
        }
        js = json.loads(requests.post('https://yt1s.com/api/ajaxSearch/index', headers=headers, data=data).text)
        return js["links"]["mp3"]["mp3128"]["k"] + "!" + js["vid"]

    def Req2(data):
        s = data.split("!")
        headers = {
            'authority': 'yt1s.com',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'accept': '*/*',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://yt1s.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://yt1s.com/en3',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': '__cfduid=d439cdfb738517f0266928797b0d1930e1617294868; _ga=GA1.2.964011950.1617294870; _gid=GA1.2.1293958132.1617294870; atssc=google%3B1; _gat_gtag_UA_173445049_1=1; atuvc=4%7C13; atuvs=6065f62587a4998b003; _PN_SBSCRBR_FALLBACK_DENIED=1617296845563',
        }

        data = {
            'vid': s[1],
            'k': s[0]
        }

        return requests.post('https://yt1s.com/api/ajaxConvert/convert', headers=headers, data=data).text
    def dl(url):
        return youtube1.Req2(youtube1.Req1(url))


class youtube2:
    def __init__(self,url):
        self.url = url
    def dl(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.u2convert.com',
            'Connection': 'keep-alive',
            'Referer': 'https://www.u2convert.com/',
            'TE': 'Trailers',
        }

        data = {
            'url': url,
            'quality': '320'
        }

        return requests.post('https://dl.u2convert.com/convert2mp3/', headers=headers, data=data).text


class youtube3:
    def __init__(self,id):
        self.id = id

    def dl(id):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json;charset=utf-8',
            'Origin': 'https://www.flv2mp3.by',
            'Connection': 'keep-alive',
            'Referer': 'https://www.flv2mp3.by/en35/',
        }

        data = '{"videoId":"' + id + '","formatId":"1"}'

        id = json.loads(requests.post('https://www.flv2mp3.by/conv/init', headers=headers, data=data).text)["convertId"]
        return "https://www.flv2mp3.by/conv/download/{}".format(id)

class soundcloud:
    def __init__(self,url):
        self.url = url

    def dl(url):
        cookie = requests.get("https://visoundcloud.com/ajax.php").cookies["__cfduid"]
        cookies = {
            '__cfduid': cookie,
            '_ga': 'GA1.2.1007187401.1617302474',
            '_gid': 'GA1.2.192900121.1617302474',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:85.0) Gecko/20100101 Firefox/85.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://visoundcloud.com',
            'Connection': 'keep-alive',
            'Referer': 'https://visoundcloud.com/?link={}'.format(url),
        }

        data = {
            'url': url
        }

        return requests.post('https://visoundcloud.com/ajax.php', headers=headers, cookies=cookies, data=data).text


class twitter:
    def __init__(self,url):
        self.url = url
    def dl(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:85.0) Gecko/20100101 Firefox/85.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://onlinevideoconverter.pro',
            'Connection': 'keep-alive',
            'Referer': 'https://onlinevideoconverter.pro/',
        }

        params = (
            ('url', url),
        )

        return requests.post('https://onlinevideoconverter.pro/api/convert', headers=headers, params=params).text

class twitter1:
    def __init__(self,url):
        self.url = url
    def dl(url):
       # cookie = requests.get("https://twdown.net/download.php").cookies["__cfduid"]
        cookies = {
            #'__cfduid': cookie,
            '_ga': 'GA1.2.1946905291.1617323343',
            '_gid': 'GA1.2.1147599499.1617323343',
            '__gads': 'ID=50cf855f3303fda4-22b7cd22f0ba0087:T=1617323345:RT=1617323345:S=ALNI_MbX3aA-k9XMaIZ6STGk20T9gy39ng',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:85.0) Gecko/20100101 Firefox/85.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://twdown.net',
            'Connection': 'keep-alive',
            'Referer': 'https://twdown.net/',
            'Upgrade-Insecure-Requests': '1',
            'TE': 'Trailers',
        }

        data = {
            'URL': url
        }

        return requests.post('https://twdown.net/download.php', headers=headers, cookies=cookies, data=data).text

class twitter2:
    def __init__(self,url):
        self.url = url

    def dl (url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:85.0) Gecko/20100101 Firefox/85.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://odownloader.com',
            'Connection': 'keep-alive',
            'Referer': 'https://odownloader.com/twitter-videos-downloader-online-1080p',
        }

        data = {
            'q': url
        }

        return requests.post('https://odownloader.com/ajdownload', headers=headers, data=data).text

class twitter3:
    def __init__(self,url):
        self.url = url

    def dl(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:85.0) Gecko/20100101 Firefox/85.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.getmytweet.com',
            'Connection': 'keep-alive',
            'Referer': 'https://www.getmytweet.com/',
            'Upgrade-Insecure-Requests': '1',
        }

        data = {
            'url': url
        }

        return requests.post('https://www.getmytweet.com/down.php', headers=headers, data=data)
class pinterest_search:
    def __init__(self,text):
       self.text = text
    def search(text):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:85.0) Gecko/20100101 Firefox/85.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Upgrade-Insecure-Requests': '1',
            'Connection': 'keep-alive',
        }

        params = (
            ('source_url', '/search/pins/?q=' + text),
            ('rs', 'typed'),
            ('data',
             '{"options":{"isPrefetch":false,"query":"' + text + '","scope":"pins","no_fetch_context_on_resource":false},"context":{}}'),
        )
        res = json.loads(requests.get('https://www.pinterest.com/resource/BaseSearchResource/get/', headers=headers,
                                      params=params).text)
        links = []
        #for i in range(len(res["resource_response"]["data"]["results"])):
            #r = res["resource_response"]["data"]["results"]#[i]["images"]["orig"]["url"]
        return res

class pinterest:
    def __init__(self,url):
        self.url = url
    def dl(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:85.0) Gecko/20100101 Firefox/85.0',
            'Accept': '*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.videosolo.com',
            'Connection': 'keep-alive',
            'Referer': 'https://www.videosolo.com/online-video-downloader/',
        }

        data = {
            'url': url,
            'format': 'web'
        }

        return requests.post('https://parsevideoapi.videosolo.com/downloader/', headers=headers, data=data).text

class currency:
    def __init__(self,men,lwen,flos):
        self.men = men
        self.lwen = lwen
        self.flos = flos

    def exchange(men, lwen, flos):
        if men.isupper():
            pass
        else:
            men = men.upper()
        if lwen.isupper():
            pass
        else:
            lwen = lwen.upper()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:85.0) Gecko/20100101 Firefox/85.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Referer': 'http://www.geoplugin.com/',
        }

        params = (
            ('jsoncallback', 'jsonp1617418496981'),
            ('_', '1617418573096'),
            ('from', men),
            ('to', lwen),
            ('amount', flos),
        )
        return requests.get('http://www.geoplugin.net/currency_converter.gp', headers=headers, params=params).text

class tiktok:
    def __init__(self,url):
        self.url = url
    def dl(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:85.0) Gecko/20100101 Firefox/85.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://www.instafollowers.co',
            'Connection': 'keep-alive',
            'Referer': 'https://www.instafollowers.co/free-tiktok-views',
            'TE': 'Trailers',
        }

        data = {
            'user': url,
            'productAsks': '{"sm_domain":"https://www.tiktok.com/","preview":"0","sm_type_id":42,"link_status":0,"image_way":""}',
            'multiOptionTake': '',
            'nextTimeline': ''
        }

        return requests.post('https://www.instafollowers.co/phpCurl', headers=headers, data=data).text

class speech:
    def __init__(self,text,lang):
        self.text = text
        self.lang = lang
    def say(text,lang):
        myobj = gTTS(text=text, lang=lang, slow=False)
        if myobj.save(rand + ".mp3") != False:
            return ("saved as  " + rand + ".mp3")
        else:
            return ("error")
