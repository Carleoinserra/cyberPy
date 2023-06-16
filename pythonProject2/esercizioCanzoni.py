import pickle
class Canzone:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Titolo: {self.title}, Autore: {self.author}, Anno: {self.year}"


def AddSong():
    print("Inserisci i parametri della canzone da aggiungere")
    title = input("Titolo della canzone: ")
    author = input("Autore: ")
    year = int(input("Anno di pubblicazione: "))
    print()

    newSong = Canzone(title, author, year)

    return newSong

def SearchSong(listSong):
    num = 2

    while not num == 0:
        count = 0
        print("Inserisci il titolo della canzone da cercare")
        searchTitle = input()
        print()

        for el in listSong:
            if el.title == searchTitle:
                print("Canzone trovata!! Ecco tutti i dettagli")
                print(f"Titolo: {el.title}")
                print(f"Autore: {el.author}")
                print(f"Anno di pubblicazione: {el.year}")
                print()
                count += 1

        if not count == 1:
            print("Errore!! La canzone non è stata trovata")
            print("Vuoi riprovare? Premi 0 per NO, altrimenti premi un qualsiasi altro numero")
            num = int(input())
            print()
        else:
            num = 0

def AuthorSongs(listSong):
    count = 0
    num = 2

    while not num == 0:
        print("Inserisci l'autore da cercare")
        search = input()
        print()

        for el in listSong:
            if el.author == search:
                print(f"Titolo: {el.title}, Anno: {el.year}")
                print()
                count += 1

        if(not count >= 1):
            print("Errore!! L'autore non è stato trovato")
            print("Vuoi riprovare? Premi 0 per NO, altrimenti premi un qualsiasi altro numero")
            num = int(input())
            print()
        else:
            num = 0

def Remove(listSong):
    num = 2

    while not num == 0:
        count = 0
        print("Inserisci il titolo della canzone da eliminare")
        searchTitle = input()
        print()

        for el in listSong:
            if el.title == searchTitle:
                print("Canzone Eliminata")
                print()
                listSong.remove(el)
                count = 1

        if not count == 1:
            print("Errore!! La canzone non è stata trovata")
            print("Vuoi riprovare? Premi 0 per NO, altrimenti premi un qualsiasi altro numero")
            num = int(input())
            print()
        else:
            num = 0
            return listSong


num = 10
listSong = []

while not num == 0:
    print("Scegli un opzione")
    print("1. Aggiungi una canzone")
    print("2. Cerca una canzone")
    print("3. Visualizza tutte le canzoni di un autore")
    print("4. Elimina una canzone")
    print("0. Esci dal programma")

    num = int(input())

    print()

    if num == 1:
        listSong.append(AddSong())

    elif num == 2:
        if not listSong == []:
            SearchSong(listSong)
        else:
            print("Errore!! Non c'è alcuna canzone")

    elif num == 3:
        if not listSong == []:
            AuthorSongs(listSong)
        else:
            print("Errore!! Non c'è alcuna canzone")

    elif num == 4:
        if not listSong == []:
            listSong = Remove(listSong)
        else:
            print("Errore!! Non c'è alcuna canzone")
    elif num == 5:


        f = open("test3.pkl", "wb")

        pickle.dump(listSong, f)


        f.close()

    elif num == 6:
        f = open("test3.pkl", "rb")
        unpickler = pickle.Unpickler(f);
        listSong = unpickler.load();
        f.close()
        for i in listSong:
            print(i)

    elif num == 0:
        print("Sei uscito dal programma")

    else:
        print("ERRORE!! Inserimento invalido")
        print("Riprova")
        print()