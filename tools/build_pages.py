#!/usr/bin/env python3
"""Builds the German SEO landing pages (problem / solution / use case) from one template.
Shared header, contact form and footer are copied from index.html so they stay in sync.
Run from the repo root: python3 tools/build_pages.py"""
import re, json, html, os

home = open('index.html', encoding='utf-8').read()
def grab(a, b):
    i = home.index(a); j = home.index(b, i) + len(b); return home[i:j]
HEADER = grab('<header>', '</div></header>').replace('href="#', 'href="/#')
CONTACT = grab('<section id="kontakt"', '</div></section>')
TAIL = home[home.index('<footer>'):]
CSSV = re.search(r'style\.css\?v=(\d+)', home).group(1)
ICONV = re.search(r'favicon\.ico\?v=(\d+)', home).group(1)
BASE = 'https://ackermann-robotics.org'
TEL = '<a class="tel" href="tel:+4915114162414"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path fill="currentColor" d="M6.6 10.8a15.2 15.2 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.6a1 1 0 0 1-.25 1z"/></svg>0151&nbsp;14162414</a>'

PAGES = [
 dict(slug='roboter-mieten', nav='Roboter mieten',
  title='Roboter mieten für die Produktion – ohne Investition | Ackermann Robotics',
  desc='Roboter mieten statt kaufen: Wir installieren, betreiben und warten den Roboter. Feste Monatsgebühr, keine Investition. Sie zahlen erst, wenn er läuft.',
  eyebrow='Robot as a Service (RaaS)', h1='Roboter mieten statt kaufen.',
  lead='Mehr als Miete: Sie bekommen einen kognitiven Roboter, der eine Aufgabe in Ihrer Produktion übernimmt. Wir installieren, betreiben und warten ihn. Sie zahlen eine feste Monatsgebühr, erst wenn er zuverlässig läuft, und immer weniger als die Stelle heute kostet.',
  img='hero', alt='Kognitiver Roboter richtet Kartons auf',
  problem=('Warum Kaufen oft scheitert.', ['Ein Roboter mit Integration kostet schnell sechsstellig, bevor er ein Teil bewegt.', 'Sie brauchen jemanden, der ihn programmiert, betreut und repariert.', 'Ändert sich das Produkt, beginnt die Integration von vorne.']),
  solution=('Was Mieten bei uns heißt.', ['Keine Investition: kein Kauf, keine Anzahlung, keine Integrationskosten.', 'Feste Monatsgebühr inklusive Wartung, Reparatur und Fernbetreuung während Ihrer Produktionszeiten.', 'Die Gebühr liegt immer unter 70&nbsp;% dessen, was die Stelle Sie heute kostet.', 'Neue Varianten lernt der Roboter durch Vormachen. Das Nachtrainieren ist inklusive.']),
  faq=[('Was kostet es, einen Roboter zu mieten?', 'Die Monatsgebühr legen wir nach der Demo fest. Sie liegt immer unter 70&nbsp;% dessen, was Sie die Stelle heute kostet. Ein Beispiel: 2.000&nbsp;€ im Monat statt 3.000&nbsp;€ für einen Produktionshelfer.'),
       ('Ab wann zahlen wir?', 'Erst ab dem Monat, in dem der Roboter die Aufgabe zuverlässig erledigt. Demo, Aufnahme und Training sind für Sie kostenlos.'),
       ('Wer kümmert sich, wenn der Roboter hängt?', 'Unser Operator übernimmt aus der Ferne, während Ihrer Produktionszeiten. Reparaturen und Ersatzteile sind in der Gebühr enthalten.')]),
 dict(slug='produktionshelfer-gesucht', nav='Produktionshelfer gesucht',
  title='Produktionshelfer gesucht? Roboter statt Neueinstellung | Ackermann Robotics',
  desc='Sie finden keine Produktionshelfer? Ein kognitiver Roboter übernimmt die Stelle: nie krank, 30 % günstiger, ohne Investition. Sie zahlen erst, wenn er läuft.',
  eyebrow='Personalmangel in der Produktion', h1='Produktionshelfer gesucht? Ein Roboter übernimmt die Stelle.',
  lead='Die Stelle bleibt offen, Aufträge warten, Ihr Team macht Überstunden. Ein kognitiver Roboter übernimmt die Handgriffe, für die Sie niemanden mehr finden, und kostet 30&nbsp;% weniger.',
  img='folding', alt='Roboterarm faltet einen Karton an der Linie',
  problem=('Was eine offene Helferstelle kostet.', ['Stellenanzeigen, Zeitarbeit und Einarbeitung kosten Zeit und Geld, und oft kommt niemand.', 'Wer gerade eingearbeitet ist, kündigt. Das Wissen geht mit.', 'Krankheit, Urlaub, Nachtzuschläge: Die Schichtplanung wird zum Dauerproblem.']),
  solution=('Was der Roboter anders macht.', ['Nie krank, kein Urlaub, keine Kündigung. Das Können bleibt an der Linie.', 'Fährt auch die Zusatzschicht, nachts und am Wochenende zum gleichen Satz.', 'Rechenbeispiel: 2.000&nbsp;€ Monatsgebühr statt 3.000&nbsp;€ Lohn plus Nebenkosten. 12.000&nbsp;€ Ersparnis im Jahr.', 'Ihr Team zeigt die Aufgabe einmal vor. Den Rest machen wir.']),
  faq=[('Welche Helfertätigkeiten kann der Roboter übernehmen?', 'Wiederkehrende Handgriffe, die sich jedes Mal leicht unterscheiden: Kartons aufrichten, Verpacken, Kommissionieren und Teile umsetzen.'),
       ('Ersetzt der Roboter unsere Mitarbeiter?', 'Er übernimmt die Stelle, die Sie nicht besetzt bekommen. Ihre Leute werden für die Aufgaben frei, für die man Erfahrung braucht.'),
       ('Was, wenn es bei unserer Aufgabe nicht klappt?', 'Dann zahlen Sie nichts. Die Gebühr beginnt erst, wenn der Roboter die Aufgabe zuverlässig erledigt.')]),
 dict(slug='kartons-aufrichten-automatisieren', nav='Kartons aufrichten',
  title='Kartons aufrichten automatisieren – auch wechselnde Formate | Ackermann Robotics',
  desc='Kartons aufrichten, falten und verschließen mit einem kognitiven Roboter. Auch bei wechselnden Formaten und kleinen Losen. Keine Investition, Zahlung erst, wenn er läuft.',
  eyebrow='Anwendung', h1='Kartons aufrichten automatisieren. Auch bei wechselnden Formaten.',
  lead='Ein Kartonaufrichter lohnt sich nur bei großen Mengen im selben Format. Unser kognitiver Roboter richtet Kartons auf, faltet und verschließt sie, auch wenn die Größe wechselt.',
  img='folding', alt='Roboterarm richtet einen Karton auf',
  problem=('Warum das bisher an Menschen hing.', ['Viele Formate, kleine Lose: Für jede Größe eine eigene Maschine oder Umrüstung lohnt sich nicht.', 'Pappe ist weich und gibt nach. Ein klassischer Roboter mit fester Bahn greift daneben.', 'Also faltet ein Helfer, Schicht für Schicht.']),
  solution=('So macht es der kognitive Roboter.', ['Kameras sehen, wo der Zuschnitt liegt und wie er sich verhält.', 'Ihr Team zeigt das Falten ein paar Mal vor. Der Roboter lernt daraus.', 'Neues Format: kurz vormachen statt neu programmieren.', 'Feste Monatsgebühr, keine Investition. Sie zahlen erst, wenn er zuverlässig läuft.']),
  faq=[('Welche Kartonformate gehen?', 'Das prüfen wir in der kostenlosen Demo an Ihren Kartons. Danach wissen Sie, ob es geht und was es kostet.'),
       ('Kann der Roboter die Kartons auch verschließen?', 'Ja, Falten und Verschließen gehören zur Aufgabe, die er lernt.'),
       ('Brauchen wir einen Kartonaufrichter dazu?', 'Nein. Der Roboter arbeitet mit Ihren Zuschnitten an Ihrer Linie.')]),
 dict(slug='verpacken-automatisieren', nav='Verpacken',
  title='Verpacken automatisieren mit KI-Roboter | Ackermann Robotics',
  desc='Produkte in Kartons und Trays legen, auch wenn sie nie gleich liegen. Kognitiver Roboter ohne Investition, Zahlung erst, wenn er zuverlässig läuft.',
  eyebrow='Anwendung', h1='Verpacken automatisieren. Auch wenn kein Teil gleich liegt.',
  lead='Unser kognitiver Roboter legt Produkte in Kartons und Trays. Er sieht, wie jedes Teil liegt, und greift entsprechend. Ohne Vorrichtungen, ohne neue Programmierung für jede Variante.',
  img='boxes', alt='Roboterarm verpackt Teile in einen Karton',
  problem=('Warum Verpacken oft Handarbeit bleibt.', ['Produkte kommen ungeordnet an und liegen jedes Mal anders.', 'Viele Varianten: Für jede ein eigenes Programm und eigene Vorrichtungen lohnt sich nicht.', 'Die Stelle am Packtisch ist schwer zu besetzen und wechselt ständig.']),
  solution=('So macht es der kognitive Roboter.', ['Kameras erkennen Lage und Ausrichtung jedes Teils.', 'Ihr Team packt ein paar Mal vor, der Roboter lernt die Aufgabe.', 'Neue Variante: kurz vormachen. Das Nachtrainieren ist inklusive.', 'Keine Investition, feste Monatsgebühr, Zahlung erst, wenn er läuft.']),
  faq=[('Welche Produkte kann der Roboter verpacken?', 'Das hängt von Größe, Gewicht und Oberfläche ab. In der kostenlosen Demo prüfen wir es an Ihren Teilen.'),
       ('Arbeitet der Roboter neben unseren Mitarbeitern?', 'Wir richten ihn nach den geltenden Regeln der Maschinensicherheit ein und machen die Gefährdungsbeurteilung mit Ihnen, bevor er startet.'),
       ('Was passiert bei Störungen?', 'Unser Operator übernimmt aus der Ferne, während Ihrer Produktionszeiten. Reparaturen sind in der Gebühr enthalten.')]),
 dict(slug='kommissionieren-automatisieren', nav='Kommissionieren',
  title='Kommissionieren automatisieren: Teilesätze für die Montage | Ackermann Robotics',
  desc='Teilesätze und Kits für die Montage automatisch zusammenstellen, auch bei vielen Varianten und kleinen Losen. Kognitiver Roboter ohne Investition.',
  eyebrow='Anwendung', h1='Kommissionieren automatisieren. Auch bei vielen Varianten.',
  lead='Unser kognitiver Roboter stellt Teilesätze für die Montage zusammen. Er greift die Teile aus Behältern und legt sie in den Satz, auch wenn sich die Zusammenstellung oft ändert.',
  img='packing', alt='Roboterarme kommissionieren Teile für die Montage',
  problem=('Warum Kitting bisher Handarbeit ist.', ['Viele Varianten, kleine Lose: Jede Zusammenstellung neu zu programmieren lohnt sich nicht.', 'Teile liegen nicht sortiert, sondern lose im Behälter.', 'Fehler im Satz stoppen die Montage.']),
  solution=('So macht es der kognitive Roboter.', ['Kameras sehen, wo welches Teil liegt.', 'Ihr Team stellt den Satz ein paar Mal zusammen, der Roboter lernt daraus.', 'Neue Variante: kurz vormachen statt programmieren.', 'Keine Investition, feste Monatsgebühr, Zahlung erst, wenn er läuft.']),
  faq=[('Wie viele Varianten schafft der Roboter?', 'Jede Variante lernt er durch Vormachen. Wie viele bei Ihnen sinnvoll sind, klären wir in der kostenlosen Demo.'),
       ('Funktioniert das mit unseren Behältern?', 'In der Regel ja. Der Roboter arbeitet mit Ihren Behältern an Ihrem Arbeitsplatz.'),
       ('Haben wir schon einen Roboter, geht das trotzdem?', 'Ja. Wir binden Ihren vorhandenen Roboter ein und rüsten Kameras und Sensoren nach.')]),
 dict(slug='pick-and-place-automatisieren', nav='Teile umsetzen',
  title='Pick and Place automatisieren: Teile aus dem Behälter umsetzen | Ackermann Robotics',
  desc='Teile zwischen Behältern, Bändern und Maschinen umsetzen, auch wenn sie ungeordnet liegen. Kognitiver Roboter statt Helfer, ohne Investition.',
  eyebrow='Anwendung', h1='Teile umsetzen automatisieren. Auch aus dem ungeordneten Behälter.',
  lead='Unser kognitiver Roboter setzt Teile zwischen Behältern, Bändern und Maschinen um. Er sieht, wo das Teil liegt, und greift es, ohne dass Sie Vorrichtungen bauen müssen.',
  img='kitting', alt='Roboterarm setzt Teile zwischen Behältern um',
  problem=('Warum Umsetzen oft Handarbeit bleibt.', ['Teile liegen ungeordnet im Behälter. Ein klassischer Roboter braucht sie exakt positioniert.', 'Vorrichtungen und Zuführtechnik kosten viel und passen nur für ein Teil.', 'Also steht ein Helfer an der Maschine und legt ein.']),
  solution=('So macht es der kognitive Roboter.', ['Kameras erkennen Lage und Ausrichtung jedes Teils.', 'Ihr Team zeigt das Umsetzen ein paar Mal vor, der Roboter lernt daraus.', 'Neues Teil: kurz vormachen statt neu programmieren.', 'Keine Investition, feste Monatsgebühr, Zahlung erst, wenn er läuft.']),
  faq=[('Kann der Roboter eine Maschine beschicken?', 'Das prüfen wir in der kostenlosen Demo an Ihrer Maschine. Danach wissen Sie, ob es geht und was es kostet.'),
       ('Welche Teile kann er greifen?', 'Das hängt von Größe, Gewicht und Oberfläche ab. Wir prüfen es an Ihren Teilen.'),
       ('Ist das sicher für unsere Mitarbeiter?', 'Wir richten den Roboter nach den geltenden Regeln der Maschinensicherheit ein und machen die Gefährdungsbeurteilung mit Ihnen, bevor er startet.')]),
 dict(slug='kognitive-robotik', nav='Kognitive Robotik',
  title='Kognitive Robotik: Roboter, die sehen und durch Vormachen lernen | Ackermann Robotics',
  desc='Was ist kognitive Robotik? Roboter, die mit Kameras sehen, sich anpassen und durch Vormachen lernen. Damit automatisieren Sie Handgriffe, an denen klassische Roboter scheitern.',
  eyebrow='Technologie', h1='Kognitive Robotik: Roboter, die sehen und durch Vormachen lernen.',
  lead='Ein klassischer Industrieroboter fährt fest programmierte Bahnen. Ein kognitiver Roboter sieht, passt sich an und lernt neue Aufgaben, indem Ihr Team sie vormacht. Diese KI ist erst seit Kurzem zuverlässig genug für die Produktion.',
  img='packing', alt='Kognitive Roboterarme bei der Arbeit',
  problem=('Wo klassische Roboter an Grenzen stoßen.', ['Jede Bewegung muss programmiert werden.', 'Teile müssen exakt gleich liegen, sonst greift er daneben.', 'Jede neue Variante heißt neu programmieren. Das lohnt sich nur bei großen Stückzahlen.']),
  solution=('Was ein kognitiver Roboter anders macht.', ['Sehen: Kameras erkennen, wo das Teil liegt und wie es ausgerichtet ist.', 'Lernen durch Vormachen: Ihr Team zeigt die Aufgabe, der Roboter lernt daraus.', 'Anpassen: Kleine Abweichungen gleicht er selbst aus.', 'Korrigieren: Unser Operator hilft aus der Ferne, wenn er nicht weiterkommt, und der Roboter lernt daraus.']),
  faq=[('Ist kognitive Robotik dasselbe wie Physical AI?', 'Ja, beide Begriffe meinen Roboter, die mit KI ihre Umgebung wahrnehmen und Aufgaben lernen, statt starr programmiert zu werden.'),
       ('Für welche Aufgaben lohnt sich das?', 'Für Handgriffe, die sich jedes Mal leicht unterscheiden: Kartons aufrichten, Verpacken, Kommissionieren, Teile umsetzen.'),
       ('Brauchen wir dafür eigene KI- oder Robotik-Experten?', 'Nein. Wir installieren, betreiben und warten den Roboter. Ihr Team zeigt nur die Aufgabe.')]),
 dict(slug='physical-ai-produktion', nav='Physical AI',
  title='Physical AI in der Produktion: KI-Roboter im Einsatz | Ackermann Robotics',
  desc='Physical AI in der Produktion: KI-Roboter, die sehen, greifen und durch Vormachen lernen. Wir installieren und betreiben sie an Ihrer Linie, ohne Investition.',
  eyebrow='Physical AI', h1='Physical AI in der Produktion. Nicht im Labor, an Ihrer Linie.',
  lead='Physical AI heißt: KI, die nicht nur Text schreibt, sondern einen Roboter steuert. Er sieht mit Kameras, greift und lernt Handgriffe, indem Ihr Team sie vormacht. Wir bringen das in Ihre Halle und betreiben es für Sie.',
  img='folding', alt='KI-gesteuerter Roboterarm faltet einen Karton',
  problem=('Warum Physical AI bisher selten in der Halle ankommt.', ['Die Technik ist neu, eigene Experten dafür hat kaum ein Werk.', 'Pilotprojekte kosten oft sechsstellig, bevor klar ist, ob es klappt.', 'Zwischen Demo-Video und zuverlässigem Schichtbetrieb liegt viel Integrationsarbeit.']),
  solution=('Wie wir es lösen.', ['Wir prüfen Ihre Aufgabe kostenlos vor Ort oder per Video.', 'Wir installieren den Roboter, trainieren ihn an Ihrer Linie und betreuen ihn.', 'Unser Operator hilft aus der Ferne, wenn er nicht weiterkommt. Daraus lernt der Roboter.', 'Keine Investition. Die Monatsgebühr startet erst, wenn er zuverlässig läuft.']),
  faq=[('Was ist der Unterschied zwischen Physical AI und kognitiver Robotik?', 'Kaum einer. Beide Begriffe meinen Roboter, die mit KI wahrnehmen und lernen, statt starr programmiert zu werden. <a href="/kognitive-robotik/">Mehr zu kognitiver Robotik</a>'),
       ('Für welche Aufgaben ist Physical AI heute reif?', 'Für Handgriffe mit kleinen Abweichungen: Kartons aufrichten, Verpacken, Kommissionieren, Teile umsetzen.'),
       ('Brauchen wir dafür eine KI-Abteilung?', 'Nein. Ihr Team zeigt die Aufgabe, den Rest übernehmen wir.')]),
 dict(slug='roboter-kosten', nav='Was kostet ein Roboter?',
  title='Was kostet ein Roboter in der Produktion? Kaufen vs. mieten | Ackermann Robotics',
  desc='Was kostet ein Roboter für die Produktion wirklich? Arm, Greifer, Kameras, Integration und Wartung im Überblick, und wie es ohne Investition geht: Monatsgebühr ab Betriebsstart.',
  eyebrow='Kosten', h1='Was kostet ein Roboter in der Produktion?',
  lead='Der Roboterarm ist nur ein Teil der Rechnung. Greifer, Kameras, Integration, Sicherheit und Programmierung kosten oft mehr als der Arm selbst. Fertig integriert landen viele Anwendungen schnell bei 40.000 € bis weit über 100.000 €. Bei uns zahlen Sie stattdessen eine Monatsgebühr, und erst, wenn er läuft.',
  img='boxes', alt='Roboterarm verpackt Teile in einen Karton',
  problem=('Was beim Kauf alles anfällt.', ['Roboterarm: nur etwa die Hälfte der Gesamtkosten.', 'Greifer, Kameras, Halterungen und Sicherheitstechnik.', 'Integration und Programmierung, bei jeder neuen Variante erneut.', 'Wartung, Reparaturen und jemand im Haus, der sich auskennt.']),
  solution=('Was Sie bei uns zahlen.', ['Keine Investition: kein Kauf, keine Anzahlung, keine Integrationskosten.', 'Eine feste Monatsgebühr, höchstens 70&nbsp;% dessen, was die Stelle Sie heute kostet.', 'Wartung, Reparaturen, Nachtrainieren und Fernbetreuung sind enthalten.', 'Die Gebühr startet erst, wenn der Roboter zuverlässig läuft.']),
  faq=[('Wie hoch ist die Monatsgebühr konkret?', 'Sie hängt von Aufgabe und Schichten ab und liegt immer unter 70&nbsp;% der heutigen Kosten der Stelle. Bei 3.000 € Personalkosten sind das höchstens 2.100 € im Monat. Den Rechner finden Sie auf der <a href="/#kontakt">Startseite</a>.'),
       ('Lohnt sich das auch für nur eine Stelle?', 'Ja. Weil Sie nichts investieren, rechnet sich der Roboter ab dem ersten Monat, auch bei einer einzelnen Stelle.'),
       ('Was ist günstiger, kaufen oder mieten?', 'Bei großen Stückzahlen und einer Aufgabe, die sich nie ändert, kann Kaufen günstiger sein. Bei wechselnden Varianten und ohne eigene Robotik-Experten ist die Monatsgebühr meist die bessere Wahl, weil Integration, Nachtrainieren und Wartung enthalten sind.')]),
]

def page(p):
    url = f'{BASE}/{p["slug"]}/'
    faq_ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":html.unescape(a)}} for q,a in p['faq']]}
    bc_ld = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Ackermann Robotics","item":BASE+'/'},{"@type":"ListItem","position":2,"name":p['nav'],"item":url}]}
    ld = json.dumps([faq_ld, bc_ld], ensure_ascii=False, separators=(',',':'))
    li = lambda xs: ''.join(f'<li>{x}</li>' for x in xs)
    others = ''.join(f'<a href="/{o["slug"]}/">{o["nav"]}</a>' for o in PAGES if o is not p)
    faq = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in p['faq'])
    return f'''<!DOCTYPE html>
<html lang="de">
<head><script>if(location.protocol==='http:')location.replace('https://'+location.host+location.pathname+location.search+location.hash)</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p["title"]}</title>
<meta name="description" content="{p["desc"]}">
<link rel="canonical" href="{url}">
<link rel="icon" href="/favicon-192.png" type="image/png" sizes="192x192">
<link rel="icon" href="/favicon.ico?v={ICONV}" sizes="any">
<link rel="icon" href="/favicon.svg?v={ICONV}" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png?v={ICONV}">
<meta property="og:title" content="{p["title"]}">
<meta property="og:description" content="{p["desc"]}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Ackermann Robotics">
<meta property="og:image" content="{BASE}/img/{p["img"]}.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="/img/{p["img"]}.webp" as="image" fetchpriority="high">
<script type="application/ld+json">{ld}</script>
<link rel="preload" href="/fonts/carlito-bold.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/style.css?v={CSSV}">
</head>
<body>
{HEADER}
<main>
<section class="hero lp"><div class="wrap">
  <div>
    <nav class="crumbs" aria-label="Brotkrumen"><a href="/">Start</a> / <span>{p["nav"]}</span></nav>
    <span class="eyebrow">{p["eyebrow"]}</span>
    <h1>{p["h1"]}</h1>
    <p class="lead">{p["lead"]}</p>
    <div class="ctas"><a class="btn" href="#kontakt">Demo buchen <span class="arr">→</span></a><a class="btn alt" href="tel:+4915114162414">Anrufen</a></div>
    <p class="micro">Kostenlos, 30 Minuten. Danach wissen Sie, ob es geht und was es kostet. Oder anrufen: {TEL}</p>
  </div>
  <div class="heroimg"><picture><source srcset="/img/{p["img"]}.webp" type="image/webp"><img src="/img/{p["img"]}.jpg" alt="{p["alt"]}" width="900" height="506" fetchpriority="high"></picture></div>
</div></section>

<section class="soft"><div class="wrap lp-two">
  <div><h2>{p["problem"][0]}</h2><ul class="lp-list minus">{li(p["problem"][1])}</ul></div>
  <div><h2>{p["solution"][0]}</h2><ul class="lp-list plus">{li(p["solution"][1])}</ul></div>
</div></section>

<section><div class="wrap">
  <div class="sec-head"><h2>So geht es los.</h2><p>Schritt 1 bis 3 sind für Sie kostenlos. Die Gebühr startet erst, wenn der Roboter zuverlässig läuft.</p></div>
  <ol class="lp-steps"><li><b>Sie zeigen uns die Aufgabe</b>30 Minuten vor Ort oder per Video.</li><li><b>Aufnehmen</b>Ihr Team macht die Aufgabe ein paar Mal vor.</li><li><b>Trainieren</b>Der Roboter lernt an Ihrer Linie.</li><li><b>Produzieren</b>Erst jetzt beginnt die Monatsgebühr.</li></ol>
</div></section>

<section class="soft"><div class="wrap faq">
  <h2>Häufige Fragen.</h2>
  <div>{faq}</div>
</div></section>

{CONTACT}

<section class="lp-more"><div class="wrap"><b>Mehr dazu:</b> <a href="/">Startseite mit Rechenbeispiel</a>{others}</div></section>
</main>
<div class="mbar" id="mbar"><a class="btn alt" href="tel:+4915114162414">Anrufen</a><a class="btn" href="#kontakt">Demo buchen</a></div>
<script>(function(){{var b=document.getElementById("mbar"),h=document.querySelector(".hero"),c=document.querySelector("#kontakt");if(!("IntersectionObserver"in window)||!b)return;var hv=true,cv=false;function u(){{b.classList.toggle("on",!hv&&!cv)}}new IntersectionObserver(function(e){{hv=e[0].isIntersecting;u()}}).observe(h);new IntersectionObserver(function(e){{cv=e[0].isIntersecting;u()}}).observe(c);}})();</script>

{TAIL}'''

for p in PAGES:
    os.makedirs(p['slug'], exist_ok=True)
    open(f'{p["slug"]}/index.html', 'w', encoding='utf-8').write(page(p))

# sitemap
urls = [('/', 'de', '/en/'), ('/en/', 'en', '/')] + [(f'/{p["slug"]}/', 'de', None) for p in PAGES] + [('/video/','de','/en/video/'),('/en/video/','en','/video/')]
from datetime import date
out = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for u, lang, alt in urls:
    out.append(f'<url><loc>{BASE}{u}</loc><lastmod>{date.today()}</lastmod>')
    if alt:
        other = 'en' if lang == 'de' else 'de'
        out.append(f'<xhtml:link rel="alternate" hreflang="{lang}" href="{BASE}{u}"/><xhtml:link rel="alternate" hreflang="{other}" href="{BASE}{alt}"/>')
    out.append('</url>')
out.append('</urlset>')
open('sitemap.xml', 'w').write('\n'.join(out) + '\n')
print('built', len(PAGES), 'pages + sitemap')
