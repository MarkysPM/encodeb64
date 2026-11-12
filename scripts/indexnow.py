"""Submit all sitemap URLs to IndexNow (Bing, Yandex, etc.). Run after deploy: python scripts/indexnow.py"""
import json, re, urllib.request
KEY = "9ab6aa4a6d98cbcb6130399145504c44"
HOST = "encodeb64.com"
UA = {"User-Agent": "Mozilla/5.0 (indexnow-submit)"}
sm = urllib.request.urlopen(urllib.request.Request(f"https://{HOST}/sitemap.xml", headers=UA)).read().decode("utf8")
urls = sorted(set(re.findall(r"<loc>(.*?)</loc>", sm)))
body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt", "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", body, {"Content-Type": "application/json; charset=utf-8", **UA})
try:
    print(len(urls), "URLs ->", urllib.request.urlopen(req).status)
except urllib.error.HTTPError as e:
    print("HTTP", e.code, e.read().decode())
