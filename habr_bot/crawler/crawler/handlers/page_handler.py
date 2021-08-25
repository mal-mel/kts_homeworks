from dateutil import parser
from bs4 import BeautifulSoup

from typing import List, Optional

from crawler.types import Article
from .url_handler import UrlHandler


class PageHandler:
    def __init__(self, url_handler: UrlHandler):
        self.url_handler = url_handler

    def get_page_urls(self, soup: BeautifulSoup) -> List[str]:
        links = []
        for url in (tag.get("href") for tag in soup.find_all("a")):
            if url:
                url = self.url_handler.get_absolute_url(url)
                if self.url_handler.is_url(url):
                    if self.url_handler.is_url_belong_to_the_domain(url):
                        links.append(self.url_handler.get_normalize_url(url))
        return links

    @staticmethod
    def get_article_data(soup: BeautifulSoup, url: str) -> Optional[Article]:
        article_content = soup.find("article").text
        if article_content:
            return Article(
                content=article_content,
                url=url
            )


# html = """<html lang="ru"><head>
#   <meta charset="UTF-8">
#   <meta name="viewport" content="width=device-width,initial-scale=1.0,viewport-fit=cover">
#   <title>DMA: мифы и реальность / Хабр</title>
#   <style>
#     /* cyrillic-ext */
#     @font-face {
#       font-family: 'Fira Sans';
#       font-style: normal;
#       font-weight: 500;
#       font-display: swap;
#       src: url(https://fonts.gstatic.com/s/firasans/v11/va9B4kDNxMZdWfMOD5VnZKveSxf6TF0.woff2) format('woff2');
#       unicode-range: U+0460-052F, U+1C80-1C88, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F;
#     }
#
#     /* cyrillic */
#     @font-face {
#       font-family: 'Fira Sans';
#       font-style: normal;
#       font-weight: 500;
#       font-display: swap;
#       src: url(https://fonts.gstatic.com/s/firasans/v11/va9B4kDNxMZdWfMOD5VnZKveQhf6TF0.woff2) format('woff2');
#       unicode-range: U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116;
#     }
#
#     /* latin-ext */
#     @font-face {
#       font-family: 'Fira Sans';
#       font-style: normal;
#       font-weight: 500;
#       font-display: swap;
#       src: url(https://fonts.gstatic.com/s/firasans/v11/va9B4kDNxMZdWfMOD5VnZKveSBf6TF0.woff2) format('woff2');
#       unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
#     }
#
#     /* latin */
#     @font-face {
#       font-family: 'Fira Sans';
#       font-style: normal;
#       font-weight: 500;
#       font-display: swap;
#       src: url(https://fonts.gstatic.com/s/firasans/v11/va9B4kDNxMZdWfMOD5VnZKveRhf6.woff2) format('woff2');
#       unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
#     }
#   </style>
#   <link rel="preload" href="https://assets.habr.com/habr-web/css/chunk-vendors.db52f5c6.css" as="style"><link rel="preload" href="https://assets.habr.com/habr-web/js/chunk-vendors.9e4ba848.js" as="script"><link rel="preload" href="https://assets.habr.com/habr-web/css/app.ac61f8eb.css" as="style"><link rel="preload" href="https://assets.habr.com/habr-web/js/app.5d04126c.js" as="script"><link rel="preload" href="https://assets.habr.com/habr-web/css/chunk-f458c7c4.b28016e6.css" as="style"><link rel="preload" href="https://assets.habr.com/habr-web/js/chunk-f458c7c4.529673c8.js" as="script">
#   <link rel="stylesheet" href="https://assets.habr.com/habr-web/css/chunk-vendors.db52f5c6.css"><link rel="stylesheet" href="https://assets.habr.com/habr-web/css/app.ac61f8eb.css"><link rel="stylesheet" href="https://assets.habr.com/habr-web/css/chunk-f458c7c4.b28016e6.css">
#   <script async="" src="https://mc.yandex.ru/metrika/tag.js"></script><script async="" src="//www.google-analytics.com/analytics.js"></script><script>window.i18nFetch = new Promise((res, rej) => {
#           const xhr = new XMLHttpRequest();
#           xhr.open('GET', '/js/i18n/ru-compiled.07ab3411a33038d0c6f862dbea0a2c45.json');
#           xhr.responseType = 'json';
#           xhr.onload = function(e) {
#             if (this.status === 200) {
#               res({ru: xhr.response});
#             } else {
#               rej(e);
#             }
#           };
#           xhr.send();
#         });</script>
#
#   <script data-vue-meta="ssr" src="/js/ads.js" onload="window['zhY4i4nJ9K'] = true" data-vmid="checkad"></script><script data-vue-meta="ssr" type="application/ld+json" data-vmid="ldjson-schema">{"@context":"http:\/\/schema.org","@type":"Article","mainEntityOfPage":{"@type":"WebPage","@id":"https:\/\/habr.com\/ru\/post\/437112\/"},"headline":"DMA: мифы и реальность","datePublished":"2019-02-01T10:23:44+03:00","dateModified":"2019-02-05T12:03:17+03:00","author":{"@type":"Person","name":"Павел Локтев"},"publisher":{"@type":"Organization","name":"Habr","logo":{"@type":"ImageObject","url":"https:\/\/habrastorage.org\/webt\/a_\/lk\/9m\/a_lk9mjkccjox-zccjrpfolmkmq.png"}},"description":"Введение В прошлой статье (&laquo;Часть 2: Использование блоков UDB контроллеров PSoC фирмы Cypress для уменьшения числа прерываний в 3D-принтере&raquo;) я отметил один оч...","url":"https:\/\/habr.com\/ru\/post\/437112\/#post-content-body","about":["h_system_programming","h_controllers","h_hardware","f_develop","f_popsci"],"image":["https:\/\/habrastorage.org\/webt\/m4\/12\/q3\/m412q3b8zbug620xzvv0the7ix0.jpeg","https:\/\/habrastorage.org\/webt\/pv\/cu\/1q\/pvcu1qmbxk9zkbgxk8u51unthpe.png","https:\/\/habrastorage.org\/webt\/h8\/re\/rp\/h8rerphupbsfvawmjiwgwqr_thw.png","https:\/\/habrastorage.org\/webt\/ze\/dz\/ab\/zedzab8iuaoxnu0esg32xwwga3g.png","https:\/\/habrastorage.org\/webt\/ts\/bm\/dn\/tsbmdn-puyugsmixnsipf81pboa.png","https:\/\/habrastorage.org\/webt\/px\/5s\/_w\/px5s_wj1zqwjedrk0h7ty7tbu_4.png","https:\/\/habrastorage.org\/webt\/mb\/-s\/j0\/mb-sj05-chkdijmqn3mue8hmjnk.png","https:\/\/habrastorage.org\/webt\/sa\/hc\/br\/sahcbrgearj6wnw5-4lykaew1qy.png","https:\/\/habrastorage.org\/webt\/b-\/8v\/iq\/b-8viqzbm1isamdkiljvmwevwme.png","https:\/\/habrastorage.org\/webt\/ko\/65\/0j\/ko650jp1nj58h1nm5dzal4bzdhw.png","https:\/\/habrastorage.org\/webt\/ox\/fi\/x_\/oxfix_l8jpspyxgbiumrlagm9ma.png","https:\/\/habrastorage.org\/webt\/fc\/mq\/bj\/fcmqbjhfee7mf7u7_xnkgyspq18.png","https:\/\/habrastorage.org\/webt\/ms\/po\/gq\/mspogqifm21mt0o34s0ltbh1fyu.png","https:\/\/habrastorage.org\/webt\/h5\/5k\/y0\/h55ky0f4pfsfaco90dvfgahwwki.png","https:\/\/habrastorage.org\/webt\/od\/u2\/es\/odu2esatrpusmpi8od4ecfaftk8.png","https:\/\/habrastorage.org\/webt\/0x\/de\/1a\/0xde1acpu3rpgslyseaw2kcysc4.png","https:\/\/habrastorage.org\/webt\/ee\/nl\/2i\/eenl2ix0_9zgzgaaxxeffbjzwjk.png","https:\/\/habrastorage.org\/webt\/9l\/y8\/tp\/9ly8tp_8hj1vohrh6jcnyktfa_a.png","https:\/\/habrastorage.org\/webt\/jw\/fu\/ds\/jwfudsdqtgwfunc3htoczgrw5eg.png","https:\/\/habrastorage.org\/webt\/zz\/cs\/vt\/zzcsvtte2m06u7tzhkfefvfa8wg.png","https:\/\/habrastorage.org\/webt\/oj\/m5\/1d\/ojm51d2qjhkz_rii2zfb4zvzdos.png","https:\/\/habrastorage.org\/webt\/vu\/ki\/pg\/vukipghxkaqqtxdnvz4a2qjp1wu.png","https:\/\/habrastorage.org\/webt\/iw\/1l\/lk\/iw1llkwh0nki1yczmva7gzxgrgk.png","https:\/\/habrastorage.org\/webt\/f6\/vf\/o3\/f6vfo3mgv4mpos2kdrrwmo9dzsm.png","https:\/\/habrastorage.org\/webt\/zo\/u3\/5s\/zou35sqtetrlryln8lxe04tdkwy.png","https:\/\/habrastorage.org\/webt\/bs\/ld\/kc\/bsldkce9ztqrbk15x7e1omcharg.png","https:\/\/habrastorage.org\/webt\/jg\/wr\/_2\/jgwr_2kidbaoxg_-17muiyvo3n4.png","https:\/\/habrastorage.org\/webt\/40\/qo\/c5\/40qoc5ngwnq2tenzpmcc2ornd4w.png","https:\/\/habrastorage.org\/webt\/te\/mq\/_7\/temq_7wguw109a0t-oi_rsi3jju.png","https:\/\/habrastorage.org\/webt\/yq\/bc\/ah\/yqbcahagnawdxrr70dh7zvbetmo.png","https:\/\/habrastorage.org\/webt\/_m\/m9\/2b\/_mm92b5yfgjltz6cizilmdtg4d4.png","https:\/\/habrastorage.org\/webt\/ks\/k-\/c6\/ksk-c6feobygy2krzseq0nlka78.png"]}</script>
#   <script src="//www.googletagservices.com/tag/js/gpt.js" async=""></script>
#   <style>.grecaptcha-badge{visibility: hidden;}</style>
#   <meta name="habr-version" content="2.44.0">
#   <meta name="csrf-token" content="bi9Lzxbx-a9AJiVtv10N8s3JXRDfqtMnriL4">
#   <meta data-vue-meta="ssr" property="fb:app_id" content="444736788986613"><meta data-vue-meta="ssr" property="fb:pages" content="472597926099084"><meta data-vue-meta="ssr" name="twitter:card" content="summary_large_image"><meta data-vue-meta="ssr" name="twitter:site" content="@habr_eng"><meta data-vue-meta="ssr" property="og:title" content="DMA: мифы и реальность" data-vmid="og:title"><meta data-vue-meta="ssr" name="twitter:title" content="DMA: мифы и реальность" data-vmid="twitter:title"><meta data-vue-meta="ssr" name="aiturec:title" content="DMA: мифы и реальность" data-vmid="aiturec:title"><meta data-vue-meta="ssr" itemprop="image" content="https://habr.com/share/publication/437112/2b134ac2366f3394546fa081f36963a0/" data-vmid="image:itemprop"><meta data-vue-meta="ssr" property="og:image" content="https://habr.com/share/publication/437112/2b134ac2366f3394546fa081f36963a0/" data-vmid="og:image"><meta data-vue-meta="ssr" property="aiturec:image" content="https://habr.com/share/publication/437112/2b134ac2366f3394546fa081f36963a0/" data-vmid="aiturec:image"><meta data-vue-meta="ssr" name="twitter:image" content="https://habr.com/share/publication/437112/2b134ac2366f3394546fa081f36963a0/" data-vmid="twitter:image"><meta data-vue-meta="ssr" property="vk:image" content="https://habr.com/share/publication/437112/2b134ac2366f3394546fa081f36963a0/" data-vmid="vk:image"><meta data-vue-meta="ssr" property="aiturec:item_id" content="437112" data-vmid="aiturec:item_id"><meta data-vue-meta="ssr" property="aiturec:datetime" content="2019-02-01T07:23:44.000Z" data-vmid="aiturec:datetime"><meta data-vue-meta="ssr" property="og:type" content="article" data-vmid="og:type"><meta data-vue-meta="ssr" property="og:locale" content="ru_RU" data-vmid="og:locale"><meta data-vue-meta="ssr" property="og:image:width" content="1200" data-vmid="og:image:width"><meta data-vue-meta="ssr" property="og:image:height" content="630" data-vmid="og:image:height">
#   <link data-vue-meta="ssr" href="https://habr.com/ru/rss/post/437112/?fl=ru" type="application/rss+xml" title="" rel="alternate" name="rss"><link data-vue-meta="ssr" href="https://habr.com/ru/post/437112/" rel="canonical" data-vmid="canonical"><link data-vue-meta="ssr" data-vmid="hreflang"><link data-vue-meta="ssr" image_src="image" href="https://habr.com/share/publication/437112/2b134ac2366f3394546fa081f36963a0/" data-vmid="image:href">
#   <meta name="apple-mobile-web-app-status-bar-style" content="#303b44">
#   <meta name="msapplication-TileColor" content="#629FBC">
#   <meta name="apple-mobile-web-app-capable" content="yes">
#   <meta name="mobile-web-app-capable" content="yes">
#   <link rel="shortcut icon" type="image/png" sizes="16x16" href="https://assets.habr.com/habr-web/img/favicons/favicon-16.png">
#   <link rel="shortcut icon" type="image/png" sizes="32x32" href="https://assets.habr.com/habr-web/img/favicons/favicon-32.png">
#   <link rel="apple-touch-icon" type="image/png" sizes="76x76" href="https://assets.habr.com/habr-web/img/favicons/apple-touch-icon-76.png">
#   <link rel="apple-touch-icon" type="image/png" sizes="120x120" href="https://assets.habr.com/habr-web/img/favicons/apple-touch-icon-120.png">
#   <link rel="apple-touch-icon" type="image/png" sizes="152x152" href="https://assets.habr.com/habr-web/img/favicons/apple-touch-icon-152.png">
#   <link rel="apple-touch-icon" type="image/png" sizes="180x180" href="https://assets.habr.com/habr-web/img/favicons/apple-touch-icon-180.png">
#   <link rel="apple-touch-icon" type="image/png" sizes="256x256" href="https://assets.habr.com/habr-web/img/favicons/apple-touch-icon-256.png">
#   <link rel="apple-touch-startup-image" media="screen and (device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)" href="https://assets.habr.com/habr-web/img/splashes/splash_1136x640.png">
#   <link rel="apple-touch-startup-image" media="screen and (device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)" href="https://assets.habr.com/habr-web/img/splashes/splash_2436x1125.png">
#   <link rel="apple-touch-startup-image" media="screen and (device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)" href="https://assets.habr.com/habr-web/img/splashes/splash_1792x828.png">
#   <link rel="apple-touch-startup-image" media="screen and (device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)" href="https://assets.habr.com/habr-web/img/splashes/splash_828x1792.png">
#   <link rel="apple-touch-startup-image" media="screen and (device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)" href="https://assets.habr.com/habr-web/img/splashes/splash_1334x750.png">
#   <link rel="apple-touch-startup-image" media="screen and (device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)" href="https://assets.habr.com/habr-web/img/splashes/splash_1242x2668.png">
#   <link rel="apple-touch-startup-image" media="screen and (device-width: 414px) and (device-height: 736px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)" href="https://assets.habr.com/habr-web/img/splashes/splash_2208x1242.png">
#   <link rel="apple-touch-startup-image" media="screen and (device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)" href="https://assets.habr.com/habr-web/img/splashes/splash_1125x2436.png">
#   <link rel="apple-touch-startup-image" media="screen and (device-width: 414px) and (device-height: 736px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)" href="https://assets.habr.com/habr-web/img/splashes/splash_1242x2208.png">
#   <link rel="apple-touch-startup-image" media="screen and (device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)" href="https://assets.habr.com/habr-web/img/splashes/splash_2732x2048.png">
#   <link rel="apple-touch-startup-image" media="screen and (device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)" href="https://assets.habr.com/habr-web/img/splashes/splash_2688x1242.png">
#   <link rel="apple-touch-startup-image" media="screen and (device-width: 834px) and (device-height: 1112px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)" href="https://assets.habr.com/habr-web/img/splashes/splash_2224x1668.png">
#   <link rel="apple-touch-startup-image" media="screen and (device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)" href="https://assets.habr.com/habr-web/img/splashes/splash_750x1334.png">
#   <link rel="apple-touch-startup-image" media="screen and (device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)" href="https://assets.habr.com/habr-web/img/splashes/splash_2048x2732.png">
#   <link rel="apple-touch-startup-image" media="screen and (device-width: 834px) and (device-height: 1194px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)" href="https://assets.habr.com/habr-web/img/splashes/splash_2388x1668.png">
#   <link rel="apple-touch-startup-image" media="screen and (device-width: 834px) and (device-height: 1112px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)" href="https://assets.habr.com/habr-web/img/splashes/splash_1668x2224.png">
#   <link rel="apple-touch-startup-image" media="screen and (device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)" href="https://assets.habr.com/habr-web/img/splashes/splash_640x1136.png">
#   <link rel="apple-touch-startup-image" media="screen and (device-width: 834px) and (device-height: 1194px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)" href="https://assets.habr.com/habr-web/img/splashes/splash_1668x2388.png">
#   <link rel="apple-touch-startup-image" media="screen and (device-width: 768px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)" href="https://assets.habr.com/habr-web/img/splashes/splash_2048x1536.png">
#   <link rel="apple-touch-startup-image" media="screen and (device-width: 768px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)" href="https://assets.habr.com/habr-web/img/splashes/splash_1536x2048.png">
#   <link rel="mask-icon" color="#77a2b6" href="https://assets.habr.com/habr-web/img/favicons/apple-touch-icon-120.svg">
#   <link crossorigin="use-credentials" href="/manifest.webmanifest" rel="manifest">
# <script charset="utf-8" src="https://assets.habr.com/habr-web/js/chunk-2d0e544c.95c18ea8.js"></script><script charset="utf-8" src="https://assets.habr.com/habr-web/js/chunk-2d21ab85.a318b7bd.js"></script><script charset="utf-8" src="https://assets.habr.com/habr-web/js/hljs.c67ce31f.js"></script><link rel="stylesheet" type="text/css" href="https://assets.habr.com/habr-web/css/gallery.4938c96a.css"><script charset="utf-8" src="https://assets.habr.com/habr-web/js/gallery.42a5862c.js"></script><meta data-vue-meta="ssr" name="description" content="Введение
# В прошлой статье («Часть 2: Использование блоков UDB контроллеров PSoC фирмы Cypress для уменьшения числа прерываний в 3D-принтере») я отметил один очень интересный факт: если автомат в..." data-vmid="description"><meta data-vue-meta="ssr" itemprop="description" content="Введение
# В прошлой статье («Часть 2: Использование блоков UDB контроллеров PSoC фирмы Cypress для уменьшения числа прерываний в 3D-принтере») я отметил один очень интересный факт: если автомат в..." data-vmid="description:itemprop"><meta data-vue-meta="ssr" property="og:description" content="Введение
# В прошлой статье («Часть 2: Использование блоков UDB контроллеров PSoC фирмы Cypress для уменьшения числа прерываний в 3D-принтере») я отметил один очень интересный факт: если автомат в..." data-vmid="og:description"><meta data-vue-meta="ssr" name="twitter:description" content="Введение
# В прошлой статье («Часть 2: Использование блоков UDB контроллеров PSoC фирмы Cypress для уменьшения числа прерываний в 3D-принтере») я отметил один очень интересный факт: если автомат в..." data-vmid="twitter:description"><meta data-vue-meta="ssr" property="aiturec:description" content="Введение
# В прошлой статье («Часть 2: Использование блоков UDB контроллеров PSoC фирмы Cypress для уменьшения числа прерываний в 3D-принтере») я отметил один очень интересный факт: если автомат в..." data-vmid="aiturec:description"><script data-vue-meta="ssr" onload="window['e0044d29c024'] = true" src="https://habr.com/auth/checklogin/" data-vmid="checklogin"></script><script charset="utf-8" src="https://assets.habr.com/habr-web/js/chunk-2d21042a.e8278305.js"></script><script charset="utf-8" src="https://assets.habr.com/habr-web/js/photoswipe.2b48f110.js"></script></head>
# <body cz-shortcut-listen="true">
#
#
# <div id="app" data-async-called="true"><div class="tm-layout__wrapper"><!----><div></div><!----><header class="tm-header"><div class="tm-page-width"><div class="tm-header__container"><!----><span class="tm-header__logo-wrap"><a href="/ru/" class="tm-header__logo tm-header__logo_ru"><svg height="16" width="16" class="tm-svg-img tm-header__icon"><title>Хабр</title><use xlink:href="/img/habr-logo-ru.svg#logo"></use></svg></a><span class="tm-header__beta-sign" style="display:none;">β</span></span><div class="tm-dropdown tm-header__projects"><div class="tm-dropdown__head"><button class="tm-header__dropdown-toggle"><svg height="16" width="16" class="tm-svg-img tm-header__icon tm-header__icon_dropdown"><title>Открыть список</title><use xlink:href="/img/megazord-v24.cee85629.svg#arrow-down"></use></svg></button></div><!----></div><a href="/ru/sandbox/start/" class="tm-header__become-author-btn">
#               Как стать автором
#             </a><!----><!----><!----></div></div></header><div class="tm-layout"><div class="tm-page-progress-bar"></div><div data-menu-sticky="true" class="tm-base-layout__header tm-base-layout__header_is-sticky"><div class="tm-page-width"><div class="tm-base-layout__header-wrapper"><div class="tm-main-menu"><div class="tm-main-menu__section"><nav class="tm-main-menu__section-content"><a href="/ru/feed/" class="tm-main-menu__item">
#         Моя лента
#       </a><a href="/ru/all/" class="tm-main-menu__item">
#         Все потоки
#       </a><a href="/ru/flows/develop/" class="tm-main-menu__item">
#           Разработка
#         </a><a href="/ru/flows/admin/" class="tm-main-menu__item">
#           Администрирование
#         </a><a href="/ru/flows/design/" class="tm-main-menu__item">
#           Дизайн
#         </a><a href="/ru/flows/management/" class="tm-main-menu__item">
#           Менеджмент
#         </a><a href="/ru/flows/marketing/" class="tm-main-menu__item">
#           Маркетинг
#         </a><a href="/ru/flows/popsci/" class="tm-main-menu__item">
#           Научпоп
#         </a></nav></div></div><div class="tm-header-user-menu tm-base-layout__user-menu"><a href="/ru/search/" class="tm-header-user-menu__item tm-header-user-menu__search"><svg height="24" width="24" class="tm-svg-img tm-header-user-menu__icon tm-header-user-menu__icon_search tm-header-user-menu__icon_dark"><title>Поиск</title><use xlink:href="/img/megazord-v24.cee85629.svg#search"></use></svg></a><div class="tm-tracker-dropdown tm-header-user-menu__item"><div class="tm-dropdown"><div class="tm-dropdown__head"><button title="Трекер" class="tm-tracker-dropdown__notifications-button tm-tracker-dropdown__button_dark"><!----><svg height="24" width="24" class="tm-svg-img tm-tracker-dropdown__icon"><title>Трекер</title><use xlink:href="/img/megazord-v24.cee85629.svg#notifications"></use></svg></button></div><!----></div></div><!----><div class="tm-header-user-menu__item tm-header-user-menu__write"><a href="/ru/publication/new/" class=""><svg height="24" width="24" class="tm-svg-img tm-header-user-menu__icon tm-header-user-menu__icon_write tm-header-user-menu__icon_dark"><title>Написать публикацию</title><use xlink:href="/img/megazord-v24.cee85629.svg#write"></use></svg></a><!----></div><div class="tm-header-user-menu__item tm-header-user-menu__user_desktop"><div class="tm-dropdown"><div class="tm-dropdown__head"><div data-test-id="menu-toggle-user" class="tm-entity-image"><svg height="32" width="32" class="tm-svg-img tm-image-placeholder tm-image-placeholder_green"><!----><use xlink:href="/img/megazord-v24.cee85629.svg#placeholder-user"></use></svg></div><!----></div><!----></div><!----></div><!----></div></div></div></div><button class="tm-scroll-top"><span title="Наверх" class="tm-svg-icon__wrapper tm-scroll-top__arrow"><svg height="16" width="16" class="tm-svg-img tm-svg-icon"><title>Наверх</title><use xlink:href="/img/megazord-v24.cee85629.svg#small-arrow"></use></svg></span></button><div class="tm-page-width"></div><main class="tm-layout__container"><div hl="ru" data-async-called="true" class="tm-page"><div class="tm-page-width"><!----><div class="tm-page__wrapper"><div class="tm-page__main tm-page__main_has-sidebar"><div class="pull-down"><div class="pull-down__header" style="height:0px;"><div class="pull-down__content" style="bottom:10px;"><svg height="24" width="24" class="tm-svg-img pull-down__arrow"><title>Обновить</title><use xlink:href="/img/megazord-v24.cee85629.svg#pull-arrow"></use></svg></div></div><!----><div class="tm-page-article__body"><article class="tm-page-article__content tm-page-article__content_inner"><div class="tm-page-article__head-wrapper"><!----><div class="tm-article-snippet tm-page-article__snippet"><div class="tm-article-snippet__meta-container"><div class="tm-article-snippet__meta"><span class="tm-user-info tm-article-snippet__author"><a href="/ru/users/EasyLy/" title="EasyLy" class="tm-user-info__userpic"><div class="tm-entity-image"><img alt="" height="24" loading="lazy" src="//habrastorage.org/r/w32/getpro/habr/avatars/2eb/39b/24c/2eb39b24c4a68d43ad0b0015c5c56aa2.png" width="24" class="tm-entity-image__pic"></div></a><span class="tm-user-info__user"><a href="/ru/users/EasyLy/" class="tm-user-info__username">
#       EasyLy
#     </a></span></span><span class="tm-article-snippet__datetime-published"><time datetime="2019-02-01T07:23:44.000Z" title="2019-02-01, 10:23">1  февраля  2019 в 10:23</time></span></div><!----></div><h1 lang="ru" class="tm-article-snippet__title tm-article-snippet__title_h1"><span>DMA: мифы и реальность</span></h1><div class="tm-article-snippet__hubs"><span class="tm-article-snippet__hubs-item"><a href="/ru/hub/system_programming/" class="tm-article-snippet__hubs-item-link"><span>Системное программирование</span><span title="Профильный хаб" class="tm-article-snippet__profiled-hub">*</span></a></span><span class="tm-article-snippet__hubs-item"><a href="/ru/hub/controllers/" class="tm-article-snippet__hubs-item-link"><span>Программирование микроконтроллеров</span><span title="Профильный хаб" class="tm-article-snippet__profiled-hub">*</span></a></span><span class="tm-article-snippet__hubs-item"><a href="/ru/hub/hardware/" class="tm-article-snippet__hubs-item-link"><span>Компьютерное железо</span><!----></a></span></div><div class="tm-article-snippet__labels"><!----></div><!----><!----></div></div><!----><div data-gallery-root="" lang="ru" class="tm-article-body"><div id="post-content-body" class="article-formatted-body article-formatted-body_version-1"><div xmlns="http://www.w3.org/1999/xhtml"><img src="https://habrastorage.org/r/w1560/webt/m4/12/q3/m412q3b8zbug620xzvv0the7ix0.jpeg" data-src="https://habrastorage.org/webt/m4/12/q3/m412q3b8zbug620xzvv0the7ix0.jpeg"><br>
# <br>
# <h2>Введение</h2><br>
# В прошлой статье (<a href="https://habr.com/ru/post/434742/">«Часть 2: Использование блоков UDB контроллеров PSoC фирмы Cypress для уменьшения числа прерываний в 3D-принтере»</a>) я отметил один очень интересный факт: если автомат в UDB изымал данные из FIFO слишком быстро, он успевал заметить состояние, что новых данных в FIFO нет, после чего переходил в ложное состояние <b>Idle</b>. Разумеется, меня заинтересовал этот факт. Вскрывшиеся результаты я показал группе знакомых. Один человек ответил, что это всё вполне очевидно, и даже назвал причины. Остальные были удивлены не менее, чем я в начале исследований. Так что некоторые специалисты не найдут здесь ничего нового, но неплохо бы донести эту информацию до широкой общественности, чтобы её имели в виду все программисты для микроконтроллеров. <br>
# <a name="habracut"></a><br>
# Не то чтобы это был срыв каких-то покровов. Оказалось, что всё это отлично задокументировано, но беда в том, что не в основных, а в дополнительных документах. И лично я пребывал в счастливом неведении, считая, что DMA — это очень шустрая подсистема, которая позволяет резко повысить эффективность программ, так как там идёт планомерная перекачка данных без отвлечения на те же команды инкремента регистров и организации цикла. Насчёт повышения эффективности – всё верно, но за счёт чуть иных вещей.<br>
# <br>
# Но обо всём по порядку.<br>
# <br>
# <h2>Эксперименты с Cypress PSoC</h2><br>
# Сделаем простейший автомат. У него будет условно два состояния: состояние покоя и состояние, в которое он будет попадать, когда в FIFO имеется хотя бы один байт данных. Войдя в такое состояние, он просто изымет эти данные, после чего снова провалится в состояние покоя. Слово «условно» я привёл не случайно. У нас два FIFO, поэтому я сделаю два таких состояния, по одному на каждое FIFO, чтобы убедиться в том, что они полностью идентичны по поведению. Граф переходов у автомата получился таким:<br>
# <br>
# <img data-src="https://habrastorage.org/webt/pv/cu/1q/pvcu1qmbxk9zkbgxk8u51unthpe.png" src="https://habrastorage.org/r/w1560/webt/pv/cu/1q/pvcu1qmbxk9zkbgxk8u51unthpe.png"> <br>
# <br>
# Флаги для выхода из состояния Idle определяем так:<br>
# <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/h8/re/rp/h8rerphupbsfvawmjiwgwqr_thw.png"> <br>
# <br>
# Не забываем на входы Datapath подать биты номера состояния:<br>
#  <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/ze/dz/ab/zedzab8iuaoxnu0esg32xwwga3g.png"><br>
# <br>
# Наружу мы выводим две группы сигналов: пару сигналов, что в FIFO имеется свободное место (для того чтобы DMA могли начать закачивать в них данные), и пару сигналов, что FIFO пусты (чтобы отображать этот факт на осциллографе).<br>
# <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/ts/bm/dn/tsbmdn-puyugsmixnsipf81pboa.png"> <br>
# <br>
# АЛУ будет просто фиктивно забирать данные из FIFO:<br>
# <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/px/5s/_w/px5s_wj1zqwjedrk0h7ty7tbu_4.png"> <br>
# <br>
# Давайте я покажу детализацию для состояния «0001»:<br>
#  <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/mb/-s/j0/mb-sj05-chkdijmqn3mue8hmjnk.png"><br>
# <br>
# Ещё я поставил разрядность шины, какая была в проекте, на котором я заметил данный эффект, 16 бит:<br>
#  <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/sa/hc/br/sahcbrgearj6wnw5-4lykaew1qy.png"><br>
# <br>
# Переходим к схеме самого проекта. Наружу я выдаю не только сигналы о том, что FIFO опустошилось, но и тактовые импульсы. Это позволит мне обойтись без курсорных измерений на осциллографе. Я могу просто считать такты пальцем.<br>
#  <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/b-/8v/iq/b-8viqzbm1isamdkiljvmwevwme.png"><br>
# <br>
# Как видно, тактовую частоту я сделал 24 мегагерца. У процессорного ядра частота точно такая же. Чем ниже частота, тем меньше помех на китайском осциллографе (официально у него полоса 250 МГц, но то китайские мегагерцы), а замеры все будут вестись относительно тактовых импульсов. Какая бы частота ни была, система всё равно отработает относительно них. Я бы и один мегагерц поставил, но среда разработки запретила мне вводить значение частоты процессорного ядра менее, чем 24 МГц.<br>
# <br>
# Теперь тестовые вещи. Для записи в FIFO0 я сделал такую функцию:<br>
# <br>
# <pre><code class="plaintext hljs">void WriteTo0FromROM()
# {
#     static const uint16 steps[] = {
#       0x0001,0x0001,0x0001,0x0001,0x0001,0x0001,0x0001,0x0001,0x0001,0x0001,
#       0x0001,0x0001,0x0001,0x0001,0x0001,0x0001,0x0001,0x0001,0x0001,0x0001
#     };
#
#     // Инициализировали DMA прямо здесь, так как массив живёт здесь
#     uint8 channel = DMA_0_DmaInitialize (sizeof(steps[0]),1,HI16(steps),HI16(JustReadFromFIFO_1_Datapath_1_F0_PTR));
#
#     CyDmaChRoundRobin (channel,1);
#
#     // Так как мы всё делаем для опытов, выделили дескриптор для задачи тоже здесь
#     uint8 td = CyDmaTdAllocate();
#
#     // Задали параметры дескриптора и длину в байтах. Также сказали, что следующего дескриптора нет.
#     CyDmaTdSetConfiguration(td, sizeof(steps), CY_DMA_DISABLE_TD, TD_INC_SRC_ADR / TD_AUTO_EXEC_NEXT);
#
#     // Теперь задали начальные адреса для дескриптора
#     CyDmaTdSetAddress(td, LO16((uint32)steps), LO16((uint32)JustReadFromFIFO_1_Datapath_1_F0_PTR));
#
#     // Подключили этот дескриптор к каналу
#     CyDmaChSetInitialTd(channel, td);
#
#     // Запустили процесс с возвратом дескриптора к исходному виду
#     CyDmaChEnable(channel, 1);
#
# }
# </code></pre><br>
# Слово ROM в имени функции связано с тем, что отправляемый массив хранится в области ПЗУ, а Cortex M3 имеет Гарвардскую архитектуру. Скорость доступа к шине ОЗУ и шине ПЗУ может различаться, хотелось это проверить, поэтому меня есть аналогичная функция для отправки массива из ОЗУ (у массива <b>steps</b> в её теле отсутствует модификатор <b>static const</b>). Ну, и есть такая же пара функций для посылки в FIFO1, там отличается регистр приёмника: не F0, а F1. В остальном все функции идентичны. Так как особой разницы в результатах я не заметил, рассматривать буду результаты вызова именно приведённой выше функции. Жёлтый луч — тактовые импульсы, голубой — выход <b>FIFO0empty</b>.<br>
#  <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/ko/65/0j/ko650jp1nj58h1nm5dzal4bzdhw.png"><br>
# <br>
# Сначала проверим правдоподобность, почему FIFO заполнено на протяжении двух тактов. Посмотрим этот участок поподробнее:<br>
#  <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/ox/fi/x_/oxfix_l8jpspyxgbiumrlagm9ma.png"><br>
# <br>
# По фронту 1 данные попадают в FIFO, флаг <b>FIFO0enmpty</b> падает. По фронту 2 автомат переходит в состояние <b>GetDataFromFifo1</b>. По фронту 3 в этом состоянии происходит копирование данных из FIFO в регистр АЛУ, FIFO опустошается, флаг <b>FIFO0empty</b> вновь взводится. То есть осциллограмма ведёт себя правдоподобно, можно считать на ней такты на цикл. Получаем 9 штук.<br>
#  <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/fc/mq/bj/fcmqbjhfee7mf7u7_xnkgyspq18.png"><br>
# <br>
# <b>Итого, на осмотренном участке, на копирование одного слова данных из ОЗУ в UDB силами DMA требуется 9 тактов.</b> <br>
# <br>
# А теперь то же самое, но силами процессорного ядра. Сначала — идеальный код, слабо достижимый в реальной жизни:<br>
# <br>
# <pre><code class="plaintext hljs">    volatile uint16_t* ptr = (uint16_t*)JustReadFromFIFO_1_Datapath_1_F0_PTR;
#     ptr[0] = 0;
#     ptr[0] = 0;
# </code></pre><br>
# что превратится в ассемблерный код:<br>
# <br>
# <pre><code class="plaintext hljs">		ldr	r3, [pc, #8]	; (90 &lt;main+0xc&gt;)
# 		movs	r2, #0
# 		strh	r2, [r3, #0]
# 		strh	r2, [r3, #0]
# 		b.n	8e &lt;main+0xa&gt;
# 		.word	0x40006898
# </code></pre><br>
# Никаких разрывов, никаких лишних тактов. Две пары тактов подряд…<br>
#  <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/ms/po/gq/mspogqifm21mt0o34s0ltbh1fyu.png"><br>
# <br>
# Сделаем код чуть более реальным (с накладными расходами на организацию цикла выборку данных и инкремент указателей):<br>
# <br>
# <pre><code class="plaintext hljs">void SoftWriteTo0FromROM()
# {
#     // В этом тесте просто шлём массив из двадцати шагов.
#     // Хитрый алгоритм с упаковкой будем проверять чуть позже
#     static const uint16 steps[] = {
#       0x0001,0x0001,0x0001,0x0001,0x0001,0x0001,0x0001,0x0001,0x0001,0x0001,
#       0x0001,0x0001,0x0001,0x0001,0x0001,0x0001,0x0001,0x0001,0x0001,0x0001
#     };
#    uint16_t* src = steps;
#    volatile uint16_t* dest = (uint16_t*)JustReadFromFIFO_1_Datapath_1_F0_PTR;
#     for (int i=sizeof(steps)/sizeof(steps[0]);i&gt;0;i--)
#     {
#         *dest = *src++;
#     }
#
# }
# </code></pre><br>
# полученный ассемблерный код:<br>
# <br>
# <pre><code class="plaintext hljs">		ldr	r3, [pc, #14]	; (9c &lt;CYDEV_CACHE_SIZE&gt;)
# 		ldr	r0, [pc, #14]	; (a0 &lt;CYDEV_CACHE_SIZE+0x4&gt;)
# 		add.w	r1, r3, #28	; 0x28
# 		ldrh.w	r2, [r3], #2
# 		cmp	r3, r1
# 		strh	r2, [r0, #0]
# 		bne.n	8e &lt;main+0xa&gt;
# </code></pre><br>
# На осциллограмме видим всего 7 тактов на цикл против девяти в случае DMA:<br>
# <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/h5/5k/y0/h55ky0f4pfsfaco90dvfgahwwki.png"> <br>
# <br>
# <h2>Немного о мифе</h2><br>
# Если честно, для меня первоначально это было шоком. Я как-то привык считать, что механизм DMA позволяет быстро и эффективно переносить данные. 1/9 от частоты шины — это не то, чтобы очень быстро. Но оказалось, что никто этого и не скрывает. В документе TRM для PSoC 5LP даже имеется ряд теоретических выкладок, а документ «AN84810 — PSoC 3 and PSoC 5LP Advanced DMA Topics» детально расписывает процесс обращения к DMA. Виной всему латентность. Цикл обмена с шиной занимает некоторое количество тактов. Собственно, именно эти такты и играют решающую роль в возникновении задержки. В общем, никто ничего не скрывает, но это надо знать.<br>
# <br>
# <b>Если знаменитый GPIF, используемый в FX2LP (другой архитектуре, выпускаемой фирмой Cypress), скорость ничем не ограничивает, то здесь ограничение скорости обусловлено латентностями, возникающими при обращениях к шине.</b><br>
# <br>
# <h2>Проверка DMA на STM32</h2><br>
# Я был под таким впечатлением, что решил провести эксперимент на STM32. В качестве подопытного кролика был взят STM32F103, имеющий такое же процессорное ядро Cortex M3. У него нет UDB, из которого можно было бы вывести служебные сигналы, но проверить DMA вполне можно. Что такое GPIO? Это набор регистров в общем адресном пространстве. Вот и прекрасно. Настроим DMA в режим копирования «память-память», указав в качестве источника реальную память (ПЗУ или ОЗУ), а в качестве приёмника — регистр данных GPIO без инкремента адреса. Будем слать туда поочерёдно то 0, то 1, а результат фиксировать осциллографом. Для начала я выбрал порт B, к нему было проще подключиться на макетке. <br>
# <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/od/u2/es/odu2esatrpusmpi8od4ecfaftk8.png"> <br>
# <br>
# Мне очень понравилось считать такты пальцем, а не курсорами. Можно ли сделать так же на данном контроллере? Вполне! Опорную тактовую частоту для осциллографа возьмём с ножки MCO, которая у STM32F10C8T6 связана с портом PA8. Выбор источников для этого дешёвого кристалла не велик (тот же STM32F103, но посолиднее, даёт гораздо больше вариантов), подадим на этот выход сигнал SYSCLK. Так как частота на MCO не может быть выше 50 МГц, уменьшим общую тактовую частоту системы до 48 МГц. Будем умножать частоту кварца 8 МГц не на 9, а на 6 (так как 6 * 8 = 48):<br>
# <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/0x/de/1a/0xde1acpu3rpgslyseaw2kcysc4.png"><br>
# <br>
# <div class="spoiler"><b class="spoiler_title">То же самое текстом:</b><div class="spoiler_text"><pre><code class="plaintext hljs">void SystemClock_Config(void)
# {
#
#   RCC_OscInitTypeDef RCC_OscInitStruct;
#   RCC_ClkInitTypeDef RCC_ClkInitStruct;
#   RCC_PeriphCLKInitTypeDef PeriphClkInit;
#
#     /**Initializes the CPU, AHB and APB busses clocks
#     */
#   RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
#   RCC_OscInitStruct.HSEState = RCC_HSE_ON;
#   RCC_OscInitStruct.HSEPredivValue = RCC_HSE_PREDIV_DIV1;
#   RCC_OscInitStruct.HSIState = RCC_HSI_ON;
#   RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
#   RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
# //  RCC_OscInitStruct.PLL.PLLMUL = RCC_PLL_MUL9;
#   RCC_OscInitStruct.PLL.PLLMUL = RCC_PLL_MUL6;
#   if (HAL_RCC_OscConfig(&amp;RCC_OscInitStruct) != HAL_OK)
#   {
#     _Error_Handler(__FILE__, __LINE__);
#   }
# </code></pre><br>
# </div></div><br>
# MCO запрограммируем средствами библиотеки <b>mcucpp</b> Константина Чижова (дальше я все обращения к аппаратуре буду вести через эту замечательную библиотеку):<br>
# <br>
# <pre><code class="plaintext hljs">	// Настраиваем MCO
# 	Mcucpp::Clock::McoBitField::Set (0x4);
# 	// Подключаем ногу MCO к альтернативному порту
# 	Mcucpp::IO::Pa8::SetConfiguration (Mcucpp::IO::Pa8::Port::AltFunc);
# 	// Программируем скорость выходного каскада
# 	Mcucpp::IO::Pa8::SetSpeed (Mcucpp::IO::Pa8::Port::Fastest);
# </code></pre><br>
# Ну, и теперь задаём вывод массива данных в GPIOB:<br>
# <br>
# <pre><code class="plaintext hljs">typedef Mcucpp::IO::Pb0 dmaTest0;
# typedef Mcucpp::IO::Pb1 dmaTest1;
# ...
# // Запускаем GPIOB и настраиваем биты на выход
# dmaTest0::ConfigPort::Enable();
# dmaTest0::SetDirWrite();
# dmaTest1::ConfigPort::Enable();
# dmaTest1::SetDirWrite();
#
# uint16_t dataForDma[]={0x0000,0x8001,0x0000,0x8001,0x0000,
# 0x8001,0x0000,0x8001,0x0000,0x8001,0x0000,0x8001,0x0000,0x8001};
# typedef Mcucpp::Dma1Channel1 channel;
#
# // Передёргиваем голубой луч
# dmaTest1::Set();
# dmaTest1::Clear();
# dmaTest1::Set();
# // Всё, настроили и запустили DMA
# channel::Init (channel::Mem2Mem|channel::MSize16Bits|channel::PSize16Bits|channel::PeriphIncriment,(void*)&amp;GPIOB-&gt;ODR,dataForDma,sizeof(dataForDma)/2);
#
#   while (1)
#   {
#   }
#
# }
# </code></pre><br>
# Полученная осциллограмма очень похожа на ту, что была на PSoC.<br>
#  <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/ee/nl/2i/eenl2ix0_9zgzgaaxxeffbjzwjk.png"><br>
# <br>
# В середине большой голубой горб. Это идёт процесс инициализации DMA. Голубые импульсы слева получены чисто программным путём на PB1. Растянем их пошире:<br>
# <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/9l/y8/tp/9ly8tp_8hj1vohrh6jcnyktfa_a.png"> <br>
# <br>
# 2 такта на импульс. Работа системы соответствует ожидаемой. Но теперь посмотрим покрупнее область, отмеченную на основной осциллограмме тёмно-синим фоном. В этом месте уже работает блок DMA.<br>
# <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/jw/fu/ds/jwfudsdqtgwfunc3htoczgrw5eg.png"> <br>
# <br>
# 10 тактов на одно изменение линии GPIO. Вообще-то, работа идёт с ОЗУ, а программа зациклена в постоянном цикле. Обращений к ОЗУ от процессорного ядра нет. Шина полностью в распоряжении блока DMA, но 10 тактов. Но на самом деле, результаты не сильно отличаются от увиденных на PSoC, поэтому просто начинаем искать Application Notes, относящийся к DMA на STM32. Их оказалось несколько. Есть AN2548 на F0/F1, есть AN3117 на L0/L1/L3, есть AN4031 на F2/F4/F77. Возможно, есть ещё какие-то… <br>
# <br>
# Но, тем не менее, из них мы видим, что и здесь во всём виновата латентность. Причём у F103 пакетные обращения к шине у DMA невозможны. Они возможны для F4, но не более, чем для четырёх слов. Дальше снова возникнет проблема латентности. <br>
# <br>
# Попробуем выполнить те же действия, но при помощи программной записи. Выше мы видели, что прямая запись в порты идёт моментально. Но там была скорее идеальная запись. Строки:<br>
# <br>
# <pre><code class="plaintext hljs">// Передёргиваем голубой луч
# dmaTest1::Set();
# dmaTest1::Clear();
# dmaTest1::Set();
# </code></pre><br>
# при условии таких настроек оптимизации (обязательно следует указать оптимизацию для времени):<br>
#  <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/zz/cs/vt/zzcsvtte2m06u7tzhkfefvfa8wg.png"><br>
# <br>
# превратились в следующий ассемблерный код:<br>
# <br>
# <pre><code class="plaintext hljs">		STR      r6,[r2,#0x00]
# 		MOV      r0,#0x20000
# 		STR      r0,[r2,#0x00]
# 		STR      r6,[r2,#0x00]
# </code></pre><br>
# В реальном копировании будет обращение к источнику, к приёмнику, изменение переменной цикла, ветвление… В общем, масса накладных расходов (от которых, как считается, как раз и избавляет DMA). Какая будет скорость изменений в порту? Итак, пишем:<br>
# <br>
# <pre><code class="plaintext hljs">uint16_t* src = dataForDma;
# uint16_t* dest = (uint16_t*)&amp;GPIOB-&gt;ODR;
# for (int i=sizeof(dataForDma)/sizeof(dataForDma[0]);i&gt;0;i--)
# {
# 	*dest = *src++;
# }
# </code></pre><br>
# Этот код на C++ превращается в такой ассемблерный код:<br>
# <br>
# <pre><code class="plaintext hljs">	MOVS     r1,#0x0E
#
# 	LDRH     r3,[r0],#0x02
# 	STRH     r3,[r2,#0x00]
# 	LDRH     r3,[r0],#0x02
# 	SUBS     r1,r1,#2
# 	STRH     r3,[r2,#0x00]
# 	CMP      r1,#0x00
# 	BGT      0x080032A8
# </code></pre><br>
# И получаем:<br>
#  <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/oj/m5/1d/ojm51d2qjhkz_rii2zfb4zvzdos.png"><br>
# <br>
# 8 тактов в верхнем полупериоде и 6 — в нижнем (я проверил, результат повторяется для всех полупериодов). Разница возникла потому, что оптимизатор сделал 2 копирования на каждую итерацию. Поэтому 2 такта в одном из полупериодов добавляются на операцию ветвления.<br>
# <br>
# <b>Грубо говоря, при программном копировании тратится 14 тактов на копирование двух слов против 20 тактов на то же самое, но силами DMA. Результат вполне документированный, но весьма неожиданный для тех, кто ещё не читал расширенную литературу.</b><br>
# <br>
# Хорошо. А что будет, если начать писать данные сразу в два потока DMA? Насколько упадёт скорость? Подключим голубой луч к PA0 и перепишем программу следующим образом:<br>
# <br>
# <pre><code class="plaintext hljs">typedef Mcucpp::Dma1Channel1 channel1;
# typedef Mcucpp::Dma1Channel2 channel2;
#
# // Всё, настроили и запустили DMA
# channel1::Init (channel1::Mem2Mem|channel1::MSize16Bits|channel1::PSize16Bits|channel1::PeriphIncriment,(void*)&amp;GPIOB-&gt;ODR,dataForDma,sizeof(dataForDma)/2);
# channel2::Init (channel2::Mem2Mem|channel2::MSize16Bits|channel2::PSize16Bits|channel2::PeriphIncriment,(void*)&amp;GPIOA-&gt;ODR,dataForDma,sizeof(dataForDma)/2);
# </code></pre><br>
# Сначала осмотрим характер импульсов:<br>
#  <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/vu/ki/pg/vukipghxkaqqtxdnvz4a2qjp1wu.png"><br>
# <br>
# Пока идёт настройка второго канала, скорость копирования для первого выше. Затем, когда идёт копирование в паре, скорость падает. Когда первый канал закончил работу, второй начинает работать быстрее. Всё логично, осталось только выяснить, насколько именно падает скорость.<br>
# <br>
# Пока канал один, запись занимает от 10 до 12 тактов (цифры плавают). <br>
# <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/iw/1l/lk/iw1llkwh0nki1yczmva7gzxgrgk.png"><br>
# <br>
# Во время совместной работы получаем 16 тактов на одну запись в каждый порт:<br>
# <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/f6/vf/o3/f6vfo3mgv4mpos2kdrrwmo9dzsm.png"> <br>
# <br>
# То есть, скорость падает не вдвое. А что если начать писать сразу в три потока? Добавляем работу с PC15, так как PC0 не выведен (именно поэтому в массиве выдаётся не 0, 1, 0, 1..., а 0x0000,0x8001, 0x0000, 0x8001...). <br>
# <br>
# <pre><code class="plaintext hljs">typedef Mcucpp::Dma1Channel1 channel1;
# typedef Mcucpp::Dma1Channel2 channel2;
# typedef Mcucpp::Dma1Channel3 channel3;
#
# // Всё, настроили и запустили DMA
# channel1::Init (channel1::Mem2Mem|channel1::MSize16Bits|channel1::PSize16Bits|channel1::PeriphIncriment,(void*)&amp;GPIOB-&gt;ODR,dataForDma,sizeof(dataForDma)/2);
# channel2::Init (channel2::Mem2Mem|channel2::MSize16Bits|channel2::PSize16Bits|channel2::PeriphIncriment,(void*)&amp;GPIOA-&gt;ODR,dataForDma,sizeof(dataForDma)/2);
# channel3::Init (channel3::Mem2Mem|channel3::MSize16Bits|channel3::PSize16Bits|channel3::PeriphIncriment,(void*)&amp;GPIOC-&gt;ODR,dataForDma,sizeof(dataForDma)/2);
# </code></pre><br>
# Здесь результат настолько неожиданный, что я отключу луч, отображающий тактовую частоту. Нам не до измерений. Смотрим на логику работы.<br>
#  <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/zo/u3/5s/zou35sqtetrlryln8lxe04tdkwy.png"><br>
# <br>
# Пока не закончил работу первый канал, третий не начал работы. Три канала одновременно не работают! Что-то на эту тему можно вывести из AppNote на DMA, там говорится, что у F103 всего две Engine в одном блоке (а мы копирует средствами одного блока DMA, второй сейчас простаивает, и объём статьи уже такой, что его я в ход пускать не стану). Перепишем на пробу программу так, чтобы третий канал запустился раньше всех:<br>
# <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/bs/ld/kc/bsldkce9ztqrbk15x7e1omcharg.png"><br>
# <br>
# <div class="spoiler"><b class="spoiler_title">То же самое текстом:</b><div class="spoiler_text"><pre><code class="plaintext hljs">// Всё, настроили и запустили DMA
# channel3::Init (channel3::Mem2Mem|channel3::MSize16Bits|channel3::PSize16Bits|channel3::PeriphIncriment,(void*)&amp;GPIOC-&gt;ODR,dataForDma,sizeof(dataForDma)/2);
# channel1::Init (channel1::Mem2Mem|channel1::MSize16Bits|channel1::PSize16Bits|channel1::PeriphIncriment,(void*)&amp;GPIOB-&gt;ODR,dataForDma,sizeof(dataForDma)/2);
# channel2::Init (channel2::Mem2Mem|channel2::MSize16Bits|channel2::PSize16Bits|channel2::PeriphIncriment,(void*)&amp;GPIOA-&gt;ODR,dataForDma,sizeof(dataForDma)/2);
# </code></pre><br>
# </div></div><br>
# Картинка изменится следующим образом:<br>
# <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/jg/wr/_2/jgwr_2kidbaoxg_-17muiyvo3n4.png"><br>
# <br>
# Третий канал запустился, он даже работал вместе с первым, но как в дело вступил второй, третьего вытеснили до тех пор, пока не закончил работу первый канал.<br>
#  <br>
# <h2>Немного о приоритетах</h2><br>
# Собственно, предыдущая картинка связана с приоритетами DMA, есть и такие. Если у всех работающих каналов указан один и тот же приоритет, в дело вступают их номера. В пределах одного заданного приоритета, у кого номер меньше, тот и приоритетней. Попробуем третьему каналу указать иной глобальный приоритет, возвысив его над всеми остальными (попутно повысим приоритет и второму каналу):<br>
# <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/40/qo/c5/40qoc5ngwnq2tenzpmcc2ornd4w.png"><br>
# <br>
# <div class="spoiler"><b class="spoiler_title">То же самое текстом:</b><div class="spoiler_text"><pre><code class="plaintext hljs">channel3::Init (channel3::PriorityVeryHigh|channel3::Mem2Mem|channel3::MSize16Bits|channel3::PSize16Bits|channel3::PeriphIncriment,(void*)&amp;GPIOC-&gt;ODR,dataForDma,sizeof(dataForDma)/2);
# channel1::Init (channel1::Mem2Mem|channel1::MSize16Bits|channel1::PSize16Bits|channel1::PeriphIncriment,(void*)&amp;GPIOB-&gt;ODR,dataForDma,sizeof(dataForDma)/2);
# channel2::Init (channel1::PriorityVeryHigh|channel2::Mem2Mem|channel2::MSize16Bits|channel2::PSize16Bits|channel2::PeriphIncriment,(void*)&amp;GPIOA-&gt;ODR,dataForDma,sizeof(dataForDma)/2);
# </code></pre><br>
# </div></div><br>
# Теперь ущемлённым станет первый, который раньше был самым крутым. <br>
# <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/te/mq/_7/temq_7wguw109a0t-oi_rsi3jju.png"> <br>
# <br>
# Итого, мы видим, что даже играя в приоритеты, больше двух потоков на одном блоке DMA у STM32F103 запустить не получится. В принципе, третий поток можно запустить на процессорном ядре. Это нам позволит сравнить производительность.<br>
# <br>
# <pre><code class="plaintext hljs">// Всё, настроили и запустили DMA
# 		channel3::Init (channel3::Mem2Mem|channel3::MSize16Bits|channel3::PSize16Bits|channel3::PeriphIncriment,(void*)&amp;GPIOC-&gt;ODR,dataForDma,sizeof(dataForDma)/2);
# 		channel2::Init (channel2::Mem2Mem|channel2::MSize16Bits|channel2::PSize16Bits|channel2::PeriphIncriment,(void*)&amp;GPIOA-&gt;ODR,dataForDma,sizeof(dataForDma)/2);
#
# uint16_t* src = dataForDma;
# uint16_t* dest = (uint16_t*)&amp;GPIOB-&gt;ODR;
# for (int i=sizeof(dataForDma)/sizeof(dataForDma[0]);i&gt;0;i--)
# {
# 	*dest = *src++;
# }
# </code></pre><br>
# Сначала общая картинка, на которой видно, что всё работает в параллель и у процессорного ядра скорость копирования выше всех:<br>
#  <br>
# <img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/yq/bc/ah/yqbcahagnawdxrr70dh7zvbetmo.png"><br>
# <br>
# А теперь я дам возможность всем желающим посчитать такты в то время, когда все потоки копирования активны:<br>
#  <br>
# <a href="https://habrastorage.org/webt/_m/m9/2b/_mm92b5yfgjltz6cizilmdtg4d4.png"><img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/_m/m9/2b/_mm92b5yfgjltz6cizilmdtg4d4.png"></a><br>
# <br>
# <h2>Процессорное ядро приоритетней всех</h2><br>
# Теперь вернёмся к тому факту, что при двухпоточной работе, пока настраивался второй канал, первый выдавал данные за различное число тактов. Этот факт также хорошо документирован в AppNote на DMA. Дело в том, что во время настройки второго канала, периодически шли запросы к ОЗУ, а процессорное ядро имеет при обращении к ОЗУ больший приоритет, чем ядро DMA. Когда процессор запрашивал какие-то данные, у DMA отнимались такты, оно получало данные с задержкой, поэтому производило копирование медленней. Давайте сделаем последний на сегодня эксперимент. Приблизим работу к более реальной. После запуска DMA будем не уходить в пустой цикл (когда обращений к ОЗУ точно нет), а выполнять операцию копирования из ОЗУ в ОЗУ, но эта операция не будет относиться к работе DMA ядер:<br>
# <br>
# <pre><code class="plaintext hljs">channel1::Init (channel1::Mem2Mem|channel1::MSize16Bits|channel1::PSize16Bits|channel1::PeriphIncriment,(void*)&amp;GPIOB-&gt;ODR,dataForDma,sizeof(dataForDma)/2);
# channel2::Init (channel2::Mem2Mem|channel2::MSize16Bits|channel2::PSize16Bits|channel2::PeriphIncriment,(void*)&amp;GPIOA-&gt;ODR,dataForDma,sizeof(dataForDma)/2);
#
# uint32_t src1[0x200];
# uint32_t dest1 [0x200];
#
# while (1)
# {
# 	uint32_t* src = src1;
# 	uint32_t* dest = dest1;
# 	for (int i=sizeof(src1)/sizeof(src1[0]);i&gt;0;i--)
# 	{
# 		*dest++ = *src++;
# 	}
# }
# </code></pre><br>
# <a href="https://habrastorage.org/webt/ks/k-/c6/ksk-c6feobygy2krzseq0nlka78.png"><img src="/img/image-loader.svg" data-src="https://habrastorage.org/webt/ks/k-/c6/ksk-c6feobygy2krzseq0nlka78.png"> </a><br>
# <br>
# Местами цикл растянулся с 16 до 17 тактов. Я боялся, что будет хуже. <br>
# <br>
# <h2>Начинаем делать выводы</h2><br>
# Собственно, переходим к тому, что я вообще хотел сказать.<br>
# <br>
# Начну издалека. Несколько лет назад, начиная изучать STM32, я изучал существовавшие на тот момент версии MiddleWare для USB и недоумевал, зачем разработчики убрали прокачку данных через DMA. Видно было, что исходно такой вариант имелся на виду, затем был убран на задворки, а под конец остались только рудименты от него. Теперь я начинаю подозревать, что понимаю разработчиков.<br>
# <br>
# В <a href="https://habr.com/ru/post/429882/">первой статье про UDB</a> я говорил, что хоть UDB и может работать с параллельными данными, заменить собой GPIF он вряд ли сможет, так как у PSoC шина USB работает на скорости Full Speed против High Speed у FX2LP. Оказывается, есть более серьёзный ограничивающий фактор. DMA просто не успеет доставлять данные с той же скоростью, с какой доставляет их GPIF даже в пределах контроллера, не принимая во внимание шину USB.<br>
#  <br>
# Как видим, нет единой сущности DMA. Во-первых, каждый производитель делает его по-своему. Мало того, даже один производитель для разных семейств может варьировать подход к построению DMA. Если планируется серьёзная нагрузка на этот блок, следует внимательно проанализировать, будут ли удовлетворены потребности.<br>
#  <br>
# Наверное, надо разбавить пессимистический поток одной оптимистической репликой. Я даже выделю ее.<br>
# <br>
# <b>DMA у контроллеров Cortex M позволяют повысить производительность системы по принципу знаменитых Джавелинов: «Запустил и забыл». Да, программное копирование данных идёт чуть быстрее. Но если надо копировать несколько потоков, никакой оптимизатор не сможет сделать так, чтобы процессор всех их гнал без накладных расходов на перезагрузку регистров и закручивание циклов. Кроме того, для медленных портов процессор должен ещё ждать готовности, а DMA делает это на аппаратном уровне.</b><br>
# <br>
# Но даже тут возможны различные нюансы. Если порт всего лишь условно медленный… Ну, скажем, SPI, работающий на максимально возможной частоте, то теоретически возможны ситуации, когда DMA не успеет забрать данные из буфера, и произойдёт переполнение. Или наоборот — поместить данные в буферный регистр. Когда поток данных один, вряд ли это произойдёт, но когда их много, мы видели, какие удивительные накладки могут возникать. Чтобы бороться с этим, следует разрабатывать задачи не обособленно, а в комплексе. А тестерам стараться спровоцировать подобные проблемы (такая у тестеров деструктивная работа).<br>
# <br>
# Ещё раз повторю, что эти данные никто не скрывает. Но почему-то всё это обычно содержится не в основном документе, а в Application Notes. Так что моя задача была именно обратить внимание программистов на то, что DMA — это не панацея, а всего лишь удобный инструмент. <br>
# <br>
# Но, разумеется, не только программистов, а ещё и разработчиков аппаратуры. Скажем, у нас в организации сейчас разрабатывается большой программно-аппаратный комплекс для удалённой отладки встраиваемых систем. Идея состоит в том, что кто-то разрабатывает некое устройство, а «прошивку» хочет заказать на стороне. И почему-то не может предоставить оборудование на сторону. Оно может быть громоздким, оно может быть дорогим, оно может быть уникальным и быть «нужно самим», с ним могут работать разные группы в разных часовых поясах, обеспечивая этакую многосменную работу, оно может постоянно доводиться до ума… В общем, причин придумать можно много, нашей группе просто спустили эту задачу, как данность.<br>
# <br>
# Соответственно, комплекс для отладки должен уметь имитировать собой как можно большее число внешних устройств, от банальной имитации нажатия кнопок до различных протоколов SPI, I2C, CAN, 4-20 mA и прочего, прочего, прочего, чтобы через них эмуляторы могли воссоздавать различное поведение внешних блоков, подключаемых к разрабатываемому оборудованию (лично я в своё время сделал много имитаторов для наземной отладки навесного оборудования для вертолётов, у нас <a href="https://www.astrosoft.ru/about/clients/cassel-aero/">на сайте соответствующие кейсы ищутся по слову Cassel Aero</a>). <br>
# <br>
# И вот, в ТЗ на разработку спущены определённые требования. Столько-то SPI, столько-то I2C, столько-то GPIO. Они должны работать на таких-то предельных частотах. Кажется, что всё понятно. Ставим STM32F4 и ULPI для работы с USB в режиме HS. Технология отработанная. Но вот наступают длинные выходные с ноябрьскими праздниками, на которых я разобрался с UDB. Увидев неладное, я уже по вечерам получил те практические результаты, что приведены в начале этой статьи. И понял, что всё, конечно, здорово, но не для данного проекта. Как я уже отметил, когда возможная пиковая производительность системы приближается к верхней границе, следует проектировать всё не раздельно, а в комплексе. <br>
# <br>
# А здесь комплексного проектирования задач не может быть в принципе. Сегодня идёт работа с одним сторонним оборудованием, завтра — совсем с другим. Шины будут использоваться программистами под каждый случай эмуляции по их усмотрению. Поэтому вариант был отвергнут, в схему было добавлено некоторое количество различных мостов FTDI. В пределах моста одна-две-четыре функции будут разрулены по жёсткой схеме, а между мостами всё будет разруливать USB хост. Увы. В данной задаче я не могу доверять DMA. Можно, конечно, сказать, что программисты потом выкрутятся, но часы на процесс выкрутасов – это трудозатраты, которых следует избегать.<br>
# <br>
# Но это крайность. Чаще всего следует просто держать ограничения подсистемы DMA в уме (например, вводить поправочный коэффициент 10: если требуется поток 1 миллион транзакций в секунду, учитывать, что это не 1 миллион, а 10 миллионов тактов) и рассматривать производительность в комплексе.</div></div><div aria-hidden="true" role="dialog" tabindex="-1" class="pswp"><div class="pswp__bg"></div><div class="pswp__scroll-wrap"><div class="pswp__container"><div class="pswp__item"></div><div class="pswp__item"></div><div class="pswp__item"></div></div><div class="pswp__ui pswp__ui--hidden"><div class="pswp__top-bar"><span class="tm-svg-icon__wrapper pswp__button pswp__button--close"><svg height="16" width="16" class="tm-svg-img tm-svg-icon"><title>Закрыть</title><use xlink:href="/img/megazord-v24.cee85629.svg#close"></use></svg></span><div class="pswp__preloader"><div class="pswp__preloader__icn"><div class="pswp__preloader__cut"><div class="pswp__preloader__donut"></div></div></div></div></div></div></div></div><!----></div><div class="tm-article-body__tags"><div class="tm-article-body__tags-links"><span class="tm-article-body__tags-title">Теги:</span><span class="tm-article-body__tags-item"><a href="/ru/search/?target_type=posts&amp;order=relevance&amp;q=%5Bpsoc%20%D0%BC%D0%B8%D0%BA%D1%80%D0%BE%D0%BA%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D0%BB%D0%B5%D1%80%D1%8B%20DMA%5D" class="tm-article-body__tags-item-link">psoc микроконтроллеры DMA</a></span></div><div class="tm-article-body__tags-links"><span class="tm-article-body__tags-title">Хабы:</span><span class="tm-article-body__tags-item"><a href="/ru/hub/system_programming/" class="tm-article-body__tags-item-link">
#                   Системное программирование
#                 </a></span><span class="tm-article-body__tags-item"><a href="/ru/hub/controllers/" class="tm-article-body__tags-item-link">
#                   Программирование микроконтроллеров
#                 </a></span><span class="tm-article-body__tags-item"><a href="/ru/hub/hardware/" class="tm-article-body__tags-item-link">
#                   Компьютерное железо
#                 </a></span></div></div></article><div class="tm-article__icons-wrapper"><div class="tm-data-icons tm-page-article__counters-panel" style="display: none;"><div class="tm-article-rating tm-data-icons__item"><div class="tm-votes-meter tm-article-rating__votes-switcher"><svg height="16" width="16" class="tm-svg-img tm-votes-meter__icon tm-votes-meter__icon_medium"><title>Всего голосов 46: ↑46 и ↓0</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-rating"></use></svg><span title="Всего голосов 46: ↑46 и ↓0" class="tm-votes-meter__value tm-votes-meter__value_positive tm-votes-meter__value_medium">+46</span></div><div class="v-portal" style="display:none;"></div></div><!----><span class="tm-icon-counter tm-data-icons__item" title="Количество просмотров"><svg height="16" width="16" class="tm-svg-img tm-icon-counter__icon"><title>Просмотры</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-views"></use></svg><span class="tm-icon-counter__value">14K</span></span><button title="Добавить в закладки" type="button" class="bookmarks-button tm-data-icons__item"><span title="Добавить в закладки" class="tm-svg-icon__wrapper bookmarks-button__icon"><svg height="16" width="16" class="tm-svg-img tm-svg-icon"><title>Добавить в закладки</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-favorite"></use></svg></span><span title="Количество пользователей, добавивших публикацию в закладки" class="bookmarks-button__counter">
#     89
#   </span></button><!----><div title="Поделиться" class="tm-sharing tm-data-icons__item"><button type="button" class="tm-sharing__button"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="tm-sharing__icon"><path fill="currentColor" d="M10.33.275l9.047 7.572a.2.2 0 010 .306l-9.048 7.572a.2.2 0 01-.328-.153V11c-8 0-9.94 6-9.94 6S-1 5 10 5V.428a.2.2 0 01.328-.153z"></path></svg></button><!----></div><div class="v-portal" style="display:none;"></div></div><!----></div></div><!----><div class="tm-page-article__additional-blocks"><!----><section class="tm-block tm-block_spacing-bottom"><!----><div class="tm-block__body"><div class="tm-article-author tm-page-article__author"><!----><div class="tm-user-card tm-article-author__user-card tm-user-card_variant-two-column"><div class="tm-user-card__info-container"><div class="tm-user-card__header"><div class="tm-user-card__header-data"><a href="/ru/users/EasyLy/" class="tm-user-card__userpic tm-user-card__userpic_size-40"><div class="tm-entity-image"><img alt="" src="//habrastorage.org/getpro/habr/avatars/2eb/39b/24c/2eb39b24c4a68d43ad0b0015c5c56aa2.png" class="tm-entity-image__pic"></div></a><div class="tm-user-card__meta"><div title=" 147 голосов " class="tm-karma tm-user-card__karma"><div class="tm-karma__votes tm-karma__votes_positive">
#     123
#   </div><div class="tm-karma__text">
#     Карма
#   </div></div><div title="Рейтинг пользователя" class="tm-rating tm-user-card__rating"><div class="tm-rating__header"><div class="tm-rating__counter">5</div></div><div class="tm-rating__text">
#     Рейтинг
#   </div></div></div></div></div><div class="tm-user-card__info"><div class="tm-user-card__title"><span class="tm-user-card__name">Павел Локтев</span><a href="/ru/users/EasyLy/" class="tm-user-card__nickname">
#           @EasyLy
#         </a><!----></div><p class="tm-user-card__short-info">Системное ПО, инструменты для разработчиков</p></div></div><div class="tm-user-card__buttons tm-user-card__buttons_variant-two-column"><!----><div class="tm-user-card__button"><div class="tm-button-follow tm-user-card__button-follow"><span class="tm-button-follow__unfollow">
#     ×
#   </span><button type="button" class="tm-button-follow__button tm-button-follow__button_big">
#     Подписаться
#   </button></div></div><!----><a href="/ru/conversations/easyly/" class="tm-user-card__button tm-user-card__button_write"><svg height="16" width="16" class="tm-svg-img tm-user-card__button-icon"><title>Отправить сообщение</title><use xlink:href="/img/megazord-v24.cee85629.svg#mail"></use></svg></a><!----></div></div><!----></div></div><!----></section><div class="tm-page-article__comments"><div class="tm-article-page-comments"><div class="tm-article-comments-counter-link tm-article-comments-counter-button"><a href="/ru/post/437112/comments/" class="tm-article-comments-counter-link__link tm-article-comments-counter-link__link_button-style"><svg height="16" width="16" class="tm-svg-img tm-article-comments-counter-link__icon tm-article-comments-counter-link__icon_contrasted"><title>Комментарии</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-comments"></use></svg><span class="tm-article-comments-counter-link__value tm-article-comments-counter-link__value_contrasted">
#        Комментарии 8
#     </span></a><a href="/ru/post/437112/comments/" class="tm-article-comments-counter-link__link tm-article-comments-counter-link__link_button-style"><span title="Читать новые комментарии" class="tm-article-comments-counter-link__unread-counter tm-article-comments-counter-link__unread-counter_contrasted">
#       +8
#     </span></a></div></div></div><!----><section class="tm-block tm-block_spacing-around"><header class="tm-block__header"><h2 class="tm-block__title">Похожие публикации</h2><!----></header><div class="tm-block__body"><ul class="tm-article-list-block__list"><li class="tm-article-list-block__item"><article class="tm-article-snippet-block-block tm-article-snippet-block-block_preview"><div class="tm-article-snippet-block__user-meta"><div class="tm-article-snippet-block__date"><time datetime="2021-08-16T11:00:02.000Z" title="2021-08-16, 14:00">16  августа   в 14:00</time></div></div><h2 class="tm-article-title tm-article-title_block"><a href="/ru/post/572630/" class="tm-article-title__link"><span>Пишем терминальный сервер для микроконтроллера на С</span></a></h2><div class="tm-data-icons"><!----><div class="tm-votes-meter tm-data-icons__item"><svg height="16" width="16" class="tm-svg-img tm-votes-meter__icon tm-votes-meter__icon_small"><title>Всего голосов 35: ↑34 и ↓1</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-rating"></use></svg><span title="Всего голосов 35: ↑34 и ↓1" class="tm-votes-meter__value tm-votes-meter__value_positive tm-votes-meter__value_small">+33</span></div><span title="Количество просмотров" class="tm-icon-counter tm-data-icons__item"><svg height="16" width="16" class="tm-svg-img tm-icon-counter__icon"><title>Просмотры</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-views"></use></svg><span class="tm-icon-counter__value">7.7K</span></span><button title="Добавить в закладки" type="button" class="bookmarks-button tm-data-icons__item"><span title="Добавить в закладки" class="tm-svg-icon__wrapper bookmarks-button__icon"><svg height="16" width="16" class="tm-svg-img tm-svg-icon"><title>Добавить в закладки</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-favorite"></use></svg></span><span title="Количество пользователей, добавивших публикацию в закладки" class="bookmarks-button__counter">
#     106
#   </span></button><div title="Читать комментарии" class="tm-article-comments-counter-link tm-data-icons__item"><a href="/ru/post/572630/comments/" class="tm-article-comments-counter-link__link"><svg height="16" width="16" class="tm-svg-img tm-article-comments-counter-link__icon"><title>Комментарии</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-comments"></use></svg><span class="tm-article-comments-counter-link__value">
#       16
#     </span></a><!----></div><!----><div class="v-portal" style="display:none;"></div></div></article></li><li class="tm-article-list-block__item"><article class="tm-article-snippet-block-block tm-article-snippet-block-block_preview"><div class="tm-article-snippet-block__user-meta"><div class="tm-article-snippet-block__date"><time datetime="2021-08-04T07:49:55.000Z" title="2021-08-04, 10:49">4  августа   в 10:49</time></div></div><h2 class="tm-article-title tm-article-title_block"><a href="/ru/post/571172/" class="tm-article-title__link"><span>Реализация счетчика наработки на микроконтроллере 1986BE92QI</span></a></h2><div class="tm-data-icons"><!----><div class="tm-votes-meter tm-data-icons__item"><svg height="16" width="16" class="tm-svg-img tm-votes-meter__icon tm-votes-meter__icon_small"><title>Всего голосов 27: ↑25 и ↓2</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-rating"></use></svg><span title="Всего голосов 27: ↑25 и ↓2" class="tm-votes-meter__value tm-votes-meter__value_positive tm-votes-meter__value_small">+23</span></div><span title="Количество просмотров" class="tm-icon-counter tm-data-icons__item"><svg height="16" width="16" class="tm-svg-img tm-icon-counter__icon"><title>Просмотры</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-views"></use></svg><span class="tm-icon-counter__value">4.1K</span></span><button title="Добавить в закладки" type="button" class="bookmarks-button tm-data-icons__item"><span title="Добавить в закладки" class="tm-svg-icon__wrapper bookmarks-button__icon"><svg height="16" width="16" class="tm-svg-img tm-svg-icon"><title>Добавить в закладки</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-favorite"></use></svg></span><span title="Количество пользователей, добавивших публикацию в закладки" class="bookmarks-button__counter">
#     30
#   </span></button><div title="Читать комментарии" class="tm-article-comments-counter-link tm-data-icons__item"><a href="/ru/post/571172/comments/" class="tm-article-comments-counter-link__link"><svg height="16" width="16" class="tm-svg-img tm-article-comments-counter-link__icon"><title>Комментарии</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-comments"></use></svg><span class="tm-article-comments-counter-link__value">
#       31
#     </span></a><!----></div><!----><div class="v-portal" style="display:none;"></div></div></article></li><li class="tm-article-list-block__item"><article class="tm-article-snippet-block-block tm-article-snippet-block-block_preview"><div class="tm-article-snippet-block__user-meta"><div class="tm-article-snippet-block__date"><time datetime="2019-03-14T10:21:52.000Z" title="2019-03-14, 13:21">14  марта  2019 в 13:21</time></div></div><h2 class="tm-article-title tm-article-title_block"><a href="/ru/post/443554/" class="tm-article-title__link"><span>Особенности формирования тактовых частот в PSoC 5LP</span></a></h2><div class="tm-data-icons"><!----><div class="tm-votes-meter tm-data-icons__item"><svg height="16" width="16" class="tm-svg-img tm-votes-meter__icon tm-votes-meter__icon_small"><title>Всего голосов 16: ↑15 и ↓1</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-rating"></use></svg><span title="Всего голосов 16: ↑15 и ↓1" class="tm-votes-meter__value tm-votes-meter__value_positive tm-votes-meter__value_small">+14</span></div><span title="Количество просмотров" class="tm-icon-counter tm-data-icons__item"><svg height="16" width="16" class="tm-svg-img tm-icon-counter__icon"><title>Просмотры</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-views"></use></svg><span class="tm-icon-counter__value">1.6K</span></span><button title="Добавить в закладки" type="button" class="bookmarks-button tm-data-icons__item"><span title="Добавить в закладки" class="tm-svg-icon__wrapper bookmarks-button__icon"><svg height="16" width="16" class="tm-svg-img tm-svg-icon"><title>Добавить в закладки</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-favorite"></use></svg></span><span title="Количество пользователей, добавивших публикацию в закладки" class="bookmarks-button__counter">
#     15
#   </span></button><div title="Читать комментарии" class="tm-article-comments-counter-link tm-data-icons__item"><a href="/ru/post/443554/comments/" class="tm-article-comments-counter-link__link"><svg height="16" width="16" class="tm-svg-img tm-article-comments-counter-link__icon"><title>Комментарии</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-comments"></use></svg><span class="tm-article-comments-counter-link__value">
#       0
#     </span></a><!----></div><!----><div class="v-portal" style="display:none;"></div></div></article></li><!----></ul></div><!----></section><section class="tm-block tm-block_spacing-around"><header class="tm-block__header"><h2 class="tm-block__title">Минуточку внимания</h2><div class="tm-block__header-aside"><a href="https://tmtm.ru/megapost/" target="_blank" class="tm-block-extralink">
#       Разместить
#     </a></div></header><div class="tm-block__body"><div pagination="" slides-per-view="1" class="tm-promo-block__content-wrapper"><div class="tm-promo-block__item-wrapper"><a href="https://effect.habr.com/s/P6vvb1abT_JUqde4MJbQkQ.xtbSc9T203FOqG-LBaKSoLkKoySIwNCiRbT0VBvvg6NzTeOYU8OTPBhq5YKi2xxl6F_qNQtP9iQiRT6xBx0tbw" rel="nofollow " class="tm-promo-block__item tm-article-title__link"><header class="tm-promo-block__head"><div class="tm-promo-block__image-wrapper"><img alt="" src="https://effect.habr.com/s/Ta2sGMh1xt2P-M2nd9IBEA.eIc9duAnezAROal8GrfbCfsnM6gb4J2Jguh0jmAV2PPN3rPS-qW8j3mNSUIU65oE3KnheGdIiSxvGleaJ72na49c6BJJSnOYCI9IZ0E23C1awePhpw0tfJQNR_BWDZQnJjWFBFRZh8BqvDCu9OUGVi2adf-LlratGvAh1if38l4" class="tm-promo-block__image"></div><div class="tm-promo-block__label">
#               Опрос
#               <!----></div></header><div class="tm-promo-block__info"><h3 class="tm-promo-block__title">Печеньки с привкусом серы: рейтинг IT-работодателей</h3></div></a></div><div class="tm-promo-block__item-wrapper"><a href="https://effect.habr.com/s/SxQ78RBZWJ-IwYYvm7rEeA.rGcOEDbrqsYbZ9a-FXpbCnpkhtsc_H3A9pw4p6-tWq4jv0VqoFjkR__8W0l6LbNRRpXQL3MCYB0tswA4YN-jS3RceYolQrYwJ1eDGRZ_PBU" rel="nofollow sponsored" class="tm-promo-block__item tm-article-title__link"><header class="tm-promo-block__head"><div class="tm-promo-block__image-wrapper"><img alt="" src="https://effect.habr.com/s/9obu_2us_g0Cl4m6hxJ7hg.mU-0HGgBfEfp62OyDsWnRe7D_NakdS83mGZrOtp_Zs8kYdSM7yrf1spmpKYFL2MHgtokdC91H7uwiH1evGdrEe4PGbHy06ss16qiBZN1dSuA7049zBKvQXvrziObu9vil2WyFMlBM6GZlzZ72WGAYgFkofXWmj5MDCP9N2NI0jw" class="tm-promo-block__image"></div><div class="tm-promo-block__label">
#               Промо
#               <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 11 11" class="tm-block-promo__external"><path fill="currentColor" d="M7.5 0a.5.5 0 000 1h1.793L5.146 5.146a.5.5 0 10.708.708L10 1.707V3.5a.5.5 0 001 0v-3a.5.5 0 00-.5-.5h-3zm-7 1a.5.5 0 00-.5.5v9a.5.5 0 00.5.5h9a.5.5 0 00.5-.5V6a.5.5 0 00-1 0v4H1V2h4a.5.5 0 000-1H.5z"></path></svg></div></header><div class="tm-promo-block__info"><h3 class="tm-promo-block__title">Туристы уже обгорели, а промокод – термостойкий</h3></div></a></div><div class="tm-promo-block__item-wrapper"><a href="https://effect.habr.com/s/gzLSxsvUemUlOiDsW_OkKw.wBFoBsxklEveRLyl8ssP9LK0pkA2_To85l2ZkkKjGBYgboYMOsjAaC4uYKZBU493Y54MmgQLqdwR2raBJ_QA5A" rel="nofollow " class="tm-promo-block__item tm-article-title__link"><header class="tm-promo-block__head"><div class="tm-promo-block__image-wrapper"><img alt="" src="https://effect.habr.com/s/fe4qV80k6cEc5JuMwawm6w.dHnkr0xRGn-uJpjKJ7sk5dAatSMejY4S679kB23_mrCbyG7EHI3ZEm3QJ_zpTIebQHOfxpixI7VjwI56pBelNxKVBVQLDKN7fpSlF4L6SB2E73VbmtJqltiHN6WUc5v-yNz4ikQZhdGOcIX-CuIRJdj4eMVSC2sSU4rHEg9jj3I" class="tm-promo-block__image"></div><div class="tm-promo-block__label">
#               Мегатест
#               <!----></div></header><div class="tm-promo-block__info"><h3 class="tm-promo-block__title">Любовь, код и роботы в тесте на знание Python</h3></div></a></div></div></div><!----></section><div class="tm-project-block tm-project-block_variant-vacancies"><div class="tm-project-block__header"><div class="tm-project-block__title"><a href="https://career.habr.com/vacancies?utm_campaign=vacancies_postlist&amp;utm_content=vacancies&amp;utm_medium=habr_block&amp;utm_source=habr_mob" rel="noopener" target="_blank" class="tm-project-block__title-link"> Вакансии </a></div></div><div class="tm-project-block__content"><ul class="tm-project-block-items"><li class="tm-project-block-items__item"><a href="https://career.habr.com/vacancies/1000082444?utm_campaign=vacancies_postlist&amp;utm_content=vacancy&amp;utm_medium=habr_block&amp;utm_source=habr_mob" rel="noopener" target="_blank" class="tm-project-block-items__detail tm-project-block-items__title"><!---->Hardware Engineer / Инженер-электронщик
#     </a><div class="tm-project-block-items__properties"><span class="tm-project-block-items__property-item">от 140&nbsp;000 ₽</span><span class="tm-project-block-items__property-item">Bio-Dive</span><span class="tm-project-block-items__property-item">Сочи</span></div></li><li class="tm-project-block-items__item"><a href="https://career.habr.com/vacancies/1000081526?utm_campaign=vacancies_postlist&amp;utm_content=vacancy&amp;utm_medium=habr_block&amp;utm_source=habr_mob" rel="noopener" target="_blank" class="tm-project-block-items__detail tm-project-block-items__title"><!---->Разработчик Fullstack Node.js
#     </a><div class="tm-project-block-items__properties"><span class="tm-project-block-items__property-item">от 130&nbsp;000 до 160&nbsp;000 ₽</span><span class="tm-project-block-items__property-item">Serenity</span><span class="tm-project-block-items__property-item">Можно удаленно</span></div></li><li class="tm-project-block-items__item"><a href="https://career.habr.com/vacancies/1000082112?utm_campaign=vacancies_postlist&amp;utm_content=vacancy&amp;utm_medium=habr_block&amp;utm_source=habr_mob" rel="noopener" target="_blank" class="tm-project-block-items__detail tm-project-block-items__title"><!---->Программист
#     </a><div class="tm-project-block-items__properties"><span class="tm-project-block-items__property-item">от 100&nbsp;000 ₽</span><span class="tm-project-block-items__property-item">НПО САУТ</span><span class="tm-project-block-items__property-item">Екатеринбург</span></div></li><li class="tm-project-block-items__item"><a href="https://career.habr.com/vacancies/1000083422?utm_campaign=vacancies_postlist&amp;utm_content=vacancy&amp;utm_medium=habr_block&amp;utm_source=habr_mob" rel="noopener" target="_blank" class="tm-project-block-items__detail tm-project-block-items__title"><!---->Системный администратор
#     </a><div class="tm-project-block-items__properties"><span class="tm-project-block-items__property-item">от 70&nbsp;000 ₽</span><span class="tm-project-block-items__property-item">Фертоинг</span><span class="tm-project-block-items__property-item">Санкт-Петербург</span></div></li><li class="tm-project-block-items__item"><a href="https://career.habr.com/vacancies/1000062787?utm_campaign=vacancies_postlist&amp;utm_content=vacancy&amp;utm_medium=habr_block&amp;utm_source=habr_mob" rel="noopener" target="_blank" class="tm-project-block-items__detail tm-project-block-items__title"><!---->Middle Разработчик IoT устройств / Программист микроконтроллеров
#     </a><div class="tm-project-block-items__properties"><span class="tm-project-block-items__property-item">от 140&nbsp;000 до 200&nbsp;000 ₽</span><span class="tm-project-block-items__property-item">Fenix Link</span><span class="tm-project-block-items__property-item">Москва</span></div></li></ul></div><div class="tm-project-block__footer"><a href="https://career.habr.com/vacancies?utm_campaign=vacancies_postlist&amp;utm_content=vacancies_all&amp;utm_medium=habr_block&amp;utm_source=habr_mob" rel="noopener" target="_blank" class="tm-project-block__link">Больше вакансий на Хабр Карьере</a></div></div><section class="tm-block tm-block_spacing-around"><header class="tm-block__header"><h2 class="tm-block__title">Лучшие публикации за сутки</h2><!----></header><div class="tm-block__body"><ul class="tm-article-list-block__list"><li class="tm-article-list-block__item"><article class="tm-article-snippet-block-block tm-article-snippet-block-block_preview"><div class="tm-article-snippet-block__user-meta"><div class="tm-article-snippet-block__date"><time datetime="2021-08-24T06:34:53.000Z" title="2021-08-24, 09:34">сегодня в 09:34</time></div></div><h2 class="tm-article-title tm-article-title_block"><a href="/ru/company/flant/blog/573878/" class="tm-article-title__link"><span>Катастрофы, с которыми я столкнулся в мире микросервисов</span></a></h2><div class="tm-data-icons"><!----><div class="tm-votes-meter tm-data-icons__item"><svg height="16" width="16" class="tm-svg-img tm-votes-meter__icon tm-votes-meter__icon_small"><title>Всего голосов 46: ↑46 и ↓0</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-rating"></use></svg><span title="Всего голосов 46: ↑46 и ↓0" class="tm-votes-meter__value tm-votes-meter__value_positive tm-votes-meter__value_small">+46</span></div><span title="Количество просмотров" class="tm-icon-counter tm-data-icons__item"><svg height="16" width="16" class="tm-svg-img tm-icon-counter__icon"><title>Просмотры</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-views"></use></svg><span class="tm-icon-counter__value">7.6K</span></span><button title="Добавить в закладки" type="button" class="bookmarks-button tm-data-icons__item"><span title="Добавить в закладки" class="tm-svg-icon__wrapper bookmarks-button__icon"><svg height="16" width="16" class="tm-svg-img tm-svg-icon"><title>Добавить в закладки</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-favorite"></use></svg></span><span title="Количество пользователей, добавивших публикацию в закладки" class="bookmarks-button__counter">
#     54
#   </span></button><div title="Читать комментарии" class="tm-article-comments-counter-link tm-data-icons__item"><a href="/ru/company/flant/blog/573878/comments/" class="tm-article-comments-counter-link__link"><svg height="16" width="16" class="tm-svg-img tm-article-comments-counter-link__icon"><title>Комментарии</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-comments"></use></svg><span class="tm-article-comments-counter-link__value">
#       7
#     </span></a><a href="/ru/company/flant/blog/573878/comments/" class="tm-article-comments-counter-link__link"><span title="Читать новые комментарии" class="tm-article-comments-counter-link__unread-counter">
#       +7
#     </span></a></div><!----><div class="v-portal" style="display:none;"></div></div></article></li><li class="tm-article-list-block__item"><article class="tm-article-snippet-block-block tm-article-snippet-block-block_preview"><div class="tm-article-snippet-block__user-meta"><div class="tm-article-snippet-block__date"><time datetime="2021-08-24T03:23:02.000Z" title="2021-08-24, 06:23">сегодня в 06:23</time></div></div><h2 class="tm-article-title tm-article-title_block"><a href="/ru/post/574308/" class="tm-article-title__link"><span>20 лет Windows XP</span></a></h2><div class="tm-data-icons"><!----><div class="tm-votes-meter tm-data-icons__item"><svg height="16" width="16" class="tm-svg-img tm-votes-meter__icon tm-votes-meter__icon_small"><title>Всего голосов 41: ↑40 и ↓1</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-rating"></use></svg><span title="Всего голосов 41: ↑40 и ↓1" class="tm-votes-meter__value tm-votes-meter__value_positive tm-votes-meter__value_small">+39</span></div><span title="Количество просмотров" class="tm-icon-counter tm-data-icons__item"><svg height="16" width="16" class="tm-svg-img tm-icon-counter__icon"><title>Просмотры</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-views"></use></svg><span class="tm-icon-counter__value">13K</span></span><button title="Добавить в закладки" type="button" class="bookmarks-button tm-data-icons__item"><span title="Добавить в закладки" class="tm-svg-icon__wrapper bookmarks-button__icon"><svg height="16" width="16" class="tm-svg-img tm-svg-icon"><title>Добавить в закладки</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-favorite"></use></svg></span><span title="Количество пользователей, добавивших публикацию в закладки" class="bookmarks-button__counter">
#     26
#   </span></button><div title="Читать комментарии" class="tm-article-comments-counter-link tm-data-icons__item"><a href="/ru/post/574308/comments/" class="tm-article-comments-counter-link__link"><svg height="16" width="16" class="tm-svg-img tm-article-comments-counter-link__icon"><title>Комментарии</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-comments"></use></svg><span class="tm-article-comments-counter-link__value">
#       60
#     </span></a><a href="/ru/post/574308/comments/" class="tm-article-comments-counter-link__link"><span title="Читать новые комментарии" class="tm-article-comments-counter-link__unread-counter">
#       +60
#     </span></a></div><!----><div class="v-portal" style="display:none;"></div></div></article></li><li class="tm-article-list-block__item"><article class="tm-article-snippet-block-block tm-article-snippet-block-block_preview"><div class="tm-article-snippet-block__user-meta"><div class="tm-article-snippet-block__date"><time datetime="2021-08-24T09:03:49.000Z" title="2021-08-24, 12:03">сегодня в 12:03</time></div></div><h2 class="tm-article-title tm-article-title_block"><a href="/ru/post/574360/" class="tm-article-title__link"><span>Протокол, который невозможен: как на самом деле в ДЭГ обеспечивают тайну голосования</span></a></h2><div class="tm-data-icons"><!----><div class="tm-votes-meter tm-data-icons__item"><svg height="16" width="16" class="tm-svg-img tm-votes-meter__icon tm-votes-meter__icon_small"><title>Всего голосов 39: ↑37 и ↓2</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-rating"></use></svg><span title="Всего голосов 39: ↑37 и ↓2" class="tm-votes-meter__value tm-votes-meter__value_positive tm-votes-meter__value_small">+35</span></div><span title="Количество просмотров" class="tm-icon-counter tm-data-icons__item"><svg height="16" width="16" class="tm-svg-img tm-icon-counter__icon"><title>Просмотры</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-views"></use></svg><span class="tm-icon-counter__value">4K</span></span><button title="Добавить в закладки" type="button" class="bookmarks-button tm-data-icons__item"><span title="Добавить в закладки" class="tm-svg-icon__wrapper bookmarks-button__icon"><svg height="16" width="16" class="tm-svg-img tm-svg-icon"><title>Добавить в закладки</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-favorite"></use></svg></span><span title="Количество пользователей, добавивших публикацию в закладки" class="bookmarks-button__counter">
#     26
#   </span></button><div title="Читать комментарии" class="tm-article-comments-counter-link tm-data-icons__item"><a href="/ru/post/574360/comments/" class="tm-article-comments-counter-link__link"><svg height="16" width="16" class="tm-svg-img tm-article-comments-counter-link__icon"><title>Комментарии</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-comments"></use></svg><span class="tm-article-comments-counter-link__value">
#       27
#     </span></a><a href="/ru/post/574360/comments/" class="tm-article-comments-counter-link__link"><span title="Читать новые комментарии" class="tm-article-comments-counter-link__unread-counter">
#       +27
#     </span></a></div><!----><div class="v-portal" style="display:none;"></div></div></article></li><li class="tm-article-list-block__item"><article class="tm-article-snippet-block-block tm-article-snippet-block-block_preview"><div class="tm-article-snippet-block__user-meta"><div class="tm-article-snippet-block__date"><time datetime="2021-08-24T11:01:01.000Z" title="2021-08-24, 14:01">сегодня в 14:01</time></div></div><h2 class="tm-article-title tm-article-title_block"><a href="/ru/company/ruvds/blog/574266/" class="tm-article-title__link"><span>Управление репутацией хостинга: почему стало так важно рассказывать про процессы открыто</span></a></h2><div class="tm-data-icons"><!----><div class="tm-votes-meter tm-data-icons__item"><svg height="16" width="16" class="tm-svg-img tm-votes-meter__icon tm-votes-meter__icon_small"><title>Всего голосов 31: ↑29 и ↓2</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-rating"></use></svg><span title="Всего голосов 31: ↑29 и ↓2" class="tm-votes-meter__value tm-votes-meter__value_positive tm-votes-meter__value_small">+27</span></div><span title="Количество просмотров" class="tm-icon-counter tm-data-icons__item"><svg height="16" width="16" class="tm-svg-img tm-icon-counter__icon"><title>Просмотры</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-views"></use></svg><span class="tm-icon-counter__value">1.1K</span></span><button title="Добавить в закладки" type="button" class="bookmarks-button tm-data-icons__item"><span title="Добавить в закладки" class="tm-svg-icon__wrapper bookmarks-button__icon"><svg height="16" width="16" class="tm-svg-img tm-svg-icon"><title>Добавить в закладки</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-favorite"></use></svg></span><span title="Количество пользователей, добавивших публикацию в закладки" class="bookmarks-button__counter">
#     18
#   </span></button><div title="Читать комментарии" class="tm-article-comments-counter-link tm-data-icons__item"><a href="/ru/company/ruvds/blog/574266/comments/" class="tm-article-comments-counter-link__link"><svg height="16" width="16" class="tm-svg-img tm-article-comments-counter-link__icon"><title>Комментарии</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-comments"></use></svg><span class="tm-article-comments-counter-link__value">
#       4
#     </span></a><a href="/ru/company/ruvds/blog/574266/comments/#first_unread" class="tm-article-comments-counter-link__link"><span title="Читать новые комментарии" class="tm-article-comments-counter-link__unread-counter">
#       +3
#     </span></a></div><!----><div class="v-portal" style="display:none;"></div></div></article></li><li class="tm-article-list-block__item"><article class="tm-article-snippet-block-block tm-article-snippet-block-block_preview"><div class="tm-article-snippet-block__user-meta"><div class="tm-article-snippet-block__date"><time datetime="2021-08-24T11:30:54.000Z" title="2021-08-24, 14:30">сегодня в 14:30</time></div></div><h2 class="tm-article-title tm-article-title_block"><a href="/ru/company/funcorp/blog/574200/" class="tm-article-title__link"><span>Защита данных пользователя: как добавить поддержку правил CCPA и GDPR в мобильное приложение</span></a></h2><div class="tm-data-icons"><!----><div class="tm-votes-meter tm-data-icons__item"><svg height="16" width="16" class="tm-svg-img tm-votes-meter__icon tm-votes-meter__icon_small"><title>Всего голосов 27: ↑26 и ↓1</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-rating"></use></svg><span title="Всего голосов 27: ↑26 и ↓1" class="tm-votes-meter__value tm-votes-meter__value_positive tm-votes-meter__value_small">+25</span></div><span title="Количество просмотров" class="tm-icon-counter tm-data-icons__item"><svg height="16" width="16" class="tm-svg-img tm-icon-counter__icon"><title>Просмотры</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-views"></use></svg><span class="tm-icon-counter__value">600</span></span><button title="Добавить в закладки" type="button" class="bookmarks-button tm-data-icons__item"><span title="Добавить в закладки" class="tm-svg-icon__wrapper bookmarks-button__icon"><svg height="16" width="16" class="tm-svg-img tm-svg-icon"><title>Добавить в закладки</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-favorite"></use></svg></span><span title="Количество пользователей, добавивших публикацию в закладки" class="bookmarks-button__counter">
#     33
#   </span></button><div title="Читать комментарии" class="tm-article-comments-counter-link tm-data-icons__item"><a href="/ru/company/funcorp/blog/574200/comments/" class="tm-article-comments-counter-link__link"><svg height="16" width="16" class="tm-svg-img tm-article-comments-counter-link__icon"><title>Комментарии</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-comments"></use></svg><span class="tm-article-comments-counter-link__value">
#       1
#     </span></a><a href="/ru/company/funcorp/blog/574200/comments/" class="tm-article-comments-counter-link__link"><span title="Читать новые комментарии" class="tm-article-comments-counter-link__unread-counter">
#       +1
#     </span></a></div><!----><div class="v-portal" style="display:none;"></div></div></article></li><!----></ul></div><!----></section><!----><!----></div></div></div><div class="tm-page__sidebar"><div hl="ru" id="437112" class="tm-layout-sidebar"><div class="tm-layout-sidebar__ads tm-layout-sidebar__ads_stick-bottom"><!----></div><div class="tm-sexy-sidebar tm-sexy-sidebar_stick-bottom" style="margin-top: 0px;"><section class="tm-block tm-block_spacing-bottom"><header class="tm-block__header"><h2 class="tm-block__title">Читают сейчас</h2><!----></header><div class="tm-block__body"><ul class="tm-article-list-block__list"><li class="tm-article-list-block__item"><article class="tm-article-snippet-block-sidebar tm-article-snippet-block-sidebar_preview"><!----><h2 class="tm-article-title tm-article-title_sidebar"><a href="/ru/post/574396/" class="tm-article-title__link"><span>Диверсия на полмиллиарда</span></a></h2><div class="tm-data-icons"><!----><!----><span class="tm-icon-counter tm-data-icons__item" title="Количество просмотров"><svg height="16" width="16" class="tm-svg-img tm-icon-counter__icon"><title>Просмотры</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-views"></use></svg><span class="tm-icon-counter__value">7K</span></span><!----><div class="tm-article-comments-counter-link tm-data-icons__item" title="Читать комментарии"><a href="/ru/post/574396/comments/" class="tm-article-comments-counter-link__link"><svg height="16" width="16" class="tm-svg-img tm-article-comments-counter-link__icon"><title>Комментарии</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-comments"></use></svg><span class="tm-article-comments-counter-link__value">
#       18
#     </span></a><a href="/ru/post/574396/comments/" class="tm-article-comments-counter-link__link"><span title="Читать новые комментарии" class="tm-article-comments-counter-link__unread-counter">
#       +18
#     </span></a></div><!----><div class="v-portal" style="display: none;"></div></div></article></li><li class="tm-article-list-block__item"><article class="tm-article-snippet-block-sidebar tm-article-snippet-block-sidebar_preview"><!----><h2 class="tm-article-title tm-article-title_sidebar"><a href="/ru/news/t/574332/" class="tm-article-title__link"><span>Из Google Pay ушли десятки сотрудников</span></a></h2><div class="tm-data-icons"><!----><!----><span class="tm-icon-counter tm-data-icons__item" title="Количество просмотров"><svg height="16" width="16" class="tm-svg-img tm-icon-counter__icon"><title>Просмотры</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-views"></use></svg><span class="tm-icon-counter__value">15K</span></span><!----><div class="tm-article-comments-counter-link tm-data-icons__item" title="Читать комментарии"><a href="/ru/news/t/574332/comments/" class="tm-article-comments-counter-link__link"><svg height="16" width="16" class="tm-svg-img tm-article-comments-counter-link__icon"><title>Комментарии</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-comments"></use></svg><span class="tm-article-comments-counter-link__value">
#       53
#     </span></a><a href="/ru/news/t/574332/comments/" class="tm-article-comments-counter-link__link"><span title="Читать новые комментарии" class="tm-article-comments-counter-link__unread-counter">
#       +53
#     </span></a></div><!----><div class="v-portal" style="display: none;"></div></div></article></li><li class="tm-article-list-block__item"><article class="tm-article-snippet-block-sidebar tm-article-snippet-block-sidebar_preview"><!----><h2 class="tm-article-title tm-article-title_sidebar"><a href="/ru/news/t/574400/" class="tm-article-title__link"><span>Покупатели iPhone в РФ жалуются, что Apple обходит закон об обязательной предустановке отечественного ПО</span></a></h2><div class="tm-data-icons"><!----><!----><span class="tm-icon-counter tm-data-icons__item" title="Количество просмотров"><svg height="16" width="16" class="tm-svg-img tm-icon-counter__icon"><title>Просмотры</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-views"></use></svg><span class="tm-icon-counter__value">7.2K</span></span><!----><div class="tm-article-comments-counter-link tm-data-icons__item" title="Читать комментарии"><a href="/ru/news/t/574400/comments/" class="tm-article-comments-counter-link__link"><svg height="16" width="16" class="tm-svg-img tm-article-comments-counter-link__icon"><title>Комментарии</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-comments"></use></svg><span class="tm-article-comments-counter-link__value">
#       36
#     </span></a><a href="/ru/news/t/574400/comments/" class="tm-article-comments-counter-link__link"><span title="Читать новые комментарии" class="tm-article-comments-counter-link__unread-counter">
#       +36
#     </span></a></div><!----><div class="v-portal" style="display: none;"></div></div></article></li><li class="tm-article-list-block__item"><article class="tm-article-snippet-block-sidebar tm-article-snippet-block-sidebar_preview"><!----><h2 class="tm-article-title tm-article-title_sidebar"><a href="/ru/post/574356/" class="tm-article-title__link"><span>Эксперимент с двумя щелями и границы макромира</span></a></h2><div class="tm-data-icons"><!----><!----><span class="tm-icon-counter tm-data-icons__item" title="Количество просмотров"><svg height="16" width="16" class="tm-svg-img tm-icon-counter__icon"><title>Просмотры</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-views"></use></svg><span class="tm-icon-counter__value">9.1K</span></span><!----><div class="tm-article-comments-counter-link tm-data-icons__item" title="Читать комментарии"><a href="/ru/post/574356/comments/" class="tm-article-comments-counter-link__link"><svg height="16" width="16" class="tm-svg-img tm-article-comments-counter-link__icon"><title>Комментарии</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-comments"></use></svg><span class="tm-article-comments-counter-link__value">
#       40
#     </span></a><a href="/ru/post/574356/comments/" class="tm-article-comments-counter-link__link"><span title="Читать новые комментарии" class="tm-article-comments-counter-link__unread-counter">
#       +40
#     </span></a></div><!----><div class="v-portal" style="display: none;"></div></div></article></li><li class="tm-article-list-block__item"><article class="tm-article-snippet-block-sidebar tm-article-snippet-block-sidebar_preview"><!----><h2 class="tm-article-title tm-article-title_sidebar"><a href="/ru/news/t/574478/" class="tm-article-title__link"><span>CEO OnlyFans: «У нас не было выбора. Если коротко — это всё банки»</span></a></h2><div class="tm-data-icons"><!----><!----><span class="tm-icon-counter tm-data-icons__item" title="Количество просмотров"><svg height="16" width="16" class="tm-svg-img tm-icon-counter__icon"><title>Просмотры</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-views"></use></svg><span class="tm-icon-counter__value">1.3K</span></span><!----><div class="tm-article-comments-counter-link tm-data-icons__item" title="Читать комментарии"><a href="/ru/news/t/574478/comments/" class="tm-article-comments-counter-link__link"><svg height="16" width="16" class="tm-svg-img tm-article-comments-counter-link__icon"><title>Комментарии</title><use xlink:href="/img/megazord-v24.cee85629.svg#counter-comments"></use></svg><span class="tm-article-comments-counter-link__value">
#       8
#     </span></a><a href="/ru/news/t/574478/comments/" class="tm-article-comments-counter-link__link"><span title="Читать новые комментарии" class="tm-article-comments-counter-link__unread-counter">
#       +8
#     </span></a></div><!----><div class="v-portal" style="display: none;"></div></div></article></li><li class="tm-article-list-block__item"><a href="https://u.habr.com/itbqr" class="tm-most-reading-block__promo-post">Топ компаний, в которых айтишнику не больно</a><div class="tm-most-reading-block__label">Опрос</div></li></ul></div><!----></section></div></div></div></div></div></div></main><!----></div><div class="tm-footer-menu"><div class="tm-page-width"><div class="tm-footer-menu__container"><div class="tm-footer-menu__block"><h3 class="tm-footer-menu__block-title">
#           Ваш аккаунт
#         </h3><div class="tm-footer-menu__block-content"><ul class="tm-footer-menu__list"><li class="tm-footer-menu__list-item"><a href="/ru/users/mal_mel/posts/" class="footer-menu__item-link">
#                 Профиль
#               </a></li><li class="tm-footer-menu__list-item"><a href="/ru/tracker/" class="footer-menu__item-link">
#                 Трекер
#               </a></li><li class="tm-footer-menu__list-item"><a href="/ru/conversations/" class="footer-menu__item-link">
#                 Диалоги
#               </a></li><li class="tm-footer-menu__list-item"><a href="/ru/auth/settings/profile/" class="footer-menu__item-link">
#                 Настройки
#               </a></li><li class="tm-footer-menu__list-item"><a href="/ru/ppa/" class="footer-menu__item-link">
#                 ППА
#               </a></li></ul></div></div><div class="tm-footer-menu__block"><h3 class="tm-footer-menu__block-title">
#           Разделы
#         </h3><div class="tm-footer-menu__block-content"><ul class="tm-footer-menu__list"><li class="tm-footer-menu__list-item"><a href="/ru/" class="footer-menu__item-link router-link-active">
#                 Публикации
#               </a></li><li class="tm-footer-menu__list-item"><a href="/ru/news/" class="footer-menu__item-link">
#                 Новости
#               </a></li><li class="tm-footer-menu__list-item"><a href="/ru/hubs/" class="footer-menu__item-link">
#                 Хабы
#               </a></li><li class="tm-footer-menu__list-item"><a href="/ru/companies/" class="footer-menu__item-link">
#                 Компании
#               </a></li><li class="tm-footer-menu__list-item"><a href="/ru/users/" class="footer-menu__item-link">
#                 Авторы
#               </a></li><li class="tm-footer-menu__list-item"><a href="/ru/sandbox/" class="footer-menu__item-link">
#                 Песочница
#               </a></li></ul></div></div><div class="tm-footer-menu__block"><h3 class="tm-footer-menu__block-title">
#           Информация
#         </h3><div class="tm-footer-menu__block-content"><ul class="tm-footer-menu__list"><li class="tm-footer-menu__list-item"><a href="/ru/docs/help/" class="footer-menu__item-link">
#                 Устройство сайта
#               </a></li><li class="tm-footer-menu__list-item"><a href="/ru/docs/authors/codex/" class="footer-menu__item-link">
#                 Для авторов
#               </a></li><li class="tm-footer-menu__list-item"><a href="/ru/docs/companies/corpblogs/" class="footer-menu__item-link">
#                 Для компаний
#               </a></li><li class="tm-footer-menu__list-item"><a href="/ru/docs/docs/transparency/" class="footer-menu__item-link">
#                 Документы
#               </a></li><li class="tm-footer-menu__list-item"><a href="https://account.habr.com/info/agreement" target="_blank">
#                 Соглашение
#               </a></li><li class="tm-footer-menu__list-item"><a href="https://account.habr.com/info/confidential/" target="_blank">
#                 Конфиденциальность
#               </a></li></ul></div></div><div class="tm-footer-menu__block"><h3 class="tm-footer-menu__block-title">
#           Услуги
#         </h3><div class="tm-footer-menu__block-content"><ul class="tm-footer-menu__list"><li class="tm-footer-menu__list-item"><a href="https://docs.google.com/presentation/d/e/2PACX-1vQLwRfQmXibiUlWaRg-BAc38s7oM3lJiaPju7qmdJsp8ysIvZ_G-Npem0njJLMozE2bPHMpDqiI5hhy/pub?start=false&amp;loop=false&amp;delayms=60000&amp;slide=id.g91a03369cd_4_297" target="_blank">
#                 Реклама
#               </a></li><li class="tm-footer-menu__list-item"><a href="https://habrastorage.org/storage/stuff/habr/service_price.pdf" target="_blank">
#                 Тарифы
#               </a></li><li class="tm-footer-menu__list-item"><a href="https://docs.google.com/presentation/d/e/2PACX-1vQJJds8-Di7BQSP_guHxICN7woVYoN5NP_22ra-BIo4bqnTT9FR6fB-Ku2P0AoRpX0Ds-LRkDeAoD8F/pub?start=false&amp;loop=false&amp;delayms=60000" target="_blank">
#                 Контент
#               </a></li><li class="tm-footer-menu__list-item"><a href="https://tmtm.timepad.ru/" target="_blank">
#                 Семинары
#               </a></li><li class="tm-footer-menu__list-item"><a href="/ru/megaprojects/" class="footer-menu__item-link">
#                 Мегапроекты
#               </a></li></ul></div></div></div></div></div><div class="tm-footer"><div class="tm-page-width"><div class="tm-footer__container"><!----><div class="tm-footer__social"><a href="https://www.facebook.com/habrahabr.ru" rel="nofollow noopener noreferrer" target="_blank" class="tm-svg-icon__wrapper tm-social-icons__icon"><svg height="16" width="16" class="tm-svg-img tm-svg-icon"><title>Facebook</title><use xlink:href="/img/social-icons-sprite.svg#social-logo-facebook"></use></svg></a><a href="https://twitter.com/habr_com" rel="nofollow noopener noreferrer" target="_blank" class="tm-svg-icon__wrapper tm-social-icons__icon"><svg height="16" width="16" class="tm-svg-img tm-svg-icon"><title>Twitter</title><use xlink:href="/img/social-icons-sprite.svg#social-logo-twitter"></use></svg></a><a href="https://vk.com/habr" rel="nofollow noopener noreferrer" target="_blank" class="tm-svg-icon__wrapper tm-social-icons__icon"><svg height="16" width="16" class="tm-svg-img tm-svg-icon"><title>VK</title><use xlink:href="/img/social-icons-sprite.svg#social-logo-vkontakte"></use></svg></a><a href="https://telegram.me/habr_com" rel="nofollow noopener noreferrer" target="_blank" class="tm-svg-icon__wrapper tm-social-icons__icon"><svg height="16" width="16" class="tm-svg-img tm-svg-icon"><title>Telegram</title><use xlink:href="/img/social-icons-sprite.svg#social-logo-telegram"></use></svg></a><a href="https://www.youtube.com/channel/UCd_sTwKqVrweTt4oAKY5y4w" rel="nofollow noopener noreferrer" target="_blank" class="tm-svg-icon__wrapper tm-social-icons__icon"><svg height="16" width="16" class="tm-svg-img tm-svg-icon"><title>Youtube</title><use xlink:href="/img/social-icons-sprite.svg#social-logo-youtube"></use></svg></a><a href="https://zen.yandex.ru/habr" rel="nofollow noopener noreferrer" target="_blank" class="tm-svg-icon__wrapper tm-social-icons__icon"><svg height="16" width="16" class="tm-svg-img tm-svg-icon"><title>Яндекс Дзен</title><use xlink:href="/img/social-icons-sprite.svg#social-logo-zen"></use></svg></a></div><div class="v-portal" style="display:none;"></div><button class="tm-footer__link"><!---->
#         Настройка языка
#       </button><a href="/ru/about" class="tm-footer__link">
#         О сайте
#       </a><a href="/ru/feedback/" class="tm-footer__link">
#         Техническая поддержка
#       </a><!----><a href="/berserk-mode-nope" class="tm-footer__link">
#         Вернуться на старую версию
#       </a><div class="tm-footer-copyright"><span class="tm-copyright"><span class="tm-copyright__years">© 2006–2021 </span><span class="tm-copyright__name">«<a href="https://company.habr.com/" rel="noopener" target="_blank" class="tm-copyright__link">Habr</a>»</span></span></div></div></div></div><!----><!----></div><div class="vue-portal-target"><!----></div></div>
#
# <script src="https://assets.habr.com/habr-web/js/chunk-vendors.9e4ba848.js" defer=""></script><script src="https://assets.habr.com/habr-web/js/chunk-f458c7c4.529673c8.js" defer=""></script><script src="https://assets.habr.com/habr-web/js/app.5d04126c.js" defer=""></script>
#
#
#
#     <script>
#       (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
#         (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
#         m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
#       })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
#     </script>
#
#   <script type="text/javascript">
#     (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
#     m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
#     (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");
#
#     ym(24049213, "init", {
#       defer:true,
#       trackLinks:true,
#       accurateTrackBounce:true,
#       webvisor:false,
#     });
#   </script>
#   <noscript>
#     <div>
#       <img src="https://mc.yandex.ru/watch/24049213" style="position:absolute; left:-9999px;" alt="" />
#     </div>
#   </noscript>
#
#     <script type="text/javascript">
#       window.addEventListener('load', function () {
#         setTimeout(() => {
#           const img = new Image();
#           img.src = 'https://vk.com/rtrg?p=VK-RTRG-421343-57vKE';
#         }, 0);
#       });
#     </script>
#
#
#
# <div><div><div class="Vue-Toastification__container top-left"></div></div><div><div class="Vue-Toastification__container top-center"></div></div><div><div class="Vue-Toastification__container top-right"></div></div><div><div class="Vue-Toastification__container bottom-left"></div></div><div><div class="Vue-Toastification__container bottom-center"></div></div><div><div class="Vue-Toastification__container bottom-right"></div></div></div><div id="K9Jn4i4Yhz" style="display: none;"></div></body></html>"""
# s = BeautifulSoup(html, "lxml")
# print(PageHandler(UrlHandler("")).get_article_data(s, ""))
