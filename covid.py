  #!/usr/bin/python


import smtplib
from os import system

def main():
   print """
                                /$$       /$$         /$$    /$$$$$$ 
                               |__/      | $$       /$$$$   /$$__  $$
  /$$$$$$$  /$$$$$$  /$$    /$$ /$$  /$$$$$$$      |_  $$  | $$  \ $$
 /$$_____/ /$$__  $$|  $$  /$$/| $$ /$$__  $$ /$$$$$$| $$  |  $$$$$$$
| $$      | $$  \ $$ \  $$/$$/ | $$| $$  | $$|______/| $$   \____  $$
| $$      | $$  | $$  \  $$$/  | $$| $$  | $$        | $$   /$$  \ $$
|  $$$$$$$|  $$$$$$/   \  $/   | $$|  $$$$$$$       /$$$$$$|  $$$$$$/
 \_______/ \______/     \_/    |__/ \_______/      |______/ \______/ 
                                                                     
                                                                     
                                                                     
"""
main()
print '[1] Sintomas'
print '[2] Precausiones'
print '[3] Descontaminacion De Objetos'
print '[4] AYUDA'
print '[5] Salir'
option = input('Introdusca la opcion =>')
if option == 1:
   system('clear')
   print "Los sintomas mas habituales son:"
   print ""
   print "Fiebre"
   print "Tos seca"
   print "cansancio"
   print ""
   print "Sintomas menos habituales son:"
   print ""
   print "Molestias y dolores."
   print "Dolor de garganta."
   print "Diarrea."
   print "Conjuntivitis."
   print "Dolor de cabeza."
   print "Pérdida de olfato o de gusto."
   print "pérdida de color en los dedos de las manos o de los pies."
   print ""
   print "para mas ayuda visita la paguina: www.argentina.god.ar"

if option == 2:
   system('clear')
   print "Las precausiones que hay que tomas son:"
   print ""
   print "Usar barbijo al salir de casa o/a comprar/cominar/correr/etc."
   print "Lavarse las manos constantemente."
   print "NO tocarnos la cara."
   print "Mantener la distancia social"
   print ""
   print "para mas ayuda visita la paguina: www.argentina.god.ar"
   

if option == 3:
   system('clear')
   print "Para preparar alcohol siga los siguientes pasos:"
   print ""
   print "Cada 100 ml de alcohol 96° (el que se compra en farmacias), se incorporan 41 ml de agua. Suele decirse que son 40 ml aproximadamente, pero la medida exacta es de 41, y para eso se requieren materiales de medición precisos (que bien pueden reemplazarse por algún medidor de cocina correctamente utilizado). El agua que usamos debe ser potable y es conveniente hervirla primero. Luego del hervor, debe dejarse enfriar para evitar que el alcohol se evapore y la concentración sea la esperada.La confusión más habitual es creer que el alcohol diluido al 70% puede realizarse mezclando 7 partes de alcohol con 3 partes de agua. Esto no es correcto porque la mezcla de alcohol y agua producen que el volumen se contraiga. Lo que se necesita, entonces, es más volumen de agua. Esto es: si quiero hacer 100 ml de producto, necesito 41 ml (como se menciona antes) de agua. Así se obtiene la concentración adecuada."
   print ""
   print "Para mas informacion entra a : www.argentina.god.ar"

if option == 4:
   system('clear')
   print "Para mas informacion entra a : www.argentina.god.ar"

if option == 5:
   system('clear')
   print "Gracias por usar este programa"
