# FileOrganizer

FileOrganizer è il progetto del primo modulo del corso di Data Science. Il progetto consiste nell'utilizzo del linguaggio di programmazione python e della libreria numpy per la gestione di alcuni file.

## 1. Organizzazione dei file

Lo script sposterà ogni file nella cartella corrispondente al suo tipo. Se le cartelle sono presenti le crea senza sovrascriverle. I file categorizzati vengono elencati nel file `recap.csv`. Il file è creato se non esiste e continuamente aggiornato e non sovrascritto.

## 2. Realizzazione dell'eseguibile

Lo script realizzato nel capitolo 1 è stato convertito in eseguibile. L'eseguibile nominato `addfile.py` si trova nella stessa cartella del notebook.

L'eseguibile è stato realizzato utilizzando la libreria `typer` in quanto essa fornisce automaticamente messaggi di errore per argomenti mancanti e funzione help.

Il file da organizzare si deve trovare all'interno della cartella `files` ma **NON** in una delle sottocartelle.

Lo script stamperà a schermo i dati sul file che verranno poi scritti in `recap.csv`.

## 3. Utilizzo di NumPy e PIL per mostrare informazionni sulle immagini

Si crea una tabella che mostra la media dei valori dell'array che rappresenta l'immagine come matrice.

Per le immagini in bianco e nero è presente solo la media della scala di grigi.

Per le immagini a colori è presente la media dei tre canali RGB.

Per una delle immagini è presente anche l'opacità (canale alpha).

## 4. Setup

Il notebook e lo script sono stati testati utilizzando Python 3.10.2.

Creando un ambiente virtuale con installati i pacchetti presenti in `requirements.txt` non si dovrebbero riscontrare problemi.

Per identificare il tipo di file si è utilizzata una libreria chiamata `python-magic`. Se dovessero esserci problemi con questa libreria queste sono possibili soluzioni:

### macOS:
```bash
brew install libmagic
pip install python-magic
```
### Linux:
```bash
sudo apt-get install libmagic
pip install python-magic
```
### Windows:
```powershell
pip install python-magic-bin
```
