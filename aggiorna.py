import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# MAPPA DELLE FONTI: Associa ogni titolo della tua lista alla pagina del player video.
MAPPA_FONTI = {
    "A Star is Born (2018)": "https://miixdrop.net/f/4dvwznw9cx0kg8",
    "Al bar dello sport (1983)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Avatar: Fuoco e Cenere (2025)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Avvocato Ligas S01 E01": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Avvocato Ligas S01 E02": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Avvocato Ligas S01 E03": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Avvocato Ligas S01 E04": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Avvocato Ligas S01 E05": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Avvocato Ligas S01 E06": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Big Hero 6 (2014)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Don Franco e Don Ciccio nell anno della contestazione (1970)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "EPiC: Elvis Presley In Concert (2026)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Euphoria S01 E01": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Euphoria S01 E02": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Euphoria S01 E03": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Euphoria S01 E04": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Euphoria S01 E05": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Euphoria S01 E06": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Euphoria S01 E07": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Euphoria S01 E08": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Euphoria S02 E01": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Euphoria S02 E02": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Euphoria S02 E03": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Euphoria S02 E04": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Euphoria S02 E05": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Euphoria S02 E06": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Euphoria S02 E07": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Euphoria S02 E08": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Finchè morte non ci separi 2 (2026)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Francesca e Giovanni (2025)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Franco e Ciccio… ladro e guardia (1970)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "I due pezzi da 90 (1971)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "I pompieri (1985)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Il Padrino (1972)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Il Padrino - Parte 2 (1974)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Il Padrino - Parte 3 (1990)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Il diavolo veste Prada 2 (2026)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Il miglio verde (1999)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Interstellar (2014)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "L'infiltrata (2024)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Lavoreremo da grandi (2026)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Lo chiamavano Trinità… (1970)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Man on the run (2026)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Michael (2026)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Mio fratello è un vichingo (2025)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Missione eroica - I pompieri 2 (1987)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Monsters & Co. (2001)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Notte prima degli esami 3.0 (2026)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Obsession (2026)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Oceania (2016)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Oceania 2 (2024)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Pecore sotto copertura (2026)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Portobello S01 E01": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Portobello S01 E02": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Portobello S01 E03": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Portobello S01 E04": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Portobello S01 E05": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Portobello S01 E06": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Reminders of him: La parte migliore di te (2026)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Ritorno al futuro (1985)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Ritorno al futuro: Parte 2 (1989)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Ritorno al futuro: Parte 3 (1990)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Scream 7 (2026)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Scuola di ladri (1986)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Scuola di ladri - Parte seconda (1987)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Spaghetti a mezzanotte (1981)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Stand by Me – Ricordo di un'estate (1986)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Super Mario Galaxy – Il film (2026)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Tom Clancy’s Jack Ryan: Ghost War (2026)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Toy Story (1995)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Toy Story 2 (1999)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Toy Story 3 (2010)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Toy Story 4 (2019)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Un futuro aprile (2026)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Una notte da leoni (2009)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Una notte da leoni 2 (2011)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Una notte da leoni 3 (2013)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Vieni avanti cretino (1982)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "Wicked - Parte 2 (2025)": "INSERISCI_QUI_URL_PLAYER_VIDEO",
    "…continuavano a chiamarlo Trinità (1972)": "INSERISCI_QUI_URL_PLAYER_VIDEO"
}

def cerca_m3u8_nei_tag(soup):
    # Cerca nei link normali
    for tag in soup.find_all('a', href=True):
        if '.m3u8' in tag['href']:
            return tag['href']
    # Cerca nei blocchi JavaScript del player
    for script in soup.find_all('script'):
        if script.string and '.m3u8' in script.string:
            for riga in script.string.split('\n'):
                if '.m3u8' in riga:
                    inizio = riga.find('http')
                    fine = riga.find('.m3u8') + 5
                    if inizio != -1:
                        return riga[inizio:fine]
    return None

def estrai_nuovo_link(url_pagina):
    if not url_pagina or "INSERISCI_QUI" in url_pagina:
        return None
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        risposta = requests.get(url_pagina, headers=headers, timeout=10)
        if risposta.status_code == 200:
            soup = BeautifulSoup(risposta.text, 'html.parser')
            
            # Gestione Iframe: se trova un iframe, prova a entrarci dentro
            iframe = soup.find('iframe', src=True)
            if iframe:
                url_iframe = iframe['src']
                if url_iframe.startswith('/'):
                    url_iframe = urljoin(url_pagina, url_iframe)
                
                risposta_iframe = requests.get(url_iframe, headers=headers, timeout=10)
                if risposta_iframe.status_code == 200:
                    soup_iframe = BeautifulSoup(risposta_iframe.text, 'html.parser')
                    link_trovato = cerca_m3u8_nei_tag(soup_iframe)
                    if link_trovato:
                        return link_trovato
            
            # Se non c'era un iframe o l'iframe era vuoto, controlla la pagina principale
            return cerca_m3u8_nei_tag(soup)
    except Exception as e:
        print(f"Errore caricamento: {e}")
    return None

def aggiorna_lista():
    with open("lista_originale.m3u", "r", encoding="utf-8") as f:
        righe = f.readlines()

    nuove_righe = []
    film_corrente = None

    for riga in righe:
        if riga.startswith("#EXTINF"):
            nuove_righe.append(riga)
            parti = riga.split(",")
            if len(parti) > 1:
                film_corrente = parti[-1].strip()
        elif riga.startswith("http"):
            if film_corrente in MAPPA_FONTI:
                url_sito_madre = MAPPA_FONTI[film_corrente]
                nuovo_link = estrai_nuovo_link(url_sito_madre)
                
                if nuovo_link:
                    nuove_righe.append(nuovo_link + "\n")
                    print(f"[OK] Aggiornato: {film_corrente}")
                else:
                    nuove_righe.append(riga)
                    print(f"[INFO] Mantenuto vecchio link per: {film_corrente}")
            else:
                nuove_righe.append(riga)
            film_corrente = None
        else:
            nuove_righe.append(riga)

    with open("lista_aggiornata.m3u", "w", encoding="utf-8") as f:
        f.writelines(nuove_righe)

if __name__ == "__main__":
    aggiorna_lista()
