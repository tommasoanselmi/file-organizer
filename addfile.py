#!/usr/bin/env python3
import typer
import os
import magic
import re
import shutil
import csv


def main(file: str):
    # Ottengo il percorso della cartella contenente i file da organizzare
    files_directory = "files"
    files_path = os.path.join(os.getcwd(), files_directory)
    # Controllo se sono presenti le sottocartelle. Se non sono presenti le
    # creo.
    sub_directories = ['audio', 'docs', 'images']

    for dir in sub_directories:
        if not os.path.isdir(os.path.join(files_path, dir)):
            os.mkdir(os.path.join(files_path, dir))

    # Funzione per ottenere il tipo di file
    def get_type(file):
        f = magic.Magic(mime=True)
        file_type = f.from_file(os.path.join(files_path, file))
        if re.search(r'audio', file_type):
            return 'audio'
        elif re.search(r'text', file_type):
            return 'doc'
        elif re.search(r'image', file_type):
            return 'image'
        else:
            raise TypeError(f"{file}: Tipo di file non supportato!")

    # Funzione per ottenere la dimensione di un file

    def get_size(file):
        return os.path.getsize(os.path.join(files_path, file))

    # Funzione per ottenere il nome del file senza estensione

    def get_name(file):
        file = os.path.splitext(file)[0]
        return file.split('/')[-1]

    # Controlla se il file recap.csv esiste
    if os.path.isfile(os.path.join(files_path, 'recap.csv')):
        # se esiste si apre in modalità "append" per non sovrascrivere il file
        # esistente
        recap_csv = open(os.path.join(files_path, 'recap.csv'), "a")
        # Oggetto "writer" per aggiungere righe al file
        writer = csv.writer(recap_csv)
    else:
        # se non esiste si crea in modalità esclusiva (restituisce errore se il
        # file esiste)
        recap_csv = open(os.path.join(files_path, 'recap.csv'), "x")
        # Prima riga con i nomi delle colonne
        title_row = ['name', 'type', 'size(B)']
        # Oggetto "writer" per aggiungere righe al file
        writer = csv.writer(recap_csv)
        # Inizializza il file csv con i titoli delle colonne
        writer.writerow(title_row)

    # Stampa a schermo l'operazione
    typer.echo(
        f"{get_name(file)} type:{get_type(file)} size:{get_size(file)}B")
    # Salva l'operazione su csv
    row = [get_name(file), get_type(file), get_size(file)]
    writer.writerow(row)
    # Sposta i file in base al tipo
    if get_type(file) == 'audio':
        shutil.move(
            os.path.join(
                files_path, file), os.path.join(
                files_path, 'audio'))
    elif get_type(file) == 'doc':
        shutil.move(
            os.path.join(
                files_path, file), os.path.join(
                files_path, 'docs'))
    else:
        shutil.move(
            os.path.join(
                files_path, file), os.path.join(
                files_path, 'images'))
    # Chiude il file csv
    recap_csv.close()


if __name__ == "__main__":
    typer.run(main)
