"""Additional landing pages, title/description overrides and extra FAQ entries.
Loaded by build_pages.py. Facts on this site must stay consistent across pages:
- parts up to about 1-2 kg, work area about 1 m2, one or two arms, two-finger gripper
- no investment, monthly fee below 70 % of today's cost of the position, fee starts with productive operation
"""

PRICE = 'Keine Investition. Die Monatsgebühr liegt immer unter 70&nbsp;% dessen, was die Stelle Sie heute kostet, und startet erst, wenn der Roboter zuverlässig läuft. <a href="/roboter-kosten/">Kaufen und Mieten im Vergleich</a>'
SAFE = 'Wir richten den Roboter nach den geltenden Regeln der Maschinensicherheit ein und machen die Gefährdungsbeurteilung mit Ihnen, bevor er startet.'

# shorter titles (Google cuts at about 60 characters) and descriptions (about 155)
TITLES = {
 'ki-produktionsautomatisierung': 'Produktionsautomatisierung mit KI | Ackermann Robotics',
 'automatisierung-stuttgart': 'Automatisierung Stuttgart &amp; Reutlingen | Ackermann Robotics',
 'roboter-mieten': 'Roboter mieten für die Produktion | Ackermann Robotics',
 'produktionshelfer-gesucht': 'Produktionshelfer gesucht? Roboter statt Neueinstellung',
 'kartons-aufrichten-automatisieren': 'Kartons aufrichten automatisieren | Ackermann Robotics',
 'kommissionieren-automatisieren': 'Kommissionieren automatisieren | Ackermann Robotics',
 'pick-and-place-automatisieren': 'Pick and Place automatisieren | Ackermann Robotics',
 'kognitive-robotik': 'Kognitive Robotik einfach erklärt | Ackermann Robotics',
 'physical-ai-produktion': 'Physical AI in der Produktion | Ackermann Robotics',
 'roboter-kosten': 'Was kostet ein Roboter in der Produktion? Kaufen vs. mieten',
}
DESCS = {
 'ki-produktionsautomatisierung': 'Produktionsautomatisierung mit KI: Roboter, die sehen, greifen und durch Vormachen lernen. Für Verpacken, Kommissionieren, Kartons. Keine Investition.',
 'kartons-aufrichten-automatisieren': 'Kartons aufrichten, falten und verschließen mit einem kognitiven Roboter. Auch bei wechselnden Formaten und kleinen Losen. Keine Investition.',
 'kognitive-robotik': 'Was ist kognitive Robotik? Roboter, die mit Kameras sehen, sich anpassen und durch Vormachen lernen. Für Handgriffe, an denen klassische Roboter scheitern.',
 'roboter-kosten': 'Was kostet ein Roboter für die Produktion wirklich? Arm, Greifer, Kameras, Integration und Wartung im Überblick. Und wie es ohne Investition geht.',
 'produktionshelfer-gesucht': 'Sie finden keine Produktionshelfer? Ein kognitiver Roboter übernimmt die Stelle: nie krank, 30 % günstiger, ohne Investition. Zahlung erst, wenn er läuft.',
}

# extra FAQ entries for existing pages (search terms buyers use + links to the new pages)
FAQ_ADD = {
 'ki-produktionsautomatisierung': [
  ('Welche Teile und Gewichte gehen?', 'Leichte Teile bis etwa 1 bis 2&nbsp;kg an einem Arbeitsplatz von rund einem Quadratmeter. <a href="/was-kann-der-roboter/">Eckdaten und Grenzen</a>'),
  ('Lohnt sich das bei kleinen Losgrößen?', 'Gerade dann. Neue Varianten lernt der Roboter durch Vormachen, und Sie investieren nichts, was sich amortisieren muss. <a href="/kleine-losgroessen-automatisieren/">Kleine Losgrößen automatisieren</a>')],
 'automatisierung-stuttgart': [
  ('Gibt es Fördermittel in Baden-Württemberg?', 'Ja. Mit dem Innovationsgutschein „Mittelstand trifft Start-ups“ bezuschusst das Land 50&nbsp;% der Kosten, bis zu 20.000&nbsp;€. <a href="/foerderung-automatisierung-baden-wuerttemberg/">Förderung im Überblick</a>')],
 'roboter-mieten': [
  ('Was ist der Unterschied zwischen Mieten, Leasing und Robotics as a Service?', 'Bei Miete und Leasing bezahlen Sie für eine Maschine. Bei Robotics as a Service bezahlen Sie für die erledigte Aufgabe, inklusive Installation, Betrieb und Wartung. <a href="/robotics-as-a-service/">Robotics as a Service erklärt</a>')],
 'produktionshelfer-gesucht': [
  ('Ist das eine Alternative zur Zeitarbeit?', 'Für wiederkehrende Handgriffe mit leichten Teilen ja: feste Monatsgebühr statt Stundensatz, und der Roboter bleibt. <a href="/zeitarbeit-alternative-produktion/">Roboter und Zeitarbeit im Vergleich</a>')],
 'kartons-aufrichten-automatisieren': [
  ('Kartonaufrichter oder Roboter: Was passt wann?', 'Läuft ein Format in großer Menge, ist ein Kartonaufrichter schneller. Wechseln die Formate oft, rechnet sich der Roboter. <a href="/kartonaufrichter-oder-roboter/">Zum Vergleich</a>')],
 'verpacken-automatisieren': [
  ('Was ist ein Verpackungsroboter?', 'Ein Roboter, der Produkte greift und in Kartons, Trays oder Blister legt. Klassische Verpackungsroboter brauchen Teile in fester Lage. Unser kognitiver Roboter sieht, wie jedes Teil liegt.'),
  ('Geht das auch für Sets und Displays?', 'Ja. Sets zusammenstellen, Displays bestücken und Umpacken lernt der Roboter durch Vormachen. <a href="/konfektionierung-automatisieren/">Konfektionierung automatisieren</a>')],
 'kommissionieren-automatisieren': [
  ('Ist das ein Kommissionierroboter fürs Lager?', 'Nein. Kommissionierroboter im Lager holen Ware aus Regalen. Unser Roboter stellt an einem festen Arbeitsplatz Teilesätze für Montage und Versand zusammen.')],
 'pick-and-place-automatisieren': [
  ('Ist das ein Handhabungsroboter?', 'Ja: ein Handhabungs- oder Bestückungsroboter, der Teile greift und umsetzt. Der Unterschied zum klassischen Roboter: Die Teile müssen nicht fest positioniert sein.'),
  ('Kann er Maschinen be- und entladen?', 'Für leichte Teile prüfen wir das kostenlos an Ihrer Maschine. <a href="/maschinenbeschickung-automatisieren/">Maschinenbeschickung automatisieren</a>')],
 'kognitive-robotik': [
  ('Muss der Roboter programmiert werden?', 'Nein. Ihr Team macht die Aufgabe vor, die KI lernt daraus. <a href="/roboter-ohne-programmierung/">Roboter ohne Programmierung</a>')],
 'roboter-kosten': [
  ('Gibt es Fördermittel?', 'In Baden-Württemberg ja: Der Innovationsgutschein „Mittelstand trifft Start-ups“ bezuschusst 50&nbsp;% der Kosten, bis zu 20.000&nbsp;€. <a href="/foerderung-automatisierung-baden-wuerttemberg/">Förderung im Überblick</a>')],
}


def extend(PAGES, VS, CARD, DT):
    for p in PAGES:
        if p['slug'] in TITLES: p['title'] = TITLES[p['slug']]
        if p['slug'] in DESCS: p['desc'] = DESCS[p['slug']]
        p['faq'] = list(p['faq']) + FAQ_ADD.get(p['slug'], [])
        if p['slug'] not in ('automatisierung-stuttgart', 'kognitive-robotik', 'physical-ai-produktion'):
            p.setdefault('service', True)

    usecases = ('<div class="cards c4">'
        + CARD('/kartons-aufrichten-automatisieren/', 'Kartons aufrichten', 'Falten und verschließen, auch bei wechselnden Formaten.')
        + CARD('/verpacken-automatisieren/', 'Verpacken', 'Produkte in Kartons und Trays legen, auch wenn sie nie gleich liegen.')
        + CARD('/kommissionieren-automatisieren/', 'Kommissionieren', 'Teilesätze für die Montage, auch bei vielen Varianten.')
        + CARD('/pick-and-place-automatisieren/', 'Teile umsetzen', 'Zwischen Behältern, Bändern und Maschinen.')
        + '</div>')

    PAGES.extend([
     # ---------------------------------------------------------------- specs
     dict(slug='was-kann-der-roboter', nav='Eckdaten und Grenzen', service=True,
      title='KI-Roboter: Eckdaten und Grenzen | Ackermann Robotics',
      desc='Welche Teile, welches Gewicht, welcher Takt? Die Eckdaten unserer KI-Roboter für die Produktion. Und ehrlich: wofür sie sich nicht eignen.',
      eyebrow='Technik', h1='Was unser Roboter kann. Und was nicht.',
      lead='Bevor Sie Zeit in eine Demo stecken, sollen Sie wissen, ob Ihre Aufgabe grundsätzlich passt. Hier stehen die Eckdaten: Teilegewicht, Arbeitsbereich, Greifer, Lernen und die Grenzen.',
      img='kitting', alt='KI-Roboterarm greift Teile aus einem Behälter',
      problem=('Dafür eignet er sich nicht.', ['Schwere Teile: Über etwa 2&nbsp;kg pro Teil ist ein klassischer Industrieroboter die bessere Wahl.', 'Takte im Sekundenbereich mit immer gleichen Teilen. Das kann eine klassische Anlage schneller.', 'Fügen mit hohen Kräften oder Toleranzen im Hundertstelbereich.', 'Palettieren über mehrere Lagen und größere Entfernungen.']),
      solution=('Dafür ist er gebaut.', ['Leichte Teile bis etwa 1 bis 2&nbsp;kg, die jedes Mal etwas anders liegen.', 'Wechselnde Varianten und kleine Lose.', 'Handgriffe an einem festen Arbeitsplatz von rund einem Quadratmeter.', 'Aufgaben, für die ein Mensch zwei Hände braucht. Dafür arbeiten zwei Arme zusammen.']),
      extra='<section><div class="wrap"><div class="sec-head"><h2>Die Eckdaten.</h2><p>Richtwerte für die Einschätzung. Ob Ihre Aufgabe passt, zeigt die kostenlose Demo an Ihren Teilen.</p></div>'
       + DT(['Merkmal', 'Richtwert'], [
          ['Teilegewicht', 'bis etwa 1 bis 2&nbsp;kg pro Teil'],
          ['Arbeitsbereich', 'rund 1&nbsp;m² pro Station'],
          ['Arme', 'einer oder zwei, je nach Aufgabe'],
          ['Greifer', 'Zweifingergreifer'],
          ['Wahrnehmung', 'Kameras. Der Roboter erkennt Lage und Ausrichtung der Teile.'],
          ['Einrichten', 'Lernen durch Vormachen. Keine Programmierung auf Ihrer Seite.'],
          ['Neue Variante', 'kurz vormachen. Das Nachtrainieren ist in der Gebühr enthalten.'],
          ['Betreuung', 'Operator aus der Ferne während Ihrer Produktionszeiten'],
          ['Wartung und Reparatur', 'in der Monatsgebühr enthalten'],
          ['Vorhandene Roboter', 'binden wir oft ein und rüsten Kameras und Sensoren nach'],
          ['Kosten', 'keine Investition. Monatsgebühr unter 70&nbsp;% der heutigen Stellenkosten, erst ab Produktivbetrieb.']])
       + '</div></section>'
       + '<section class="soft"><div class="wrap"><div class="sec-head"><h2>Und der Takt?</h2><p>An einer Linie bestimmt die langsamste Station das Tempo. Deshalb messen wir im Training an Ihrer Linie, ob der Roboter Ihren Takt und Ihre Qualität hält. Erst wenn er das zuverlässig tut, beginnt die Monatsgebühr.</p></div></div></section>',
      faq=[('Wie schwer dürfen die Teile sein?', 'Bis etwa 1 bis 2&nbsp;kg pro Teil, je nach Greifer und Bewegung. Ob Ihr Teil passt, prüfen wir in der kostenlosen Demo.'),
           ('Wie schnell arbeitet der Roboter?', 'Das hängt von der Aufgabe ab. Für Takte im Sekundenbereich mit immer gleichen Teilen ist eine klassische Anlage schneller. Bei wechselnden Teilen messen wir den Takt im Training an Ihrer Linie. Sie zahlen erst, wenn er passt.'),
           ('Braucht der Roboter Vorrichtungen oder Zuführtechnik?', 'In der Regel nicht. Er sieht mit Kameras, wo das Teil liegt, und greift aus Ihren Behältern.'),
           ('Wie viel Platz braucht er?', 'Der Arbeitsbereich ist rund ein Quadratmeter. Dazu kommt Platz für Behälter, Kartons und die Absicherung. Wie das an Ihrer Linie aussieht, klären wir vor Ort.'),
           ('Kann er neben unseren Mitarbeitern arbeiten?', SAFE)]),

     # ---------------------------------------------------------------- RaaS
     dict(slug='robotics-as-a-service', nav='Robotics as a Service', service=True,
      title='Robotics as a Service (RaaS) erklärt | Ackermann Robotics',
      desc='Robotics as a Service (RaaS): Roboter nutzen statt kaufen. Wie das Modell funktioniert, was es kostet und wie es sich von Kauf und Leasing unterscheidet.',
      eyebrow='Robotics as a Service (RaaS)', h1='Robotics as a Service: Roboter nutzen statt kaufen.',
      lead='Robotics as a Service, kurz RaaS, heißt: Sie kaufen keinen Roboter, sondern bezahlen für eine erledigte Aufgabe. Der Anbieter stellt Roboter, Software, Betrieb und Wartung. Sie zahlen eine laufende Gebühr.',
      img='hero', alt='KI-Roboter richtet Kartons in einer Produktion auf',
      problem=('Was Kauf und Leasing gemeinsam haben.', ['Sie zahlen für die Anlage, egal ob sie die Aufgabe am Ende schafft.', 'Integration, Programmierung und Sicherheitstechnik kommen dazu.', 'Für Störungen, Wartung und neue Varianten brauchen Sie eigene Leute oder einen Dienstleister.']),
      solution=('Was RaaS bei uns heißt.', ['Keine Investition: kein Kauf, keine Anzahlung, keine Integrationskosten.', 'Eine feste Monatsgebühr, immer unter 70&nbsp;% dessen, was die Stelle Sie heute kostet.', 'Installation, Training, Wartung, Reparatur und Fernbetreuung sind enthalten.', 'Die Gebühr startet erst, wenn der Roboter die Aufgabe zuverlässig erledigt.']),
      extra='<section><div class="wrap"><div class="sec-head"><h2>Kauf, Leasing und RaaS im Vergleich.</h2></div>'
       + DT(['', 'Kauf', 'Leasing', 'RaaS bei Ackermann Robotics'], [
          ['Investition vorab', 'hoch', 'gering', 'keine'],
          ['Integration und Programmierung', 'zahlen Sie', 'zahlen Sie', 'enthalten'],
          ['Wartung und Reparatur', 'Ihre Sache', 'meist Ihre Sache', 'enthalten'],
          ['Neue Variante', 'neu programmieren lassen', 'neu programmieren lassen', 'vormachen, Nachtrainieren enthalten'],
          ['Risiko, dass es nicht klappt', 'bei Ihnen', 'bei Ihnen', 'bei uns: keine Zahlung, bis es läuft'],
          ['Passt am besten für', 'große Stückzahlen, Aufgabe ändert sich nie', 'wie Kauf, mit verteilter Zahlung', 'wechselnde Teile, kein eigenes Robotik-Team']])
       + '</div></section>'
       + '<section class="soft"><div class="wrap"><div class="sec-head"><h2>Wie RaaS abgerechnet wird.</h2><p>Am Markt gibt es drei Modelle: eine feste Monatsgebühr, Abrechnung pro Stunde oder Abrechnung pro Stück. Wir rechnen mit einer festen Monatsgebühr ab. So wissen Sie vorher, was die Aufgabe kostet, und können es direkt mit den Kosten der Stelle vergleichen.</p></div></div></section>',
      faq=[('Was bedeutet Robotics as a Service?', 'Robotics as a Service (RaaS) ist ein Modell, bei dem Sie einen Roboter nicht kaufen, sondern für seine Leistung bezahlen. Roboter, Software, Betrieb und Wartung kommen vom Anbieter.'),
           ('Was ist der Unterschied zwischen RaaS und Leasing?', 'Beim Leasing finanzieren Sie eine Maschine. Ob sie Ihre Aufgabe schafft, bleibt Ihr Risiko, ebenso Integration und Wartung. Bei RaaS bezahlen Sie für die erledigte Aufgabe, inklusive Betrieb.'),
           ('Was kostet RaaS?', PRICE),
           ('Wem gehört der Roboter?', 'In der Regel uns. Er steht bei Ihnen, wir betreiben und warten ihn. Wenn Sie schon einen Roboter haben, binden wir ihn oft ein.'),
           ('Für wen lohnt sich RaaS?', 'Für Betriebe mit wechselnden Teilen und ohne eigenes Robotik-Team. Wer eine einzige Aufgabe in großer Stückzahl über Jahre fährt, ist mit einer gekauften Anlage oft besser bedient.')]),

     # ---------------------------------------------------------------- Zeitarbeit
     dict(slug='zeitarbeit-alternative-produktion', nav='Alternative zur Zeitarbeit', service=True,
      title='Alternative zur Zeitarbeit in der Produktion: KI-Roboter',
      desc='Zeitarbeit in der Produktion ist teuer und endet nach 18 Monaten. Ein KI-Roboter übernimmt die Stelle dauerhaft: feste Monatsgebühr, keine Investition.',
      eyebrow='Personal in der Produktion', h1='Die Alternative zur Zeitarbeit: ein Roboter, der bleibt.',
      lead='Zeitarbeit überbrückt Engpässe. Als Dauerlösung wird sie teuer: Der Verrechnungssatz liegt deutlich über dem Lohn, die Leute wechseln, und nach 18 Monaten ist grundsätzlich Schluss. Für wiederkehrende Handgriffe gibt es jetzt eine Alternative.',
      img='folding', alt='Roboterarm faltet einen Karton an der Linie',
      problem=('Was Zeitarbeit auf Dauer kostet.', ['Sie zahlen für jede Stunde den Verrechnungssatz: Lohn plus Aufschlag des Verleihers.', 'Nach neun Monaten gilt grundsätzlich Equal Pay, nach 18 Monaten endet die Überlassung desselben Mitarbeiters. Tarifverträge können davon abweichen.', 'Jeder Wechsel heißt neu einarbeiten. Das Wissen geht mit.', 'Kurzfristige Ausfälle treffen Sie trotzdem.']),
      solution=('Was der Roboter anders macht.', ['Feste Monatsgebühr statt Stundensatz. Sie wissen vorher, was die Aufgabe kostet.', 'Er bleibt. Was er gelernt hat, geht nicht mehr verloren.', 'Zusatzschicht, Nacht und Wochenende zum gleichen Satz.', 'Keine Investition. Die Gebühr startet erst, wenn er zuverlässig läuft.']),
      extra='<section><div class="wrap"><div class="sec-head"><h2>Zeitarbeit und Roboter im Vergleich.</h2><p>Beides hat seinen Platz. Zeitarbeit ist schneller da und kann fast alles. Der Roboter rechnet sich bei Dauerbedarf.</p></div>'
       + DT(['', 'Zeitarbeit', 'KI-Roboter'], [
          ['Abrechnung', 'Stundensatz, jede Stunde', 'feste Monatsgebühr'],
          ['Start', 'kurzfristig', 'nach Demo, Aufnahme und Training'],
          ['Tätigkeiten', 'fast jede', 'wiederkehrende Handgriffe mit leichten Teilen'],
          ['Einarbeitung', 'bei jedem Wechsel neu', 'einmal vormachen'],
          ['Nacht und Wochenende', 'mit Zuschlägen', 'zum gleichen Satz'],
          ['Dauer', 'grundsätzlich höchstens 18 Monate je Mitarbeiter', 'bleibt an der Linie']])
       + '</div></section>'
       + '<section class="soft"><div class="wrap"><div class="sec-head"><h2>So rechnen Sie es für Ihre Stelle.</h2><p>Nehmen Sie Ihren Verrechnungssatz mal die Stunden im Monat. Ein Beispiel: 30&nbsp;€ pro Stunde mal 160 Stunden sind 4.800&nbsp;€ im Monat für eine Schicht. Vergleichen Sie das mit unserer Monatsgebühr: Sie liegt immer unter 70&nbsp;% dessen, was die Stelle Sie heute kostet. Den Rechner finden Sie auf der <a href="/#kontakt">Startseite</a>.</p></div></div></section>',
      faq=[('Für welche Stellen ist ein Roboter eine Alternative zur Zeitarbeit?', 'Für wiederkehrende Handgriffe mit leichten Teilen: Kartons aufrichten, Verpacken, Kommissionieren, Teile umsetzen. <a href="/was-kann-der-roboter/">Eckdaten und Grenzen</a>'),
           ('Wie schnell ist der Roboter einsatzbereit?', 'Nicht von heute auf morgen. Nach der Demo folgen Aufnahme und Training an Ihrer Linie, den Zeitplan nennen wir Ihnen nach der Demo. Für akute Engpässe bleibt Zeitarbeit die schnellere Lösung, für Dauerbedarf ist der Roboter die günstigere.'),
           ('Was kostet der Roboter im Vergleich zur Zeitarbeit?', PRICE),
           ('Was, wenn es bei unserer Aufgabe nicht klappt?', 'Dann zahlen Sie nichts. Die Gebühr beginnt erst, wenn der Roboter die Aufgabe zuverlässig erledigt.')]),

     # ---------------------------------------------------------------- machine tending
     dict(slug='maschinenbeschickung-automatisieren', nav='Maschinenbeschickung', service=True,
      title='Maschinenbeschickung automatisieren | Ackermann Robotics',
      desc='Maschinen be- und entladen mit einem KI-Roboter: Teile aus dem Behälter greifen und einlegen, auch bei wechselnden Teilen. Keine Investition.',
      eyebrow='Anwendung', h1='Maschinen&shy;beschickung automatisieren. Auch bei wechselnden Teilen.',
      lead='An vielen Maschinen steht ein Mitarbeiter, legt Teile ein und nimmt sie wieder heraus. Für leichte Teile kann das ein kognitiver Roboter übernehmen: Er greift sie aus dem Behälter, legt sie ein und setzt die fertigen Teile ab. Ob es an Ihrer Maschine geht, prüfen wir kostenlos.',
      img='kitting', alt='Roboterarm greift Teile aus einem Behälter und setzt sie um',
      problem=('Warum an der Maschine oft noch ein Mensch steht.', ['Ein klassischer Beladeroboter braucht Teile in fester Lage: Paletten, Schubladen, Zuführtechnik.', 'Die Vorrichtungen passen nur für ein Teil. Bei kleinen Losen rechnet sich das nicht.', 'Also wartet ein Mitarbeiter auf das Zyklusende, statt etwas Wertvolleres zu tun.']),
      solution=('So macht es der kognitive Roboter.', ['Kameras erkennen, wie das Rohteil im Behälter liegt.', 'Ihr Team macht Einlegen und Entnehmen ein paar Mal vor.', 'Neues Teil: kurz vormachen statt Vorrichtung bauen.', 'Keine Investition, feste Monatsgebühr, Zahlung erst, wenn er läuft.']),
      extra='<section><div class="wrap"><div class="sec-head"><h2>Wo es passt und wo nicht.</h2><p>Gut geeignet sind leichte Teile bis etwa 1 bis 2&nbsp;kg, die mit etwas Spiel eingelegt werden: in Nester und Aufnahmen an Prüf-, Montage- und Verpackungsstationen. Nicht unser Feld sind schwere Werkstücke, Spannmittel mit sehr engen Toleranzen und Maschinen mit Zykluszeiten von wenigen Sekunden.</p></div></div></section>',
      faq=[('Welche Maschinen kann der Roboter beladen?', 'Das hängt von Teil, Aufnahme und Takt ab. Typisch sind Prüf-, Montage- und Verpackungsstationen mit leichten Teilen. Wir prüfen es kostenlos an Ihrer Maschine.'),
           ('Braucht der Roboter Paletten oder Zuführtechnik?', 'In der Regel nicht. Er sieht mit Kameras, wie die Teile liegen, und greift aus Ihren Behältern.'),
           ('Ist das sicher für unsere Mitarbeiter?', SAFE),
           ('Was kostet das?', PRICE)]),

     # ---------------------------------------------------------------- co-packing
     dict(slug='konfektionierung-automatisieren', nav='Konfektionierung', service=True,
      title='Konfektionierung automatisieren | Ackermann Robotics',
      desc='Sets zusammenstellen, Displays bestücken, umpacken: Konfektionierung mit KI-Roboter automatisieren, auch bei wechselnden Aktionen und kleinen Losen.',
      eyebrow='Anwendung', h1='Konfektionierung automatisieren. Auch wenn jede Aktion anders ist.',
      lead='Sets zusammenstellen, Displays bestücken, Ware umpacken: Konfektionierung ändert sich mit jeder Aktion und bleibt deshalb Handarbeit. Ein kognitiver Roboter lernt die neue Zusammenstellung durch Vormachen.',
      img='boxes', alt='Roboterarm legt Produkte in einen Karton',
      problem=('Warum Konfektionierung Handarbeit bleibt.', ['Jede Aktion ist anders: neue Produkte, neue Sets, neue Displays.', 'Die Lose sind klein. Eine eigene Anlage lohnt sich dafür nicht.', 'Saisonspitzen brauchen kurzfristig viele Hände, die schwer zu bekommen sind.']),
      solution=('So macht es der kognitive Roboter.', ['Ihr Team stellt das Set ein paar Mal zusammen, der Roboter lernt daraus.', 'Kameras sehen, wo welches Produkt liegt.', 'Neue Aktion: kurz vormachen. Das Nachtrainieren ist inklusive.', 'Keine Investition, feste Monatsgebühr, Zahlung erst, wenn er läuft.']),
      extra='<section><div class="wrap"><div class="sec-head"><h2>Typische Aufgaben.</h2></div><div class="cards c4">'
       + CARD('/kommissionieren-automatisieren/', 'Sets zusammenstellen', 'Mehrere Artikel zu einem Set oder einer Verkaufseinheit.')
       + CARD('/verpacken-automatisieren/', 'Displays bestücken', 'Produkte in Trays und Displays legen.')
       + CARD('/pick-and-place-automatisieren/', 'Umpacken', 'Aus dem Großgebinde in die Verkaufseinheit.')
       + CARD('/kartons-aufrichten-automatisieren/', 'Kartons aufrichten', 'Aufrichten, befüllen, verschließen.')
       + '</div></div></section>',
      faq=[('Lohnt sich das bei ständig wechselnden Aktionen?', 'Genau dafür ist es gedacht. Eine neue Zusammenstellung lernt der Roboter durch Vormachen, ohne neue Programmierung. Das Nachtrainieren ist in der Gebühr enthalten.'),
           ('Welche Produkte gehen?', 'Leichte, formstabile Produkte bis etwa 1 bis 2&nbsp;kg. Sehr weiche, rutschige oder zerbrechliche Produkte prüfen wir in der Demo.'),
           ('Arbeiten Sie auch für Lohnverpacker und Co-Packer?', 'Ja. Für Betriebe mit vielen wechselnden Aufträgen passt das Modell besonders gut.'),
           ('Was kostet das?', PRICE)]),

     # ---------------------------------------------------------------- plastics
     dict(slug='automatisierung-kunststoffverarbeitung', nav='Kunststoffverarbeitung', service=True,
      title='Automatisierung Kunststoffverarbeitung | Ackermann Robotics',
      desc='Für Spritzgießer und Kunststoffverarbeiter: KI-Roboter legen Teile in Trays, verpacken und kommissionieren, auch bei vielen Varianten. Keine Investition.',
      eyebrow='Branche: Kunststoff', h1='Automatisierung für Kunststoff&shy;verarbeiter. Nach der Maschine beginnt die Handarbeit.',
      lead='Die Spritzgießmaschine läuft automatisch, oft auch die Entnahme. Danach wird es manuell: Teile sortieren, in Trays legen, verpacken, Kartons aufrichten. Diese Handgriffe übernimmt ein kognitiver Roboter, auch bei vielen Werkzeugen und kleinen Losen.',
      img='boxes', alt='Roboterarm verpackt Kunststoffteile in einen Karton',
      problem=('Was Kunststoffverarbeiter kennen.', ['Viele Werkzeuge, häufige Wechsel: Für jedes Teil eine eigene Automatisierung lohnt sich nicht.', 'Teile fallen als Schüttgut in den Behälter und liegen jedes Mal anders.', 'Verpacken und Abstapeln hängen an Helfern, die schwer zu finden sind, besonders für Nacht- und Wochenendschichten.']),
      solution=('Was der kognitive Roboter übernimmt.', ['Teile aus dem Behälter oder vom Band greifen und in Trays oder Kartons legen.', 'Kartons aufrichten, befüllen und verschließen.', 'Teilesätze aus mehreren Artikeln zusammenstellen.', 'Werkzeugwechsel: neues Teil kurz vormachen, ohne neue Programmierung.']),
      extra='<section><div class="wrap"><div class="sec-head"><h2>Die Aufgaben im Einzelnen.</h2></div>' + usecases
       + '<div class="sec-head" style="margin-top:56px"><h2>Was wir nicht machen.</h2><p>Entnahme aus dem Werkzeug im Sekundentakt, Angüsse abtrennen, Entgraten oder Prüfen. Dafür gibt es bewährte Technik. Wir setzen dort an, wo heute ein Mensch die Teile in die Hand nimmt.</p></div></div></section>',
      faq=[('Funktioniert das bei häufigen Werkzeugwechseln?', 'Ja. Ein neues Teil lernt der Roboter durch Vormachen, ohne neue Programmierung und ohne neue Vorrichtung. Das Nachtrainieren ist in der Gebühr enthalten.'),
           ('Geht das auch im Dreischichtbetrieb?', 'Ja. Der Roboter fährt jede Schicht zum gleichen Satz. Unser Operator betreut ihn aus der Ferne während Ihrer Produktionszeiten.'),
           ('Welche Kunststoffteile kann er greifen?', 'Formstabile Teile bis etwa 1 bis 2&nbsp;kg. Sehr kleine, dünnwandige oder empfindliche Sichtteile prüfen wir in der Demo an Ihren Teilen.'),
           ('Was kostet das?', PRICE)]),

     # ---------------------------------------------------------------- electronics
     dict(slug='automatisierung-elektronikfertigung', nav='Elektronikfertigung', service=True,
      title='Automatisierung Elektronikfertigung | Ackermann Robotics',
      desc='Für Elektro- und Elektronikhersteller: KI-Roboter verpacken Baugruppen, bestücken Trays und stellen Teilesätze zusammen, auch bei hoher Variantenvielfalt.',
      eyebrow='Branche: Elektro und Elektronik', h1='Automatisierung für Elektro- und Elektronik&shy;hersteller.',
      lead='Die Bestückung ist längst automatisiert. Davor und danach bleibt viel Handarbeit: Bauteile bereitstellen, Baugruppen in Trays legen, Geräte verpacken, Beipack zusammenstellen. Diese Handgriffe übernimmt ein kognitiver Roboter, auch bei vielen Varianten.',
      img='packing', alt='Roboterarme stellen Teilesätze zusammen',
      problem=('Was Elektronikfertiger kennen.', ['Hohe Variantenvielfalt, kleine Lose: Jede Variante zu programmieren lohnt sich nicht.', 'Schalter, Stecker, Gehäuse und Baugruppen liegen lose im Behälter.', 'Verpackung und Beipack ändern sich je Kunde und Auftrag.']),
      solution=('Was der kognitive Roboter übernimmt.', ['Baugruppen und Geräte in Trays, Blister und Kartons legen.', 'Teilesätze und Beipack für Montage und Versand zusammenstellen.', 'Teile zwischen Behältern, Bändern und Prüfplätzen umsetzen.', 'Neue Variante: kurz vormachen statt neu programmieren.']),
      extra='<section><div class="wrap"><div class="sec-head"><h2>Die Aufgaben im Einzelnen.</h2></div>' + usecases
       + '<div class="sec-head" style="margin-top:56px"><h2>ESD, Kabel und Präzision: ehrlich eingeordnet.</h2><p>Für ESD-empfindliche Baugruppen klären wir vor der Demo, welche Schutzmaßnahmen an Ihrem Arbeitsplatz gelten. Biegeschlaffe Teile wie lose Kabel und Leitungssätze sind für Roboter schwierig. Ob Ihre Aufgabe geht, zeigt die Demo. Nicht unser Feld sind SMD-Bestückung, Löten und Stecken mit engen Toleranzen.</p></div></div></section>',
      faq=[('Kann der Roboter Leiterplatten und Baugruppen handhaben?', 'Das hängt von Größe, Empfindlichkeit und ESD-Anforderungen ab. Wir prüfen es in der kostenlosen Demo an Ihren Teilen.'),
           ('Geht das auch in der Kabelkonfektion?', 'Verpacken und Zusammenstellen fertiger Kabel und Leitungen prüfen wir gern. Lose Kabel sind biegeschlaff und damit anspruchsvoll. Die Demo zeigt, ob es bei Ihnen geht.'),
           ('Wir haben viele Varianten und kleine Lose. Lohnt sich das?', 'Gerade dann. Neue Varianten lernt der Roboter durch Vormachen, und Sie investieren nichts, was sich amortisieren muss. <a href="/kleine-losgroessen-automatisieren/">Kleine Losgrößen automatisieren</a>'),
           ('Was kostet das?', PRICE)]),

     # ---------------------------------------------------------------- case erector vs robot
     dict(slug='kartonaufrichter-oder-roboter', nav='Kartonaufrichter oder Roboter', service=True,
      title='Kartonaufrichter oder Roboter? | Ackermann Robotics',
      desc='Kartonaufrichter oder KI-Roboter? Vergleich nach Stückzahl, Formatwechsel und Kosten. Für wechselnde Formate und kleine Lose, ohne Investition.',
      eyebrow='Vergleich', h1='Kartonaufrichter oder Roboter? Es kommt auf Ihre Formate an.',
      lead='Ein Kartonaufrichter ist unschlagbar, wenn tausende Kartons im selben Format laufen. Bei vielen Formaten und kleinen Losen steht er oft still oder wird umgerüstet. Dann ist ein Roboter, der Kartons aufrichtet, befüllt und verschließt, die bessere Wahl.',
      img='folding', alt='Roboterarm richtet einen Karton auf',
      problem=('Wo der Kartonaufrichter an Grenzen kommt.', ['Formatwechsel heißt umrüsten. Bei vielen Formaten am Tag kostet das Zeit.', 'Die Maschine macht nur den Karton. Befüllen und Verschließen brauchen weitere Technik oder Hände.', 'Sie investieren vorab, auch wenn die Auslastung gering ist.']),
      solution=('Was der Roboter anders macht.', ['Neues Format: kurz vormachen statt umrüsten.', 'Aufrichten, befüllen und verschließen an einem Platz.', 'Keine Investition. Feste Monatsgebühr, erst wenn er zuverlässig läuft.', 'Wartung, Reparatur und Nachtrainieren sind enthalten.']),
      extra='<section><div class="wrap"><div class="sec-head"><h2>Der Vergleich.</h2><p>Kartonaufrichter und Schachtelaufrichter richten Versandkartons auf, Faltschachtelaufrichter die dünneren Faltschachteln. Für alle gilt dieselbe Abwägung.</p></div>'
       + DT(['', 'Kartonaufrichter (Maschine)', 'KI-Roboter'], [
          ['Stärke', 'sehr hohe Stückzahlen im selben Format', 'wechselnde Formate und kleine Lose'],
          ['Tempo', 'höher', 'niedriger'],
          ['Formatwechsel', 'umrüsten', 'vormachen'],
          ['Umfang', 'richtet den Karton auf', 'richtet auf, befüllt und verschließt'],
          ['Kosten', 'Kauf oder Leasing', 'Monatsgebühr, keine Investition'],
          ['Wartung', 'Ihre Sache', 'enthalten']])
       + '<div class="sec-head" style="margin-top:44px"><p><b>Die Faustregel:</b> Läuft bei Ihnen ein Format in großer Menge, nehmen Sie einen Kartonaufrichter. Wechseln die Formate oft und faltet heute ein Mensch, rechnet sich der Roboter.</p></div></div></section>',
      faq=[('Ab welcher Stückzahl lohnt sich ein Kartonaufrichter?', 'Wenn ein Format in großer Menge durchläuft und selten gewechselt wird. Bei vielen Formaten und kleinen Losen frisst das Umrüsten den Vorteil auf.'),
           ('Ist der Roboter so schnell wie ein Kartonaufrichter?', 'Nein. Bei einem einzigen Format in großer Menge ist die Maschine schneller. Der Roboter ist dort im Vorteil, wo Formate wechseln und heute ein Mensch faltet.'),
           ('Kann der Roboter auch Faltschachteln aufrichten?', 'Das prüfen wir in der kostenlosen Demo an Ihren Zuschnitten.'),
           ('Was kostet das?', PRICE)]),

     # ---------------------------------------------------------------- high mix low volume
     dict(slug='kleine-losgroessen-automatisieren', nav='Kleine Losgrößen', service=True,
      title='Kleine Losgrößen automatisieren | Ackermann Robotics',
      desc='Viele Varianten, kleine Lose: Warum klassische Automatisierung sich dann nicht rechnet und wie KI-Roboter, die durch Vormachen lernen, die Lücke schließen.',
      eyebrow='Variantenreiche Fertigung', h1='Kleine Losgrößen automatisieren. Auch bei vielen Varianten.',
      lead='Klassische Automatisierung rechnet sich über die Stückzahl. Bei vielen Varianten und kleinen Losen fressen Programmierung, Vorrichtungen und Umrüsten den Nutzen auf. Ein Roboter, der neue Teile durch Vormachen lernt, ändert diese Rechnung.',
      img='packing', alt='KI-Roboterarme arbeiten mit wechselnden Teilen',
      problem=('Warum sich kleine Lose bisher nicht rechnen.', ['Jede Variante braucht ein eigenes Programm.', 'Jedes Teil braucht eigene Vorrichtungen und Zuführtechnik.', 'Umrüsten kostet Zeit, in der nichts produziert wird.', 'Die Investition verteilt sich auf zu wenige Teile.']),
      solution=('Was sich mit KI-Robotern ändert.', ['Neue Variante: vormachen statt programmieren.', 'Kameras statt Vorrichtungen: Der Roboter sieht, wie das Teil liegt.', 'Keine Investition, die sich amortisieren muss.', 'Das Nachtrainieren für neue Teile ist in der Gebühr enthalten.']),
      extra='<section><div class="wrap"><div class="sec-head"><h2>High Mix, Low Volume: Dafür sind KI-Roboter gemacht.</h2><p>Viele Varianten, kleine Stückzahlen je Variante. Genau hier bleiben Handgriffe bis heute beim Menschen, und genau hier setzen wir an.</p></div>' + usecases + '</div></section>',
      faq=[('Ab welcher Losgröße lohnt sich ein KI-Roboter?', 'Es gibt keine feste Grenze, weil Sie nichts investieren. Entscheidend ist, dass sich die Handgriffe ähneln: gleiche Art von Aufgabe, wechselnde Teile.'),
           ('Wie lange dauert es, eine neue Variante anzulernen?', 'Das hängt vom Teil ab. Ähnliche Teile lernt der Roboter schneller als ganz neue Handgriffe. Das Nachtrainieren ist in der Gebühr enthalten.'),
           ('Was bedeutet High Mix, Low Volume?', 'Eine Fertigung mit vielen Varianten und kleinen Stückzahlen je Variante. Für klassische Automatisierung ist das der schwierigste Fall, weil jede Variante Programmierung und Vorrichtungen braucht.'),
           ('Was kostet das?', PRICE)]),

     # ---------------------------------------------------------------- no-code teaching
     dict(slug='roboter-ohne-programmierung', nav='Roboter ohne Programmierung',
      title='Roboter ohne Programmierung anlernen | Ackermann Robotics',
      desc='Roboter ohne Programmierkenntnisse einrichten: der Unterschied zwischen Teach-in, Handführung und Lernen durch Vormachen, und was das für Sie heißt.',
      eyebrow='Technologie', h1='Roboter ohne Programmierung. Vormachen statt Code.',
      lead='Bisher brauchte jeder Roboter jemanden, der ihn programmiert oder teacht. Kognitive Roboter lernen anders: Ihr Team macht die Aufgabe vor, die KI lernt daraus und passt die Bewegung an, wenn ein Teil anders liegt.',
      img='hero', alt='KI-Roboter lernt eine Aufgabe in der Produktion',
      problem=('Wie Roboter bisher eingerichtet werden.', ['Programmieren: Ein Spezialist schreibt jede Bewegung als Programm.', 'Teach-in: Jeder Punkt der Bahn wird mit dem Handbediengerät angefahren und gespeichert.', 'Handführung beim Cobot: schneller, aber der Roboter fährt danach dieselbe starre Bahn.', 'In allen drei Fällen gilt: Liegt das Teil anders, stimmt die Bahn nicht mehr.']),
      solution=('Wie Lernen durch Vormachen funktioniert.', ['Ihr Team macht die Aufgabe mit einem Handgreifer vor.', 'Dabei wird aufgezeichnet, wie die Teile liegen und wie gegriffen wird.', 'Die KI lernt daraus keine Bahn, sondern die Aufgabe.', 'Liegt ein Teil anders, passt der Roboter seine Bewegung an.']),
      extra='<section><div class="wrap"><div class="sec-head"><h2>Vier Wege, einen Roboter einzurichten.</h2></div>'
       + DT(['Verfahren', 'Wer richtet ein', 'Wenn das Teil anders liegt'], [
          ['Programmieren', 'Robotik-Spezialist', 'ohne zusätzliches Kamerasystem: alte Bahn'],
          ['Teach-in', 'geschulter Bediener', 'ohne zusätzliches Kamerasystem: alte Bahn'],
          ['Handführung (Cobot)', 'Bediener', 'ohne zusätzliches Kamerasystem: alte Bahn'],
          ['Lernen durch Vormachen', 'Ihr Team an der Linie', 'der Roboter passt sich an']])
       + '</div></section>',
      faq=[('Brauchen unsere Mitarbeiter eine Schulung?', 'Nein. Sie machen die Aufgabe so vor, wie sie sie heute erledigen. Wir sind bei der Aufnahme dabei.'),
           ('Wie oft muss die Aufgabe vorgemacht werden?', 'Das hängt von der Aufgabe ab. Die Aufnahme ist für Sie kostenlos.'),
           ('Was ist der Unterschied zu einem Cobot?', 'Ein Cobot ist ein Roboter, der dafür gebaut ist, nah am Menschen zu arbeiten. Wie er eine Aufgabe lernt, ist damit nicht gesagt: Die meisten Cobots fahren fest eingelernte Bahnen. Kognitive Robotik beschreibt, wie der Roboter lernt und sich anpasst. <a href="/kognitive-robotik/">Mehr zu kognitiver Robotik</a>'),
           ('Was passiert bei einer neuen Variante?', 'Ihr Team macht sie kurz vor. Das Nachtrainieren ist in der Gebühr enthalten.')]),

     # ---------------------------------------------------------------- funding BW
     dict(slug='foerderung-automatisierung-baden-wuerttemberg', nav='Förderung Baden-Württemberg',
      title='Förderung für Automatisierung in Baden-Württemberg',
      desc='Innovationsgutschein „Mittelstand trifft Start-ups“: Baden-Württemberg fördert KMU, die mit einem Start-up automatisieren, mit 50 %, bis zu 20.000 €.',
      eyebrow='Fördermittel', h1='Förderung für Ihr Automatisierungs&shy;projekt in Baden-Württemberg.',
      lead='Das Land Baden-Württemberg bezuschusst Vorhaben, bei denen ein kleines oder mittleres Unternehmen Produkte oder Leistungen eines Start-ups einkauft: 50&nbsp;% der Kosten, bis zu 20.000&nbsp;€. Das Programm heißt Innovationsgutschein „Mittelstand trifft Start-ups“.',
      img='hero', alt='KI-Roboter richtet Kartons in einer Produktion auf',
      problem=('Die Bedingungen.', ['Den Antrag stellen Sie, nicht wir: ein Unternehmen mit Niederlassung oder Betriebsstätte in Baden-Württemberg.', 'Bis 250 Beschäftigte und bis 50&nbsp;Mio.&nbsp;€ Umsatz oder 43&nbsp;Mio.&nbsp;€ Bilanzsumme.', 'Gefördert werden Rechnungen des Start-ups für Produkte oder Leistungen in einem innovativen Vorhaben.', 'Ein Gutschein je Unternehmen. Es gibt keinen Rechtsanspruch, die L-Bank entscheidet.']),
      solution=('So läuft es ab.', ['Antrag online bei der L-Bank stellen, vor Projektbeginn.', 'Ein Ausschuss bewertet das Vorhaben, die L-Bank entscheidet.', 'Den Vertrag erst nach dem Zuwendungsbescheid schließen.', 'Vorhaben in zehn Monaten umsetzen, Rechnungen einreichen, Zuschuss erhalten.']),
      extra='<section><div class="wrap"><div class="sec-head"><h2>Was das für ein Projekt mit uns heißt.</h2><p>Wir sind ein junges Unternehmen aus Stuttgart. Wenn Sie in Baden-Württemberg produzieren und eine Aufgabe mit uns automatisieren wollen, können Sie den Gutschein für dieses Vorhaben beantragen. Ob es gefördert wird, entscheidet die L-Bank. Bei der Projektbeschreibung für den Antrag unterstützen wir Sie.</p><p class="src">Stand: November 2026, nach dem Merkblatt der L-Bank vom 20.07.2026. Maßgeblich sind die Unterlagen und Auskünfte der L-Bank: <a href="https://www.l-bank.de/innovationsgutschein" rel="noopener">l-bank.de/innovationsgutschein</a>. Diese Seite ist keine Förderberatung.</p></div></div></section>',
      steps=False,
      faq=[('Wie hoch ist die Förderung?', '50&nbsp;% der förderfähigen Kosten, höchstens 20.000&nbsp;€ je Gutschein. Die Mehrwertsteuer wird nicht gefördert.'),
           ('Wann muss der Antrag gestellt werden?', 'Vor Projektbeginn. Verträge dürfen erst nach dem Zuwendungsbescheid geschlossen werden. Anträge sind laufend möglich.'),
           ('Wer stellt den Antrag?', 'Das Unternehmen, das die Leistung einkauft, also Sie. Der Antrag läuft online über die L-Bank.'),
           ('Kann die Demo vor dem Antrag stattfinden?', 'Ja. Die Demo ist kostenlos und unverbindlich. Danach wissen Sie, ob es geht und was es kostet, und können den Antrag stellen. Den Vertrag schließen wir erst nach dem Zuwendungsbescheid.'),
           ('Gilt das auch außerhalb von Baden-Württemberg?', 'Nein. Der Innovationsgutschein ist ein Landesprogramm für Unternehmen mit Standort in Baden-Württemberg. Andere Bundesländer haben eigene Programme.')]),

     # ---------------------------------------------------------------- FAQ hub
     dict(slug='faq', nav='Fragen und Antworten',
      title='KI-Roboter in der Produktion: Fragen und Antworten',
      desc='Die wichtigsten Fragen zu KI-Robotern in der Produktion: Aufgaben, Kosten, Sicherheit, Lernen durch Vormachen und Grenzen. Kurz und ehrlich beantwortet.',
      eyebrow='Fragen und Antworten', h1='KI-Roboter in der Produktion: Fragen und Antworten.',
      lead='Was können KI-Roboter heute, was kosten sie, und wo liegen ihre Grenzen? Hier stehen die Antworten auf die Fragen, die Produktionsleiter und Inhaber uns am häufigsten stellen.',
      img='hero', alt='KI-Roboter richtet Kartons in einer Produktion auf',
      groups=[
       ('Grundlagen.', [
        ('Was ist ein KI-Roboter in der Produktion?', 'Ein Roboterarm, der nicht Bewegung für Bewegung programmiert wird, sondern mit Kameras sieht und Aufgaben durch Vormachen lernt. Damit lassen sich Handgriffe automatisieren, bei denen Teile unterschiedlich liegen oder Varianten oft wechseln. <a href="/ki-produktionsautomatisierung/">Produktionsautomatisierung mit KI</a>'),
        ('Was ist kognitive Robotik?', 'Kognitive Robotik meint Roboter, die ihre Umgebung wahrnehmen, sich anpassen und neue Aufgaben lernen, statt fest programmierte Bahnen zu fahren. <a href="/kognitive-robotik/">Kognitive Robotik erklärt</a>'),
        ('Was ist Physical AI?', 'Physical AI ist KI, die nicht Text oder Bilder erzeugt, sondern eine Maschine in der echten Welt steuert, zum Beispiel einen Roboterarm. Der Begriff meint praktisch dasselbe wie kognitive Robotik. <a href="/physical-ai-produktion/">Physical AI in der Produktion</a>'),
        ('Was ist der Unterschied zu einem klassischen Industrieroboter?', 'Ein klassischer Industrieroboter fährt fest programmierte Bahnen: Jedes Teil muss exakt liegen, jede Variante wird neu programmiert. Ein KI-Roboter sieht, wo das Teil liegt, und lernt neue Varianten durch Vormachen. Dafür ist die klassische Anlage bei großen Stückzahlen schneller.'),
        ('Was ist der Unterschied zwischen einem Cobot und einem KI-Roboter?', 'Ein Cobot ist ein Roboter, der dafür gebaut ist, nah am Menschen zu arbeiten. Die meisten Cobots fahren trotzdem fest eingelernte Bahnen. KI-Roboter unterscheiden sich darin, wie sie lernen: durch Vormachen statt Programmierung. <a href="/roboter-ohne-programmierung/">Roboter ohne Programmierung</a>'),
        ('Was heißt Lernen durch Vormachen?', 'Ihr Team macht die Aufgabe mit einem Handgreifer vor. Dabei wird aufgezeichnet, wie die Teile liegen und wie gegriffen wird. Die KI lernt daraus die Aufgabe und passt die Bewegung an, wenn ein Teil anders liegt.')]),
       ('Aufgaben und Grenzen.', [
        ('Welche Aufgaben kann ein KI-Roboter heute übernehmen?', 'Wiederkehrende Handgriffe, die jedes Mal ein bisschen anders sind: <a href="/kartons-aufrichten-automatisieren/">Kartons aufrichten</a>, <a href="/verpacken-automatisieren/">Verpacken</a>, <a href="/kommissionieren-automatisieren/">Kommissionieren</a>, <a href="/pick-and-place-automatisieren/">Teile umsetzen</a>, <a href="/konfektionierung-automatisieren/">Konfektionieren</a> und das <a href="/maschinenbeschickung-automatisieren/">Beladen von Maschinen</a> mit leichten Teilen.'),
        ('Wie schwer dürfen die Teile sein?', 'Bis etwa 1 bis 2&nbsp;kg pro Teil, an einem Arbeitsplatz von rund einem Quadratmeter. <a href="/was-kann-der-roboter/">Eckdaten und Grenzen</a>'),
        ('Wie schnell arbeitet der Roboter?', 'Das hängt von der Aufgabe ab. Für Takte im Sekundenbereich mit immer gleichen Teilen ist eine klassische Anlage schneller. Bei wechselnden Teilen messen wir den Takt im Training an Ihrer Linie. Sie zahlen erst, wenn er passt.'),
        ('Wofür eignet sich ein KI-Roboter nicht?', 'Für schwere Teile, für Takte im Sekundenbereich mit immer gleichen Teilen, für Fügen mit hohen Kräften oder sehr engen Toleranzen und für Palettieren über mehrere Lagen und größere Entfernungen.'),
        ('Geht das auch bei kleinen Losgrößen und vielen Varianten?', 'Gerade dann. Neue Varianten lernt der Roboter durch Vormachen, und Sie investieren nichts, was sich amortisieren muss. <a href="/kleine-losgroessen-automatisieren/">Kleine Losgrößen automatisieren</a>'),
        ('Können vorhandene Roboter eingebunden werden?', 'Oft ja. Wir binden vorhandene Roboter ein und rüsten Kameras und Sensoren nach.')]),
       ('Kosten.', [
        ('Was kostet ein KI-Roboter für die Produktion?', 'Bei uns keine Investition. Sie zahlen eine feste Monatsgebühr, immer unter 70&nbsp;% dessen, was die Stelle Sie heute kostet. Bei 3.000&nbsp;€ Personalkosten sind das höchstens 2.100&nbsp;€ im Monat. <a href="/roboter-kosten/">Was kostet ein Roboter?</a>'),
        ('Was ist Robotics as a Service?', 'Ein Modell, bei dem Sie einen Roboter nicht kaufen, sondern für seine Leistung bezahlen. Roboter, Software, Betrieb und Wartung kommen vom Anbieter. <a href="/robotics-as-a-service/">Robotics as a Service erklärt</a>'),
        ('Ab wann zahlen wir?', 'Erst ab dem Monat, in dem der Roboter die Aufgabe zuverlässig erledigt. Demo, Aufnahme und Training sind für Sie kostenlos.'),
        ('Was ist günstiger: kaufen, leasen oder mieten?', 'Bei großen Stückzahlen und einer Aufgabe, die sich nie ändert, kann Kaufen günstiger sein. Bei wechselnden Varianten und ohne eigene Robotik-Experten ist die Monatsgebühr meist die bessere Wahl, weil Integration, Nachtrainieren und Wartung enthalten sind.'),
        ('Ist das günstiger als Zeitarbeit?', 'Bei Dauerbedarf in der Regel ja: feste Monatsgebühr statt Stundensatz. <a href="/zeitarbeit-alternative-produktion/">Roboter und Zeitarbeit im Vergleich</a>'),
        ('Gibt es Fördermittel?', 'In Baden-Württemberg bezuschusst der Innovationsgutschein „Mittelstand trifft Start-ups“ 50&nbsp;% der Kosten, bis zu 20.000&nbsp;€. <a href="/foerderung-automatisierung-baden-wuerttemberg/">Förderung im Überblick</a>')]),
       ('Einführung und Betrieb.', [
        ('Wie läuft die Einführung ab?', 'In vier Schritten: Sie zeigen uns die Aufgabe, 30 Minuten vor Ort oder per Video. Ihr Team macht sie vor. Der Roboter lernt an Ihrer Linie. Dann produziert er, und erst jetzt beginnt die Monatsgebühr.'),
        ('Brauchen wir eigene Robotik- oder KI-Experten?', 'Nein. Wir installieren, betreiben und warten den Roboter. Ihr Team zeigt nur die Aufgabe.'),
        ('Was passiert, wenn der Roboter hängen bleibt oder ausfällt?', 'Unser Operator übernimmt aus der Ferne, während Ihrer Produktionszeiten. Reparaturen und Ersatzteile sind in der Gebühr enthalten.'),
        ('Was passiert, wenn sich unser Produkt ändert?', 'Ihr Team macht die neue Variante kurz vor. Das Nachtrainieren ist in der Gebühr enthalten.'),
        ('In welchen Regionen arbeiten Sie?', 'Für Produktionsbetriebe in Deutschland, Österreich und der Schweiz. Am schnellsten vor Ort sind wir in der Region Stuttgart und Neckar-Alb. <a href="/automatisierung-stuttgart/">Region Stuttgart</a>')]),
       ('Sicherheit und Mitarbeiter.', [
        ('Darf ein Roboter neben Mitarbeitern arbeiten?', 'Ja, wenn die Anlage dafür ausgelegt und abgesichert ist. Welche Schutzmaßnahmen nötig sind, ergibt sich aus der Beurteilung der Anlage und des Arbeitsplatzes. ' + SAFE),
        ('Wer ist für die Gefährdungsbeurteilung zuständig?', 'Der Arbeitgeber, also der Betrieb, in dem der Roboter steht. Das verlangen Arbeitsschutzgesetz und Betriebssicherheitsverordnung. Wir machen sie gemeinsam mit Ihnen, bevor der Roboter startet.'),
        ('Ersetzt der Roboter unsere Mitarbeiter?', 'Er übernimmt die Stelle, die Sie nicht besetzt bekommen. Ihre Leute werden für die Aufgaben frei, für die man Erfahrung braucht.'),
        ('Was, wenn es bei unserer Aufgabe nicht klappt?', 'Dann zahlen Sie nichts.')])]),
    ])
    PAGES.extend(_regional_and_binpicking(CARD, DT))


# ------------------------------------------------------------------ Nov 26: Baden-Württemberg, Reutlingen, bin picking
TITLES['automatisierung-stuttgart'] = 'Robotik &amp; Automatisierung Stuttgart | Ackermann Robotics'
TITLES['roboter-kosten'] = 'Roboter mieten oder kaufen? Kosten im Vergleich'
FAQ_ADD['automatisierung-stuttgart'] = FAQ_ADD['automatisierung-stuttgart'] + [
  ('Arbeiten Sie in ganz Baden-Württemberg?', 'Ja. Am schnellsten vor Ort sind wir in der Region Stuttgart und in Neckar-Alb, im übrigen Land nach Absprache. <a href="/kognitive-robotik-baden-wuerttemberg/">Kognitive Robotik in Baden-Württemberg</a>'),
  ('Sind Sie auch in Reutlingen und Metzingen vor Ort?', 'Ja, dort arbeiten unsere Techniker. <a href="/robotik-reutlingen/">Robotik in Reutlingen, Metzingen und Tübingen</a>')]
FAQ_ADD['kognitive-robotik'] = FAQ_ADD['kognitive-robotik'] + [
  ('Gibt es Anbieter für kognitive Robotik in Baden-Württemberg?', 'Ja. Ackermann Robotics aus Stuttgart bringt kognitive Roboter als Service in Produktionsbetriebe im ganzen Land. <a href="/kognitive-robotik-baden-wuerttemberg/">Kognitive Robotik in Baden-Württemberg</a>')]
FAQ_ADD['pick-and-place-automatisieren'] = FAQ_ADD['pick-and-place-automatisieren'] + [
  ('Geht auch der Griff in die Kiste?', 'Ja, für leichte Teile, die ungeordnet im Behälter liegen. <a href="/bin-picking/">Bin Picking mit KI</a>')]


def _regional_and_binpicking(CARD, DT):
    sectors = ('<div class="cards c4">'
        + CARD('/automatisierung-elektronikfertigung/', 'Elektronikfertigung', 'Bauteile umsetzen, Baugruppen verpacken, Sets kommissionieren.')
        + CARD('/automatisierung-kunststoffverarbeitung/', 'Kunststoffverarbeitung', 'Spritzgussteile entnehmen, ablegen und verpacken.')
        + CARD('/konfektionierung-automatisieren/', 'Konfektionierung', 'Sets zusammenstellen, Displays bestücken, umpacken.')
        + CARD('/bin-picking/', 'Bin Picking', 'Ungeordnete Teile aus der Kiste greifen und ablegen.')
        + '</div>')
    return [
     # ---------------------------------------------------------------- Baden-Württemberg
     dict(slug='kognitive-robotik-baden-wuerttemberg', nav='Kognitive Robotik in Baden-Württemberg',
      title='Kognitive Robotik in Baden-Württemberg | Ackermann Robotics',
      desc='Robotik aus Stuttgart: kognitive Roboter, die sehen und durch Vormachen lernen. Für Produktionsbetriebe in ganz Baden-Württemberg, ohne Investition.',
      eyebrow='Robotik aus Baden-Württemberg', h1='Kognitive Robotik aus Baden-Württemberg. Für die Produktion im Land.',
      lead='Ackermann Robotics ist ein Robotik-Unternehmen aus Stuttgart. Wir bringen kognitive Roboter in Produktionsbetriebe in ganz Baden-Württemberg: Roboter, die mit Kameras sehen, durch Vormachen lernen und Handgriffe übernehmen, an denen klassische Automatisierung scheitert. Sie kaufen nichts. Sie zahlen eine Monatsgebühr, erst wenn der Roboter zuverlässig läuft.',
      img='hero', alt='Kognitiver Roboter richtet Kartons in einer Produktion auf',
      problem=('Was Produktionsbetriebe im Land kennen.', ['Helferstellen in Verpackung, Montagevorbereitung und Versand bleiben monatelang offen.', 'Klassische Roboter brauchen Teile in fester Lage. Bei wechselnden Varianten und kleinen Losen rechnet sich das nicht.', 'Große Integratoren lohnen sich erst bei großen Projekten. Für eine einzelne Station findet sich oft niemand.']),
      solution=('Was wir anders machen.', ['Kognitive Roboter: Kameras erkennen, wie jedes Teil liegt. Neue Varianten lernt der Roboter durch Vormachen.', 'Robotics as a Service: keine Investition, Monatsgebühr unter 70&nbsp;% der heutigen Stellenkosten.', 'Ein Team aus der Region: Sitz in Stuttgart, Techniker im Raum Reutlingen und Metzingen.', 'Landesförderung: Der Innovationsgutschein kann 50&nbsp;% der Kosten übernehmen, bis zu 20.000&nbsp;€, wenn Ihr Betrieb die Bedingungen erfüllt.']),
      extra='<section><div class="wrap"><div class="sec-head"><h2>Wo wir in Baden-Württemberg arbeiten.</h2><p>Die kostenlose Demo geht überall im Land auch per Video. Für Installation und Service kommen wir zu Ihnen.</p></div>'
       + DT(['Region', 'Städte', 'Vor Ort'], [
          ['Region Stuttgart', 'Stuttgart, Böblingen, Sindelfingen, Ludwigsburg, Esslingen, Waiblingen, Leonberg, Nürtingen', 'kurzfristig'],
          ['Neckar-Alb', 'Reutlingen, Metzingen, Tübingen, Balingen', 'kurzfristig'],
          ['Heilbronn-Franken', 'Heilbronn, Neckarsulm, Schwäbisch Hall', 'nach Absprache'],
          ['Ostwürttemberg', 'Aalen, Heidenheim, Schwäbisch Gmünd', 'nach Absprache'],
          ['Karlsruhe und Nordschwarzwald', 'Karlsruhe, Pforzheim, Rastatt', 'nach Absprache'],
          ['Rhein-Neckar', 'Mannheim, Heidelberg', 'nach Absprache'],
          ['Ulm, Oberschwaben und Bodensee', 'Ulm, Biberach, Ravensburg, Friedrichshafen', 'nach Absprache'],
          ['Schwarzwald-Baar-Heuberg', 'Villingen-Schwenningen, Tuttlingen, Rottweil', 'nach Absprache']])
       + '</div></section>'
       + '<section class="soft"><div class="wrap"><div class="sec-head"><h2>Für die Branchen im Land.</h2><p>Überall dort, wo viele Varianten, kleine Lose und leichte Teile zusammenkommen.</p></div>' + sectors + '</div></section>',
      area=['Stuttgart', 'Reutlingen', 'Metzingen', 'Tübingen', 'Böblingen', 'Ludwigsburg', 'Esslingen am Neckar', 'Heilbronn', 'Aalen', 'Karlsruhe', 'Pforzheim', 'Mannheim', 'Heidelberg', 'Ulm', 'Ravensburg', 'Friedrichshafen', 'Villingen-Schwenningen'],
      faq=[('Welche Robotik-Unternehmen in Baden-Württemberg stellen Roboter für die Produktion als Service bereit?', 'Ackermann Robotics aus Stuttgart stellt kognitive Roboter als Service bereit: Wir installieren, betreiben und warten den Roboter, Sie zahlen eine feste Monatsgebühr. Daneben gibt es Hersteller und Integratoren, die klassische Roboter und Cobots vermieten. <a href="/roboter-mieten/">Roboter mieten</a>'),
           ('Was ist kognitive Robotik?', 'Roboter, die ihre Umgebung mit Kameras wahrnehmen, sich anpassen und Aufgaben durch Vormachen lernen, statt fest programmierte Bahnen zu fahren. <a href="/kognitive-robotik/">Kognitive Robotik erklärt</a>'),
           ('Welche Aufgaben übernimmt der Roboter?', 'Wiederkehrende Handgriffe mit leichten Teilen bis etwa 1 bis 2&nbsp;kg: Kartons aufrichten, Verpacken, Kommissionieren, Teile umsetzen und der Griff in die Kiste. <a href="/was-kann-der-roboter/">Eckdaten und Grenzen</a>'),
           ('Kommen Sie für die Demo zu uns?', 'In der Region Stuttgart und in Neckar-Alb kurzfristig, im übrigen Baden-Württemberg nach Absprache. Die Demo geht auch per Video und ist kostenlos.'),
           ('Gibt es Förderung in Baden-Württemberg?', 'Ja. Der Innovationsgutschein „Mittelstand trifft Start-ups“ bezuschusst 50&nbsp;% der Kosten, bis zu 20.000&nbsp;€, für Unternehmen mit Standort im Land. <a href="/foerderung-automatisierung-baden-wuerttemberg/">Förderung im Überblick</a>'),
           ('Wo sitzt Ackermann Robotics?', 'In Stuttgart-Botnang. Unsere Techniker arbeiten im Raum Reutlingen und Metzingen.')]),

     # ---------------------------------------------------------------- Reutlingen / Neckar-Alb
     dict(slug='robotik-reutlingen', nav='Robotik Reutlingen',
      title='Robotik &amp; Automatisierung Reutlingen | Ackermann Robotics',
      desc='Robotik für Produktionsbetriebe in Reutlingen, Metzingen und Tübingen: KI-Roboter für Verpacken, Kommissionieren und Teile umsetzen. Techniker vor Ort.',
      eyebrow='Region Neckar-Alb', h1='Robotik und Automatisierung in Reutlingen, Metzingen und Tübingen.',
      lead='Unsere Techniker arbeiten im Raum Reutlingen und Metzingen. Für Produktionsbetriebe in Neckar-Alb heißt das: Demo in Ihrer Halle, Installation und Service ohne lange Anfahrt. Wir bringen kognitive Roboter an Ihre Linie, die Handgriffe übernehmen, für die Sie keine Helfer mehr finden.',
      img='kitting', alt='KI-Roboterarm stellt Teilesätze zusammen',
      problem=('Was Betriebe in Neckar-Alb kennen.', ['Elektronik, Kunststoff, Metall und Textil: viele Varianten, kleine Lose, viel Handarbeit.', 'Helferstellen bleiben offen, weil im Umkreis alle dieselben Leute suchen.', 'Für eine einzelne Station mit wechselnden Teilen lohnt sich kein großes Automatisierungsprojekt.']),
      solution=('Was wir hier bieten.', ['Kurze Wege: Demo, Installation und Service durch unsere Techniker aus der Region.', 'Ein kognitiver Roboter, der Teile mit Kameras erkennt und Aufgaben durch Vormachen lernt.', 'Fernbetreuung durch unseren Operator während Ihrer Produktionszeiten.', 'Keine Investition. Die Monatsgebühr startet erst, wenn der Roboter zuverlässig läuft.']),
      extra='<section><div class="wrap"><div class="sec-head"><h2>Wo wir in Neckar-Alb arbeiten.</h2><p>Reutlingen, Metzingen, Pfullingen, Eningen, Bad Urach, Tübingen, Rottenburg, Mössingen, Hechingen, Balingen und Albstadt. Dazu die Nachbarschaft in Nürtingen, Kirchheim und im Kreis Böblingen. <a href="/kognitive-robotik-baden-wuerttemberg/">Ganz Baden-Württemberg</a></p></div></div></section>'
       + '<section class="soft"><div class="wrap"><div class="sec-head"><h2>Typische Aufgaben in der Region.</h2></div>' + sectors + '</div></section>',
      area=['Reutlingen', 'Metzingen', 'Pfullingen', 'Eningen unter Achalm', 'Bad Urach', 'Tübingen', 'Rottenburg am Neckar', 'Mössingen', 'Hechingen', 'Balingen', 'Albstadt', 'Nürtingen'],
      faq=[('Gibt es in Reutlingen ein Robotik-Unternehmen, das Roboter für die Produktion bereitstellt?', 'Ackermann Robotics hat seinen Sitz in Stuttgart, unsere Techniker arbeiten im Raum Reutlingen und Metzingen. Wir stellen kognitive Roboter als Service bereit: Installation, Betrieb und Wartung inklusive.'),
           ('Wie schnell sind Sie vor Ort?', 'Im Raum Reutlingen, Metzingen und Tübingen kurzfristig, für die Demo genauso wie im Service. Hängt der Roboter, übernimmt zuerst unser Operator aus der Ferne.'),
           ('Welche Aufgaben übernimmt der Roboter?', 'Wiederkehrende Handgriffe mit leichten Teilen bis etwa 1 bis 2&nbsp;kg: Kartons aufrichten, Verpacken, Kommissionieren, Teile umsetzen. <a href="/was-kann-der-roboter/">Eckdaten und Grenzen</a>'),
           ('Was kostet das?', PRICE),
           ('Gibt es Förderung?', 'Für Betriebe in Baden-Württemberg: Der Innovationsgutschein bezuschusst 50&nbsp;% der Kosten, bis zu 20.000&nbsp;€. <a href="/foerderung-automatisierung-baden-wuerttemberg/">Förderung im Überblick</a>')]),

     # ---------------------------------------------------------------- bin picking
     dict(slug='bin-picking', nav='Bin Picking', service=True,
      title='Bin Picking mit KI: Griff in die Kiste | Ackermann Robotics',
      desc='Bin Picking ohne Programmierung: Ein KI-Roboter greift ungeordnete Teile aus der Kiste und legt sie ab. Teile bis 1 bis 2 kg, keine Investition.',
      eyebrow='Anwendung', h1='Bin Picking: der Griff in die Kiste, gelernt statt programmiert.',
      lead='Beim Bin Picking greift ein Roboter Teile, die ungeordnet in einer Kiste liegen. Klassische Systeme werden dafür für jedes Teil eingerichtet. Unser kognitiver Roboter lernt den Griff durch Vormachen und legt die Teile dort ab, wo Sie sie brauchen: auf einem Band, in einer Maschine oder in einem Karton.',
      img='kitting', alt='KI-Roboterarm greift Teile aus einem Behälter',
      problem=('Warum Bin Picking oft am Aufwand scheitert.', ['Klassische Systeme werden für jedes Teil einzeln eingerichtet, oft mit CAD-Daten und viel Feintuning.', 'Glänzende, weiche oder ineinander verhakte Teile machen der Erkennung Probleme.', 'Kamera, Software und Integration kosten, bevor das erste Teil gegriffen ist.', 'Bei vielen Varianten wird der Aufwand pro Teil zu hoch.']),
      solution=('Wie unser Roboter in die Kiste greift.', ['Kameras erkennen, wie jedes Teil liegt.', 'Den Griff lernt er durch Vormachen an Ihren echten Teilen. Keine CAD-Daten, kein Programmieren auf Ihrer Seite.', 'Er legt das Teil gezielt ab: auf ein Band, in eine Maschine, auf einen Werkstückträger oder in einen Karton.', 'Keine Investition. Die Monatsgebühr startet erst, wenn er zuverlässig läuft.']),
      extra='<section><div class="wrap"><div class="sec-head"><h2>Bin Picking, Griff in die Kiste, Pick and Place: Was ist was?</h2></div>'
       + DT(['Begriff', 'Bedeutung'], [
          ['Bin Picking', 'Ein Roboter greift Teile, die ungeordnet in einem Behälter liegen, und legt sie definiert ab.'],
          ['Griff in die Kiste', 'Der deutsche Begriff für Bin Picking.'],
          ['Teilevereinzelung', 'Teile aus Schüttgut einzeln greifen und in definierter Lage weitergeben.'],
          ['Pick and Place', 'Der Oberbegriff: ein Teil greifen und an anderer Stelle ablegen, egal wie es vorher lag. <a href="/pick-and-place-automatisieren/">Pick and Place automatisieren</a>']])
       + '</div></section>'
       + '<section class="soft"><div class="wrap"><div class="sec-head"><h2>Ehrlich: Wo die Grenzen liegen.</h2><p>Teile über etwa 2&nbsp;kg, Takte im Sekundenbereich und stark ineinander verhakte Teile wie Federn sind Fälle für Spezialanlagen. Ob Ihre Teile passen, prüfen wir in der kostenlosen Demo an Ihren echten Teilen. <a href="/was-kann-der-roboter/">Eckdaten und Grenzen</a></p></div></div></section>',
      faq=[('Was ist Bin Picking?', 'Bin Picking, auf Deutsch Griff in die Kiste, heißt: Ein Roboter greift Teile, die ungeordnet in einem Behälter liegen, und legt sie definiert ab.'),
           ('Brauchen wir CAD-Daten unserer Teile?', 'Nein. Der Roboter lernt den Griff durch Vormachen an Ihren echten Teilen.'),
           ('Welche Teile eignen sich?', 'Teile bis etwa 1 bis 2&nbsp;kg, die ein Zweifingergreifer fassen kann. Stark verhakte oder sehr kleine Teile prüfen wir in der Demo.'),
           ('Wie schnell ist das?', 'Das hängt vom Teil ab. Für Takte im Sekundenbereich ist eine Spezialanlage schneller. Wir messen den Takt im Training an Ihrer Linie. Sie zahlen erst, wenn er passt.'),
           ('Was kostet Bin Picking?', PRICE),
           ('Kann der Roboter damit auch Maschinen beschicken?', 'Für leichte Teile ja. <a href="/maschinenbeschickung-automatisieren/">Maschinenbeschickung automatisieren</a>')]),
    ]
