#!/usr/bin/env python3
"""Patch language-specific meta tags into each lang/image-to-base64.html for encodeb64."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

META = {
    'en': {
        'title':      'Image to Base64 Converter — Free Online Tool | encodeb64.com',
        'desc_full':  'Free online image to Base64 converter. Convert JPG, PNG, GIF, WebP, SVG and more to Base64 instantly — right in your browser. No uploads, 100% private.',
        'desc_short': 'Free online image to Base64 converter. Convert JPG, PNG, GIF, WebP, SVG and more to Base64 instantly. No uploads, 100% private.',
        'locale':     'en_US',
        'img_alt':    'Image to Base64 Converter on encodeb64.com',
    },
    'es': {
        'title':      'Convertidor de Imagen a Base64 — Herramienta Gratuita | encodeb64.com',
        'desc_full':  'Convertidor online gratuito de imagen a Base64. Convierte JPG, PNG, GIF, WebP, SVG y más a Base64 al instante — en tu navegador. Sin subidas, 100% privado.',
        'desc_short': 'Convertidor online gratuito de imagen a Base64. Convierte JPG, PNG, GIF, WebP, SVG y más al instante. Sin subidas, 100% privado.',
        'locale':     'es_ES',
        'img_alt':    'Convertidor de Imagen a Base64 en encodeb64.com',
    },
    'pt': {
        'title':      'Conversor de Imagem para Base64 — Ferramenta Gratuita | encodeb64.com',
        'desc_full':  'Conversor online gratuito de imagem para Base64. Converta JPG, PNG, GIF, WebP, SVG e mais para Base64 instantaneamente — no seu navegador. Sem uploads, 100% privado.',
        'desc_short': 'Conversor online gratuito de imagem para Base64. Converta JPG, PNG, GIF, WebP, SVG e mais instantaneamente. Sem uploads, 100% privado.',
        'locale':     'pt_BR',
        'img_alt':    'Conversor de Imagem para Base64 em encodeb64.com',
    },
    'fr': {
        'title':      "Convertisseur Image en Base64 — Outil Gratuit | encodeb64.com",
        'desc_full':  "Convertisseur en ligne gratuit d'image en Base64. Convertissez JPG, PNG, GIF, WebP, SVG et plus en Base64 instantanément — dans votre navigateur. Sans upload, 100% privé.",
        'desc_short': "Convertisseur en ligne gratuit d'image en Base64. Convertissez JPG, PNG, GIF, WebP, SVG et plus instantanément. Sans upload, 100% privé.",
        'locale':     'fr_FR',
        'img_alt':    'Convertisseur Image en Base64 sur encodeb64.com',
    },
    'de': {
        'title':      'Bild zu Base64 Konverter — Kostenloses Online-Tool | encodeb64.com',
        'desc_full':  'Kostenloser Online-Konverter von Bild zu Base64. JPG, PNG, GIF, WebP, SVG und mehr sofort in Base64 konvertieren — im Browser. Kein Upload, 100% privat.',
        'desc_short': 'Kostenloser Online-Konverter von Bild zu Base64. JPG, PNG, GIF, WebP, SVG sofort konvertieren. Kein Upload, 100% privat.',
        'locale':     'de_DE',
        'img_alt':    'Bild zu Base64 Konverter auf encodeb64.com',
    },
    'it': {
        'title':      'Convertitore Immagine in Base64 — Strumento Gratuito | encodeb64.com',
        'desc_full':  'Convertitore online gratuito da immagine a Base64. Converti JPG, PNG, GIF, WebP, SVG e altri in Base64 istantaneamente — nel browser. Nessun upload, 100% privato.',
        'desc_short': 'Convertitore online gratuito da immagine a Base64. Converti JPG, PNG, GIF, WebP, SVG istantaneamente. Nessun upload, 100% privato.',
        'locale':     'it_IT',
        'img_alt':    'Convertitore Immagine in Base64 su encodeb64.com',
    },
    'zh': {
        'title':      '图片转Base64编码器 — 免费在线工具 | encodeb64.com',
        'desc_full':  '免费在线图片转Base64工具。即时将 JPG、PNG、GIF、WebP、SVG 等转换为 Base64 — 完全在浏览器中完成。无需上传，100% 私密。',
        'desc_short': '免费在线图片转Base64工具。即时将 JPG、PNG、GIF、WebP、SVG 等转换为 Base64。无需上传，100% 私密。',
        'locale':     'zh_CN',
        'img_alt':    'encodeb64.com 图片转Base64工具',
    },
    'ru': {
        'title':      'Конвертер изображений в Base64 — Бесплатный инструмент | encodeb64.com',
        'desc_full':  'Бесплатный онлайн-конвертер изображений в Base64. Конвертируйте JPG, PNG, GIF, WebP, SVG и другие в Base64 мгновенно — в браузере. Без загрузок, 100% конфиденциально.',
        'desc_short': 'Бесплатный онлайн-конвертер изображений в Base64. Конвертируйте JPG, PNG, GIF, WebP, SVG мгновенно. Без загрузок, 100% конфиденциально.',
        'locale':     'ru_RU',
        'img_alt':    'Конвертер изображений в Base64 на encodeb64.com',
    },
}

EN_TITLE     = 'Image to Base64 Converter — Free Online Tool | encodeb64.com'
EN_DESC_FULL = 'Free online image to Base64 converter. Convert JPG, PNG, GIF, WebP, SVG and more to Base64 instantly — right in your browser. No uploads, 100% private.'
EN_DESC_TW   = 'Free online image to Base64 converter. Convert JPG, PNG, GIF, WebP, SVG and more to Base64 instantly. No uploads, 100% private.'


def old_block(lang):
    url = f'https://encodeb64.com/{lang}/image-to-base64.html'
    return (
        f'  <meta property="og:title" content="{EN_TITLE}" />\n'
        f'  <meta property="og:description" content="{EN_DESC_FULL}" />\n'
        f'  <meta property="og:url" content="{url}" />\n'
        f'  <meta property="og:type" content="website" />\n'
        f'  <meta property="og:image" content="https://encodeb64.com/og-image.png" />\n'
        f'  <meta name="twitter:card" content="summary_large_image" />\n'
        f'  <meta name="twitter:title" content="{EN_TITLE}" />\n'
        f'  <meta name="twitter:description" content="{EN_DESC_TW}" />'
    )


def new_block(lang, m):
    url = f'https://encodeb64.com/{lang}/image-to-base64.html'
    return (
        f'  <meta property="og:locale" content="{m["locale"]}" />\n'
        f'  <meta property="og:type" content="website" />\n'
        f'  <meta property="og:site_name" content="encodeb64.com" />\n'
        f'  <meta property="og:title" content="{m["title"]}" />\n'
        f'  <meta property="og:description" content="{m["desc_short"]}" />\n'
        f'  <meta property="og:url" content="{url}" />\n'
        f'  <meta property="og:image" content="https://encodeb64.com/og-image.png" />\n'
        f'  <meta property="og:image:secure_url" content="https://encodeb64.com/og-image.png" />\n'
        f'  <meta property="og:image:alt" content="{m["img_alt"]}" />\n'
        f'  <meta property="og:image:width" content="1200" />\n'
        f'  <meta property="og:image:height" content="630" />\n'
        f'  <meta name="twitter:card" content="summary_large_image" />\n'
        f'  <meta name="twitter:title" content="{m["title"]}" />\n'
        f'  <meta name="twitter:description" content="{m["desc_short"]}" />\n'
        f'  <meta name="twitter:image" content="https://encodeb64.com/og-image.png" />\n'
        f'  <meta name="twitter:image:alt" content="{m["img_alt"]}" />'
    )


def patch(s, lang):
    m = META[lang]
    s = s.replace(
        f'<title>{EN_TITLE}</title>',
        f'<title>{m["title"]}</title>',
        1
    )
    s = s.replace(
        f'<meta name="description" content="{EN_DESC_FULL}" />',
        f'<meta name="description" content="{m["desc_full"]}" />',
        1
    )
    old = old_block(lang)
    new = new_block(lang, m)
    if old not in s:
        raise ValueError(f'[{lang}] og/twitter block not found')
    s = s.replace(old, new, 1)
    return s


ES_OLD_TITLE   = 'Codificador Base64 Online — Codifica texto, archivos e imágenes'
ES_OLD_DESC    = 'Convertidor gratuito de imágenes a Base64 en línea. Convierte JPG, PNG, GIF, WebP, SVG y más a Base64 al instante, directamente en tu navegador. Sin necesidad de subir archivos, 100% privado.'
ES_OLD_OG_BLOCK = (
    '  <meta property="og:locale" content="es_ES" />\n'
    '  <meta property="og:type" content="website" />\n'
    '  <meta property="og:site_name" content="encodeb64.com" />\n'
    '  <meta property="og:title" content="Convertidor de imágenes a Base64: herramienta online gratuita | encodeb64.com" />\n'
    '  <meta property="og:description" content="Convertidor gratuito de imágenes a Base64 en línea. Convierte JPG, PNG, GIF, WebP, SVG y más a Base64 al instante, directamente en tu navegador. Sin necesidad de subir archivos, 100% privado." />\n'
    '  <meta property="og:url" content="https://encodeb64.com/es/image-to-base64.html" />\n'
    '  <meta property="og:type" content="website" />\n'
    '  <meta property="og:image" content="https://encodeb64.com/og-image.png" />\n'
    '  <meta name="twitter:card" content="summary_large_image" />\n'
    '  <meta name="twitter:title" content="Convertidor de imágenes a Base64: herramienta online gratuita | encodeb64.com" />\n'
    '  <meta name="twitter:description" content="Convertidor gratuito de imágenes a Base64 en línea. Convierte JPG, PNG, GIF, WebP, SVG y más a Base64 al instante. Sin necesidad de subir archivos, 100% privado." />'
)


def patch_es(s):
    m = META['es']
    s = s.replace(f'<title>{ES_OLD_TITLE}</title>', f'<title>{m["title"]}</title>', 1)
    s = s.replace(
        f'<meta name="description" content="{ES_OLD_DESC}" />',
        f'<meta name="description" content="{m["desc_full"]}" />',
        1
    )
    if ES_OLD_OG_BLOCK not in s:
        raise ValueError('[es] og/twitter block not found — check source')
    s = s.replace(ES_OLD_OG_BLOCK, new_block('es', m), 1)
    return s


LANGS = ['pt', 'fr', 'de', 'it', 'zh', 'ru']

for lang in LANGS:
    path = os.path.join(BASE, lang, 'image-to-base64.html')
    with open(path, encoding='utf-8') as f:
        src = f.read()
    result = patch(src, lang)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f'OK  {lang}/image-to-base64.html')

# es was manually edited — patch separately
es_path = os.path.join(BASE, 'es', 'image-to-base64.html')
with open(es_path, encoding='utf-8') as f:
    src = f.read()
result = patch_es(src)
with open(es_path, 'w', encoding='utf-8') as f:
    f.write(result)
print('OK  es/image-to-base64.html')

print('Done.')
