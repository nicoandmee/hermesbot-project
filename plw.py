import os
import time
from datetime import datetime
from playwright.sync_api import sync_playwright
# from dotenv import load_dotenv
import logging
import random
import time
from playwright_stealth import stealth_sync
import logging
import re
import sys
import argparse
from user_agent import generate_user_agent

SITE_URL_WITH_DATADOME = "https://www.hermes.com/us/en/product/lindy-ii-mini-bag-H085956CK55/"
# https://www.hermes.com/us/en/product/hooded-auto-coat-H461320H40150/
# ddk: 2211F522B61E269B869FA6EAFFB5E1
with sync_playwright() as pr:
    wargs = []
    # wargs.append('--enable-logging=stderr')
    # list chromium arguments: https://peter.sh/experiments/chromium-command-line-switches/
    wargs.append('--v=1')
    wargs.append('--no-sandbox')
    # wargs.append('--enable-features=NetworkService,NetworkServiceInProcess')
    # wargs.append('--enable-automation')
    # wargs.append('--disable-popup-blocking')
    # wargs.append('--disable-web-security')
    # wargs.append('--start-maximized')
    # wargs.append('--disable-fetching-hints-at-navigation-start')
    # wargs.append('--force-first-run')
    # wargs.append('--content-shell-hide-toolbar')
    # wargs.append('--suppress-message-center-popups')
    # wargs.append('--no-first-run')
    # wargs.append('--force-show-update-menu-badge')
    #https://www.reddit.com/r/learnjavascript/comments/skbokf/fetch_request_from_server_to_web_api_returns/?rdt=62425
    # 
    browser =  pr.chromium.launch(headless=False, args=wargs)

    proxy = {"server":"http://residential-proxy.scrapeops.io:8181",
             "username":"scrapeops",
             "password":"f2d43fe5-5bee-41ab-83f9-da70ae59c60a"
    }
    context = browser.new_context(
        user_agent=generate_user_agent(),
        no_viewport=True,
        permissions=['geolocation', 'notifications'],
        java_script_enabled=True,
        
        proxy=proxy
    )
    page = context.new_page()
    stealth_sync(page)
    page.goto(SITE_URL_WITH_DATADOME, wait_until='domcontentloaded')
    breakpoint()
