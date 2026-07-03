import requests
from bs4 import BeautifulSoup

# MAPPA DELLE FONTI: Associa ogni titolo della tua lista alla pagina reale del sito streaming.
MAPPA_FONTI = {
    "A Star is Born (2018)": "https://streamingcommunityz.pl/it/watch/788",
    "Al bar dello sport (1983)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Avatar: Fuoco e Cenere (2025)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Avvocato Ligas S01 E01": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Avvocato Ligas S01 E02": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Avvocato Ligas S01 E03": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Avvocato Ligas S01 E04": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Avvocato Ligas S01 E05": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Avvocato Ligas S01 E06": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Big Hero 6 (2014)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Don Franco e Don Ciccio nell anno della contestazione (1970)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "EPiC: Elvis Presley In Concert (2026)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Euphoria S01 E01": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Euphoria S01 E02": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Euphoria S01 E03": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Euphoria S01 E04": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Euphoria S01 E05": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Euphoria S01 E06": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Euphoria S01 E07": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Euphoria S01 E08": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Euphoria S02 E01": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Euphoria S02 E02": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Euphoria S02 E03": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Euphoria S02 E04": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Euphoria S02 E05": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Euphoria S02 E06": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Euphoria S02 E07": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Euphoria S02 E08": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Finchè morte non ci separi 2 (2026)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Francesca e Giovanni (2025)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Franco e Ciccio… ladro e guardia (1970)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "I due pezzi da 90 (1971)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "I pompieri (1985)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Il Padrino (1972)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Il Padrino - Parte 2 (1974)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Il Padrino - Parte 3 (1990)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Il diavolo veste Prada 2 (2026)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Il miglio verde (1999)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Interstellar (2014)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "L'infiltrata (2024)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Lavoreremo da grandi (2026)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Lo chiamavano Trinità… (1970)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Man on the run (2026)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Michael (2026)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Mio fratello è un vichingo (2025)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Missione eroica - I pompieri 2 (1987)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Monsters & Co. (2001)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Notte prima degli esami 3.0 (2026)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Obsession (2026)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Oceania (2016)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Oceania 2 (2024)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Pecore sotto copertura (2026)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Portobello S01 E01": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Portobello S01 E02": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Portobello S01 E03": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Portobello S01 E04": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Portobello S01 E05": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Portobello S01 E06": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Reminders of him: La parte migliore di te (2026)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Ritorno al futuro (1985)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Ritorno al futuro: Parte 2 (1989)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Ritorno al futuro: Parte 3 (1990)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Scream 7 (2026)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Scuola di ladri (1986)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Scuola di ladri - Parte seconda (1987)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Spaghetti a mezzanotte (1981)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Stand by Me – Ricordo di un'estate (1986)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Super Mario Galaxy – Il film (2026)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Tom Clancy’s Jack Ryan: Ghost War (2026)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Toy Story (1995)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Toy Story 2 (1999)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Toy Story 3 (2010)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Toy Story 4 (2019)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Un futuro aprile (2026)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Una notte da leoni (2009)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Una notte da leoni 2 (2011)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Una notte da leoni 3 (2013)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Vieni avanti cretino (1982)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "Wicked - Parte 2 (2025)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM",
    "…continuavano a chiamarlo Trinità (1972)": "INSERISCI_QUI_URL_PAGINA_DEL_FILM"
}

def estrai_nuovo_link(url_pagina):
    if not url_pagina or "INSERISCI_QUI" in url_pagina:
        return None
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        risposta = requests.get(url_pagina, headers=headers, timeout=10)
        if risposta.status_code == 200:
            soup = BeautifulSoup(risposta.text, 'html.parser')
            
            # 1. Ricerca nei link normali
            for tag in soup.find_all('a', href=True):
                if '.m3u8' in tag['href']:
                    return tag['href']
            
            # 2. Ricerca profonda nei blocchi JavaScript del player
            for script in soup.find_all('script'):
                if script.string and '.m3u8' in script.string:
                    for riga in script.string.split('\n'):
                        if '.m3u8' in riga:
                            inizio = riga.find('http')
                            fine = riga.find('.m3u8') + 5
                            if inizio != -1:
                                return riga[inizio:fine]
    except Exception as e:
        print(f"Errore caricamento {url_pagina}: {e}")
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
