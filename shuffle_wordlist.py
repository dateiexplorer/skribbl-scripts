from os import path
import random
import sys

# Ueberprueft, ob ein Argument uebergeben wurde
if len(sys.argv) == 2:
    # Dateiname holen
    inputfile = str(sys.argv[1])
else:
    print('Enter a filename of a wordlist you want to shuffle:')
    inputfile = input()

# Ueberprueft, ob die Datei existiert
if not path.exists(inputfile) or not path.isfile(inputfile):
    print('File not found or is not valid!')
    sys.exit()


print('Read skribbl.io wordlist...')

# Oeffnen der Datei
strings = open(inputfile, 'r').readlines()

# Entfernen von Whitespace
strings = ['%s' % s.rstrip() for s in strings]

print('Shuffle wordlist...')

# Liste durchmischen
random.shuffle(strings)

# Ausgabedatei definieren
outputfile = inputfile + '.shuffle.txt'

print('Write out wordlist...')

# Datei schreiben
out = open(outputfile, 'w')
for line in strings:
    out.write(line + ',')

print('File was successfully written: ' + outputfile)

# Aufraeumen
out.flush()
out.close()
