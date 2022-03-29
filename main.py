# psutil wird zum Auslesen der CPU-Last unter Windows verwendet (Muss jedoch installiert werden).
# Unter pycharm (File > Settings > Project: pythonProject >Python interpreter > +psutil).
# Unter Python direkt oder anderen IDEs (CMD> "py -m pip install psutil").
import psutil
import os

# Die Zeit gibt, in Sekunden, an wie lange das Interval zur Messung der CPU-Last ist (Minimum=0.1)
zeit = 1

# Gibt die Anzahl der Durchläufe des Programms an (Minimum=1 für einen Durchlauf)
loop = 60

# Variablen zur bestimmung der CPU Belastungsgrenzen (Minimum und Maximum der moderaten/gelben Grenze) maxgelb>mingelb!
mingelb = 50
maxgelb = 85

def cpulast():
    # Kommando aus der PSutil Bibliothek um die Auslastung der CPU in einem Intervall anzugeben.
    cpulast = psutil.cpu_percent(interval=zeit)
    # Kommando aus os um die Konsole zu leeren (funktioniert nicht in der IDE-Konsole)
    os.system('cls')
    print(cpulast, "% CPU-Auslastung")
    return cpulast


def belastung(cpulast):
    # Wenn die CPU-Last unter der gelben Mindestgrenze somit unter gelb/moderat
    if cpulast < mingelb:
        print("Die CPU-Auslastung liegt unter", mingelb, "%, alles im grünen Bereich!")
    # Wenn die CPU-Last unter der gelben Maximum-Grenze somit innerhalb von gelb/moderat
    elif cpulast < maxgelb:
        print("Die CPU-Auslastung liegt zwischen ", mingelb, "%  und ", maxgelb, "%. moderate Auslastung!")
    else:
        print("Über ", maxgelb, "% CPU-Auslastung, starke Auslastung!")


# Visualisierung der CPU-Last mit 100 Strichen welche Parallel zur oberen Auswertung ablaufen
def visualize(cpulast):
    # Neue Variable um diese von float auf int zu setzen und +0,5 um mathematisch korrekt zu runden
    cpulastint = cpulast + 0.5
    cpulastint = int(cpulastint)
    # visuello ist zur Visualisierung der nicht genutzte CPU-Ressourcen
    # visuell1,2,3 für die Stärken der Auslastungen um diese farblich zu markieren 1=grün 2=gelb 3=rot
    # '\033[32m' stehen für Farbcodes um die Visualisierung farblich darzustellen '\x1b[0m' zum reset der farben.
    visuello = 100 - cpulastint
    visuello = visuello * "-"
    if cpulastint < mingelb:
        visuell1 = cpulastint * "|"
        print("[" + '\033[92m' + visuell1 + '\x1b[0m' + visuello + "]")
    elif cpulastint < maxgelb:
        visuell1 = mingelb * "|"
        calc = cpulastint - mingelb
        visuell2 = calc * "|"
        print("[" + '\033[92m' + visuell1 + '\033[33m' + visuell2 + '\x1b[0m' + visuello + "]")
    else:
        visuell1 = mingelb * "|"
        gelb = maxgelb-mingelb
        visuell2 = gelb * "|"
        calc = cpulastint - maxgelb
        visuell3 = calc * "|"
        print("[" + '\033[92m' + visuell1 + '\033[33m' + visuell2 + '\033[91m' + visuell3 + '\x1b[0m' + visuello + "]")


# Loop welche alle funktionen chronologisch durchgeht und diese anspricht
while loop > 0:
    loop -= 1
    # Zieht, die Variable last aus der Funktion cpulast heraus
    last = cpulast()
    # Beide funktionen nehmen die Variable Last hinein
    belastung(last)
    visualize(last)

