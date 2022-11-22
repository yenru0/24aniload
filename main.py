import urllib.request

HEADERS = headers = {
    "Connection" : "keep-alive",
    "Cache-Control" : "max-age=0",
    "sec-ch-ua-mobile" : "?0",
    "DNT" : "1",
    "Upgrade-Insecure-Requests" : "1",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site" : "none",
    "Sec-Fetch-Mode" : "navigate",
    "Sec-Fetch-User" : "?1",
    "Sec-Fetch-Dest" : "document",
    "Accept-Encoding" : "gzip, deflate, br",
    "Accept-Language" : "ko-KR,ko;q=0.9"
    }

URL = "https://cdn11-xdoodle.xyz/cdn/down/10ae8508e72c9b1b9a70b75655d51d69/Video/1080p/1080p_{}.aaa"
OUTFILE = "./loc/{}.ts"



def download(index):
    index_text = "%03d"%(index)
    url = URL.format(index_text)
    of = OUTFILE.format(index_text)
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as response, open(of, 'wb') as f:
        data = response.read() # a `bytes` object
        f.write(data)

index = 0
while True:
    download(index)
    index += 1
    