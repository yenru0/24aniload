import os
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


uuid = "362250m4"
# URL = "https://cdn11-xdoodle.xyz/cdn/down/10ae8508e72c9b1b9a70b75655d51d69/Video/1080p/1080p_{}.aaa"

# TYPE = "ani24"
TYPE = "linkkf"
if TYPE == "ani24":
    URL = "https://cdn11-xdoodle.xyz/cdn/down/%s/Video/1080p/1080p_{}.aaa"%(uuid)
elif TYPE == "linkkf":
    URL = "https://k32gg.ani69.com/k32/%s/%s-{}.html"%(uuid, uuid)

OUTFILE = "./loc/{}.ts"



def download(index):
    _ret = True
    if TYPE == "ani24":
        index_text = "%03d"%(index)
        url = URL.format(index_text)
        of = OUTFILE.format(index_text)
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req) as response, open(of, 'wb') as f:
            data = response.read() # a `bytes` object
            f.write(data)
    elif TYPE == "linkkf":
        index_text = "%04d"%(index)
        url = URL.format(index_text)
        of = OUTFILE.format(index_text)
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req) as response, open(of, 'wb') as f:
            data = response.read()
            _ret = bool(data)
            f.write(data)
    return _ret

if __name__ == '__main__':
    if not os.path.isdir('loc'):
        os.mkdir("loc")

index = 0
while True:
    print(index)
    if not download(index):
        break
    index += 1
print('cut')
    