import random
import time
import base64
import json
import argparse

from browserforge.fingerprints import Screen, FingerprintGenerator

class DataDome:
    def __init__(self, ddv, ddk, url):
        self.__ddv = ddv
        self.__ddk = ddk
        self.__url = url
        self.__screen = Screen(
            min_width=1280, max_width=5120, min_height=720, max_height=2880
        )
        self.__headers = FingerprintGenerator(
            browser=("chrome", "firefox", "safari", "edge"),
            os=("windows", "macos"),
            device="desktop",
            locale=("zh-CN", "en"),
            screen=self.__screen,
            http_version=2,
            strict=True,
            mock_webrtc=True,
        )
        self.__temps = self.__headers.generate()

    def build(self):
        # DONT CHANGE THIS ==============================================
        stcfp = f"""ps://js.datadome.co/tags.js?id={self.__ddk}:2:90854)
    at https://js.datadome.co/tags.js?id={self.__ddk}:2:53225"""
        # DONT CHANGE THIS ==============================================
        return {
            "headers": {
                "Content-type": "application/x-www-form-urlencoded",
                "Host": "api-js.datadome.co",
                "Origin": self.__url,
                "Referer": self.__url,
                "Accept-Encoding": self.__temps.headers.get("Accept-Encoding"),
                "Accept-Language": self.__temps.headers.get("Accept-Language"),
                "Sec-Ch-Ua": self.__temps.headers.get("sec-ch-ua"),
                "Sec-Ch-Ua-Mobile": self.__temps.headers.get("sec-ch-ua-mobile"),
                "Sec-Ch-Ua-Platform": self.__temps.headers.get("sec-ch-ua-platform"),
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "User-Agent": self.__temps.headers.get("User-Agent"),
                "Upgrade-Insecure-Requests": self.__temps.headers.get(
                    "Upgrade-Insecure-Requests"
                ),
            },
            "payload": {
                "ddv": self.__ddv,
                "eventCounters": [],
                "jsType": "ch",
                "ddk": self.__ddk,
                "request": "%2F",
                "responsePage": "origin",
                "cid": "null",
                "Referer": self.__url,
                "jsData": {
                    "ttst": f"{random.randint(10, 99)}.{random.randint(1000000000000, 9000000000000)}",  # runtime
                    "ifov": "false",
                    "hc": self.__temps.navigator.hardwareConcurrency or "NA",  # Hardware Concurrency
                    "br_oh": self.__temps.screen.outerHeight,  # outer height of the browser window
                    "br_ow": self.__temps.screen.outerWidth,  # outer width of the browser window
                    "ua": self.__temps.headers.get("User-Agent"),  # user agent
                    "wbd": "false",  # determine if it is within an automated testing tool environment
                    "dp0": "true",
                    "tagpu": f"{random.randint(10, 99)}.{random.randint(1000000000000, 9000000000000)}", # could be associated with GPU operations
                    "wdif": "false",  # determine if an iframe's contentWindow is the same as the top-level window object
                    "wdifrm": "false",  # to check if an iframe is within the same context as the main page
                    "npmtm": "false",  # determine if the browser supports plugins
                    "br_h": self.__temps.screen.height,  # browser window height
                    "br_w": self.__temps.screen.width,  # browser window width
                    "isf": "false",  # determine if scrolling has reached the bottom (guess)
                    "nddc": 1,  # datadome cookie status
                    "rs_h": self.__temps.screen.availHeight or "NA",  # available screen height (guess)
                    "rs_w": self.__temps.screen.availWidth or "NA",  # available screen width (guess)
                    "rs_cd": 24,
                    "phe": "false",  # detect if PhantomJS exists
                    "nm": "false",
                    "jsf": "false",
                    "lg": self.__temps.navigator.language or "NA",  # browser language
                    "pr": self.__temps.screen.devicePixelRatio or "NA",  # screen's device pixel ratio
                    "ars_h": self.__temps.screen.availHeight or "NA",  # available screen height (guess)
                    "ars_w": self.__temps.screen.availWidth or "NA",  # available screen width (guess)
                    "tz": -480,  # timezone (new Date().getTimezoneOffset())
                    "str_ss": "true",  # !!window.sessionStorage
                    "str_ls": "true",  # !!window.localStorage
                    "str_idb": "true",  # !!window.indexedDB
                    "str_odb": "false",  # !!window.openDatabase（guess）
                    "plgod": "false",  # Plugin Object Definition
                    "plg": random.randint(5, 14),  # Plugin number（guess）
                    "plgne": "true",  # plugin-related detection
                    "plgre": "true",  # plugin-related detection
                    "plgof": "false",  # plugin-related detection
                    "plggt": "false",  # plugin-related detection
                    "pltod": "false",  # plugin-related detection
                    "hcovdr": "false",  # navigator.hardwareConcurrency
                    "hcovdr2": "false",  # navigator.hardwareConcurrency
                    "plovdr": "false",  # Performance/Load Validation/Detection Result
                    "plovdr2": "false",  # Performance/Load Validation/Detection Result
                    "ftsovdr": "false",  # Feature/Test/Support Validation/Detection Result
                    "ftsovdr2": "false",  # Feature/Test/Support Validation/Detection Result
                    "lb": "false",  # detect if it is a fake browser using navigator.userAgent and navigator.productSub
                    "eva": 33,
                    "lo": "false",  # detect if it is a fake browser by using navigator.userAgent, navigator.oscpu, and navigator.platform
                    "ts_mtp": 0,  # navigator.msMaxTouchPoints touch operation support on the device
                    "ts_tec": "false",  # document.createEvent("TouchEvent")
                    "ts_tsa": "false",  # window.ontouchstart
                    "vnd": self.__temps.navigator.vendor or "NA",  # window.navigator.vendor browser graphics rendering engine provider
                    "bid": "NA",  # window.navigator.browserId（guess）
                    "mmt": "application/pdf,text/pdf",  # window.navigator.mimeTypes
                    "plu": "PDF Viewer,Chrome PDF Viewer,Chromium PDF Viewer,Microsoft Edge PDF Viewer,WebKit built-in PDF",
                    # plugins
                    "hdn": "false",  # !!document.hidden
                    "awe": "false",  # !!window.awesomium
                    "geb": "false",  # !!window.geb
                    "dat": "false",  # window.domAutomation
                    "med": "defined",  # window.navigator.mediaDevices supported is indicated as 'defined', unsupported is indicated as 'NA'
                    "aco": "probably",
                    "acots": "false",  # audio/ogg
                    "acmp": "probably",
                    "acmpts": "true",  # audio/mpeg
                    "acw": "probably",
                    "acwts": "false",  # audio/wav
                    "acma": "maybe",
                    "acmats": "false",  # audio/x-m4a
                    "acaa": "probably",
                    "acaats": "true",  # audio/aac
                    "ac3": "",
                    "ac3ts": "false",  # audio/3gpp
                    "acf": "probably",
                    "acfts": "false",  # audio/flac
                    "acmp4": "maybe",
                    "acmp4ts": "false",  # audio/mp4
                    "acmp3": "probably",
                    "acmp3ts": "false",  # audio/mp3
                    "acwm": "maybe",
                    "acwmts": "false",  # audio/wma
                    "ocpt": "false",  # canPlayType
                    "vco": "",
                    "vcots": "false",  # Video Codec Ogg Theora with MSE Support
                    "vch": "probably",
                    "vchts": "true",  # video/mp4
                    "vcw": "probably",
                    "vcwts": "true",  # video/webm
                    "vc3": "maybe",
                    "vc3ts": "false",  # video/3gpp
                    "vcmp": "",
                    "vcmpts": "false",  # video/mpeg
                    "vcq": "",
                    "vcqts": "false",  # video/quicktime
                    "vc1": "probably",
                    "vc1ts": "true",  # video/vc-1
                    "dvm": self.__temps.navigator.deviceMemory or "NA",  # navigator.deviceMemory
                    "sqt": "false",  # support for Sequentum
                    "so": "landscape-primary",  # device screen orientation
                    "wdw": "true",
                    "cokys": "bG9hZFRpbWVzY3NpYXBwL=",  # loadTimescsiapp
                    "ecpc": "false",  # might be detecting the Node environment
                    "lgs": "true",
                    "lgsod": "false",
                    "psn": "true",  # !!window.PermissionStatus
                    "edp": "true",  # !!window.EyeDropper
                    "addt": "true",  # !!window.AudioData
                    "wsdc": "true",  # !!window.WritableStreamDefaultController
                    "ccsr": "true",
                    "nuad": "true",  # !!window.NavigatorUAData
                    "bcda": "true",
                    "idn": "true",  # !(!window.Intl || !Intl.DisplayNames)
                    "capi": "false",  # detect some API capabilities of window.navigator
                    "svde": "false",  # !!window.SVGDiscardElement
                    "vpbq": "true",  # window.VideoPlaybackQuality Web video playback quality
                    "ucdv": "false",
                    "spwn": "false",  # !!window.spawn might be detecting child processes
                    "emt": "false",
                    "bfr": "false",
                    "dbov": "false",  # might be checking for browser debugging
                    "cfpfe": "ZnVuY3Rpb24oKXt2YXIgdD1kb2N1bWVudFsnXHg3MVx4NzVceDY1XHg3Mlx4NzlceDUzXHg2NVx4NmNceDY1XHg2M1x4NzRceDZmXHg3MiddKCdceDYyXHg3Mlx4NmZceDc3XHg3M1x4NjVceDcyXHg2Nlx4NmNceDZmXHg3N1x4MmRceDYzXHg2Zlx4NmVceDc0XHg2",
                    "stcfp": base64.b64encode(stcfp.encode("utf-8")).decode(),  # a stack trace containing ddk
                    "ckwa": "true",  # dd_testcookie
                    "prm": "true",  # navigator.permissions
                    "tzp": "Asia/Shanghai",
                    "cvs": "true",  # canvas
                    "usb": "defined",  # window.navigator.usb
                    "glvd": self.__temps.videoCard.vendor or "NA",  # webgl UNMASKED_VENDOR_WEBGL
                    "glrd": self.__temps.videoCard.renderer or "NA",  # webgl UNMASKED_RENDERER_WEBGL
                    "wwl": "false",
                    "jset": int(time.time()),
                },
            },
        }

    def output_json(self):
        data = self.build()
        return json.dumps(data, indent=4)

    def output_data(self):
        data = self.build()
        return data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fuck DataDome")
    parser.add_argument("--ddv", type=str, required=True, help="DataDome Version")
    parser.add_argument("--ddk", type=str, required=True, help="DataDome Key")
    parser.add_argument("--url", type=str, required=True, help="Target Website Url")
    args = parser.parse_args()

    datadome = DataDome(ddv=args.ddv, ddk=args.ddk, url=args.url)
    json_data = datadome.output_json()
    # print(json_data)
    breakpoint()

    import requests
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,id;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.hermes.com',
        'priority': 'u=1, i',
        'referer': 'https://www.hermes.com/',
        'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    }
    cookies = {
        'OptanonAlertBoxClosed': '2024-09-25T13:20:56.171Z',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Sep+26+2024+06%3A52%3A32+GMT%2B0900+(Eastern+Indonesia+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=8cadd951-2d1d-4f84-ba7c-1354960b65d9&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=ID%3BMU',
        'GeoFilteringBanner': '1',
        '_ga': 'GA1.1.4416237.1727270456',
        '_gcl_au': '1.1.766724459.1727270457',
        '_cs_c': '1',
        'rskxRunCookie': '0',
        'rCookie': 'm68ti6yl8ua50rszvwy082m1hw8i07',
        '_uetsid': '00bece207b4111efaa004b9d09ff15b1',
        '_uetvid': '00bf12a07b4111ef864cf5ad02a1b4e3',
        'x-xsrf-token': '25dbfb86-b1a8-43ae-a9dd-4520d6a65b57',
        'ECOM_SESS': 'ehmdakzus1z6qn5afgsbp0434h',
        'correlation_id': 'oeb8yns9ckcv3ldu66c6lzzvb7faz08v9ufohdlaixa3vq5z7ajlir1t4uukah6o',
        '_cs_cvars': '%7B%221%22%3A%5B%22clienttype%22%2C%22non-connected%22%5D%2C%222%22%3A%5B%22pagetype%22%2C%22single%20product%20page%22%5D%2C%223%22%3A%5B%22pagename%22%2C%22Hooded%20auto%20coat%20%7C%20Herm%C3%A8s%20USA%22%5D%2C%224%22%3A%5B%22menu_lv1%22%2C%22MEN%22%5D%2C%225%22%3A%5B%22menu_lv2%22%2C%22MENREADYTOWEAR%22%5D%2C%226%22%3A%5B%22in_store_only%22%2C%22no%22%5D%2C%227%22%3A%5B%22departmentcode%22%2C%22H%22%5D%2C%229%22%3A%5B%22category%22%2C%22H%2FH20%22%5D%2C%2212%22%3A%5B%22productcode%22%2C%22H461320H40150%22%5D%7D',
        '_fbp': 'fb.1.1727270516513.753951651614570',
        '__cf_bm': 'vCZ53i1kKu6NuqLrZMzgMZJJ5qSr.6cniHfl5IB5r80-1727300591-1.0.1.1-6E0Gbd5eRE.cmqntLCJIwgvBRuBbuSIV1smw2jiBmLVEjF3qK2iIRi_0CZG85wsgHr5td84ZaXFtqptzR07ygA',
        '_cs_mk': '0.19509414924740853_1727300608804',
        '_ga_Y862HCHCQ7': 'GS1.1.1727300608.3.1.1727301151.0.0.0',
        'lastRskxRun': '1727301152099',
        '_cs_id': 'd3247bf6-e37d-a658-f66d-19b1355a8cca.1727270458.2.1727301152.1727297963.1.1761434458701.1',
        'datadome': 'cE93RuHxP35GdV3Axfog73Eme7AHOQzcnHmU3uZ~rpN~IuZwv_zEJBwYyjkVQDhNRrveSiqkn2418Zmj6~GlkTSXH9_yviyRVASo3F~MSnCqnRC8GWOz0LljElJWRGFz',
        '_cs_s': '7.0.0.1727303043835',
    }

    # data = 'jsData=%7B%22ttst%22%3A20.799999999348074%2C%22ifov%22%3Afalse%2C%22hc%22%3A8%2C%22br_oh%22%3A816%2C%22br_ow%22%3A1536%2C%22ua%22%3A%22Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F129.0.0.0%20Safari%2F537.36%20Edg%2F129.0.0.0%22%2C%22wbd%22%3Afalse%2C%22dp0%22%3Atrue%2C%22tagpu%22%3A6.738121195946289%2C%22wdif%22%3Afalse%2C%22wdifrm%22%3Afalse%2C%22npmtm%22%3Afalse%2C%22br_h%22%3A299%2C%22br_w%22%3A1528%2C%22isf%22%3Afalse%2C%22nddc%22%3A1%2C%22rs_h%22%3A864%2C%22rs_w%22%3A1536%2C%22rs_cd%22%3A24%2C%22phe%22%3Afalse%2C%22nm%22%3Afalse%2C%22jsf%22%3Afalse%2C%22lg%22%3A%22en-US%22%2C%22pr%22%3A1.25%2C%22ars_h%22%3A816%2C%22ars_w%22%3A1536%2C%22tz%22%3A-540%2C%22str_ss%22%3Atrue%2C%22str_ls%22%3Atrue%2C%22str_idb%22%3Atrue%2C%22str_odb%22%3Afalse%2C%22plgod%22%3Afalse%2C%22plg%22%3A2%2C%22plgne%22%3Atrue%2C%22plgre%22%3Atrue%2C%22plgof%22%3Afalse%2C%22plggt%22%3Afalse%2C%22pltod%22%3Afalse%2C%22hcovdr%22%3Afalse%2C%22hcovdr2%22%3Afalse%2C%22plovdr%22%3Afalse%2C%22plovdr2%22%3Afalse%2C%22ftsovdr%22%3Afalse%2C%22ftsovdr2%22%3Afalse%2C%22lb%22%3Afalse%2C%22eva%22%3A33%2C%22lo%22%3Atrue%2C%22ts_mtp%22%3A10%2C%22ts_tec%22%3Afalse%2C%22ts_tsa%22%3Afalse%2C%22vnd%22%3A%22Google%20Inc.%22%2C%22bid%22%3A%22NA%22%2C%22mmt%22%3A%22application%2Fpdf%2Capplication%2Fx-google-chrome-pdf%22%2C%22plu%22%3A%22Microsoft%20Edge%20PDF%20Plugin%2CMicrosoft%20Edge%20PDF%20Viewer%22%2C%22hdn%22%3Afalse%2C%22awe%22%3Afalse%2C%22geb%22%3Afalse%2C%22dat%22%3Afalse%2C%22med%22%3A%22defined%22%2C%22aco%22%3A%22probably%22%2C%22acots%22%3Afalse%2C%22acmp%22%3A%22probably%22%2C%22acmpts%22%3Atrue%2C%22acw%22%3A%22probably%22%2C%22acwts%22%3Afalse%2C%22acma%22%3A%22maybe%22%2C%22acmats%22%3Afalse%2C%22acaa%22%3A%22probably%22%2C%22acaats%22%3Atrue%2C%22ac3%22%3A%22maybe%22%2C%22ac3ts%22%3Afalse%2C%22acf%22%3A%22probably%22%2C%22acfts%22%3Afalse%2C%22acmp4%22%3A%22maybe%22%2C%22acmp4ts%22%3Afalse%2C%22acmp3%22%3A%22probably%22%2C%22acmp3ts%22%3Afalse%2C%22acwm%22%3A%22maybe%22%2C%22acwmts%22%3Afalse%2C%22ocpt%22%3Afalse%2C%22vco%22%3A%22%22%2C%22vcots%22%3Afalse%2C%22vch%22%3A%22probably%22%2C%22vchts%22%3Atrue%2C%22vcw%22%3A%22probably%22%2C%22vcwts%22%3Atrue%2C%22vc3%22%3A%22maybe%22%2C%22vc3ts%22%3Afalse%2C%22vcmp%22%3A%22%22%2C%22vcmpts%22%3Afalse%2C%22vcq%22%3A%22%22%2C%22vcqts%22%3Afalse%2C%22vc1%22%3A%22probably%22%2C%22vc1ts%22%3Atrue%2C%22dvm%22%3A8%2C%22sqt%22%3Afalse%2C%22so%22%3A%22landscape-primary%22%2C%22wdw%22%3Atrue%2C%22cokys%22%3A%22bG9hZFRpbWVzY3NpYXBwL%3D%22%2C%22ecpc%22%3Afalse%2C%22lgs%22%3Atrue%2C%22lgsod%22%3Afalse%2C%22psn%22%3Atrue%2C%22edp%22%3Atrue%2C%22addt%22%3Atrue%2C%22wsdc%22%3Atrue%2C%22ccsr%22%3Atrue%2C%22nuad%22%3Atrue%2C%22bcda%22%3Afalse%2C%22idn%22%3Atrue%2C%22capi%22%3Afalse%2C%22svde%22%3Afalse%2C%22vpbq%22%3Atrue%2C%22ucdv%22%3Afalse%2C%22spwn%22%3Afalse%2C%22emt%22%3Afalse%2C%22bfr%22%3Afalse%2C%22dbov%22%3Afalse%2C%22cfpfe%22%3A%22ZnVuY3Rpb24oKXt2YXIgYT0hIWRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoIiNhZGQtdG8tY2FydC1idXR0b24taW4tc3RvY2siKTtyZXR1cm4gYX0%3D%22%2C%22stcfp%22%3A%22Yy5ldmFsdWF0ZSAoaHR0cHM6Ly93d3cuZ29vZ2xldGFnbWFuYWdlci5jb20vZ3RtLmpzP2lkPUdUTS1XMzlCMlA6MTk5OjcyKQogICAgYXQgV2MuZmUgKGh0dHBzOi8vd3d3Lmdvb2dsZXRhZ21hbmFnZXIuY29tL2d0bS5qcz9pZD1HVE0tVzM5QjJQOjIyNjo0MTQp%22%2C%22ckwa%22%3Atrue%2C%22prm%22%3Atrue%2C%22tzp%22%3A%22Asia%2FJayapura%22%2C%22cvs%22%3Atrue%2C%22usb%22%3A%22defined%22%2C%22uid%22%3A%22oeb8yns9ckcv3ldu66c6lzzvb7faz08v9ufohdlaixa3vq5z7ajlir1t4uukah6o%22%2C%22emd%22%3A%22k%3Aai%2Cvi%2Cao%22%2C%22glvd%22%3A%22Google%20Inc.%20(Intel)%22%2C%22glrd%22%3A%22ANGLE%20(Intel%2C%20Intel(R)%20Iris(R)%20Xe%20Graphics%20(0x00009A49)%20Direct3D11%20vs_5_0%20ps_5_0%2C%20D3D11)%22%2C%22wwl%22%3Afalse%2C%22log2%22%3Atrue%2C%22jset%22%3A1727270627%7D&eventCounters=%5B%5D&jsType=ch&cid=SrBlUcDuQpHscz3_q1MqgzYMT2mXnnMpwkmYZQ_WO3gBnR__x9mxb8LU25ZhO21xa9um4fA~55qavzyQyL6_TGyxgPyIAItBX0RSSXk1Lqmmu~zuqSJVi46zYNp0X1uH&ddk=2211F522B61E269B869FA6EAFFB5E1&Referer=https%253A%252F%252Fwww.hermes.com%252Fus%252Fen%252Fproduct%252Fhooded-auto-coat-H461320H40150%252F&request=%252Fus%252Fen%252Fproduct%252Fhooded-auto-coat-H461320H40150%252F&responsePage=origin&ddv=4.35.0'
    proxies = {
        "http": "http://scrapeops:f2d43fe5-5bee-41ab-83f9-da70ae59c60a@residential-proxy.scrapeops.io:8181",
        "https":"http://scrapeops:f2d43fe5-5bee-41ab-83f9-da70ae59c60a@residential-proxy.scrapeops.io:8181",
    }

    response = requests.post('https://dd.hermes.com/js/', headers= headers, data= datadome.build()['payload'], proxies=proxies) 
    # breakpoint()
    ckx = 'cE93RuHxP35GdV3Axfog73Eme7AHOQzcnHmU3uZ~rpN~IuZwv_zEJBwYyjkVQDhNRrveSiqkn2418Zmj6~GlkTSXH9_yviyRVASo3F~MSnCqnRC8GWOz0LljElJWRGFz'
    cookiesfix = response.json()['cookie'].split("=")[1].split(";")[0]
    cookies['datadome'] = ckx
    # cookies['datadome'] = cookiesfix

    response = requests.get('https://www.hermes.com/us/en/product/hooded-auto-coat-H461320H40150', cookies=cookies, headers=headers, proxies=proxies)


    
    breakpoint()