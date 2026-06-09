#!/usr/bin/env python3
"""Patch language-specific meta tags into each lang/index.html for encodeb64."""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

# ── PER-LANGUAGE META DATA ────────────────────────────────────────────────────
# title      = <title> tag + og:title + twitter:title
# desc_full  = <meta name="description"> (longer)
# desc_short = og:description + twitter:description (shorter)
# locale     = og:locale
# img_alt    = og:image:alt + twitter:image:alt

META = {
    'en': {
        'title':      'Base64 Encoder Online — Encode Text, Files & Images',
        'desc_full':  'Free online Base64 encoder for text, files, and images. UTF-8 perfect, Base64URL safe, up to 100MB, no server upload, 100% private.',
        'desc_short': 'Free online Base64 encoder for text, files, and images. UTF-8 perfect, Base64URL safe, up to 100MB, no server upload, 100% private.',
        'locale':     'en_US',
        'img_alt':    'Base64 Encoder Online on encodeb64.com',
    },
    'es': {
        'title':      'Codificador Base64 Online — Codifica texto, archivos e imágenes',
        'desc_full':  'Codificador Base64 online gratis para texto, archivos e imágenes. Compatible con UTF-8, Base64URL, hasta 100MB, sin subir datos al servidor y 100% privado.',
        'desc_short': 'Codificador Base64 online gratis para texto, archivos e imágenes. Compatible con UTF-8, Base64URL, hasta 100MB y 100% privado.',
        'locale':     'es_ES',
        'img_alt':    'Codificador Base64 Online en encodeb64.com',
    },
    'pt': {
        'title':      'Codificador Base64 Online — Codifique Texto, Arquivos e Imagens',
        'desc_full':  'Codificador Base64 online gratuito para texto, arquivos e imagens. UTF-8 perfeito, Base64URL, até 100MB, sem upload ao servidor, 100% privado.',
        'desc_short': 'Codificador Base64 online gratuito para texto, arquivos e imagens. UTF-8 perfeito, Base64URL, até 100MB, 100% privado.',
        'locale':     'pt_BR',
        'img_alt':    'Codificador Base64 Online em encodeb64.com',
    },
    'fr': {
        'title':      'Encodeur Base64 en Ligne — Encodez Texte, Fichiers et Images',
        'desc_full':  "Encodeur Base64 en ligne gratuit pour texte, fichiers et images. UTF-8 parfait, Base64URL, jusqu'à 100 Mo, sans upload serveur, 100% privé.",
        'desc_short': "Encodeur Base64 en ligne gratuit pour texte, fichiers et images. UTF-8 parfait, Base64URL, jusqu'à 100 Mo, 100% privé.",
        'locale':     'fr_FR',
        'img_alt':    'Encodeur Base64 en Ligne sur encodeb64.com',
    },
    'de': {
        'title':      'Base64 Encoder Online — Text, Dateien & Bilder kodieren',
        'desc_full':  'Kostenloser Online-Base64-Encoder für Text, Dateien und Bilder. UTF-8 perfekt, Base64URL, bis zu 100 MB, kein Server-Upload, 100% privat.',
        'desc_short': 'Kostenloser Online-Base64-Encoder für Text, Dateien und Bilder. UTF-8 perfekt, Base64URL, bis zu 100 MB, 100% privat.',
        'locale':     'de_DE',
        'img_alt':    'Base64 Encoder Online auf encodeb64.com',
    },
    'it': {
        'title':      'Codificatore Base64 Online — Codifica Testo, File e Immagini',
        'desc_full':  'Codificatore Base64 online gratuito per testo, file e immagini. UTF-8 perfetto, Base64URL, fino a 100 MB, nessun upload al server, 100% privato.',
        'desc_short': 'Codificatore Base64 online gratuito per testo, file e immagini. UTF-8 perfetto, Base64URL, fino a 100 MB, 100% privato.',
        'locale':     'it_IT',
        'img_alt':    'Codificatore Base64 Online su encodeb64.com',
    },
    'zh': {
        'title':      'Base64 在线编码器 — 编码文本、文件和图片',
        'desc_full':  '免费在线 Base64 编码器，支持文本、文件和图片。UTF-8 完美，支持 Base64URL，最大 100MB，无需上传至服务器，100% 私密。',
        'desc_short': '免费在线 Base64 编码器，支持文本、文件和图片。UTF-8 完美，支持 Base64URL，最大 100MB，100% 私密。',
        'locale':     'zh_CN',
        'img_alt':    'encodeb64.com Base64 在线编码器',
    },
    'ru': {
        'title':      'Кодировщик Base64 Онлайн — Кодирование текста, файлов и изображений',
        'desc_full':  'Бесплатный онлайн-кодировщик Base64 для текста, файлов и изображений. UTF-8 идеально, Base64URL, до 100 МБ, без загрузки на сервер, 100% приватно.',
        'desc_short': 'Бесплатный онлайн-кодировщик Base64 для текста, файлов и изображений. UTF-8 идеально, Base64URL, до 100 МБ, 100% приватно.',
        'locale':     'ru_RU',
        'img_alt':    'Кодировщик Base64 Онлайн на encodeb64.com',
    },
}

# The common English values present in all generated (non-es) files
EN_TITLE      = 'Base64 Encoder Online — Encode Text, Files & Images'
EN_DESC       = 'Free online Base64 encoder for text, files, and images. UTF-8 perfect, Base64URL safe, up to 100MB, no server upload, 100% private.'
EN_LOCALE     = 'en_US'
EN_IMG_ALT    = 'Base64 Encoder Online on encodeb64.com'


def patch(s, lang):
    m = META[lang]

    # <title>
    s = s.replace(
        f'<title>{EN_TITLE}</title>',
        f'<title>{m["title"]}</title>',
        1
    )
    # <meta name="description">
    s = s.replace(
        f'<meta name="description" content="{EN_DESC}" />',
        f'<meta name="description" content="{m["desc_full"]}" />',
        1
    )
    # og:locale
    s = s.replace(
        f'<meta property="og:locale" content="{EN_LOCALE}" />',
        f'<meta property="og:locale" content="{m["locale"]}" />',
        1
    )
    # og:title
    s = s.replace(
        f'<meta property="og:title" content="{EN_TITLE}" />',
        f'<meta property="og:title" content="{m["title"]}" />',
        1
    )
    # og:description
    s = s.replace(
        f'<meta property="og:description" content="{EN_DESC}" />',
        f'<meta property="og:description" content="{m["desc_short"]}" />',
        1
    )
    # og:image:alt
    s = s.replace(
        f'<meta property="og:image:alt" content="{EN_IMG_ALT}" />',
        f'<meta property="og:image:alt" content="{m["img_alt"]}" />',
        1
    )
    # twitter:title
    s = s.replace(
        f'<meta name="twitter:title" content="{EN_TITLE}" />',
        f'<meta name="twitter:title" content="{m["title"]}" />',
        1
    )
    # twitter:description
    s = s.replace(
        f'<meta name="twitter:description" content="{EN_DESC}" />',
        f'<meta name="twitter:description" content="{m["desc_short"]}" />',
        1
    )
    # twitter:image:alt
    s = s.replace(
        f'<meta name="twitter:image:alt" content="{EN_IMG_ALT}" />',
        f'<meta name="twitter:image:alt" content="{m["img_alt"]}" />',
        1
    )

    return s


def patch_es(s):
    """es was manually edited: only fix desc/locale mismatch and add twitter:image:alt."""
    m = META['es']
    # Fix og:locale if still en_US (shouldn't be, but guard)
    s = s.replace('content="en_US"', 'content="es_ES"', 1)
    # Add twitter:image:alt after twitter:image if missing
    tw_img = '  <meta name="twitter:image" content="https://encodeb64.com/og-image.png" />'
    tw_alt = f'  <meta name="twitter:image:alt" content="{m["img_alt"]}" />'
    if tw_alt not in s:
        s = s.replace(tw_img, tw_img + '\n' + tw_alt, 1)
    return s


LANGS_TO_PATCH = ['pt', 'fr', 'de', 'it', 'zh', 'ru']

for lang in LANGS_TO_PATCH:
    path = os.path.join(BASE, lang, 'index.html')
    with open(path, encoding='utf-8') as f:
        src = f.read()
    result = patch(src, lang)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f'OK  {lang}/index.html')

# Fix es separately
es_path = os.path.join(BASE, 'es', 'index.html')
with open(es_path, encoding='utf-8') as f:
    src = f.read()
result = patch_es(src)
with open(es_path, 'w', encoding='utf-8') as f:
    f.write(result)
print(f'OK  es/index.html')

print('Done.')
