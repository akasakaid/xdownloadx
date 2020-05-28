import requests,re,os,json,wget
from bs4 import BeautifulSoup as bs
from requests.exceptions import *
r = requests.Session()


headers = {
    "cookie":"cit=d425de7bfe989bffVcinZuPSdYf0_kgnr1mY5A%3D%3D; wpn_ad_cookie=38afcdc67a2b1d0fba8dc9ac9f1e4246; cl_f4452fd13f85235c504e57d749444c51=55703869; html5_pref=%7B%22SQ%22%3Afalse%2C%22MUTE%22%3Afalse%2C%22VOLUME%22%3A1%2C%22FORCENOPICTURE%22%3Afalse%2C%22FORCENOAUTOBUFFER%22%3Afalse%2C%22FORCENATIVEHLS%22%3Afalse%2C%22PLAUTOPLAY%22%3Atrue%2C%22CHROMECAST%22%3Afalse%2C%22EXPANDED%22%3Afalse%2C%22FORCENOLOOP%22%3Afalse%7D; last_views=%5B%2255703869-1589471295%22%5D; chat_data_c=%7B%22ct%22%3A%22%2BAWxqCM7MdCnyiLEPedLSau7SY%5C%2Fy3GEUHOx4msGzn5I6gt5jEsIF%2BwW5b%2B2YLn2T98xOdY2kHf4LRZyFffYNsHajxrEc7OHL0GUfi%5C%2Fh%5C%2FSDzVvO1c4KMnRpFe1vsb07MtwwRMnK9NcHMez5tUAEetNqwyT2Ox0K7vKSuXy3fO69qRTng7yOF6U8KNS8s%2BGnPoM8DqRx3Pk5e%5C%2F%2Bs9MeOG8yuSgIi6t2NWoSZ4%2BG%2Bp%2BxUgVgHnALICSO0%5C%2F0vJYQWsRiriLsuaGC8SRgWwD6s39YGQBNjS%2BCRADIuMy1xkv%5C%2FxK4iE02jMX%5C%2F5AJ6%5C%2Fu%5C%2FqZRzLJjTaac%5C%2F0ryYFoTR38MhNQuSjEG76TNk%2BojIESVkUiC4IjUMbLN4SHcgpAj0zqqvjtA5ez44Y3R0PWEeS5E74cbjARv6i5ga4lrlUZScNRSSx3q60JvxVdUNBRmJf0lURGg70VEr2HmwQSrI0zcRKYI3xoG4HKWpFAm9p7lKJEeHySw3RbgFArQ7dAzBRzApwhsGvKi%5C%2FgM81wvUprKvtHpRLKE9V9viC0gij5Q0nnI9c7UMnFjqJkyKDQjWRMIHPzA0cI6RDwNq4VWjhNEzIKj2e81gRbDYo7kTV4KjAj3lhJ918JW5UuFWdD80BM0ZZCBfEJQwnxut%5C%2FlvLWNjkpH7aCNwjB7pqo6o%5C%2FyrJSxFRp7Krf%5C%2FqEk0NnYfJYRNQ746vMrgFgxE%2B6%5C%2FYRUv6c8y7auYcvsuH%2B8aPtdmDjQV03ldRNEMH3eS91A2K89%2B8ZYkbEVu3389b0fCT7D84TwDzCq29jhoNwqEunSoiGn%2BrUanD10srAs7ikTLsLbMv5MQsrxZKeDEMDJ090tjeKQlVwQA1%2BpjBs1hCBrQHIeuZOac20mrZAyND4oQDhXGCXw8HRcD3ihLJK7xwvZi5pPg8K1WLlPspqEW%5C%2F8E%2B448UBGzbX%5C%2FmxDfu0uryAnJidXdzkV7YG6Q%5C%2F4oSKnYyJckpdIA4fLAl5Egq7bfHPsK8si%2BbJFIOQ5TW5T5zMXbI06CdoXTV4PgpgwLQqTkDEPRD3ySaNUjzr2d6N95%5C%2F5bCEaN3cISlcbG7zJeSiTFKxgOSPU0ABot9ap4cBrbpV1GWDM0aM0yqUutsQ0HY2gb8rR1lWKONhGWG50sIJa2%5C%2FCCGkoaAe9pTSteU46%2BmlhU5d49sLuqMk%2Bdgt9xfbo1lF%5C%2FGV0sIPg3ibaTE1Vg9slItKsoMXgKm%2B0KCJXa9AWFyTed3%2BBoCleViepEWxtrsLaMqiEHzW%2Bc9GujnoLJKjPM8OmCp1TIf%22%2C%22iv%22%3A%2290806b855d57ded78eb421d8edc9ddc2%22%2C%22s%22%3A%2261ad50c0743691a9%22%7D; multi_accounts=5482279f351b182cWPGh8270bqOKalEGoeoUDm95RXha0jByqgKdmhxlplAYrafPm4UnQfn_RscC0xxk; session_token=de607a8373e19e267VPXm9UZOXMAmefRcVwxA2TOkhKvh8yl9na0DgjDPUv7lJ4rtir8CxKl5UE0g72KFDAZqnc6b_ZvQA9RCGxYMx1xXBSZhHH7OYJrsYDQ_Uph-clb8SBDmtg9bIvDaxw2X7peEG3ZrMBk87VPx6WdjHzmizJanr4XP02Meh2OUsj3aUCoAU8Wt4XBYZtyPeIQhdsi-Iz1qh-QPfkvDNu96mFIdUlKxTgKY5UG5LYay9eSbeWq9q_TvjQFOfAGRvmWCRMVvTlyEqdYjXuHpFsbJQCnDTq-BRLuZgjnSliHAMWHbyjS5DlBpnaM--GuDui9QvarxCF3ZIVTAXQDgD1X42BxBgWvpSIcIAjbdKE7Wc06MJvhszS-ZTVPFwVNV4k4lBdQrrX0_F5dM5zadn6yU5sMPC_pYLEKGU80DmkBS2UJ2o6UH2bcsIjL3Ni8m8ms; X-Backend=10|Xr1oV|Xr1oI",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--------------------".center(30))
    print("[XNXX DOWNLOADER]".center(30))
    print("Coded by AkasakaID".center(30))
    print("--------------------".center(30))


def dl(link):
    banner()
    try:
        r1 = r.get(link,headers=headers).text
        r2 = bs(r1,'html.parser')
        vid1 = r2.find("meta",attrs={"property":"og:video"})["content"]
        vid2 = vid1.replace("https://static-l3.xnxx-cdn.com/swf/xv-player.swf?id_video=","")
        r3 = r.post('https://www.xnxx.com/video-download/'+vid2,headers=headers)
        r3_dec = json.loads(r3.text)
        if r3_dec["LOGGED"] == False:exit("Tidak bisa download\nHubungi Author !!\nhttps://t.me/AkasakaID")
        else:
            url1 = r3_dec["URL"]
            url2 = r3_dec["URL_LOW"]
            print("(1) MP4\n(2) 3GP")
            kl = int(input("choose video quality > "))
            if kl == 1:wget.download(url1)
            elif kl == 2:wget.download(url2)
            else:exit("byee ^-^")
    except ConnectionError:exit('bad connection !!')
    except Timeout:exit('timeout !!')
page = 1
def search(page,query):
    banner()
    try:
        a = r.get(f'https://www.xnxx.com/search/{query}/{page}',headers=headers).text
        b = bs(a,'html.parser')
        c = b.find('div',attrs={'class':'mozaique'}).findAll('div',attrs={'class':'thumb-under'})
        nv = 1
        print(f"0. Next page")
        for li in c:
            print(f"{nv}.",li.find('a').get('title'))
            nv += 1
        ch = int(input('nomor > '))
        if ch == 0:
            page += 1
            search(page,query)
        else:
            dl('https://xnxx.com'+c[ch-1].find('a').get('href'))
    except ConnectionError:exit('bad connection !!')
    except Timeout:exit('timeout !!')

banner()
print("""
1. search
2. paste
""")
pil = int(input("choice > "))
if pil == 1:
    banner()
    qr = input('search : ')
    qrr = qr.split()
    if len(qrr) > 1:
        query = "+".join(qrr)
    else:query = qr
    search(page,query)
elif pil == 2:
    banner()
    link = input('input link > ')
    dl(link)
else:
    print('wrong input')