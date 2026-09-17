#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
xyecocPROJECT v11.2
Создатели: vobas25, mr iron, окак 67 (greencat), sakura.cc (sakuradev)
Главный: окак 67 (greencat)
Админы: vobas25, mr iron, dsfsfsdfsdfds
"""

import os, sys, json, math, time, hashlib, random, threading, webbrowser, socket
from tkinter import scrolledtext
from datetime import datetime

try:
    import tkinter as tk
except ImportError:
    print("tkinter не установлен!")
    sys.exit(1)

try:
    import requests
except ImportError:
    requests = None
try:
    import whois
except ImportError:
    whois = None
try:
    import dns.resolver
except ImportError:
    dns = None

BG_DARK = "#05080d"; BG_PANEL = "#0a1018"; BG_INPUT = "#0f1720"
ACCENT = "#00ff9f"; ACCENT2 = "#ff0040"; ACCENT3 = "#00b3ff"
ACCENT4 = "#b026ff"; TEXT = "#c8d6e5"; TEXT_DIM = "#5a6c80"; WARN = "#ffaa00"

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/120.0.0.0 Safari/537.36"}

USERS_FILE = os.path.join(os.path.expanduser("~"), ".xyecoc_users.json")
SESSION_FILE = os.path.join(os.path.expanduser("~"), ".xyecoc_session.json")
CHATS_FILE = os.path.join(os.path.expanduser("~"), ".xyecoc_chats.json")

LOGO = r"""██╗  ██╗██╗   ██╗███████╗ ██████╗ ██████╗  ██████╗ 
╚██╗██╔╝╚██╗ ██╔╝██╔════╝██╔════╝██╔═══██╗██╔════╝ 
 ╚███╔╝  ╚████╔╝ █████╗  ██║     ██║   ██║██║      
 ██╔██╗   ╚██╔╝  ██╔══╝  ██║     ██║   ██║██║      
██╔╝ ██╗   ██║   ███████╗╚██████╗╚██████╔╝╚██████╗ 
╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝ """


# ==================== СОГЛАШЕНИЕ ====================
class Agreement:
    @staticmethod
    def html_path():
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), "agreement.html")

    @staticmethod
    def generate_html():
        html = """<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8">
<title>xyecocPROJECT — Соглашение</title><style>
body{background:#05080d;color:#c8d6e5;font-family:Consolas,monospace;padding:40px;line-height:1.7}
.container{max-width:900px;margin:0 auto;background:rgba(10,16,24,0.85);border:1px solid #00b3ff;border-radius:8px;padding:50px 60px;box-shadow:0 0 40px rgba(0,255,159,0.15)}
h1{font-size:28px;color:#ff0040;text-align:center;text-shadow:0 0 15px rgba(255,0,64,0.6)}
.subtitle{text-align:center;color:#00b3ff;font-size:12px;letter-spacing:4px;margin-bottom:30px}
h2{color:#00ff9f;font-size:16px;margin:25px 0 12px;padding-left:12px;border-left:3px solid #00ff9f}
p{margin-bottom:12px;padding-left:15px}
ul{list-style:none;padding-left:30px;margin-bottom:15px}li{margin-bottom:6px}
li::before{content:'›';color:#00ff9f;margin-right:8px;font-weight:bold}
.team{background:rgba(0,255,159,0.05);border:1px dashed #00ff9f;border-radius:6px;padding:20px 25px;margin:15px 0}
.role{color:#ffaa00;font-weight:bold;margin-top:10px}.name{color:#00ff9f}
.ban{color:#ff0040;font-weight:bold;margin-right:6px}.allow{color:#00ff9f;font-weight:bold;margin-right:6px}
.footer{text-align:center;margin-top:40px;padding-top:20px;border-top:1px solid #1a212e;color:#5a6c80;font-size:12px}
.brand{color:#ff0040;font-size:14px;font-weight:bold;letter-spacing:3px;margin-bottom:8px}
.tagline{color:#00b3ff;font-style:italic;margin-top:5px}
.note{color:#ffaa00;font-style:italic;font-size:11px}
.accept{display:block;margin:35px auto 0;padding:15px 40px;background:transparent;border:2px solid #00ff9f;color:#00ff9f;font-family:Consolas,monospace;font-size:14px;font-weight:bold;letter-spacing:2px;cursor:pointer;border-radius:4px;text-transform:uppercase}
</style></head><body><div class="container">
<h1>xyecocPROJECT</h1><div class="subtitle">СОГЛАШЕНИЕ ПОЛЬЗОВАТЕЛЯ</div>
<h2>1. О ПРОЕКТЕ</h2><p><span style="color:#00ff9f">xyecocPROJECT</span> — OSINT-инструмент для поиска по открытым источникам. Образовательные цели.</p>
<h2>2. ГЛАВНОЕ ПРАВИЛО</h2><p style="color:#ff0040;font-weight:bold;font-size:16px">МЫ НЕ БУДЕМ НИЧЕГО СЛИВАТЬ.</p><p>Ищем что-то, а не распространяем чужую личную информацию.</p>
<h2>3. КОМАНДА</h2><div class="team">
<div class="role">СОЗДАТЕЛИ:</div><ul>
<li><span class="name">vobas25</span></li>
<li><span class="name">mr iron</span></li>
<li><span class="name">окак 67</span> (greencat)</li>
<li><span class="name">sakura.cc</span> (sakuradev) — Roblox-скрипты, инжекторы. <span class="note">Любимый участник. Проект не тестил.</span></li>
</ul>
<div class="role">ГЛАВНЫЙ:</div><ul><li><span class="name">окак 67</span> (greencat)</li></ul>
<div class="role">АДМИНЫ:</div><ul>
<li><span class="name">vobas25</span></li><li><span class="name">mr iron</span></li><li><span class="name">dsfsfsdfsdfds</span></li>
</ul></div>
<h2>4. ЗАПРЕЩЕНО</h2><ul>
<li><span class="ban">✗</span> Преследование, сталкерство, травля</li>
<li><span class="ban">✗</span> Незаконный сбор персональных данных</li>
<li><span class="ban">✗</span> Передача чужих данных третьим лицам</li>
<li><span class="ban">✗</span> Взлом, DDoS, мошенничество</li>
<li><span class="ban">✗</span> Кража авторства проекта</li>
</ul>
<h2>5. РАЗРЕШЕНО</h2><ul>
<li><span class="allow">✓</span> Self-OSINT (о себе)</li>
<li><span class="allow">✓</span> Проверка своих ресурсов</li>
<li><span class="allow">✓</span> Образовательные задачи</li>
<li><span class="allow">✓</span> Пентест по контракту</li>
</ul>
<h2>6. ОТВЕТСТВЕННОСТЬ</h2><p>Пользователь сам отвечает за использование.</p>
<h2>7. ДАННЫЕ</h2><p>Аккаунты — ЛОКАЛЬНО. Пароли — SHA256 с солью.</p>
<h2>8. ПРИНЯТИЕ</h2><p>Регистрируясь — ты согласен.</p>
<div class="footer"><div class="brand">xyecocPROJECT</div>
<div>© 2026 • vobas25 • mr iron • окак 67 (greencat) • sakura.cc (sakuradev) • dsfsfsdfsdfds</div>
<div class="tagline">no api • no mercy</div></div>
<button class="accept" onclick="window.close()">✓ Я ПРИНИМАЮ</button>
</div></body></html>"""
        with open(Agreement.html_path(), "w", encoding="utf-8") as f:
            f.write(html)
        return Agreement.html_path()

    @staticmethod
    def open_in_browser():
        webbrowser.open("file://" + Agreement.generate_html())


# ==================== ОТЧЁТ ПО ДОМЕНУ ====================
class DomainReport:
    @staticmethod
    def desktop_path():
        home = os.path.expanduser("~")
        for p in [os.path.join(home, "Desktop"), os.path.join(home, "Рабочий стол"),
                  os.path.join(home, "OneDrive", "Desktop"),
                  os.path.join(home, "OneDrive", "Рабочий стол")]:
            if os.path.isdir(p):
                return p
        return home

    @staticmethod
    def next_filename():
        desk = DomainReport.desktop_path()
        n = 1
        while True:
            fn = os.path.join(desk, f"XYECOC-создано_{n}.html")
            if not os.path.exists(fn):
                return fn, n
            n += 1

    @staticmethod
    def gather(domain):
        info = {"domain": domain, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "ip": [], "whois": {}, "dns": {}, "headers": {}, "ports": []}
        try:
            info["ip"] = socket.gethostbyname_ex(domain)[2]
        except Exception:
            pass
        if whois:
            try:
                w = whois.whois(domain)
                info["whois"] = {
                    "Домен": str(w.domain_name or ""),
                    "Регистратор": str(w.registrar or ""),
                    "Создан": str(w.creation_date or ""),
                    "Истекает": str(w.expiration_date or ""),
                    "NS": str(w.name_servers or ""),
                    "Emails": str(w.emails or ""),
                    "Страна": str(w.country or ""),
                }
            except Exception as e:
                info["whois"] = {"Ошибка": str(e)}
        if dns:
            for rtype in ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']:
                try:
                    records = [r.to_text() for r in dns.resolver.resolve(domain, rtype)]
                    if records:
                        info["dns"][rtype] = records
                except Exception:
                    pass
        if requests:
            for scheme in ("https", "http"):
                try:
                    r = requests.get(f"{scheme}://{domain}", timeout=8,
                                     headers=HEADERS, allow_redirects=True)
                    info["headers"] = {"URL": r.url, "Код": str(r.status_code)}
                    for k, v in r.headers.items():
                        info["headers"][k] = v
                    break
                except Exception:
                    continue
        for p in [21, 22, 23, 25, 53, 80, 110, 143, 443, 445,
                  3306, 3389, 5432, 5900, 6379, 8080, 8443, 27017]:
            try:
                s = socket.socket()
                s.settimeout(0.6)
                if s.connect_ex((domain, p)) == 0:
                    try:
                        svc = socket.getservbyport(p)
                    except Exception:
                        svc = "?"
                    info["ports"].append((p, svc))
                s.close()
            except Exception:
                pass
        return info

    @staticmethod
    def generate_html(info):
        path, num = DomainReport.next_filename()
        ip_html = "".join(f"<li>{ip}</li>" for ip in info["ip"]) or "<li>нет</li>"
        whois_html = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>"
                             for k, v in info["whois"].items()) or "<tr><td>нет</td></tr>"
        dns_html = "".join(f"<tr><td><b>{t}</b></td><td>{'<br>'.join(r)}</td></tr>"
                           for t, r in info["dns"].items()) or "<tr><td>нет</td></tr>"
        headers_html = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>"
                               for k, v in info["headers"].items()) or "<tr><td>нет</td></tr>"
        ports_html = "".join(f"<li><span style='color:#00ff9f;font-weight:bold'>ОТКРЫТ</span> {p} → {s}</li>"
                             for p, s in info["ports"]) or "<li>нет</li>"
        html = f"""<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8">
<title>XYECOC-создано_{num} — {info['domain']}</title><style>
body{{background:#05080d;color:#c8d6e5;font-family:Consolas,monospace;padding:40px;line-height:1.6}}
.container{{max-width:1000px;margin:0 auto;background:rgba(10,16,24,0.9);border:1px solid #00b3ff;border-radius:8px;padding:40px 50px;box-shadow:0 0 40px rgba(0,255,159,0.15)}}
h1{{color:#ff0040;font-size:24px;text-align:center;text-shadow:0 0 15px rgba(255,0,64,0.6)}}
.subtitle{{color:#00b3ff;font-size:12px;text-align:center;letter-spacing:4px;margin-bottom:25px}}
.badge{{display:inline-block;background:linear-gradient(90deg,#00ff9f,#00b3ff);color:#05080d;font-weight:bold;padding:5px 15px;border-radius:20px;font-size:12px}}
h2{{color:#00ff9f;font-size:15px;margin:25px 0 12px;padding-left:12px;border-left:3px solid #00ff9f}}
ul{{list-style:none;padding-left:20px}}li{{margin-bottom:5px}}
li::before{{content:'›';color:#00ff9f;margin-right:8px;font-weight:bold}}
table{{width:100%;border-collapse:collapse;background:rgba(5,8,13,0.5);margin-bottom:10px}}
td{{padding:7px 12px;border-bottom:1px solid #1a212e;font-size:13px}}
td:first-child{{color:#00b3ff;width:200px}}
.domain-big{{text-align:center;font-size:20px;color:#00ff9f;margin:15px 0 25px;letter-spacing:3px}}
.footer{{text-align:center;margin-top:35px;padding-top:20px;border-top:1px solid #1a212e;color:#5a6c80;font-size:12px}}
.brand{{color:#ff0040;font-size:14px;font-weight:bold;letter-spacing:3px}}
</style></head><body><div class="container">
<h1>XYECOC — ОТЧЁТ ПО ДОМЕНУ</h1>
<div class="subtitle">OSINT REPORT</div>
<div style="text-align:center;margin-bottom:15px"><span class="badge"># {num}</span></div>
<div class="domain-big">{info['domain']}</div>
<div style="text-align:center;color:#5a6c80;font-size:12px;margin-bottom:25px">Создано: {info['date']}</div>
<h2>📍 IP</h2><ul>{ip_html}</ul>
<h2>📋 WHOIS</h2><table>{whois_html}</table>
<h2>🌐 DNS</h2><table>{dns_html}</table>
<h2>🔌 ПОРТЫ</h2><ul>{ports_html}</ul>
<h2>📡 HTTP</h2><table>{headers_html}</table>
<div class="footer"><div class="brand">xyecocPROJECT</div>
<div>© 2026 • vobas25 • mr iron • окак 67 (greencat) • sakura.cc (sakuradev) • dsfsfsdfsdfds</div>
<div style="color:#00b3ff;font-style:italic;margin-top:5px">no api • no mercy</div>
</div></div></body></html>"""
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        return path, num


# ==================== ОТЧЁТ ПО ТЕЛЕФОНУ ====================
class PhoneReport:
    @staticmethod
    def desktop_path():
        home = os.path.expanduser("~")
        for p in [os.path.join(home, "Desktop"), os.path.join(home, "Рабочий стол"),
                  os.path.join(home, "OneDrive", "Desktop"),
                  os.path.join(home, "OneDrive", "Рабочий стол")]:
            if os.path.isdir(p):
                return p
        return home

    @staticmethod
    def next_filename():
        desk = PhoneReport.desktop_path()
        n = 1
        while True:
            fn = os.path.join(desk, f"xyecoc-number-{n}.html")
            if not os.path.exists(fn):
                return fn, n
            n += 1

    @staticmethod
    def parse_number(number):
        clean = "".join(ch for ch in number if ch.isdigit())
        codes = {
            "7": ("Россия / Казахстан", "RU/KZ", "7"),
            "1": ("США / Канада", "US/CA", "1"),
            "44": ("Великобритания", "GB", "44"),
            "49": ("Германия", "DE", "49"),
            "33": ("Франция", "FR", "33"),
            "39": ("Италия", "IT", "39"),
            "34": ("Испания", "ES", "34"),
            "48": ("Польша", "PL", "48"),
            "380": ("Украина", "UA", "380"),
            "375": ("Беларусь", "BY", "375"),
            "373": ("Молдова", "MD", "373"),
            "994": ("Азербайджан", "AZ", "994"),
            "374": ("Армения", "AM", "374"),
            "995": ("Грузия", "GE", "995"),
            "996": ("Киргизия", "KG", "996"),
            "992": ("Таджикистан", "TJ", "992"),
            "998": ("Узбекистан", "UZ", "998"),
            "86": ("Китай", "CN", "86"),
            "81": ("Япония", "JP", "81"),
            "82": ("Южная Корея", "KR", "82"),
            "91": ("Индия", "IN", "91"),
            "90": ("Турция", "TR", "90"),
        }
        cname, ciso, cdial = "Неизвестно", "??", "?"
        rest = clean
        for code, (n, i, d) in sorted(codes.items(), key=lambda x: -len(x[0])):
            if clean.startswith(code):
                cname, ciso, cdial = n, i, d
                rest = clean[len(code):]
                break

        ru_ops = {}
        for c in ["900","901","902","903","904","905","906","908","909",
                  "950","951","953","960","961","962","963","964","965",
                  "966","967","968"]:
            ru_ops[c] = "Билайн"
        for c in ["910","911","912","913","914","915","916","917","918","919",
                  "980","981","982","983","984","985","986","987","988","989"]:
            ru_ops[c] = "МТС"
        for c in ["920","921","922","923","924","925","926","927","928","929",
                  "930","931","932","933","934","936","937","938","939","999"]:
            ru_ops[c] = "МегаФон"
        for c in ["940","941","942","943","944","945","946","947","948","949"]:
            ru_ops[c] = "МОТИВ"
        for c in ["952","958","977","991","992","993","994","995","996"]:
            ru_ops[c] = "Tele2"

        region_map = {
            "900":"Общероссийский","901":"Общероссийский","902":"Общероссийский",
            "903":"Общероссийский","905":"Москва и МО","906":"Москва и МО",
            "909":"Общероссийский","910":"Общероссийский","911":"Северо-Запад (СПб)",
            "912":"Урал (Екатеринбург)","913":"Сибирь (Новосибирск)","914":"Дальний Восток",
            "915":"Общероссийский","916":"Москва и МО","917":"Москва и МО",
            "918":"Юг России","919":"Общероссийский","920":"Общероссийский",
            "921":"Северо-Запад (СПб)","922":"Урал","923":"Сибирь","924":"Дальний Восток",
            "925":"Москва","926":"Москва и МО","927":"Поволжье","928":"Юг России",
            "929":"Общероссийский","930":"Общероссийский","931":"Северо-Запад",
            "932":"Урал","933":"Сибирь","934":"Дальний Восток","936":"Москва и МО",
            "937":"Поволжье","938":"Юг России","939":"Общероссийский",
            "950":"Общероссийский","951":"Общероссийский","952":"Общероссийский",
            "953":"Общероссийский","958":"Общероссийский","960":"Общероссийский",
            "961":"Общероссийский","962":"Общероссийский","963":"Общероссийский",
            "964":"Общероссийский","965":"Общероссийский","966":"Москва и МО",
            "967":"Москва и МО","968":"Общероссийский","977":"Москва и МО",
            "980":"Общероссийский","981":"Северо-Запад","982":"Урал",
            "983":"Сибирь","984":"Дальний Восток","985":"Москва и МО",
            "986":"Москва и МО","987":"Поволжье","988":"Юг России",
            "989":"Общероссийский","991":"Общероссийский","992":"Общероссийский",
            "993":"Общероссийский","994":"Общероссийский","995":"Общероссийский",
            "996":"Общероссийский","999":"Москва и МО",
        }

        operator, region = "Неизвестно", ""
        if ciso == "RU/KZ" and len(rest) >= 3:
            operator = ru_ops.get(rest[:3], "Неизвестно")
            region = region_map.get(rest[:3], "")

        if ciso == "RU/KZ" and len(rest) == 10:
            formatted = f"+7 ({rest[:3]}) {rest[3:6]}-{rest[6:8]}-{rest[8:10]}"
        else:
            formatted = "+" + clean

        return {
            "raw": number, "clean": clean, "formatted": formatted,
            "country": cname, "country_iso": ciso, "country_dial": cdial,
            "operator": operator, "region": region,
            "length": len(clean),
            "valid": clean.isdigit() and 10 <= len(clean) <= 15,
        }

    @staticmethod
    def generate_html(info):
        path, num = PhoneReport.next_filename()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        html = f"""<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8">
<title>xyecoc-number-{num} — {info['formatted']}</title><style>
body{{background:#05080d;color:#c8d6e5;font-family:Consolas,monospace;padding:40px;line-height:1.6}}
.container{{max-width:900px;margin:0 auto;background:rgba(10,16,24,0.9);border:1px solid #00b3ff;border-radius:8px;padding:40px 50px;box-shadow:0 0 40px rgba(0,255,159,0.15)}}
h1{{color:#ff0040;font-size:24px;text-align:center;text-shadow:0 0 15px rgba(255,0,64,0.6)}}
.subtitle{{color:#00b3ff;font-size:12px;text-align:center;letter-spacing:4px;margin-bottom:25px}}
.badge{{display:inline-block;background:linear-gradient(90deg,#00ff9f,#00b3ff);color:#05080d;font-weight:bold;padding:5px 15px;border-radius:20px;font-size:12px}}
.number-big{{text-align:center;font-size:28px;color:#00ff9f;margin:15px 0 25px;letter-spacing:3px;text-shadow:0 0 15px rgba(0,255,159,0.5)}}
h2{{color:#00ff9f;font-size:15px;margin:25px 0 12px;padding-left:12px;border-left:3px solid #00ff9f}}
table{{width:100%;border-collapse:collapse;background:rgba(5,8,13,0.5);margin-bottom:10px}}
td{{padding:9px 14px;border-bottom:1px solid #1a212e;font-size:13px}}
td:first-child{{color:#00b3ff;width:220px;font-weight:bold}}
.footer{{text-align:center;margin-top:35px;padding-top:20px;border-top:1px solid #1a212e;color:#5a6c80;font-size:12px}}
.brand{{color:#ff0040;font-size:14px;font-weight:bold;letter-spacing:3px}}
.warning{{background:rgba(255,170,0,0.08);border:1px dashed #ffaa00;border-radius:6px;padding:15px 20px;margin:15px 0;color:#ffaa00;font-size:12px}}
.warning strong{{color:#ff0040}}
.valid-yes{{color:#00ff9f;font-weight:bold}}.valid-no{{color:#ff0040;font-weight:bold}}
</style></head><body><div class="container">
<h1>XYECOC — ОТЧЁТ ПО НОМЕРУ</h1>
<div class="subtitle">PHONE REPORT</div>
<div style="text-align:center;margin-bottom:15px"><span class="badge"># {num}</span></div>
<div class="number-big">{info['formatted']}</div>
<div style="text-align:center;color:#5a6c80;font-size:12px;margin-bottom:25px">Создано: {now}</div>
<h2>📱 ИНФОРМАЦИЯ</h2><table>
<tr><td>Номер</td><td>{info['raw']}</td></tr>
<tr><td>Формат</td><td>{info['formatted']}</td></tr>
<tr><td>Страна</td><td>{info['country']}</td></tr>
<tr><td>Код</td><td>+{info['country_dial']}</td></tr>
<tr><td>ISO</td><td>{info['country_iso']}</td></tr>
<tr><td>Оператор</td><td style="color:#00ff9f;font-weight:bold">{info['operator']}</td></tr>
<tr><td>Регион</td><td>{info['region'] or 'не определён'}</td></tr>
<tr><td>Длина</td><td>{info['length']}</td></tr>
<tr><td>Валиден</td><td class="{'valid-yes' if info['valid'] else 'valid-no'}">{'Да' if info['valid'] else 'Нет'}</td></tr>
</table>
<h2>⚠ ВАЖНО</h2><div class="warning">
<p><strong>Один номер = много людей.</strong> Оператор выдаёт номера миллионам.</p>
<p style="margin-top:10px"><b>Номер может быть:</b></p>
<ul style="list-style:none;padding-left:15px;margin-top:5px">
<li>› перепродан другому</li><li>› оформлен на юрлицо</li>
<li>› VoIP виртуальный</li><li>› в перевыпуске</li><li>› мошенник/спамер</li></ul>
<p style="margin-top:10px"><b>Точно узнать можно:</b></p>
<ul style="list-style:none;padding-left:15px;margin-top:5px">
<li>› Truecaller / GetContact</li><li>› официальный запрос в оператор</li>
<li>› объявления (Авито)</li><li>› соцсети/мессенджеры</li></ul>
</div>
<h2>🔎 ГДЕ ПРОВЕРИТЬ</h2><table>
<tr><td>Truecaller</td><td><a href="https://www.truecaller.com/search/{info['clean']}" style="color:#00b3ff">открыть</a></td></tr>
<tr><td>Sync.me</td><td><a href="https://sync.me/search/?number=+{info['clean']}" style="color:#00b3ff">открыть</a></td></tr>
<tr><td>Google</td><td><a href="https://www.google.com/search?q=%2B{info['clean']}" style="color:#00b3ff">открыть</a></td></tr>
<tr><td>Yandex</td><td><a href="https://yandex.ru/search/?text=%2B{info['clean']}" style="color:#00b3ff">открыть</a></td></tr>
<tr><td>Авито</td><td><a href="https://www.avito.ru/all?q={info['clean']}" style="color:#00b3ff">открыть</a></td></tr>
<tr><td>Telegram</td><td><a href="https://t.me/+{info['clean']}" style="color:#00b3ff">открыть</a></td></tr>
</table>
<div class="footer"><div class="brand">xyecocPROJECT</div>
<div>© 2026 • vobas25 • mr iron • окак 67 (greencat) • sakura.cc (sakuradev) • dsfsfsdfsdfds</div>
<div style="color:#00b3ff;font-style:italic;margin-top:5px">no api • no mercy</div>
</div></div></body></html>"""
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        return path, num


# ==================== БД ПОЛЬЗОВАТЕЛЕЙ ====================
class UserDB:
    @staticmethod
    def _load():
        if not os.path.exists(USERS_FILE):
            return {}
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

    @staticmethod
    def _save(d):
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)

    @staticmethod
    def _hash(p, s):
        return hashlib.sha256((s + p).encode("utf-8")).hexdigest()

    @staticmethod
    def register(email, password, password_repeat, nickname, username):
        email = email.strip().lower()
        nickname = nickname.strip()
        username = username.strip().lstrip("@").lower()
        if "@" not in email or "." not in email:
            return False, "Некорректный email"
        if len(password) < 6:
            return False, "Пароль мин. 6"
        if password != password_repeat:
            return False, "Пароли не совпадают"
        if len(nickname) < 2:
            return False, "Ник мин. 2"
        if len(username) < 3 or not username.replace("_", "").isalnum():
            return False, "Username мин. 3 (буквы/цифры/_)"
        data = UserDB._load()
        if email in data:
            return False, "Email занят"
        for u in data.values():
            if u.get("username", "").lower() == username:
                return False, "Username занят"
        salt = hashlib.sha256(os.urandom(32)).hexdigest()[:16]
        data[email] = {"email": email, "nickname": nickname, "username": username,
                       "salt": salt, "password_hash": UserDB._hash(password, salt),
                       "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        UserDB._save(data)
        return True, "OK"

    @staticmethod
    def login(email, password):
        email = email.strip().lower()
        data = UserDB._load()
        if email not in data:
            return False, "Не найден"
        u = data[email]
        if UserDB._hash(password, u["salt"]) != u["password_hash"]:
            return False, "Неверный пароль"
        return True, u

    @staticmethod
    def update(email, **kw):
        data = UserDB._load()
        if email not in data:
            return False, "Нет юзера"
        new_un = kw.get("username", "").lower()
        if new_un:
            for k, u in data.items():
                if k != email and u.get("username", "").lower() == new_un:
                    return False, "Username занят"
        for k, v in kw.items():
            if v:
                data[email][k] = v
        UserDB._save(data)
        return True, data[email]

    @staticmethod
    def save_session(email):
        with open(SESSION_FILE, "w") as f:
            json.dump({"email": email}, f)

    @staticmethod
    def load_session():
        if not os.path.exists(SESSION_FILE):
            return None
        try:
            with open(SESSION_FILE) as f:
                s = json.load(f)
            return UserDB._load().get(s.get("email"))
        except Exception:
            return None

    @staticmethod
    def clear_session():
        if os.path.exists(SESSION_FILE):
            os.remove(SESSION_FILE)


# ==================== ЧАТ-БД ====================
class ChatDB:
    @staticmethod
    def _load():
        if not os.path.exists(CHATS_FILE):
            return {"chats": {}, "messages": {}}
        try:
            with open(CHATS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {"chats": {}, "messages": {}}

    @staticmethod
    def _save(d):
        with open(CHATS_FILE, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)

    @staticmethod
    def create_chat(name, is_group, creator_email):
        data = ChatDB._load()
        cid = hashlib.md5((name + creator_email + str(time.time())).encode()).hexdigest()[:10]
        data["chats"][cid] = {"id": cid, "name": name, "is_group": is_group,
                              "creator": creator_email, "members": [creator_email],
                              "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        data["messages"][cid] = []
        ChatDB._save(data)
        return cid

    @staticmethod
    def send_message(cid, from_email, text):
        data = ChatDB._load()
        if cid not in data["chats"]:
            return False, "Нет чата"
        data["messages"].setdefault(cid, []).append({
            "from": from_email, "text": text,
            "time": datetime.now().strftime("%H:%M:%S")})
        ChatDB._save(data)
        return True, "OK"

    @staticmethod
    def get_messages(cid):
        return ChatDB._load()["messages"].get(cid, [])

    @staticmethod
    def list_for_user(email):
        return [c for c in ChatDB._load()["chats"].values() if email in c["members"]]

    @staticmethod
    def search_chats(query):
        q = query.lower()
        return [c for c in ChatDB._load()["chats"].values() if q in c["name"].lower()]

    @staticmethod
    def join_chat(cid, email):
        data = ChatDB._load()
        if cid not in data["chats"]:
            return False
        if email not in data["chats"][cid]["members"]:
            data["chats"][cid]["members"].append(email)
        ChatDB._save(data)
        return True

    @staticmethod
    def search_users(query):
        q = query.lower().lstrip("@")
        return [u for u in UserDB._load().values()
                if q in u.get("nickname", "").lower() or q in u.get("username", "").lower()]


# ==================== ФОН ====================
class ParticleBG:
    def __init__(self, canvas, w, h, count=60):
        self.c = canvas; self.w = w; self.h = h
        self.tag = f"bg_{id(self)}"
        self.mx, self.my = -1000, -1000
        colors = [ACCENT, ACCENT3, ACCENT4, ACCENT2]
        self.p = [{"x": random.uniform(0, w), "y": random.uniform(0, h),
                   "vx": random.uniform(-.4, .4), "vy": random.uniform(-.4, .4),
                   "r": random.uniform(1.2, 2.8), "c": random.choice(colors),
                   "pu": random.uniform(0, 6.28)} for _ in range(count)]
        canvas.bind("<Motion>", self._move, add="+")

    def _move(self, e):
        self.mx, self.my = e.x, e.y

    def update(self):
        self.c.delete(self.tag)
        for p in self.p:
            p["x"] += p["vx"]; p["y"] += p["vy"]
            if p["x"] <= 0 or p["x"] >= self.w:
                p["vx"] *= -1; p["x"] = max(0, min(self.w, p["x"]))
            if p["y"] <= 0 or p["y"] >= self.h:
                p["vy"] *= -1; p["y"] = max(0, min(self.h, p["y"]))
            p["pu"] += 0.05
        md = 140
        for i in range(len(self.p)):
            for j in range(i + 1, len(self.p)):
                a, b = self.p[i], self.p[j]
                d = math.hypot(a["x"]-b["x"], a["y"]-b["y"])
                if d < md:
                    t = 1 - d / md
                    col = ACCENT3 if t > .6 else ("#004a6b" if t > .3 else "#002233")
                    self.c.create_line(a["x"], a["y"], b["x"], b["y"], fill=col, tags=self.tag)
        for p in self.p:
            d = math.hypot(p["x"]-self.mx, p["y"]-self.my)
            if d < 180:
                t = 1 - d / 180
                col = ACCENT3 if t > .6 else ("#004a6b" if t > .3 else "#002233")
                self.c.create_line(p["x"], p["y"], self.mx, self.my, fill=col, tags=self.tag)
        for p in self.p:
            r = p["r"] + math.sin(p["pu"]) * .6
            dim = {ACCENT:"#003d26",ACCENT3:"#00293d",ACCENT4:"#3d0a5c",ACCENT2:"#3d0010"}.get(p["c"],"#002233")
            self.c.create_oval(p["x"]-r*2.5, p["y"]-r*2.5, p["x"]+r*2.5, p["y"]+r*2.5,
                               outline="", fill=dim, tags=self.tag)
            self.c.create_oval(p["x"]-r, p["y"]-r, p["x"]+r, p["y"]+r,
                               outline="", fill=p["c"], tags=self.tag)
        self.c.tag_lower(self.tag)


# ==================== ХЕЛПЕРЫ ====================
def make_entry(parent, placeholder="", show=None, width=30):
    frame = tk.Frame(parent, bg=BG_INPUT, highlightthickness=1,
                     highlightbackground=ACCENT3, highlightcolor=ACCENT)
    e = tk.Entry(frame, font=("Consolas", 11), bg=BG_INPUT, fg=TEXT,
                 insertbackground=ACCENT, relief="flat", bd=0,
                 show=show, width=width, highlightthickness=0)
    e.pack(fill="both", expand=True, padx=8, pady=7)
    if placeholder:
        e.insert(0, placeholder); e.config(fg=TEXT_DIM)
        def fi(ev):
            if e.get() == placeholder:
                e.delete(0, "end"); e.config(fg=TEXT)
                if show: e.config(show=show)
        def fo(ev):
            if not e.get():
                e.insert(0, placeholder); e.config(fg=TEXT_DIM, show="")
        e.bind("<FocusIn>", fi); e.bind("<FocusOut>", fo)
    return frame, e


def val(e):
    v = e.get().strip()
    return "" if v.startswith("  ") else v


# ==================== РЕГИСТРАЦИЯ ====================
class RegisterWin(tk.Toplevel):
    def __init__(self, parent, on_ok):
        super().__init__(parent)
        self.on_ok = on_ok
        self.title("Регистрация"); self.configure(bg=BG_DARK)
        W, H = 560, 740
        self.geometry(f"{W}x{H}"); self.resizable(False, False)
        self.update_idletasks()
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f"{W}x{H}+{(sw-W)//2}+{(sh-H)//2}")
        c = tk.Canvas(self, bg=BG_DARK, highlightthickness=0)
        c.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg = ParticleBG(c, W, H, 30); self._anim()

        tk.Label(self, text="РЕГИСТРАЦИЯ", font=("Consolas", 20, "bold"),
                 fg=ACCENT, bg=BG_DARK).place(x=0, y=20, relwidth=1)
        tk.Label(self, text="─"*60, font=("Consolas", 8),
                 fg=ACCENT2, bg=BG_DARK).place(x=0, y=52, relwidth=1)

        y = 80
        self.f1, self.e_email = make_entry(self, "  email@example.com")
        self.f1.place(x=90, y=y, width=380, height=42); y += 50
        self.f2, self.e_nick = make_entry(self, "  Ник")
        self.f2.place(x=90, y=y, width=380, height=42); y += 50
        self.f3, self.e_user = make_entry(self, "  username")
        self.f3.place(x=90, y=y, width=380, height=42); y += 50
        self.f4, self.e_pass = make_entry(self, "  Пароль", show="●")
        self.f4.place(x=90, y=y, width=380, height=42); y += 50
        self.f5, self.e_pass2 = make_entry(self, "  Повтор", show="●")
        self.f5.place(x=90, y=y, width=380, height=42); y += 55

        self.agree_var = tk.BooleanVar(value=False)
        tk.Checkbutton(self, text="Я принимаю соглашение",
                       variable=self.agree_var, font=("Consolas", 9),
                       fg=TEXT, bg=BG_DARK, activebackground=BG_DARK,
                       activeforeground=ACCENT, selectcolor=BG_INPUT,
                       cursor="hand2").place(x=90, y=y, width=380, height=25)
        y += 28
        link = tk.Label(self, text="📜 Прочитать соглашение",
                        font=("Consolas", 9, "underline"), fg=ACCENT3,
                        bg=BG_DARK, cursor="hand2")
        link.place(x=90, y=y, width=380, height=22)
        link.bind("<Button-1>", lambda e: Agreement.open_in_browser())
        y += 28
        self.err = tk.Label(self, text="", font=("Consolas", 9, "bold"),
                            fg=ACCENT2, bg=BG_DARK)
        self.err.place(x=0, y=y, relwidth=1); y += 30

        tk.Button(self, text="ЗАРЕГИСТРИРОВАТЬСЯ", command=self.do,
                  font=("Consolas", 12, "bold"), fg=BG_DARK, bg=ACCENT,
                  relief="flat", bd=0, cursor="hand2").place(x=140, y=y, width=280, height=45)

    def _anim(self):
        try:
            self.bg.update(); self.after(40, self._anim)
        except Exception: pass

    def do(self):
        if not self.agree_var.get():
            self.err.config(text="✗ Прими соглашение"); return
        ok, msg = UserDB.register(val(self.e_email), val(self.e_pass),
                                   val(self.e_pass2), val(self.e_nick), val(self.e_user))
        if ok:
            self.err.config(text="✓ Аккаунт создан!", fg=ACCENT)
            email, pwd = val(self.e_email).lower(), val(self.e_pass)
            self.after(600, lambda: (self.destroy(), self.on_ok(email, pwd)))
        else:
            self.err.config(text=f"✗ {msg}")


# ==================== ВХОД ====================
class LoginWin(tk.Toplevel):
    def __init__(self, parent, on_ok):
        super().__init__(parent)
        self.on_ok = on_ok
        self.title("Вход"); self.configure(bg=BG_DARK)
        W, H = 520, 500
        self.geometry(f"{W}x{H}"); self.resizable(False, False)
        self.update_idletasks()
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f"{W}x{H}+{(sw-W)//2}+{(sh-H)//2}")
        c = tk.Canvas(self, bg=BG_DARK, highlightthickness=0)
        c.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg = ParticleBG(c, W, H, 30); self._anim()

        tk.Label(self, text="ВХОД", font=("Consolas", 20, "bold"),
                 fg=ACCENT, bg=BG_DARK).place(x=0, y=25, relwidth=1)
        tk.Label(self, text="─"*55, font=("Consolas", 8),
                 fg=ACCENT2, bg=BG_DARK).place(x=0, y=58, relwidth=1)

        self.f1, self.e_email = make_entry(self, "  email@example.com")
        self.f1.place(x=70, y=115, width=380, height=42)
        self.f2, self.e_pass = make_entry(self, "  Пароль", show="●")
        self.f2.place(x=70, y=175, width=380, height=42)
        self.err = tk.Label(self, text="", font=("Consolas", 9, "bold"),
                            fg=ACCENT2, bg=BG_DARK)
        self.err.place(x=0, y=235, relwidth=1)

        tk.Button(self, text="ВОЙТИ", command=self.do,
                  font=("Consolas", 12, "bold"), fg=BG_DARK, bg=ACCENT,
                  relief="flat", bd=0, cursor="hand2").place(x=120, y=270, width=280, height=45)
        tk.Button(self, text="Нет аккаунта? Регистрация", command=self.to_reg,
                  font=("Consolas", 9), fg=ACCENT3, bg=BG_DARK,
                  relief="flat", bd=0, cursor="hand2").place(x=0, y=330, relwidth=1)
        tk.Button(self, text="📜 Соглашение", command=Agreement.open_in_browser,
                  font=("Consolas", 9, "underline"), fg=ACCENT3, bg=BG_DARK,
                  relief="flat", bd=0, cursor="hand2").place(x=0, y=360, relwidth=1)
        tk.Button(self, text="Продолжить без аккаунта →",
                  command=lambda: (self.destroy(), self.on_ok(None)),
                  font=("Consolas", 9, "italic"), fg=TEXT_DIM, bg=BG_DARK,
                  relief="flat", bd=0, cursor="hand2").place(x=0, y=395, relwidth=1)

    def _anim(self):
        try:
            self.bg.update(); self.after(40, self._anim)
        except Exception: pass

    def do(self):
        ok, res = UserDB.login(val(self.e_email), val(self.e_pass))
        if ok:
            self.err.config(text="✓ Вход выполнен", fg=ACCENT)
            UserDB.save_session(val(self.e_email).lower())
            self.after(400, lambda: (self.destroy(), self.on_ok(res)))
        else:
            self.err.config(text=f"✗ {res}")

    def to_reg(self):
        self.destroy()
        RegisterWin(self.master, self._reg_done)

    def _reg_done(self, email, pwd):
        ok, res = UserDB.login(email, pwd)
        if ok:
            UserDB.save_session(email); self.on_ok(res)


# ==================== ПРОФИЛЬ ====================
class EditProfile(tk.Toplevel):
    def __init__(self, parent, user, on_save):
        super().__init__(parent)
        self.user = user; self.on_save = on_save
        self.title("Профиль"); self.configure(bg=BG_DARK)
        W, H = 520, 540
        self.geometry(f"{W}x{H}"); self.resizable(False, False)
        self.update_idletasks()
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f"{W}x{H}+{(sw-W)//2}+{(sh-H)//2}")
        c = tk.Canvas(self, bg=BG_DARK, highlightthickness=0)
        c.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg = ParticleBG(c, W, H, 30); self._anim()

        tk.Label(self, text="ПРОФИЛЬ", font=("Consolas", 16, "bold"),
                 fg=ACCENT, bg=BG_DARK).place(x=0, y=25, relwidth=1)
        tk.Label(self, text="─"*55, font=("Consolas", 8),
                 fg=ACCENT2, bg=BG_DARK).place(x=0, y=55, relwidth=1)

        tk.Label(self, text="Ник:", font=("Consolas", 10),
                 fg=TEXT_DIM, bg=BG_DARK).place(x=70, y=80)
        self.f1, self.e_nick = make_entry(self)
        self.e_nick.insert(0, user.get("nickname", "")); self.e_nick.config(fg=TEXT)
        self.f1.place(x=70, y=100, width=380, height=42)

        tk.Label(self, text="Username:", font=("Consolas", 10),
                 fg=TEXT_DIM, bg=BG_DARK).place(x=70, y=155)
        self.f2, self.e_user = make_entry(self)
        self.e_user.insert(0, user.get("username", "")); self.e_user.config(fg=TEXT)
        self.f2.place(x=70, y=175, width=380, height=42)

        tk.Label(self, text="Email:", font=("Consolas", 10),
                 fg=TEXT_DIM, bg=BG_DARK).place(x=70, y=230)
        self.f3, self.e_mail = make_entry(self)
        self.e_mail.insert(0, user.get("email", ""))
        self.e_mail.config(fg=TEXT_DIM, state="readonly", readonlybackground=BG_PANEL)
        self.f3.place(x=70, y=250, width=380, height=42)

        tk.Label(self, text="Новый пароль:", font=("Consolas", 10),
                 fg=TEXT_DIM, bg=BG_DARK).place(x=70, y=305)
        self.f4, self.e_pass = make_entry(self, show="●")
        self.f4.place(x=70, y=325, width=380, height=42)
        self.err = tk.Label(self, text="", font=("Consolas", 9, "bold"),
                            fg=ACCENT2, bg=BG_DARK)
        self.err.place(x=0, y=385, relwidth=1)

        tk.Button(self, text="СОХРАНИТЬ", command=self.save,
                  font=("Consolas", 11, "bold"), fg=BG_DARK, bg=ACCENT,
                  relief="flat", bd=0, cursor="hand2").place(x=70, y=420, width=180, height=42)
        tk.Button(self, text="ВЫЙТИ", command=self.logout,
                  font=("Consolas", 11, "bold"), fg=ACCENT2, bg=BG_PANEL,
                  relief="flat", bd=0, cursor="hand2", highlightthickness=1,
                  highlightbackground=ACCENT2).place(x=270, y=420, width=180, height=42)

    def _anim(self):
        try:
            self.bg.update(); self.after(40, self._anim)
        except Exception: pass

    def save(self):
        nick, user, pwd = val(self.e_nick), val(self.e_user).lstrip("@").lower(), val(self.e_pass)
        if len(nick) < 2:
            self.err.config(text="✗ Ник мин. 2"); return
        if len(user) < 3 or not user.replace("_", "").isalnum():
            self.err.config(text="✗ Username мин.3"); return
        upd = {"nickname": nick, "username": user}
        if pwd:
            if len(pwd) < 6:
                self.err.config(text="✗ Пароль мин.6"); return
            salt = hashlib.sha256(os.urandom(32)).hexdigest()[:16]
            upd["salt"] = salt
            upd["password_hash"] = UserDB._hash(pwd, salt)
        ok, res = UserDB.update(self.user["email"], **upd)
        if ok:
            self.err.config(text="✓ Сохранено", fg=ACCENT)
            self.after(400, lambda: (self.destroy(), self.on_save(res)))
        else:
            self.err.config(text=f"✗ {res}")

    def logout(self):
        UserDB.clear_session(); self.destroy()
        os.execl(sys.executable, sys.executable, *sys.argv)


# ==================== ЧАТЫ ====================
class ChatWindow(tk.Toplevel):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user = user; self.parent = parent; self.current_chat = None
        self.title("ЧАТЫ [РЕЖИМ ТЕСТ]"); self.configure(bg=BG_DARK)
        W, H = 1100, 700
        self.geometry(f"{W}x{H}"); self.resizable(False, False)
        self.update_idletasks()
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f"{W}x{H}+{(sw-W)//2}+{(sh-H)//2}")
        c = tk.Canvas(self, bg=BG_DARK, highlightthickness=0)
        c.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg = ParticleBG(c, W, H, 40); self._anim()

        tk.Label(self, text="💬 ЧАТЫ", font=("Consolas", 16, "bold"),
                 fg=ACCENT, bg=BG_DARK).place(x=20, y=10)
        tk.Label(self, text="⚠ РЕЖИМ ТЕСТ — данные хранятся локально",
                 font=("Consolas", 9, "italic"), fg=WARN, bg=BG_DARK).place(x=150, y=18)

        left = tk.Frame(self, bg=BG_PANEL, highlightthickness=1,
                        highlightbackground=ACCENT3)
        left.place(x=15, y=50, width=320, height=635)

        tk.Label(left, text="🔍 ПОИСК", font=("Consolas", 9, "bold"),
                 fg=ACCENT3, bg=BG_PANEL, anchor="w").pack(fill="x", padx=10, pady=(10,3))
        self.search_entry = tk.Entry(left, font=("Consolas", 10), bg=BG_INPUT,
                                      fg=TEXT, insertbackground=ACCENT, relief="flat",
                                      bd=0, highlightthickness=1, highlightbackground=ACCENT3)
        self.search_entry.pack(fill="x", padx=10, ipady=5)
        self.search_entry.bind("<Return>", lambda e: self.do_search())
        tk.Button(left, text="🔍 НАЙТИ", command=self.do_search,
                  font=("Consolas", 9, "bold"), fg=BG_DARK, bg=ACCENT,
                  relief="flat", bd=0, cursor="hand2").pack(fill="x", padx=10, pady=5, ipady=3)
        tk.Button(left, text="✖ СБРОС", command=self.reset_search,
                  font=("Consolas", 9), fg=TEXT_DIM, bg=BG_PANEL,
                  relief="flat", bd=0, cursor="hand2").pack(fill="x", padx=10, pady=(0,5), ipady=3)
        tk.Frame(left, bg=ACCENT3, height=1).pack(fill="x", padx=10, pady=5)

        tk.Button(left, text="➕ СОЗДАТЬ ЧАТ", command=self.create_chat_dialog,
                  font=("Consolas", 9, "bold"), fg=BG_DARK, bg=ACCENT,
                  relief="flat", bd=0, cursor="hand2").pack(fill="x", padx=10, pady=2, ipady=3)
        tk.Button(left, text="👥 СОЗДАТЬ ГРУППУ", command=lambda: self.create_chat_dialog(True),
                  font=("Consolas", 9, "bold"), fg=BG_DARK, bg=ACCENT3,
                  relief="flat", bd=0, cursor="hand2").pack(fill="x", padx=10, pady=2, ipady=3)
        tk.Frame(left, bg=ACCENT3, height=1).pack(fill="x", padx=10, pady=5)
        tk.Label(left, text="📋 МОИ ЧАТЫ", font=("Consolas", 9, "bold"),
                 fg=ACCENT, bg=BG_PANEL, anchor="w").pack(fill="x", padx=10, pady=(5,3))

        list_frame = tk.Frame(left, bg=BG_PANEL)
        list_frame.pack(fill="both", expand=True, padx=10, pady=(0,10))
        self.chat_listbox = tk.Listbox(list_frame, bg=BG_INPUT, fg=TEXT,
                                        font=("Consolas", 10),
                                        selectbackground=ACCENT, selectforeground=BG_DARK,
                                        relief="flat", bd=0, highlightthickness=0,
                                        activestyle="none")
        self.chat_listbox.pack(side="left", fill="both", expand=True)
        sb = tk.Scrollbar(list_frame, command=self.chat_listbox.yview,
                          bg=BG_PANEL, troughcolor=BG_INPUT, bd=0)
        sb.pack(side="right", fill="y")
        self.chat_listbox.config(yscrollcommand=sb.set)
        self.chat_listbox.bind("<<ListboxSelect>>", self.on_chat_select)

        right = tk.Frame(self, bg=BG_PANEL, highlightthickness=1,
                         highlightbackground=ACCENT3)
        right.place(x=345, y=50, width=740, height=635)
        self.chat_title = tk.Label(right, text="← выбери чат", font=("Consolas", 13, "bold"),
                                    fg=ACCENT, bg=BG_PANEL, anchor="w")
        self.chat_title.pack(fill="x", padx=15, pady=(10,5))
        self.chat_subtitle = tk.Label(right, text="", font=("Consolas", 9),
                                       fg=TEXT_DIM, bg=BG_PANEL, anchor="w")
        self.chat_subtitle.pack(fill="x", padx=15, pady=(0,5))
        tk.Frame(right, bg=ACCENT3, height=1).pack(fill="x", padx=15)

        msg_frame = tk.Frame(right, bg=BG_PANEL)
        msg_frame.pack(fill="both", expand=True, padx=15, pady=10)
        self.messages = scrolledtext.ScrolledText(msg_frame, bg=BG_INPUT, fg=TEXT,
                                                    font=("Consolas", 10), relief="flat",
                                                    bd=0, wrap="word", state="disabled")
        self.messages.pack(fill="both", expand=True)
        self.messages.tag_config("me", foreground=ACCENT, font=("Consolas", 10, "bold"))
        self.messages.tag_config("other", foreground=ACCENT3, font=("Consolas", 10, "bold"))
        self.messages.tag_config("time", foreground=TEXT_DIM, font=("Consolas", 8))
        self.messages.tag_config("text", foreground=TEXT)

        input_frame = tk.Frame(right, bg=BG_PANEL)
        input_frame.pack(fill="x", padx=15, pady=(0,15))
        self.msg_entry = tk.Entry(input_frame, font=("Consolas", 11), bg=BG_INPUT,
                                   fg=TEXT, insertbackground=ACCENT, relief="flat", bd=0,
                                   highlightthickness=1, highlightbackground=ACCENT3,
                                   highlightcolor=ACCENT)
        self.msg_entry.pack(side="left", fill="both", expand=True, ipady=8, padx=(0,8))
        self.msg_entry.bind("<Return>", lambda e: self.send_msg())
        tk.Button(input_frame, text="ОТПРАВИТЬ", command=self.send_msg,
                  font=("Consolas", 10, "bold"), fg=BG_DARK, bg=ACCENT,
                  relief="flat", bd=0, cursor="hand2").pack(side="right", ipadx=15, ipady=5)
        self.messages.bind("<Button-1>", self.on_msg_click)
        self._chat_map = {}
        self.load_chats()

    def _anim(self):
        try:
            self.bg.update(); self.after(40, self._anim)
        except Exception: pass

    def load_chats(self, chats=None):
        self.chat_listbox.delete(0, "end")
        if chats is None:
            chats = ChatDB.list_for_user(self.user["email"])
        self._chat_map = {}
        for ch in chats:
            prefix = "👥" if ch["is_group"] else "💬"
            self.chat_listbox.insert("end", f" {prefix} {ch['name']}")
            self._chat_map[self.chat_listbox.size()-1] = ch["id"]

    def on_chat_select(self, event):
        sel = self.chat_listbox.curselection()
        if not sel: return
        cid = self._chat_map.get(sel[0])
        if cid: self.open_chat(cid)

    def open_chat(self, cid):
        data = ChatDB._load()
        chat = data["chats"].get(cid)
        if not chat: return
        self.current_chat = cid
        prefix = "👥 ГРУППА" if chat["is_group"] else "💬 ЧАТ"
        self.chat_title.config(text=f"{prefix}: {chat['name']}")
        users = UserDB._load()
        creator_nick = users.get(chat["creator"], {}).get("nickname", chat["creator"])
        self.chat_subtitle.config(text=f"создатель: {creator_nick}  •  участников: {len(chat['members'])}")
        self.refresh_messages()

    def refresh_messages(self):
        if not self.current_chat: return
        self.messages.config(state="normal")
        self.messages.delete("1.0", "end")
        users = UserDB._load()
        for msg in ChatDB.get_messages(self.current_chat):
            frm = msg["from"]
            nick = users.get(frm, {}).get("nickname", frm)
            is_me = (frm == self.user["email"])
            self.messages.insert("end", "Я" if is_me else nick, "me" if is_me else "other")
            self.messages.insert("end", f"  [{msg['time']}]\n", "time")
            self.messages.insert("end", f"{msg['text']}\n\n", "text")
        self.messages.config(state="disabled")
        self.messages.see("end")

    def on_msg_click(self, event):
        index = self.messages.index(f"@{event.x},{event.y}")
        line = int(index.split(".")[0])
        try:
            line_text = self.messages.get(f"{line}.0", f"{line}.end")
        except Exception:
            return
        if not line_text: return
        name = line_text.split("  [")[0].strip()
        if not name or name == "Я": return
        for u in UserDB._load().values():
            if u.get("nickname", "") == name:
                self.show_user_profile(u); return

    def show_user_profile(self, target_user):
        w = tk.Toplevel(self)
        w.title("Профиль"); w.configure(bg=BG_DARK)
        W, H = 480, 420
        w.geometry(f"{W}x{H}"); w.transient(self); w.grab_set()
        w.update_idletasks()
        sw, sh = w.winfo_screenwidth(), w.winfo_screenheight()
        w.geometry(f"{W}x{H}+{(sw-W)//2}+{(sh-H)//2}")
        c = tk.Canvas(w, bg=BG_DARK, highlightthickness=0)
        c.place(x=0, y=0, relwidth=1, relheight=1)
        bg = ParticleBG(c, W, H, 30)
        def anim():
            try: bg.update(); c.tag_raise("ui"); w.after(40, anim)
            except Exception: pass
        anim()

        tk.Label(w, text="ПРОФИЛЬ", font=("Consolas", 14, "bold"),
                 fg=ACCENT, bg=BG_DARK).place(x=0, y=20, relwidth=1)
        av = tk.Canvas(w, width=100, height=100, bg=BG_DARK, highlightthickness=0)
        av.place(x=190, y=70)
        av.create_oval(2, 2, 98, 98, outline=ACCENT, width=3, fill=BG_INPUT)
        av.create_text(50, 50, text=target_user.get("nickname","?")[0].upper(),
                       font=("Consolas", 40, "bold"), fill=ACCENT)
        tk.Label(w, text=target_user.get("nickname", "user"), font=("Consolas", 16, "bold"),
                 fg=ACCENT, bg=BG_DARK).place(x=0, y=185, relwidth=1)
        tk.Label(w, text="@" + target_user.get("username", ""), font=("Consolas", 11),
                 fg=ACCENT3, bg=BG_DARK).place(x=0, y=210, relwidth=1)
        tk.Label(w, text=f"Email: {target_user.get('email','скрыт')}", font=("Consolas", 9),
                 fg=TEXT_DIM, bg=BG_DARK).place(x=0, y=240, relwidth=1)
        tk.Label(w, text=f"Создан: {target_user.get('created','?')}", font=("Consolas", 9),
                 fg=TEXT_DIM, bg=BG_DARK).place(x=0, y=262, relwidth=1)

        def dm():
            data = ChatDB._load()
            for cid, chat in data["chats"].items():
                if not chat["is_group"] and set(chat["members"]) == {self.user["email"], target_user["email"]}:
                    w.destroy(); self.open_chat(cid); return
            cid = ChatDB.create_chat(f"dm_{self.user.get('username','')}_{target_user.get('username','')}",
                                      False, self.user["email"])
            ChatDB.join_chat(cid, target_user["email"])
            d = ChatDB._load()
            d["chats"][cid]["name"] = f"Личка с {target_user.get('nickname','')}"
            ChatDB._save(d); w.destroy(); self.load_chats(); self.open_chat(cid)

        tk.Button(w, text="💬 НАПИСАТЬ", command=dm,
                  font=("Consolas", 10, "bold"), fg=BG_DARK, bg=ACCENT,
                  relief="flat", bd=0, cursor="hand2").place(x=90, y=300, width=300, height=40)
        tk.Button(w, text="Закрыть", command=w.destroy,
                  font=("Consolas", 9), fg=TEXT_DIM, bg=BG_DARK,
                  relief="flat", bd=0, cursor="hand2").place(x=0, y=360, relwidth=1)

    def do_search(self):
        q = self.search_entry.get().strip()
        if not q: return
        chats = ChatDB.search_chats(q)
        users = ChatDB.search_users(q)
        w = tk.Toplevel(self)
        w.title(f"Поиск: {q}"); w.configure(bg=BG_DARK)
        W, H = 600, 500
        w.geometry(f"{W}x{H}"); w.transient(self); w.grab_set()
        w.update_idletasks()
        sw, sh = w.winfo_screenwidth(), w.winfo_screenheight()
        w.geometry(f"{W}x{H}+{(sw-W)//2}+{(sh-H)//2}")
        c = tk.Canvas(w, bg=BG_DARK, highlightthickness=0)
        c.place(x=0, y=0, relwidth=1, relheight=1)
        bg = ParticleBG(c, W, H, 30)
        def anim():
            try: bg.update(); c.tag_raise("ui"); w.after(40, anim)
            except Exception: pass
        anim()
        tk.Label(w, text=f"🔍 РЕЗУЛЬТАТЫ: {q}", font=("Consolas", 13, "bold"),
                 fg=ACCENT, bg=BG_DARK).place(x=0, y=15, relwidth=1)
        tk.Label(w, text=f"👤 ЛЮДИ ({len(users)})", font=("Consolas", 10, "bold"),
                 fg=ACCENT3, bg=BG_DARK, anchor="w").place(x=20, y=55)
        uf = tk.Frame(w, bg=BG_PANEL, highlightthickness=1, highlightbackground=ACCENT3)
        uf.place(x=20, y=80, width=560, height=150)
        if users:
            ul = tk.Listbox(uf, bg=BG_INPUT, fg=TEXT, font=("Consolas", 10),
                            relief="flat", bd=0, selectbackground=ACCENT,
                            selectforeground=BG_DARK, activestyle="none")
            ul.pack(fill="both", expand=True, padx=2, pady=2)
            umap = {}
            for i, u in enumerate(users):
                ul.insert("end", f"  @{u.get('username','')}  ({u.get('nickname','')})")
                umap[i] = u
            def clk(e):
                sel = ul.curselection()
                if sel and umap.get(sel[0]): self.show_user_profile(umap[sel[0]])
            ul.bind("<Double-Button-1>", clk)
        else:
            tk.Label(uf, text="не найдено", font=("Consolas", 10, "italic"),
                     fg=TEXT_DIM, bg=BG_PANEL).pack(expand=True)
        tk.Label(w, text=f"💬 ЧАТЫ ({len(chats)})", font=("Consolas", 10, "bold"),
                 fg=ACCENT3, bg=BG_DARK, anchor="w").place(x=20, y=245)
        cf = tk.Frame(w, bg=BG_PANEL, highlightthickness=1, highlightbackground=ACCENT3)
        cf.place(x=20, y=270, width=560, height=200)
        if chats:
            cl = tk.Listbox(cf, bg=BG_INPUT, fg=TEXT, font=("Consolas", 10),
                            relief="flat", bd=0, selectbackground=ACCENT,
                            selectforeground=BG_DARK, activestyle="none")
            cl.pack(fill="both", expand=True, padx=2, pady=2)
            cmap = {}
            for i, ch in enumerate(chats):
                prefix = "👥" if ch["is_group"] else "💬"
                cl.insert("end", f"  {prefix} {ch['name']}")
                cmap[i] = ch
            def clk2(e):
                sel = cl.curselection()
                if sel and cmap.get(sel[0]):
                    ChatDB.join_chat(cmap[sel[0]]["id"], self.user["email"])
                    w.destroy(); self.load_chats(); self.open_chat(cmap[sel[0]]["id"])
            cl.bind("<Double-Button-1>", clk2)
        else:
            tk.Label(cf, text="не найдено", font=("Consolas", 10, "italic"),
                     fg=TEXT_DIM, bg=BG_PANEL).pack(expand=True)

    def reset_search(self):
        self.search_entry.delete(0, "end"); self.load_chats()

    def create_chat_dialog(self, is_group=False):
        w = tk.Toplevel(self)
        w.title("Создать"); w.configure(bg=BG_DARK)
        W, H = 480, 260
        w.geometry(f"{W}x{H}"); w.transient(self); w.grab_set()
        w.update_idletasks()
        sw, sh = w.winfo_screenwidth(), w.winfo_screenheight()
        w.geometry(f"{W}x{H}+{(sw-W)//2}+{(sh-H)//2}")
        c = tk.Canvas(w, bg=BG_DARK, highlightthickness=0)
        c.place(x=0, y=0, relwidth=1, relheight=1)
        bg = ParticleBG(c, W, H, 20)
        def anim():
            try: bg.update(); c.tag_raise("ui"); w.after(40, anim)
            except Exception: pass
        anim()
        title = "👥 ГРУППА" if is_group else "💬 ЧАТ"
        tk.Label(w, text=f"СОЗДАТЬ {title}", font=("Consolas", 14, "bold"),
                 fg=ACCENT if not is_group else ACCENT3, bg=BG_DARK).place(x=0, y=20, relwidth=1)
        tk.Label(w, text="Название:", font=("Consolas", 10), fg=TEXT_DIM,
                 bg=BG_DARK, anchor="w").place(x=60, y=75)
        f, e_name = make_entry(w, "  Название")
        f.place(x=60, y=95, width=360, height=42)
        err = tk.Label(w, text="", font=("Consolas", 9, "bold"),
                       fg=ACCENT2, bg=BG_DARK)
        err.place(x=0, y=150, relwidth=1)
        def create():
            name = val(e_name).strip()
            if len(name) < 2:
                err.config(text="✗ Название мин. 2"); return
            cid = ChatDB.create_chat(name, is_group, self.user["email"])
            self.load_chats(); w.destroy(); self.open_chat(cid)
        tk.Button(w, text="СОЗДАТЬ", command=create,
                  font=("Consolas", 11, "bold"), fg=BG_DARK,
                  bg=ACCENT if not is_group else ACCENT3,
                  relief="flat", bd=0, cursor="hand2").place(x=140, y=180, width=200, height=42)

    def send_msg(self):
        if not self.current_chat: return
        text = self.msg_entry.get().strip()
        if not text: return
        ChatDB.send_message(self.current_chat, self.user["email"], text)
        self.msg_entry.delete(0, "end")
        self.refresh_messages()


# ==================== ГЛАВНОЕ ОКНО ====================
class MainApp:
    def __init__(self, root, user=None):
        self.root = root; self.user = user
        self.root.deiconify()
        self.root.title("xyecocPROJECT v11.2")
        self.root.configure(bg=BG_DARK)
        self.root.geometry("1200x760")
        self.root.minsize(1000, 700)
        self.root.update_idletasks()
        sw, sh = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry(f"1200x760+{(sw-1200)//2}+{(sh-760)//2}")
        self.build()

    def build(self):
        c = tk.Canvas(self.root, bg=BG_DARK, highlightthickness=0)
        c.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg = ParticleBG(c, 1200, 760, 70); self._anim()

        pf = tk.Frame(self.root, bg=BG_PANEL, highlightthickness=1,
                      highlightbackground=ACCENT3)
        pf.place(x=12, y=12, width=290, height=100)
        self.av = tk.Canvas(pf, width=60, height=60, bg=BG_PANEL, highlightthickness=0)
        self.av.place(x=12, y=20); self._draw_av()

        if self.user:
            n = self.user.get("nickname", "user")
            u = "@" + self.user.get("username", "")
        else:
            n, u = "Гость", "@anonymous"
        self.lbl_nick = tk.Label(pf, text=n, font=("Consolas", 11, "bold"),
                                 fg=ACCENT, bg=BG_PANEL, anchor="w")
        self.lbl_nick.place(x=85, y=25, width=195)
        self.lbl_user = tk.Label(pf, text=u, font=("Consolas", 9),
                                 fg=ACCENT3, bg=BG_PANEL, anchor="w")
        self.lbl_user.place(x=85, y=45, width=195)
        if self.user:
            hint = tk.Label(pf, text="[клик → профиль]", font=("Consolas", 8, "italic"),
                            fg=TEXT_DIM, bg=BG_PANEL, anchor="w")
            hint.place(x=85, y=67, width=195)
            for w in [pf, self.lbl_nick, self.lbl_user, self.av, hint]:
                w.bind("<Button-1>", lambda e: self.open_profile())
                try: w.config(cursor="hand2")
                except: pass

        tk.Label(self.root, text=LOGO, font=("Consolas", 6, "bold"),
                 fg=ACCENT2, bg=BG_DARK, justify="left").place(x=320, y=15)
        tk.Label(self.root, text="xyecocPROJECT", font=("Consolas", 16, "bold"),
                 fg=ACCENT, bg=BG_DARK).place(x=800, y=25)
        tk.Label(self.root, text="v11.2  •  no api • no mercy", font=("Consolas", 9),
                 fg=ACCENT3, bg=BG_DARK).place(x=800, y=50)

        mf = tk.Frame(self.root, bg=BG_PANEL)
        mf.place(x=15, y=130, relwidth=1, width=-30, height=60)
        btns = [
            ("IP INFO", self.act_ip, ACCENT),
            ("DNS", self.act_dns, ACCENT),
            ("HTTP", self.act_headers, ACCENT3),
            ("🌐 DOMAIN", self.act_domain_report, ACCENT),
            ("📱 PHONE REPORT", self.act_phone_report, ACCENT4),
            ("💬 ЧАТЫ", self.act_chats, ACCENT),
        ]
        for i, (n, cmd, col) in enumerate(btns):
            tk.Button(mf, text=n, command=cmd, font=("Consolas", 10, "bold"),
                      fg=col, bg=BG_PANEL, relief="flat", bd=0, cursor="hand2",
                      highlightthickness=1, highlightbackground=col).grid(
                row=0, column=i, padx=3, sticky="nsew")
            mf.columnconfigure(i, weight=1)
        mf.rowconfigure(0, weight=1)

        inf = tk.Frame(self.root, bg=BG_DARK)
        inf.place(x=15, y=205, relwidth=1, width=-30, height=48)
        tk.Label(inf, text=">_", font=("Consolas", 14, "bold"),
                 fg=ACCENT, bg=BG_DARK).pack(side="left", padx=(0, 8))
        self.entry = tk.Entry(inf, font=("Consolas", 12), bg=BG_INPUT, fg=TEXT,
                              insertbackground=ACCENT, relief="flat", bd=0,
                              highlightthickness=1, highlightbackground=ACCENT3,
                              highlightcolor=ACCENT)
        self.entry.pack(side="left", fill="both", expand=True, ipady=8, padx=(0, 8))
        self.entry.bind("<Return>", lambda e: self.run_cur())
        tk.Label(inf, text="[Enter] запуск", font=("Consolas", 9),
                 fg=TEXT_DIM, bg=BG_DARK).pack(side="left")

        of = tk.Frame(self.root, bg=BG_DARK)
        of.place(x=15, y=265, relwidth=1, width=-30, relheight=1, height=-320)
        self.out = scrolledtext.ScrolledText(of, bg=BG_PANEL, fg=TEXT,
                                                font=("Consolas", 10),
                                                relief="flat", bd=0, wrap="word")
        self.out.pack(fill="both", expand=True)
        for tag, col in [("ok", ACCENT), ("err", ACCENT2), ("info", ACCENT3),
                         ("warn", WARN), ("dim", TEXT_DIM)]:
            self.out.tag_config(tag, foreground=col)
        self.out.tag_config("head", foreground=ACCENT2, font=("Consolas", 11, "bold"))

        self.status = tk.Label(self.root,
                               text="● Готов  |  xyecocPROJECT © 2026  |  "
                                    "vobas25 • mr iron • окак 67 (greencat) • "
                                    "sakura.cc (sakuradev) • dsfsfsdfsdfds",
                               font=("Consolas", 9), fg=ACCENT, bg=BG_PANEL,
                               anchor="w", padx=10, pady=5)
        self.status.place(x=0, rely=1, y=-30, relwidth=1)
        self.cur = None

        self.log("=" * 78, "dim")
        if self.user:
            self.log(f"  Привет, {self.user.get('nickname')}! (@{self.user.get('username')})", "head")
        else:
            self.log("  Привет, Гость!", "head")
        self.log("=" * 78, "dim")
        self.log("")
        self.log("[*] IP INFO — введи IP → инфа о нём", "info")
        self.log("[*] DNS — введи домен → DNS-записи", "info")
        self.log("[*] HTTP — введи URL → HTTP-заголовки", "info")
        self.log("[*] 🌐 DOMAIN — введи домен → XYECOC-создано_N.html на рабочем столе", "info")
        self.log("[*] 📱 PHONE REPORT — введи номер → xyecoc-number-N.html на рабочем столе", "info")
        self.log("[*] 💬 ЧАТЫ — чат-система (режим тест)", "info")
        self.log("")

    def _anim(self):
        try:
            self.bg.update(); self.root.after(33, self._anim)
        except Exception: pass

    def _draw_av(self):
        self.av.delete("all")
        col = ACCENT if self.user else TEXT_DIM
        self.av.create_oval(2, 2, 58, 58, outline=col, width=2, fill=BG_INPUT)
        t = self.user.get("nickname", "?")[0].upper() if self.user else "?"
        self.av.create_text(30, 30, text=t, font=("Consolas", 22, "bold"), fill=col)

    def open_profile(self):
        if self.user:
            EditProfile(self.root, self.user, self.on_saved)

    def on_saved(self, u):
        self.user = u
        self.lbl_nick.config(text=u.get("nickname"))
        self.lbl_user.config(text="@" + u.get("username", ""))
        self._draw_av()
        self.log(f"[+] Профиль обновлён: {u.get('nickname')}", "ok")

    def log(self, t, tag=None):
        self.out.insert("end", t + "\n", tag); self.out.see("end")

    def set_status(self, t, col=ACCENT):
        self.status.config(text=f"● {t}", fg=col)

    def run_cur(self):
        if self.cur: self.cur()

    def spawn(self, f):
        threading.Thread(target=f, daemon=True).start()

    def get(self):
        return self.entry.get().strip()

    # ─── IP INFO ───
    def act_ip(self):
        self.cur = self._ip_setup
        self.log("[>] IP INFO. Введи IP-адрес", "warn")

    def _ip_setup(self):
        ip = self.get()
        if not ip: return
        self.entry.delete(0, "end")
        self.spawn(lambda: self._ip(ip))

    def _ip(self, ip):
        if requests is None:
            self.log("[-] Установи requests", "err"); return
        self.set_status(f"IP {ip}...", WARN)
        self.log(f"\n[+] IP: {ip}", "info")
        try:
            d = requests.get(f"http://ip-api.com/json/{ip}?lang=ru", timeout=10).json()
            if d.get("status") == "success":
                for k, v in [("IP", d.get("query")), ("Страна", d.get("country")),
                             ("Регион", d.get("regionName")), ("Город", d.get("city")),
                             ("Провайдер", d.get("isp")), ("Организация", d.get("org")),
                             ("Координаты", f"{d.get('lat')}, {d.get('lon')}"),
                             ("Timezone", d.get("timezone"))]:
                    self.log(f"  {k + ':':<14}{v}", "ok")
            else:
                self.log("[-] Не найдено", "err")
        except Exception as e:
            self.log(f"[-] {e}", "err")
        self.set_status("Готов")

    # ─── DNS ───
    def act_dns(self):
        self.cur = self._dns_setup
        self.log("[>] DNS. Введи домен", "warn")

    def _dns_setup(self):
        d = self.get()
        if not d: return
        self.entry.delete(0, "end")
        self.spawn(lambda: self._dns(d))

    def _dns(self, d):
        if dns is None:
            self.log("[-] pip install dnspython", "err"); return
        self.log(f"\n[+] DNS: {d}", "info")
        for t in ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']:
            try:
                for a in dns.resolver.resolve(d, t):
                    self.log(f"  [{t}] {a.to_text()}", "ok")
            except Exception:
                pass

    # ─── HTTP ───
    def act_headers(self):
        self.cur = self._hd_setup
        self.log("[>] HTTP. Введи URL", "warn")

    def _hd_setup(self):
        u = self.get()
        if not u: return
        self.entry.delete(0, "end")
        self.spawn(lambda: self._hd(u))

    def _hd(self, url):
        if requests is None:
            self.log("[-] Установи requests", "err"); return
        if not url.startswith("http"):
            url = "http://" + url
        self.set_status(f"HTTP {url}...", WARN)
        self.log(f"\n[+] HTTP: {url}", "info")
        try:
            r = requests.get(url, timeout=10, headers=HEADERS, allow_redirects=True)
            self.log(f"  Status: {r.status_code}", "ok")
            for k, v in r.headers.items():
                self.log(f"  {k}: {v}", "info")
        except Exception as e:
            self.log(f"[-] {e}", "err")
        self.set_status("Готов")

    # ─── DOMAIN ───
    def act_domain_report(self):
        self.cur = self._domrep_setup
        self.log("[>] ОТЧЁТ ПО ДОМЕНУ. Введи домен", "warn")

    def _domrep_setup(self):
        d = self.get()
        if not d: return
        self.entry.delete(0, "end")
        self.spawn(lambda: self._domrep(d))

    def _domrep(self, domain):
        self.set_status(f"Собираю по {domain}...", WARN)
        self.log("\n" + "=" * 78, "dim")
        self.log(f"  📄 ОТЧЁТ ПО ДОМЕНУ: {domain}", "head")
        self.log("=" * 78, "dim")
        try:
            info = DomainReport.gather(domain)
            self.log(f"[*] IP: {len(info['ip'])}", "info")
            for ip in info["ip"]: self.log(f"    {ip}", "ok")
            self.log(f"[*] WHOIS: {len(info['whois'])}", "info")
            self.log(f"[*] DNS: {len(info['dns'])}", "info")
            for rt, recs in info["dns"].items():
                pv = ", ".join(recs[:3]) + ("..." if len(recs) > 3 else "")
                self.log(f"    [{rt}] {pv}", "ok")
            self.log(f"[*] Портов: {len(info['ports'])}", "info")
            for p, s in info["ports"]: self.log(f"    {p} → {s}", "ok")
            path, num = DomainReport.generate_html(info)
            self.log(f"\n[✓] HTML создан: {path}", "ok")
            self.log(f"[✓] Отчёт #{num}", "ok")
            webbrowser.open("file://" + path)
        except Exception as e:
            self.log(f"[-] {e}", "err")
        self.set_status("Готов")

    # ─── PHONE REPORT ───
    def act_phone_report(self):
        self.cur = self._phonerep_setup
        self.log("[>] ОТЧЁТ ПО НОМЕРУ. Введи номер", "warn")

    def _phonerep_setup(self):
        d = self.get()
        if not d: return
        self.entry.delete(0, "end")
        self.spawn(lambda: self._phonerep(d))

    def _phonerep(self, phone):
        self.set_status(f"Анализирую {phone}...", WARN)
        self.log("\n" + "=" * 78, "dim")
        self.log(f"  📱 ОТЧЁТ ПО НОМЕРУ: {phone}", "head")
        self.log("=" * 78, "dim")
        try:
            info = PhoneReport.parse_number(phone)
            self.log(f"[*] Формат:    {info['formatted']}", "info")
            self.log(f"[*] Страна:    {info['country']}", "ok")
            self.log(f"[*] Оператор:  {info['operator']}", "ok")
            self.log(f"[*] Регион:    {info.get('region') or 'не определён'}", "ok")
            self.log(f"[*] Валиден:   {'Да' if info['valid'] else 'Нет'}",
                     "ok" if info["valid"] else "err")
            path, num = PhoneReport.generate_html(info)
            self.log(f"\n[✓] HTML создан: {path}", "ok")
            self.log(f"[✓] Отчёт #{num}", "ok")
            webbrowser.open("file://" + path)
        except Exception as e:
            self.log(f"[-] {e}", "err")
        self.set_status("Готов")

    # ─── ЧАТЫ ───
    def act_chats(self):
        self.cur = None
        if not self.user:
            self.log("[-] Войди в аккаунт для чатов", "err")
            return
        ChatWindow(self.root, self.user)


# ==================== ЗАПУСК ====================
def run_app(root, user):
    for w in root.winfo_children():
        try: w.destroy()
        except: pass
    MainApp(root, user)


def main():
    try: Agreement.generate_html()
    except: pass
    root = tk.Tk(); root.withdraw()
    def after_login(user): run_app(root, user)
    saved = UserDB.load_session()
    if saved:
        root.after(100, lambda: run_app(root, saved))
    else:
        root.after(100, lambda: LoginWin(root, after_login))
    root.mainloop()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback
        traceback.print_exc()
        input("\nОшибка. Enter для выхода...")