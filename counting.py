import sys
def readfile(inputfile):
    try:
        with open(inputfile, "r") as file:
            data = file.read().splitlines() #luetaan rivettäin ja palautetaan tieto
        return data
    except IOError:
        print(f"Error file handling the file '{inputfile}' ..abort")
        sys.exit(0)


def analyzefile(brands):
    calculate = {}
    for brand in brands:
        if brand in calculate:
            calculate[brand] += 1 #jos avain kirjastossa, kasvatetaan sen arvoa yhdellä, kunnes avain vaihtuu
        else:
            calculate[brand] = 1 #lisätään avain kirjastoon

    return calculate #palautetaan kirjasto pääohjelmaan

def writefile(outputfile, calculate, brands):
    try:
        with open(outputfile, "w", encoding="utf-8") as file:
            print(f"Recognized {len(calculate)} car brands and {len(brands)} cars:")
            file.write(f"Recognized {len(calculate)} car brands and {len(brands)} cars:\n")
            for brand in sorted(calculate):
                lukumaara = calculate[brand] # otetaan avain merkkinä, lukumääräksi määritellään sen arvo
                if lukumaara == 1: #jos arvo on 1, tulee yksikkö tulostus ja kirjoitus
                    file.write(f"{brand}: {lukumaara} car\n") 
                    print(f"{brand}: {lukumaara} car") 
                else:
                    file.write(f"{brand}: {lukumaara} cars\n") #kirjoitetaan tieto tiedostoon
                    print(f"{brand}: {lukumaara} cars") #tulostetaan tieto konsoliin
    except IOError:
        print(f"Error processing file '{outputfile}', abort.")
        sys.exit(0)
    return None


def main():
    inputfile = input("Enter the name of the file to be read: ")
    outputfile = input("Enter the name of the file to be written: ")
    brands = readfile(inputfile) #merkit listaa monta riviä tekstiä ollut

    if not brands: #jos rivejä ei ole tiedostossa, katkaistaan ohjelman pyöritys.
        print("The file was empty, no car brand was recognized.")
        print("Thank you for using the program.")
        sys.exit(0)
    laskuri = analyzefile(brands) #laskuri on kirjasto jonne analysoitu tieto tallentuu
    
    writefile(outputfile, laskuri, brands) #kirjoitetaan laskurin (kirjasto) tiedot kirjoitettavaan tiedostoon

    print("Thank you for using the program.")
    return None

main()