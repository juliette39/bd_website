from main.add_album import get_infos_bd
from main.add_album.error import Error
from main.add_album.sheet_connection import Conn
from main.update_database import update

def liste_from_dict(infos):
    titles = ["ISBN", "Album", "Numéro", "Série", "Scénario", "Dessin", "Couleurs",
              "Éditeur", "Date de publication", "Edition", "Pages", None, "Prix", None, None, None, None, "Synopsis",
              "Image"]

    liste = []
    for title in titles:
        if title in infos:
            liste.append(infos[title])
        elif title is None:
            liste.append("")
        else:
            raise IndexError(f"{title} is missing")
    return liste


def add_line(connection, infos, test=False):
    liste = liste_from_dict(infos)
    if not test:
        connection.append(liste)


def add(isbn, doc_name, sheet=None, test=False, logs="logs.txt"):
    connection = None
    try:
        if not test:
            connection = Conn(logs)
            connection.open(doc_name, sheet)
    except:
        message_log = "Google Sheet non accessible."
        raise Error(message_log, isbn, logs)
    else:
        if not test:
            if connection.double(isbn):
                message_log = f"{isbn} est déjà dans la base de données"
                raise Error(message_log, isbn, logs)

        try:
            infos = get_infos_bd.main(isbn, logs)
        except:
            raise Error("Erreur dans la recherche de données", isbn, logs)

        if type(infos) is not type(dict()):
            message_log = f"{infos} pas du bon type"
            raise Error(message_log, isbn, logs)

        try:
            add_line(connection, infos, test)
        except:
            message_log = f"{infos} n'a pas été ajouté correctement"
            raise Error(message_log, isbn, logs)
        else:
            title = infos["Album"]
            if title is None or title == "":
                title = infos["ISBN"]
            if not test:
                print(f"{title} ajouté avec succès !")
            return infos


def add_album(isbn):
    doc_name = "bd"
    sheet_name = "BD"

    if isbn == 0:
        message_log = f"Aucun ISBN n'a été renseigné"
        Error(message_log, "")
    else:
        try:
            isbn = int(isbn)
        except TypeError:
            if isbn is not None and isbn != "":
                raise Error(f"ISBN {isbn} invalide (doit être un grand entier)", isbn)
            else:
                raise Error(f"ISBN vide ou nul", isbn)
        else:
            infos = add(isbn, doc_name, sheet_name)
            update()
            return infos
