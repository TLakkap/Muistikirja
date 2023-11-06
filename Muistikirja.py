import pickle
import time

def avaaTiedosto(tiedosto, tila):
	try:
		tiedosto = open(tiedosto, tila)
	except:
		print("Virhe tiedostossa, luodaan uusi", tiedosto + ".")
		tiedosto = open(tiedosto, "wb")
	return tiedosto

def suljeTiedosto(tiedosto):
	tiedosto.close()

def lueTiedosto(tiedosto):
	try:
		muistikirja = pickle.load(tiedosto)
	except:
		muistikirja = []
	return muistikirja

def muistikirja():
	tiedosto = avaaTiedosto("muistio.dat", "rb")
	muistikirja = lueTiedosto(tiedosto)
	while True:
		print("(1) Lue muistikirjaa")
		print("(2) Lisää merkintä")
		print("(3) Muokkaa merkintää")
		print("(4) Poista merkintä")
		print("(5) Tallenna ja lopeta\n")
		valinta = input("Mitä haluat tehdä?: ")
		if valinta == "1":
			for i in muistikirja:
				print(i)
		elif valinta == "2":
			merkinta = input("Kirjoita uusi merkintä: ")
			aika = time.strftime("%X %x")
			tallennettava = merkinta + ":::" + aika
			muistikirja.append(tallennettava)
			print(muistikirja)
		elif valinta == "3":
			pituus = len(muistikirja)
			print("Listalla on", pituus, "merkintää.")
			muutettava = int(input("Mitä niistä muutetaan?: "))
			muutettavaTeksti = muistikirja[muutettava-1]
			print(muutettavaTeksti)
			aikaleima = muutettavaTeksti[-20:]
			uusiTeksti = input("Anna uusi teksti: ")
			muistikirja[muutettava-1] = uusiTeksti + aikaleima
		elif valinta == "4":
			pituus = len(muistikirja)
			print("Listalla on", pituus, "merkintää.")
			poistettava = int(input("Mitä niistä poistetaan?: "))
			poistettavaTeksti = muistikirja.pop(poistettava-1)
			print("Poistettiin merkintä", poistettavaTeksti)
		elif valinta == "5":
			tiedosto = avaaTiedosto("muistio.dat", "wb")
			pickle.dump(muistikirja, tiedosto)
			print("Lopetetaan.")
			break
	suljeTiedosto(tiedosto)

def main():
	muistikirja()

if __name__ == "__main__":
	main()