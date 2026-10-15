#!/usr/bin/env python3
"""yerelsigorta.com static site generator."""
import os, hashlib, html, shutil, urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'site')
DOMAIN = 'https://www.yerelsigorta.com'
PHONE = '0 252 212 56 75'; PHONE_T = '02522125675'
PHONE2 = '0 252 212 53 25'; PHONE2_T = '02522125325'
MAIL = 'info@yerelsigorta.com'
WA = '905340822333'
ADDR = 'Emirbeyazıt Mh. Recai Güreli Cad. Bakkaloğlu İşhanı No:38/4 MUĞLA'
MAP = ('https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3177.3067973641123!2d28.358588815533476!3d37.21669125184299'
       '!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14bf6d89d316f1cf%3A0x1779ba0fd877c9fa!2sMu%C4%9Fla%20Yerel%20Sigorta'
       '!5e0!3m2!1str!2str!4v1585937995846!5m2!1str!2str')
MAPLINK = 'https://www.google.com/maps/search/?api=1&query=' + urllib.parse.quote('Muğla Yerel Sigorta')

E = html.escape

ICON = {
 'phone': 'M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z',
 'mail': 'M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z',
 'car': 'M18.92 6.01C18.72 5.42 18.16 5 17.5 5h-11c-.66 0-1.21.42-1.42 1.01L3 12v8c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-1h12v1c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-8l-2.08-5.99zM6.5 16c-.83 0-1.5-.67-1.5-1.5S5.67 13 6.5 13s1.5.67 1.5 1.5S7.33 16 6.5 16zm11 0c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zM5 11l1.5-4.5h11L19 11H5z',
 'home': 'M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z',
 'work': 'M20 6h-4V4c0-1.11-.89-2-2-2h-4c-1.11 0-2 .89-2 2v2H4c-1.11 0-1.99.89-1.99 2L2 19c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V8c0-1.11-.89-2-2-2zm-6 0h-4V4h4v2z',
 'plane': 'M21 16v-2l-8-5V3.5c0-.83-.67-1.5-1.5-1.5S10 2.67 10 3.5V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z',
 'heart': 'M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z',
 'pin': 'M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z',
 'doc': 'M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z',
 'up': 'M7.41 15.41L12 10.83l4.59 4.58L18 14l-6-6-6 6z',
 'left': 'M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z',
 'right': 'M8.59 16.59L13.17 12 8.59 7.41 10 6l6 6-6 6z',
 'down': 'M7.41 8.59L12 13.17l4.59-4.58L18 10l-6 6-6-6z',
 'menu': 'M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z',
 'close': 'M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z',
 'wa': 'M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.17-.3-.02-.46.13-.61.14-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.22 3.08c.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.69.63.71.23 1.36.2 1.87.12.57-.08 1.76-.72 2.01-1.41.25-.69.25-1.29.17-1.41-.07-.12-.27-.2-.57-.35zM12.04 2C6.5 2 2 6.5 2 12.04c0 1.77.46 3.5 1.34 5.03L2 22l5.07-1.33a10 10 0 0 0 4.97 1.31C17.58 22 22 17.5 22 12.04 22 6.5 17.58 2 12.04 2zm0 18.15a8.1 8.1 0 0 1-4.13-1.13l-.3-.18-3.01.79.8-2.93-.19-.31a8.1 8.1 0 1 1 6.83 3.76z',
 'check': 'M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z',
 'info': 'M11 7h2v2h-2zm0 4h2v6h-2zm1-9C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z',
}

def ic(n, cls=''):
    return f'<svg class="ic {cls}" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="{ICON[n]}"/></svg>'

# ---------------------------------------------------------------- nav
NAV = [
 ('Anasayfa', '', None),
 ('Araç', None, [('Zorunlu Trafik Sigortası', 'zorunlu-trafik-sigortasi'), ('Kasko Sigortası', 'kasko-sigortasi'), ('Yeşilkart', 'yesilkart'), ('Tekne', 'tekne')]),
 ('Konut', None, [('DASK', 'zorunlu-deprem-sigortasi'), ('Site Paket Sigortası', 'site-paket-sigortasi'), ('Konut Paket Sigortası', 'konut-paket-sigortasi')]),
 ('İş Yeri', 'is-yeri', None),
 ('Sağlık', 'tamamlayici-saglik-sigortasi', [('Tamamlayıcı Sağlık Sigortası', 'tamamlayici-saglik-sigortasi'), ('Bireysel Sağlık', 'bireysel-saglik'), ('Hayata Devam Sigortası', 'hayata-devam-sigortasi'), ('Yabancı Uyruklular Sağlık Sigortası', 'yabanci-uyruklular-saglik-sigortasi')]),
 ('Seyahat', 'seyahat', None),
 ('Diğer', 'diger', None),
 ('Hakkımızda', 'about', None),
 ('İletişim', 'iletisim', None),
 ('Bağlantılar', None, [
   ('Kaza Tespit Tutanağı', 'http://www.sbm.org.tr/tr/Documents/kaza_tespit_tutanagi.pdf'),
   ('Dask Hesaplama', 'https://www.dask.gov.tr/e-services/portal/calculatePremium'),
   ('Tramer', 'http://www.sbm.org.tr/tr'),
   ('Kasko Değer Listesi', 'http://www.tsb.org.tr/kasko-deger-listesi.aspx?pageID=631'),
   ('Sigorta Genel Şartları', 'http://www.tsb.org.tr/kasko-deger-listesi.aspx?pageID=631'),
   ('Kasko Poliçe Sorgulama', 'http://www.sbm.org.tr/tr/OnlineIslemler/Sayfalar/KaskoPoliceSorgula.aspx'),
   ('Trafik Poliçe Sorgulama', 'http://www.sbm.org.tr/tr/OnlineIslemler/Sayfalar/TrafikPoliceSorgula.aspx'),
   ('Kaza Tespit T. Sorgulama', 'http://www.sbm.org.tr/tr/OnlineIslemler/Sayfalar/TrafikPoliceSorgula.aspx')]),
]
TITLES = {'': 'Anasayfa'}
for n, s, sub in NAV:
    if s is not None: TITLES.setdefault(s, n)
    for sn, ss in (sub or []):
        if not ss.startswith('http'): TITLES[ss] = sn
TITLES.update({'sigorta-hatirlatma': 'Sigorta Hatırlatma', 'is-yeri': 'İş Yeri Paket Sigortası', 'seyahat': 'Seyahat Sigortası',
               'diger': 'Diğer Sigortalar', 'about': 'Hakkımızda', 'tamamlayici-saglik-sigortasi': 'Tamamlayıcı Sağlık Sigortası',
               'akaryakit-paket': 'Akaryakıt Paket Sigortası', 'bireysel-saglik': 'Bireysel Sağlık Sigortası',
               'zorunlu-deprem-sigortasi': 'Zorunlu Deprem Sigortası (DASK)', 'yesilkart': 'Yeşil Kart Sigortası',
               'tekne': 'Tekne Sigortası'})
# which top-level nav item is "current" for a slug
PARENT = {}
for n, s, sub in NAV:
    if s is not None: PARENT[s] = n
    for sn, ss in (sub or []):
        PARENT[ss] = n
PARENT['akaryakit-paket'] = 'İş Yeri'

DESC = {
 '': 'Muğla Yerel Sigorta Aracılık Hizmetleri: trafik, kasko, konut, işyeri, sağlık ve seyahat sigortalarında Muğla\'da güvenilir sigorta acentesi.',
 'about': 'Muğla Yerel Sigorta Aracılık Hizmetleri Ltd. Şti. 1995\'ten beri Muğla\'da sigorta hizmeti veriyor. Vizyonumuz, misyonumuz ve değerlerimiz.',
 'iletisim': 'Muğla Yerel Sigorta iletişim bilgileri: adres, telefon, e-posta, WhatsApp ve harita.',
}

# ---------------------------------------------------------------- page class
class Page:
    def __init__(self, slug, title, body, desc=None, banner=None, nav_cur=None):
        self.slug, self.title, self.body_html = slug, title, body
        self.desc = desc; self.nav_cur = nav_cur if nav_cur is not None else PARENT.get(slug)
    @property
    def depth(self): return 0 if self.slug == '' else 1

def rel(page, path):
    """relative url from page to site path"""
    up = '../' * page.depth
    return up + path

def link(page, slug):
    if slug.startswith('http'): return slug
    return rel(page, slug + '/') if slug else (rel(page, '') or './')

ASSET_V = ''

def cta_text(topic):
    return f'Merhaba, {topic} hakkında bilgi / teklif almak istiyorum.'

def wa_url(msg):
    return f'https://wa.me/{WA}?text=' + urllib.parse.quote(msg)

def mail_url(subject, body=''):
    return f'mailto:{MAIL}?subject=' + urllib.parse.quote(subject) + (('&body=' + urllib.parse.quote(body)) if body else '')

def contact_buttons(topic, cls=''):
    return (f'<div class="actions {cls}">'
            f'<a class="btn btn--call" href="tel:{PHONE_T}">{ic("phone")}<span>{PHONE}</span></a>'
            f'<a class="btn btn--wa" href="{wa_url(cta_text(topic))}" target="_blank" rel="noopener">{ic("wa")}<span>WhatsApp ile yazın</span></a>'
            f'<a class="btn btn--mail" href="{mail_url(topic + " - Teklif Talebi", cta_text(topic))}">{ic("mail")}<span>E-posta gönderin</span></a>'
            '</div>')

def cta_panel(topic, title='Teklif almak için bize ulaşın', text='Size en uygun teklifi sektörün lider sigorta şirketlerinden hazırlayalım. Arayın, WhatsApp\'tan yazın ya da e-posta gönderin; en kısa sürede dönüş yapalım.'):
    return (f'<section class="sec sec--primary cta"><div class="sec__in"><div class="cta__grid">'
            f'<div class="cta__txt"><h2>{E(title)}</h2><p>{E(text)}</p></div>'
            f'<div class="cta__act">{contact_buttons(topic, "actions--stack")}</div></div></div></section>')

def compose(kind, topic, fields, intro=''):
    """client-side form: builds a WhatsApp / mail message, nothing is sent to a server."""
    rows = ''
    for name, label, typ, req in fields:
        if typ == 'textarea':
            rows += f'<label class="f__row f__row--full"><span>{E(label)}{" *" if req else ""}</span><textarea name="{name}" rows="4"{" required" if req else ""}></textarea></label>'
        else:
            rows += f'<label class="f__row"><span>{E(label)}{" *" if req else ""}</span><input type="{typ}" name="{name}"{" required" if req else ""} autocomplete="off"></label>'
    return (f'<form class="compose" data-topic="{E(topic)}" data-wa="{WA}" data-mail="{MAIL}" novalidate>'
            f'{("<p class=compose__intro>" + E(intro) + "</p>") if intro else ""}'
            f'<div class="f__grid">{rows}</div>'
            f'<div class="compose__btns"><button type="button" class="btn btn--wa" data-send="wa">{ic("wa")}<span>WhatsApp ile gönder</span></button>'
            f'<button type="button" class="btn btn--mail" data-send="mail">{ic("mail")}<span>E-posta ile gönder</span></button></div>'
            f'<p class="compose__note">{ic("info")}<span>Bu form bilgileri sunucuya göndermez; butona bastığınızda hazırlanan mesaj WhatsApp\'ta veya e-posta uygulamanızda açılır.</span></p>'
            f'<p class="compose__err" role="alert" hidden>Lütfen zorunlu (*) alanları doldurun.</p></form>')

# ---------------------------------------------------------------- shared chrome
def header(p):
    cur = p.nav_cur
    items = ''
    for n, s, sub in NAV:
        is_cur = (n == cur) or (n == 'Anasayfa' and p.slug == '')
        cls = 'nav__item' + (' has-sub' if sub else '') + (' is-current' if is_cur else '')
        if sub:
            href = link(p, s) if s else '#'
            sublis = ''
            for sn, ss in sub:
                ext = ss.startswith('http')
                sublis += f'<li><a href="{link(p, ss)}"{" target=_blank rel=noopener" if ext else ""}>{E(sn)}</a></li>'
            tog = f'<button class="sub-toggle" type="button" aria-label="{E(n)} alt menüsü" aria-expanded="false">{ic("down")}</button>'
            main_a = (f'<a href="{href}" class="nav__link">{E(n)}</a>' if s else f'<a href="#" class="nav__link sub-toggle-link" role="button" aria-haspopup="true">{E(n)}</a>')
            items += f'<li class="{cls}">{main_a}{tog}<ul class="nav__sub">{sublis}</ul></li>'
        else:
            items += f'<li class="{cls}"><a href="{link(p, s)}" class="nav__link"{" aria-current=page" if is_cur else ""}>{E(n)}</a></li>'
    return (f'<header class="hdr"><div class="hdr__top"><a class="hdr__logo" href="{link(p, "")}" aria-label="Yerel Sigorta - Anasayfa">'
            f'<img src="{rel(p, "assets/img/logo.webp")}" width="350" height="90" alt="Yerel Sigorta"></a>'
            f'<div class="hdr__contact"><a href="tel:{PHONE_T}">{ic("phone")}<span>{PHONE}</span></a>'
            f'<a href="mailto:{MAIL}">{ic("mail")}<span>{MAIL}</span></a></div>'
            f'<button class="burger" type="button" aria-label="Menüyü aç" aria-expanded="false" aria-controls="nav">{ic("menu")}</button></div>'
            f'<nav class="hdr__nav" id="nav" aria-label="Ana menü"><div class="nav__head"><span>Menü</span><button class="nav__close" type="button" aria-label="Menüyü kapat">{ic("close")}</button></div>'
            f'<ul class="nav">{items}</ul></nav><div class="hdr__overlay"></div></header>')

def footer(p):
    def col(title, lis):
        return f'<div class="ft__col"><h3>{E(title)}</h3><ul>{"".join(lis)}</ul></div>'
    prod = [f'<li><a href="{link(p, s)}">{E(n)}</a></li>' for n, s in [
        ('Zorunlu Trafik Sigortası', 'zorunlu-trafik-sigortasi'), ('Kasko Sigortası', 'kasko-sigortasi'), ('DASK', 'zorunlu-deprem-sigortasi'),
        ('Konut Paket Sigortası', 'konut-paket-sigortasi'), ('İş Yeri Paket Sigortası', 'is-yeri'), ('Seyahat Sigortası', 'seyahat')]]
    prod2 = [f'<li><a href="{link(p, s)}">{E(n)}</a></li>' for n, s in [
        ('Tamamlayıcı Sağlık', 'tamamlayici-saglik-sigortasi'), ('Bireysel Sağlık', 'bireysel-saglik'), ('Hayata Devam', 'hayata-devam-sigortasi'),
        ('Sigorta Hatırlatma', 'sigorta-hatirlatma'), ('Hakkımızda', 'about'), ('İletişim', 'iletisim')]]
    contact = [f'<li class="ft__ct">{ic("pin")}<span>{E(ADDR)}</span></li>',
               f'<li class="ft__ct">{ic("phone")}<a href="tel:{PHONE_T}">{PHONE}</a></li>',
               f'<li class="ft__ct">{ic("phone")}<a href="tel:{PHONE2_T}">{PHONE2}</a></li>',
               f'<li class="ft__ct">{ic("mail")}<a href="mailto:{MAIL}">{MAIL}</a></li>']
    return (f'<footer class="ft"><div class="ft__top"><div class="ft__in">'
            f'<div class="ft__col ft__col--about"><h3>Muğla Yerel Sigorta</h3><p>Aracılık Hizmetleri Ltd. Şti.<br>1995\'ten beri Muğla\'da, lider sigorta şirketlerinin yetkili acentesi.</p></div>'
            f'{col("Sigortalar", prod)}{col("Kurumsal", prod2)}{col("İletişim", contact)}</div></div>'
            f'<div class="ft__bot">© {2026} Muğla Yerel Sigorta Aracılık Hizmetleri Ltd. Şti. · Tasarım <strong>Teknofikir</strong></div></footer>'
            f'<a class="wa-float" href="{wa_url("Merhaba, bilgi almak istiyorum.")}" target="_blank" rel="noopener" aria-label="WhatsApp ile yazın">{ic("wa")}</a>'
            f'<button class="toplink" type="button" aria-label="Yukarı çık" hidden>{ic("up")}</button>')

def render(p):
    title = p.title if p.slug == '' else f'{p.title} | Muğla Yerel Sigorta'
    if p.slug == '': title = 'Muğla Yerel Sigorta | Sigorta Acentesi'
    desc = p.desc or DESC.get(p.slug) or f'{p.title} - Muğla Yerel Sigorta Aracılık Hizmetleri Ltd. Şti.'
    canon = f'{DOMAIN}/' + (p.slug + '/' if p.slug else '')
    fonts = ''.join(f'@font-face{{font-family:"{f}";font-weight:{w};font-style:normal;font-display:swap;src:url({rel(p,"assets/"+fn+".woff")}) format("woff")}}'
                    for f, w, fn in [('Open Sans', 400, 'OpenSans-400'), ('Open Sans', 600, 'OpenSans-600'), ('Open Sans', 700, 'OpenSans-700'), ('Noto Sans', 400, 'NotoSans-400')])
    preload = f'<link rel="preload" href="{rel(p,"assets/OpenSans-400.woff")}" as="font" type="font/woff" crossorigin>'
    ld = ''
    if p.slug == '':
        ld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"InsuranceAgency","name":"Muğla Yerel Sigorta Aracılık Hizmetleri Ltd. Şti.",'
              f'"url":"{DOMAIN}/","telephone":"+902522125675","email":"{MAIL}","image":"{DOMAIN}/assets/img/logo.webp",'
              '"address":{"@type":"PostalAddress","streetAddress":"Emirbeyazıt Mh. Recai Güreli Cad. Bakkaloğlu İşhanı No:38/4","addressLocality":"Muğla","addressCountry":"TR"}}</script>')
    return (f'<!doctype html>\n<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{canon}">'
            f'<meta property="og:type" content="website"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}">'
            f'<meta property="og:url" content="{canon}"><meta property="og:image" content="{DOMAIN}/assets/img/slide.webp"><meta name="theme-color" content="#1b98e0">'
            f'<link rel="icon" type="image/png" href="{rel(p,"assets/img/favicon.png")}"><link rel="apple-touch-icon" href="{rel(p,"assets/img/apple.png")}">'
            f'{preload}<style>{fonts}</style><link rel="stylesheet" href="{rel(p,"css/style.css")}?v={ASSET_V}">{ld}</head>'
            f'<body class="page-{p.slug or "home"}"><a class="skip" href="#main">İçeriğe geç</a><div class="canvas">{header(p)}'
            f'<main id="main">{p.body_html(p) if callable(p.body_html) else p.body_html}</main>{footer(p)}</div>'
            f'<script src="{rel(p,"js/main.js")}?v={ASSET_V}" defer></script></body></html>')

# ---------------------------------------------------------------- body helpers
def crumbs(p, title):
    return (f'<nav class="crumbs" aria-label="Sayfa yolu"><ol><li><a href="{link(p, "")}">Giriş</a></li>'
            f'<li class="sep" aria-hidden="true">{ic("right")}</li><li aria-current="page">{E(title)}</li></ol></nav>')

def titlebar(p, h1):
    return (f'<section class="sec sec--alt titlebar"><div class="sec__in titlebar__in"><h1>{E(h1)}</h1>{crumbs(p, h1)}</div></section>')

def banner(p, key, alt=''):
    return (f'<div class="banner"><img src="{rel(p, f"assets/img/banner-{key}.webp")}" srcset="{rel(p, f"assets/img/banner-{key}-600.webp")} 600w, {rel(p, f"assets/img/banner-{key}.webp")} 1140w" '
            f'sizes="(max-width:1140px) 100vw, 1140px" width="1140" height="300" alt="{E(alt)}"></div>')

def simple_page(slug, h1, key, paras, extra='', topic=None, banner_alt=None):
    topic = topic or h1
    def body(p):
        ps = ''.join(paras)
        return (titlebar(p, h1) + f'<section class="sec"><div class="sec__in prose">{banner(p, key, banner_alt or h1) if key else ""}{ps}{extra if isinstance(extra, str) else extra(p)}</div></section>'
                + cta_panel(topic))
    return Page(slug, h1, body)

def P(t): return f'<p>{t}</p>'

# ---------------------------------------------------------------- pages
pages = []

# HOME
SERV = [('Trafik Sigortası', 'car', 'zorunlu-trafik-sigortasi'), ('Kasko Sigortası', 'car', 'kasko-sigortasi'), ('Konut Sigortası', 'home', 'konut-paket-sigortasi'),
        ('İşyeri Sigortası', 'work', 'is-yeri'), ('Seyahat Sigortası', 'plane', 'seyahat'), ('Sağlık Sigortası', 'heart', 'saglik')]
BRANDS = [('turkpi', 'Türk P ve I'), ('hdi', 'HDI Sigorta'), ('allianz', 'Allianz'), ('axa', 'AXA Sigorta'), ('anadolu', 'Anadolu Sigorta'), ('aksigorta', 'Aksigorta')]

def home_body(p):
    flips = ''.join(
        f'<li><a class="flip" href="{link(p, s)}" aria-label="{E(n)} - Detaylı bilgi"><span class="flip__in">'
        f'<span class="flip__f"><span class="flip__ic">{ic(i)}</span><span class="flip__t">{E(n)}</span></span>'
        f'<span class="flip__b"><span class="flip__t">Detaylı Bilgi</span><span class="flip__d">Sektörün lider firmalarından en uygun seçenekler.</span></span></span></a></li>'
        for n, i, s in SERV)
    brands = ''.join(f'<li><img src="{rel(p, f"assets/img/brand-{k}.webp")}" width="300" height="171" alt="{E(n)}"></li>' for k, n in BRANDS)
    return (
        f'<section class="hero"><picture><source media="(max-width:700px)" srcset="{rel(p,"assets/img/slide-mobil.webp")}" width="640" height="1138">'
        f'<img src="{rel(p,"assets/img/slide.webp")}" width="1240" height="440" alt="Sağlığım Tamam Sigortası - Özel hastanede ne kadar SGK farkı ödeyeceğim diye düşünmeyin!" fetchpriority="high"></picture>'
        f'<a class="hero__link" href="{link(p,"tamamlayici-saglik-sigortasi")}" aria-label="Tamamlayıcı Sağlık Sigortası hakkında bilgi alın"></a></section>'
        f'<section class="sec sec--alt"><div class="sec__in"><h2 class="h-center">Sigorta Hizmetlerimiz</h2></div></section>'
        f'<section class="sec sec--flips"><ul class="flips">{flips}</ul></section>'
        f'<section class="sec sec--alt deniz"><div class="sec__in center"><h2 class="h-center">Deniz Araçları Zorunlu Mali Sorumluluk Sigortası</h2>'
        f'<a class="deniz__ic" href="{rel(p,"assets/docs/deniz-araclari-sigorta-formu.pdf")}" target="_blank" rel="noopener" aria-label="Başvuru formunu indir">{ic("doc")}</a>'
        f'<h3>Başvuru Formu</h3><p><a href="{rel(p,"assets/docs/deniz-araclari-sigorta-formu.pdf")}" target="_blank" rel="noopener">DENİZ ARAÇLARI ZORUNLU MALİ SORUMLULUK SİGORTASI BAŞVURU FORMU</a></p>'
        f'<p class="muted">PDF formu indirip doldurduktan sonra bize e-posta ile gönderebilir veya ofisimize getirebilirsiniz.</p></div></section>'
        f'<section class="sec sec--primary cta"><div class="sec__in"><div class="cta__grid cta__grid--home">'
        f'<div class="cta__txt"><h2>Sizin için en uygun sigortayı öğrenmek mi istiyorsunuz?</h2><p>Detaylı bilgi ve sigorta danışmanınızdan yardım almak için hemen arayın. Ya da WhatsApp veya e-posta ile yazın, biz size ulaşalım.</p></div>'
        f'<div class="cta__act">{contact_buttons("Sigorta teklifi", "actions--stack")}</div></div></div></section>'
        f'<section class="sec brands"><div class="sec__in"><div class="carousel" data-carousel><button class="carousel__btn carousel__btn--prev" type="button" aria-label="Önceki">{ic("left")}</button>'
        f'<ul class="carousel__track">{brands}</ul><button class="carousel__btn carousel__btn--next" type="button" aria-label="Sonraki">{ic("right")}</button></div></div></section>')

pages.append(Page('', 'Anasayfa', home_body, nav_cur='Anasayfa'))

# ABOUT
TABS = [
 ('Hakkımızda', 'Şirketimiz', ['<p><b>Muğla Yerel Sigorta Aracılık Hizmetleri Limited Şirketi</b>, sigorta sektöründeki faaliyetlerine 1995 yılında G08528-4ZGP levha kayıt numarasıyla başlamış olup, tecrübeli ve eğitimli kadrosuyla siz değerli müşterilerine en iyi hizmeti sunmaya çalışmaktadır. <b>Muğla Yerel Sigorta Aracılık Hizmetleri Limited Şirketi</b>, sektörün lider sigorta kuruluşlarından olan Aksigorta, Axa Sigorta, Anadolu Sigorta, Allianz Sigorta ve HDİ Sigorta şirketlerinin yetkili acentesidir. <b>Muğla Yerel Sigorta Aracılık Hizmetleri Limited Şirketi</b> uzun yılların getirdiği tecrübe ve dürüst çalışma anlayışının desteği, sürekli artan müşteri portföyü ile sektörde güven sağlamayı başarmıştır. Müşteri memnuniyeti ve güvenilirlik ilkesi çatısı altında, her müşterisi ile şeffaf bir anlayış içerisinde çalışmayı benimseyen şirketimiz poliçeler ve teminatları konusunda en doğru yönlendirmeyi yapmak için güncel eğitimleri tamamlayarak çalışmaktadır. <b>Muğla Yerel Sigorta Aracılık Hizmetleri Limited Şirketi</b>, yetkili acentelikleri ile tüm poliçelerinizi minimum prim, maksimum teminatla güvenceye almak ve sizlere en iyi hizmeti sunarak, hayatınızdaki tüm riskleri ortadan kaldırmak ve risk anında yanınızda olmak adına çalışmaktadır.</p>']),
 ('Vizyonumuz', 'Vizyonumuz', ['<p>Sigortacılık sektöründe kaliteli, ulaşılabilinir ve hızlı hizmet veren bir acente olma özelliğimizi koruyarak ilerlemek.<br>Müşteri isteklerini daima ön planda tutmak ve müşterilerimizi doğru yönlendirmek.<br>Ticari ve sosyal ilişkilerimizde karşılıklı güven, üstün iş ahlakı ve dürüst davranış ilkesinden vazgeçmemek.<br>Kanunlara ve yasal düzenlemelere titizlikle uymak.<br>Mesleğimiz etik kurallarına bağlı kalmaktır.</p>']),
 ('Misyonumuz', 'Misyonumuz', ['<p>Hayatın devamlılığı ve kolaylaştırılması için müşterilerimizin istekleri doğrultusunda farklı bir sigorta deneyimi sunarak değer yaratmak.<br>Müşterilerimizin ihtiyaçlarını doğru olarak tespit edip, bilgiye, deneyime ve güvene dayalı bir şekilde, ihtiyaçları en kısa zamanda, doğru bir şekilde karşılamaktır. Hedefimiz siz değerli müşterilerimize satış öncesi ve satış sonrası kaliteli ve daha etkili hizmet vermektir.</p>']),
 ('Değerlerimiz', 'Değerlerimiz', ['<p>Güvenirlik<br>Toplum, müşteri ve çözüm odaklılık<br>Uzmanlık<br>Profesyonellik<br>Şeffaflık, açıklık, dürüstlük<br>İlkeli, gerçekçi ve tutarlı Olmak</p>']),
 ('Kalite Politikamız', 'Kalite Politikamız', ['<p>Tüketiciler tarafından tercih edilen ve müşterilerimizin memnuniyetini en üst seviyede sağlayan, etik kurallara ve yasalara saygılı bir biçimde çevremizde referans olarak gösterilen, her an ulaşılabileceğiniz bir kuruluş olmak için buradayız…</p>']),
]

def hero_band(p, h1, sub=None):
    return (f'<section class="sec sec--primary band"><div class="band__img" style="background-image:url({rel(p,"assets/img/parallax.webp")})"></div><div class="band__shade"></div>'
            f'<div class="sec__in band__in"><h1>{h1}</h1>{("<p>" + sub + "</p>") if sub else ""}</div></section>')

def about_body(p):
    tl = ''.join(f'<button type="button" role="tab" class="tab{" is-on" if i == 0 else ""}" id="tab-{i}" aria-controls="panel-{i}" aria-selected="{"true" if i == 0 else "false"}">{E(n)}</button>' for i, (n, _, _) in enumerate(TABS))
    tp = ''.join(f'<div class="tabpanel{" is-on" if i == 0 else ""}" role="tabpanel" id="panel-{i}" aria-labelledby="tab-{i}"><h4>{E(h)}</h4>{"".join(b)}</div>' for i, (_, h, b) in enumerate(TABS))
    return (hero_band(p, 'MUĞLA YEREL SİGORTA ARACILIK HİZMETLERİ') +
            f'<section class="sec"><div class="sec__in"><div class="tabs" data-tabs><div class="tablist" role="tablist">{tl}</div>{tp}</div></div></section>' + cta_panel('Muğla Yerel Sigorta', 'Sizinle tanışmak isteriz', 'Sigorta ihtiyaçlarınız için bizi arayabilir, WhatsApp veya e-posta ile ulaşabilirsiniz.'))

pages.append(Page('about', 'Hakkımızda', about_body, nav_cur='Hakkımızda'))

# ILETISIM
def iletisim_body(p):
    cards = (f'<div class="icards">'
             f'<div class="icard">{ic("pin")}<h3>Adres</h3><p>{E(ADDR)}</p><a class="icard__a" href="{MAPLINK}" target="_blank" rel="noopener">Haritada aç</a></div>'
             f'<div class="icard">{ic("phone")}<h3>Telefon</h3><p><a href="tel:{PHONE_T}">{PHONE}</a><br><a href="tel:{PHONE2_T}">{PHONE2}</a></p></div>'
             f'<div class="icard">{ic("mail")}<h3>E-posta</h3><p><a href="mailto:{MAIL}">{MAIL}</a></p></div>'
             f'<div class="icard">{ic("wa")}<h3>WhatsApp</h3><p><a href="{wa_url("Merhaba, bilgi almak istiyorum.")}" target="_blank" rel="noopener">Mesaj yazın</a></p></div></div>')
    form = '<p>Sigorta teklifi veya bilgi için bizi arayın, WhatsApp\'tan yazın ya da e-posta gönderin.</p>' + contact_buttons('Muğla Yerel Sigorta', 'actions--light actions--stack')
    return (hero_band(p, 'Muğla Yerel Sigorta', 'Aracılık Hizmetleri Ltd. Şti.') +
            f'<section class="sec"><div class="sec__in"><h2 class="h-left">İletişim</h2>{cards}'
            f'<div class="split"><div><h2 class="h-left">Bize Ulaşın</h2>{form}</div>'
            f'<div><h2 class="h-left">Konum</h2><div class="map"><iframe src="{MAP}" title="Muğla Yerel Sigorta harita konumu" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div></div></div></div></section>')

pages.append(Page('iletisim', 'İletişim', iletisim_body, nav_cur='İletişim'))

# PRODUCT PAGES
pages.append(simple_page('zorunlu-trafik-sigortasi', 'Zorunlu Trafik Sigortası', 'trafik',
    [P('Trafik Sigortası, kaza sonucunda diğer araç ve üçüncü şahıs veya şahıs eşyalarına verebileceğiniz zararlar için sizi teminat altına alan zorunlu bir sigorta poliçesidir.')]))
pages.append(simple_page('kasko-sigortasi', 'Kasko Sigortası', 'kasko',
    [P('Kasko Sigortası, herhangi bir motorlu kara taşıtının hareket halindeyken ya da dururken hasara uğraması, çalınması, yanması ve kaza gibi durumlarda sigorta sahibine tazminat ödenmesini sağlayan bir poliçedir.')]))
pages.append(simple_page('yesilkart', 'Yeşilkart', 'yesilkart',
    [P('Yeşil kart sistemi dahilindeki ülkelere Mali Mesuliyet Poliçesinin uluslararası uzantısı şeklinde kaza mahalli ülke mevzuatı ve limitleri dahilinde teminat veren yeşil renkli ve uluslararası tek bir formatla düzenlenen bir belgedir.')], topic='Yeşilkart Sigortası'))
pages.append(simple_page('tekne', 'Tekne Sigortası', 'tekne',
    [P('Denizlerde güvenli bir yolculuk, yatınız ve içindeki ekipmanları olası risklere karşı güvence altına almak için düzenlenen bir poliçedir.')]))
pages.append(simple_page('zorunlu-deprem-sigortasi', 'Zorunlu Deprem Sigortası (DASK)', 'dask',
    [P('Zorunlu Deprem Sigortası ile depremin ve deprem sonucu meydana gelen yangın, infilak, tsunami ve yer kaymasının doğrudan neden olacağı maddi zararları, poliçenizde belirtilmiş limitler dahilinde nakit olarak karşılar.')],
    extra='<p><a class="btn btn--line" href="https://www.dask.gov.tr/e-services/portal/calculatePremium" target="_blank" rel="noopener">DASK prim hesaplama</a></p>', topic='DASK (Zorunlu Deprem Sigortası)'))
pages.append(simple_page('site-paket-sigortasi', 'Site Paket Sigortası', 'konutpaket',
    [P('Site Paket sigortasıyla sitenizi yangından sele, yer kaymasından hırsızlığa ortak kullanım alanlarınız hatta elektronik cihazların bozulmasına kadar güvence altına alır.')]))
pages.append(simple_page('konut-paket-sigortasi', 'Konut Paket Sigortası', 'konutpaket',
    [P('Evinizi yangından yıldırıma, taşıt çarpmasından hırsızlığa, selden fırtınaya, su basmasından cam kırılmasına hatta elektronik eşyanıza gelecek zarara karşı güvence altına alan bir poliçedir.')]))

def isyeri_extra(p):
    lis = ''.join(f'<li>{x}</li>' for x in [f'<a href="{link(p,"akaryakit-paket")}">Akaryakıt paket</a>', 'Otel paket', 'Eczane paket', 'Esnafım paket', 'Kobi paket', 'Kurumsal paket'])
    return f'<ul class="ticks">{lis}</ul>'
pages.append(simple_page('is-yeri', 'İş Yeri Paket Sigortası', 'akaryakit',
    [P('İş yeri Paket Sigortası siz iş yeri sahipleri düşünülerek mümkün olan tüm riskleri en ekonomik şekilde kapsayabilmek için hazırlanmış bir sigorta paketidir. İşyerinizdeki mallardan dekorasyonunuza, müşterilerinizden çalışanlarınıza, makinelerinizden elektronik cihazlarınıza kadar değer verdiğiniz tüm taşınır ve taşınmazları ekonomik bir şekilde güvence altına alabilirsiniz. Ayrıca kendinizi, çalışanlarınızı, müşterilerinizi ve çevrenizi de korumuş olursunuz.')],
    extra=isyeri_extra))
pages.append(simple_page('akaryakit-paket', 'Akaryakıt Paket Sigortası', 'akaryakit',
    [P('Akaryakıt paket sigortası, akaryakıt istasyonu işletmecileri için hazırlanmış İş Yeri Paket Sigortası seçeneklerinden biridir. İstasyonunuza özel teminatlar ve en uygun fiyat seçenekleri için bizimle iletişime geçin.')],
    extra=lambda p: f'<p><a class="btn btn--line" href="{link(p,"is-yeri")}">İş Yeri Paket Sigortası\'na dön</a></p>', topic='Akaryakıt Paket Sigortası'))
pages.append(simple_page('saglik', 'Sağlık Sigortası', 'saglik',
    [P('Sahip olduğunuz en değerli varlığınız öncelikle kendi sağlığınızdır. Karşılaşabileceğiniz bir sağlık probleminde veya bir kaza sonucu yaralanmanız halinde ayakta ya da yatarak yapılacak hastane tedavi giderleriniz, doktor muayenesi, röntgen, tahlil benzeri tanı ve ilaç giderleriniz, küçük ya da büyük cerrahi müdahaleler için gereken harcamalarınız karşılanır. Sağlık sigortası yaptırmayı geleceğe yapılan bir yatırım olarak düşünmek ve bir lüksten ziyade ihtiyaç olarak algılamak gerekir.')],
    extra=lambda p: (f'<ul class="ticks">' + ''.join(f'<li><a href="{link(p,s)}">{E(n)}</a></li>' for n, s in [('Tamamlayıcı Sağlık Sigortası', 'tamamlayici-saglik-sigortasi'), ('Bireysel Sağlık', 'bireysel-saglik'), ('Hayata Devam Sigortası', 'hayata-devam-sigortasi'), ('Yabancı Uyruklular Sağlık Sigortası', 'yabanci-uyruklular-saglik-sigortasi')]) + '</ul>'),
    ))
pages[-1].nav_cur = 'Sağlık'
pages.append(simple_page('bireysel-saglik', 'Bireysel Sağlık', 'sagligimtamam',
    [P('Başımıza gelecek her türlü kaza, hastalık beklenmeyen sağlık sorunlarımıza karşı düzenlenen bir poliçedir.')], topic='Bireysel Sağlık Sigortası'))
pages.append(simple_page('yabanci-uyruklular-saglik-sigortasi', 'Yabancı Uyruklular Sağlık Sigortası', 'sagligimtamam',
    [P('Oturma izni veya ikamet tezkeresi için başvuran yabancı uyruklu kişilerin yaptırmaları gereken sağlık sigortaları için çözüm sunmaktadır. Bu poliçe oturma izni ya da ikamet tezkeresi için gerekli olan şartları karşılayan bir poliçedir.')]))

def seyahat_extra(p):
    items = [('Seyahat sağlık', 'Seyahatiniz esnasında aniden hastalanmanız veya yaralanmanız durumunda, ayakta tedavi ve hastane, ameliyat ve tedavi masrafları ile doktorunuzun yazdığı ilaçların masrafları limitler dâhilinde ödenmesi için yapılan bir poliçedir.'),
             ('Premium seyahat sağlık', 'Yurt dışı seyahatlerinizde karşılaşabileceğiniz acil sağlık sorunlarından bagaj kayıplarına kadar pek çok riske karşı kendinizi güvence altına alabileceğiniz bir poliçedir.'),
             ('Öğrenci seyahat sağlık', 'Yurt dışında öğrenim amacıyla yapılan seyahat sırasında meydana gelecek risklere karşı Türkiye dışında tüm dünyada güvence sunan bir poliçedir.'),
             ('Yurtiçi seyahat sağlık', 'Yurtiçi gezilerinizde başınıza gelebilecek ölüm cenaze nakil bavul kaybolması rezervasyon iptali gibi nedenlere karşı düzenlenen bir poliçedir.')]
    return '<div class="defs">' + ''.join(f'<div class="def"><h3>{E(a)}</h3><p>{E(b)}</p></div>' for a, b in items) + '</div>'
pages.append(simple_page('seyahat', 'Seyahat Sigortası', 'seyahat', [], extra=seyahat_extra))

def diger_extra(p):
    d = [('İnşaat', 'İnşaat faaliyetlerinin başlangıcından bitimine kadar geçen süre içinde, inşaat faaliyetlerine özgü ani ve beklenmedik sebeplerle ortaya çıkacak hasarları güvence altına almak için düzenlenen bir poliçedir.'),
         ('Montaj', 'Montaj faaliyetlerinin başlangıcından bitimine kadar geçen süre içinde, montaj faaliyetlerine özgü ani ve beklenmedik sebeplerle ortaya çıkacak hasarlara karşı güvence sunan bir poliçedir.'),
         ('Elektronik cihaz', 'Elektronik eşyalarınızın beklenmedik nedenlerle uğradığı zararları poliçede belirtilen koşullara bağlı olarak temin eden sigorta poliçesidir.'),
         ('Makine kırılması', 'Makinelerinizi ani ve beklenmedik sebeplerle ortaya çıkmak kaydıyla, poliçede belirtilen koşullara bağlı olarak temin eden sigorta poliçesidir.'),
         ('Nakliyat poliçeleri', 'Nakliyat Emtia Sigortası ile taşınabilecek herhangi bir yükün, onu taşımaya uygun denizyolu, havayolu, karayolu ve demiryolu nakil vasıtalarından biriyle bir yerden başka bir yere taşınması esnasında uğrayabileceği hasar ve kayıpları poliçede belirlenmiş genel ve özel şartlar kapsamında güvence altına alan sigorta türüdür.')]
    h = '<div class="defs">' + ''.join(f'<div class="def"><h3>{E(a)}</h3><p>{E(b)}</p></div>' for a, b in d)
    lis = ''.join(f'<li>{x}</li>' for x in ['Hekim sorumluluk', 'Mesleki sorumluluk', 'İşveren sorumluluk', '3. şahıs sorumluluk', 'Ürün sorumluluk', 'Doğalgaz tesisat sorumluluk', 'Tehlikeli maddeler sorumluluk'])
    return h + f'<div class="def"><h3>Sorumluluk poliçeleri</h3><ul class="ticks">{lis}</ul></div></div>'
pages.append(simple_page('diger', 'Diğer Sigortalar', None, [], extra=diger_extra, topic='Diğer sigorta ürünleri'))

# HAYATA DEVAM
def hayata_body(p):
    dis = ['Kanser', 'Böbrek yetmezliği', 'Organ Nakli (Kalp, Karaciğer, Akciğer, Pankreas)', 'Körlük', 'MS (Multiple Sklerosis)', 'Parkinson', 'Alzheimer', 'Yanık (3. Derece)', 'İşitme Kaybı', 'Kalp Kapakçığı Ameliyatı', 'Aort Ameliyatı', 'Uzuv Kaybı', 'Kalp Krizi']
    return (titlebar(p, 'Hayata Devam Sigortası') +
            f'<section class="sec"><div class="sec__in prose"><div class="media"><div><p class="lead">Aksigorta Hayata Devam Sigortası yaptırın, ciddi bir rahatsızlığa yakalanırsanız size dilediğiniz gibi kullanabileceğiniz 35.000 TL\'den başlayan tazminatlar ödeyelim.</p>'
            f'<p class="lead2">Siz hayatınıza kaldığınız yerden devam edin.</p></div><img src="{rel(p,"assets/img/hayata1.webp")}" width="600" height="556" alt="Hayata Devam Sigortası" loading="lazy"></div>'
            '<h4>Hayata Devam Sigortası’yla Hayat Devam Edecek!</h4>'
            '<p>Bu sigortayla kendinizi aşağıda sıralanan durum ve tehlikeli hastalıklara karşı güvence altına alırsınız ve böyle bir durum başınıza geldiğinde kenarda dilediğiniz gibi değerlendirebileceğiniz bir paranız bulunur. Bu sigortanın verdiği tazminatı istediğiniz şekilde değerlendirebilirsiniz. Hastalığınızla ilgili tedavi masraflarını karşılayabilir ya da çalışmaya ara vermek zorunda kalmanız halinde kendinizi ve ailenizi daha güvende hissetmek için bu parayı kullanabilirsiniz.</p>'
            '<p><strong>Hayata Devam Sigortası yaptırın, tehlikeli bir hastalığa yakalansanız da hayat kesintisiz devam etsin!</strong></p>'
            f'<div class="media media--rev"><img src="{rel(p,"assets/img/hayata2.webp")}" width="600" height="627" alt="Hayata Devam Sigortası teminat kapsamı" loading="lazy">'
            f'<ul class="ticks">{"".join(f"<li>{E(x)}</li>" for x in dis)}</ul></div></div></section>' + cta_panel('Hayata Devam Sigortası'))
pages.append(Page('hayata-devam-sigortasi', 'Hayata Devam Sigortası', hayata_body))

# TAMAMLAYICI SAGLIK
def tamam_body(p):
    feats = [('Yatarak Tedavi', 'Yatarak tedavileriniz %100 karşılanır. Yatarak tedaviler, belirtilen teminatlar, özel ve genel şartlar çerçevesinde sınırsız ve %100 olarak karşılanmaktadır. Cerrahi ve dahili yatışlar, yoğun bakım, kemoterapi, radyoterapi, diyaliz, kroner anjiyografi, küçük müdahale giderleri, standart tek kişilik özel oda, yemek ve bir kişilik refakatçi giderleri teminat altındadır.'),
             ('Ayakta Tedavi / Muayene', 'Özel ve genel şartlar çerçevesinde yılda 10 vaka ile sınırlı olup %100 olarak karşılanmaktadır. Doktor muayene, laboratuvar hizmetleri, görüntüleme ve tanı hizmetleri, ileri tanı yöntemleri ve fizik tedavi giderleri teminat altındadır.'),
             ('Ayda 30TL\'den Başlayan Fiyatlarla', 'Özel Hastanelerde, SGK Farkı Ödemeden, Prosedür Olmadan Rahatlıkla Tedavi Olun. Tamamlayıcı Sağlık Sigortası sahipleri, özel hastaneye gittiklerinde ayakta veya yatarak tedavilerinde hiçbir ücret ödemiyor.* Ayrıca SGK’lılara uygulanan ek ücret yok. Yapmanız gereken anlaşmalı hastanelerimize giderek tedavi olmak. Tamamlayıcı Sağlık Sigortası’nı kullanmak için hiçbir prosedür gerekmez.')]
    fh = ''.join(f'<div class="feat"><span class="feat__n">{ic("check")}</span><div><h3>{E(a)}</h3><p>{E(b)}</p></div></div>' for a, b in feats)
    form = contact_buttons('Tamamlayıcı Sağlık Sigortası', 'actions--light actions--stack')
    return (titlebar(p, 'Tamamlayıcı Sağlık Sigortası') +
            f'<section class="sec"><div class="sec__in prose"><div class="banner"><img src="{rel(p,"assets/img/tamamlayici.webp")}" width="1200" height="400" alt="Tamamlayıcı Sağlık Sigortası"></div>'
            f'<h2>Tamamlayıcı Sağlık Sigortası</h2><div class="feats">{fh}</div>'
            '<p class="small">* SGK’nın yasası gereği sigortalılardan özel hastanelerde alınması zorunlu olan doktor muayene fark ücreti yine yasa gereği bu ürüne konu edilememektedir. Bugün için bu tutar 15 TL olup SGK tarafından değiştirilebilir. Bunun dışında bir katılım söz konusu değildir.</p></div></section>'
            f'<section class="sec sec--alt"><div class="sec__in"><div class="split split--offer"><div class="offer__img"><img src="{rel(p,"assets/img/sagligim-tamam.webp")}" width="600" height="600" alt="Sağlığım Tamam" loading="lazy"></div>'
            f'<div><h2 class="h-left">Fiyat İste</h2><p>Size özel fiyat teklifini almak için bizi arayabilir, WhatsApp iletişim hattından veya e-posta ile bize ulaşabilirsiniz.</p>{form}</div></div></div></section>')
pages.append(Page('tamamlayici-saglik-sigortasi', 'Tamamlayıcı Sağlık Sigortası', tamam_body))

# SIGORTA HATIRLATMA
def hatirlat_body(p):
    form = contact_buttons('Sigorta hatırlatma (poliçe bitiş tarihi hatırlatması)', 'actions--light actions--stack')
    return (titlebar(p, 'Sigorta Hatırlatma') +
            f'<section class="sec"><div class="sec__in narrow"><p>Trafik ve kasko poliçenizin bitiş tarihini unutmayın! Adınızı, plakanızı ve telefon numaranızı bize bildirin, poliçeniz bitmeden önce sizi bilgilendirelim.</p>{form}</div></section>')
pages.append(Page('sigorta-hatirlatma', 'Sigorta Hatırlatma', hatirlat_body, nav_cur='__none__'))

# 404
def body404(p):
    return (f'<section class="sec"><div class="sec__in center nf"><h1>404</h1><p>Aradığınız sayfa bulunamadı.</p>'
            f'<p><a class="btn btn--line" href="/">Anasayfaya dön</a></p></div></section>')

# ---------------------------------------------------------------- write
def main():
    global ASSET_V
    h = hashlib.md5()
    for f in ('css/style.css', 'js/main.js'):
        h.update(open(os.path.join(OUT, f), 'rb').read())
    ASSET_V = h.hexdigest()[:8]
    for p in pages:
        d = os.path.join(OUT, p.slug) if p.slug else OUT
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf8').write(render(p))
    # 404 with absolute paths
    html404 = render(Page('', 'Sayfa bulunamadı', body404, nav_cur='__none__'))
    html404 = html404.replace('<title>Muğla Yerel Sigorta | Sigorta Acentesi</title>', '<title>Sayfa bulunamadı | Muğla Yerel Sigorta</title>')
    html404 = html404.replace('<head>', '<head><meta name="robots" content="noindex"><base href="/">', 1)
    html404 = html404.replace('<link rel="canonical" href="https://www.yerelsigorta.com/">', '')
    open(os.path.join(OUT, '404.html'), 'w', encoding='utf8').write(html404)
    urls = [DOMAIN + '/' + (p.slug + '/' if p.slug else '') for p in pages]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{u}</loc></url>\n' for u in urls) + '</urlset>\n'
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write(sm)
    open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n')
    open(os.path.join(OUT, 'CNAME'), 'w').write('www.yerelsigorta.com\n')
    open(os.path.join(OUT, '.nojekyll'), 'w').write('')
    print('built', len(pages), 'pages, v', ASSET_V)

if __name__ == '__main__':
    main()
