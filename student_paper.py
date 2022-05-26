import requests as req

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

url= 'https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/ccd=UCupb4/record?r1=1&h1=0'
r = req.get(url, headers=header)
#root_json = url.json()
print(r.text)