#!/usr/bin/env python3
"""Generate language-specific HTML files for encodeb64.com."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
LANGS = ['en', 'es', 'pt', 'fr', 'de', 'it', 'zh', 'ru']


def assert_replaced(src, old, new, label):
    if old not in src:
        raise ValueError(f"String not found [{label}]: {old[:80]!r}")
    return src.replace(old, new, 1)


# ── INDEX.HTML ──────────────────────────────────────────────────────────────

with open(os.path.join(BASE, 'index.html'), encoding='utf-8') as f:
    INDEX_SRC = f.read()

HREFLANG_OLD_INDEX = (
    '  <link rel="alternate" hreflang="en" href="https://encodeb64.com/" />\n'
    '  <link rel="alternate" hreflang="es" href="https://encodeb64.com/es/" />\n'
    '  <link rel="alternate" hreflang="pt" href="https://encodeb64.com/pt/" />\n'
    '  <link rel="alternate" hreflang="fr" href="https://encodeb64.com/fr/" />\n'
    '  <link rel="alternate" hreflang="de" href="https://encodeb64.com/de/" />\n'
    '  <link rel="alternate" hreflang="it" href="https://encodeb64.com/it/" />\n'
    '  <link rel="alternate" hreflang="ru" href="https://encodeb64.com/ru/" />\n'
    '  <link rel="alternate" hreflang="zh" href="https://encodeb64.com/zh/" />\n'
    '  <link rel="alternate" hreflang="x-default" href="https://encodeb64.com/" />'
)

HREFLANG_NEW_INDEX = (
    '  <link rel="alternate" hreflang="en" href="https://encodeb64.com/en/" />\n'
    '  <link rel="alternate" hreflang="es" href="https://encodeb64.com/es/" />\n'
    '  <link rel="alternate" hreflang="pt" href="https://encodeb64.com/pt/" />\n'
    '  <link rel="alternate" hreflang="fr" href="https://encodeb64.com/fr/" />\n'
    '  <link rel="alternate" hreflang="de" href="https://encodeb64.com/de/" />\n'
    '  <link rel="alternate" hreflang="it" href="https://encodeb64.com/it/" />\n'
    '  <link rel="alternate" hreflang="ru" href="https://encodeb64.com/ru/" />\n'
    '  <link rel="alternate" hreflang="zh" href="https://encodeb64.com/zh/" />\n'
    '  <link rel="alternate" hreflang="x-default" href="https://encodeb64.com/" />'
)

LANGDROP_OLD_INDEX = (
    'langDropdown.addEventListener(\'click\', (e) => {\n'
    '  const opt = e.target.closest(\'.lang-option\');\n'
    '  if (opt) {\n'
    '    applyLang(opt.dataset.lang);\n'
    '    langDropdown.classList.remove(\'open\');\n'
    '  }\n'
    '});'
)

LANGDROP_NEW_INDEX = (
    'langDropdown.addEventListener(\'click\', (e) => {\n'
    '  const opt = e.target.closest(\'.lang-option\');\n'
    '  if (opt) {\n'
    '    const sel = opt.dataset.lang;\n'
    '    localStorage.setItem(\'b64_lang\', sel);\n'
    '    window.location.href = \'/\' + sel + \'/\';\n'
    '  }\n'
    '});'
)


def gen_index(lang):
    s = INDEX_SRC

    s = assert_replaced(s, '<html lang="en">', f'<html lang="{lang}">', 'html lang')
    s = assert_replaced(s,
        '<link rel="canonical" href="https://encodeb64.com/" />',
        f'<link rel="canonical" href="https://encodeb64.com/{lang}/" />',
        'canonical')
    s = assert_replaced(s, HREFLANG_OLD_INDEX, HREFLANG_NEW_INDEX, 'hreflang block')
    s = assert_replaced(s,
        '<meta property="og:url" content="https://encodeb64.com/" />',
        f'<meta property="og:url" content="https://encodeb64.com/{lang}/" />',
        'og:url')
    s = assert_replaced(s, '<a href="/" class="logo">', '<a href="./" class="logo">', 'logo href')
    s = assert_replaced(s,
        '<a href="/image-to-base64" class="nav-pill inactive" data-i18n="nav_image">Image to Base64</a>',
        '<a href="image-to-base64.html" class="nav-pill inactive" data-i18n="nav_image">Image to Base64</a>',
        'nav image href')
    s = assert_replaced(s,
        "let currentLang = localStorage.getItem('b64_lang') || 'en';",
        f"const pageLang = '{lang}'; let currentLang = pageLang;",
        'currentLang')
    s = assert_replaced(s,
        'function applyLang(lang) {\n  const t = T[lang] || T[\'en\'];',
        'function applyLang(lang) {\n  document.documentElement.lang = lang;\n  const t = T[lang] || T[\'en\'];',
        'applyLang docLang')
    s = assert_replaced(s, LANGDROP_OLD_INDEX, LANGDROP_NEW_INDEX, 'langDropdown handler')
    s = assert_replaced(s,
        '"url": "https://encodeb64.com/",',
        f'"url": "https://encodeb64.com/{lang}/",',
        'jsonld url')

    return s


# ── IMAGE-TO-BASE64.HTML ─────────────────────────────────────────────────────

with open(os.path.join(BASE, 'image-to-base64.html'), encoding='utf-8') as f:
    IMG_SRC = f.read()

HREFLANG_OLD_IMG = (
    '  <link rel="alternate" hreflang="en" href="https://encodeb64.com/image-to-base64" />\n'
    '  <link rel="alternate" hreflang="es" href="https://encodeb64.com/image-to-base64" />\n'
    '  <link rel="alternate" hreflang="pt" href="https://encodeb64.com/image-to-base64" />\n'
    '  <link rel="alternate" hreflang="fr" href="https://encodeb64.com/image-to-base64" />\n'
    '  <link rel="alternate" hreflang="de" href="https://encodeb64.com/image-to-base64" />\n'
    '  <link rel="alternate" hreflang="it" href="https://encodeb64.com/image-to-base64" />\n'
    '  <link rel="alternate" hreflang="zh" href="https://encodeb64.com/image-to-base64" />\n'
    '  <link rel="alternate" hreflang="ru" href="https://encodeb64.com/image-to-base64" />\n'
    '  <link rel="alternate" hreflang="x-default" href="https://encodeb64.com/image-to-base64" />'
)

HREFLANG_NEW_IMG = (
    '  <link rel="alternate" hreflang="en" href="https://encodeb64.com/en/image-to-base64.html" />\n'
    '  <link rel="alternate" hreflang="es" href="https://encodeb64.com/es/image-to-base64.html" />\n'
    '  <link rel="alternate" hreflang="pt" href="https://encodeb64.com/pt/image-to-base64.html" />\n'
    '  <link rel="alternate" hreflang="fr" href="https://encodeb64.com/fr/image-to-base64.html" />\n'
    '  <link rel="alternate" hreflang="de" href="https://encodeb64.com/de/image-to-base64.html" />\n'
    '  <link rel="alternate" hreflang="it" href="https://encodeb64.com/it/image-to-base64.html" />\n'
    '  <link rel="alternate" hreflang="zh" href="https://encodeb64.com/zh/image-to-base64.html" />\n'
    '  <link rel="alternate" hreflang="ru" href="https://encodeb64.com/ru/image-to-base64.html" />\n'
    '  <link rel="alternate" hreflang="x-default" href="https://encodeb64.com/image-to-base64" />'
)

LANGDROP_OLD_IMG = (
    "document.querySelectorAll('.lang-option').forEach(opt => {\n"
    "  opt.addEventListener('click', (e) => {\n"
    "    e.stopPropagation();\n"
    "    applyLang(opt.dataset.lang);\n"
    "    langDropdown.classList.remove('open');\n"
    "    langBtn.setAttribute('aria-expanded', 'false');\n"
    "    document.body.classList.add('lang-transition');\n"
    "    setTimeout(() => document.body.classList.remove('lang-transition'), 150);\n"
    "  });\n"
    "});"
)

LANGDROP_NEW_IMG = (
    "document.querySelectorAll('.lang-option').forEach(opt => {\n"
    "  opt.addEventListener('click', (e) => {\n"
    "    e.stopPropagation();\n"
    "    const sel = opt.dataset.lang;\n"
    "    localStorage.setItem('b64_lang', sel);\n"
    "    window.location.href = '/' + sel + '/image-to-base64.html';\n"
    "  });\n"
    "});"
)

INIT_OLD_IMG = (
    '// ─── INIT ───────────────────────────────────────────────────────────────────────\n'
    '(function init() {\n'
    '  const saved = localStorage.getItem(\'b64_lang\');\n'
    '  if (saved && T[saved]) {\n'
    '    applyLang(saved);\n'
    '  } else {\n'
    "    applyLang('en');\n"
    '  }\n'
    '})();'
)

INIT_NEW_IMG = (
    '// ─── INIT ───────────────────────────────────────────────────────────────────────\n'
    'applyLang(currentLang);'
)


def gen_img(lang):
    s = IMG_SRC

    s = assert_replaced(s, '<html lang="en">', f'<html lang="{lang}">', 'html lang')
    s = assert_replaced(s,
        '<link rel="canonical" href="https://encodeb64.com/image-to-base64" />',
        f'<link rel="canonical" href="https://encodeb64.com/{lang}/image-to-base64.html" />',
        'canonical')
    s = assert_replaced(s, HREFLANG_OLD_IMG, HREFLANG_NEW_IMG, 'hreflang block')
    s = assert_replaced(s,
        '<meta property="og:url" content="https://encodeb64.com/image-to-base64" />',
        f'<meta property="og:url" content="https://encodeb64.com/{lang}/image-to-base64.html" />',
        'og:url')
    # Replace all href="https://encodeb64.com" anchor hrefs with "./"
    s = s.replace('href="https://encodeb64.com"', 'href="./"')
    s = assert_replaced(s,
        "let currentLang = 'en';",
        f"const pageLang = '{lang}'; let currentLang = pageLang;",
        'currentLang')
    s = assert_replaced(s,
        'function applyLang(lang) {\n  currentLang = lang;\n  localStorage.setItem(\'b64_lang\', lang);',
        'function applyLang(lang) {\n  document.documentElement.lang = lang;\n  currentLang = lang;\n  localStorage.setItem(\'b64_lang\', lang);',
        'applyLang docLang')
    s = assert_replaced(s, LANGDROP_OLD_IMG, LANGDROP_NEW_IMG, 'langDropdown handler')
    s = assert_replaced(s, INIT_OLD_IMG, INIT_NEW_IMG, 'init block')
    s = assert_replaced(s,
        '"url": "https://encodeb64.com/image-to-base64",',
        f'"url": "https://encodeb64.com/{lang}/image-to-base64.html",',
        'jsonld url')

    return s


# ── WRITE FILES ──────────────────────────────────────────────────────────────

for lang in LANGS:
    lang_dir = os.path.join(BASE, lang)
    os.makedirs(lang_dir, exist_ok=True)

    idx_path = os.path.join(lang_dir, 'index.html')
    with open(idx_path, 'w', encoding='utf-8') as f:
        f.write(gen_index(lang))
    print(f'OK  {lang}/index.html')

    img_path = os.path.join(lang_dir, 'image-to-base64.html')
    with open(img_path, 'w', encoding='utf-8') as f:
        f.write(gen_img(lang))
    print(f'OK  {lang}/image-to-base64.html')

print('Done.')
