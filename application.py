#coding: utf-8
import re
import urllib, os
print ""
print "                ***** MOTOR DE BUSQUEDA *****"
print "Este motor de busqueda le permite busca una palabra deseada de entre"
print "dos paginas web, debe ingresar una palabra y el motor de busqueda"
print "le mostrara en que pagina se presenta mas dicha palabra...:"
print ""
class encontrar(object):
	def busqueda(self):
		
			self.pagina1=raw_input("Ingrese la primera pagina web http://")
			self.pagina2=raw_input("Ingrese la segunda pagina web http://")
			self.palabra=raw_input("Que palabra desea buscar?: ")
			print ""
#*********** urllib permite acceder la pagina web deseada********************************
#*********** urlopen permite abrir la pagina deseada ************************************
#*********** guardamos nuestros datos en las variables pagina1_open y pagina2_open*******
			pagina1_open=urllib.urlopen(self.pagina1)
			pagina2_open=urllib.urlopen(self.pagina2)
#*********** ya que hemos accedido y abierto las pagina leemos su contenido *************
			lectura_pagina1=pagina1_open.read()
			lectura_pagina2=pagina2_open.read()
#*********** utilizamos la variable self.palabra para saber que palabra deseamos contar**
#*********** con la funcion len contamos cuantas palabras existen en cada pagina ********
			contar_pagina1=len(re.findall(self.palabra,lectura_pagina1))
			contar_pagina2=len(re.findall(self.palabra,lectura_pagina2))
			if contar_pagina2 > contar_pagina2:
				print "La pagina con mayor numero de coincidencias es: "
				print self.pagina1
				print "La cantidad de coincidencias es de: %S"%(contar_pagina1)
				
			elif contar_pagina1==0:
				print"Ninguna palabra encontrada"
			elif contar_pagina2==0:
				print "Ninguna palabra encontrada"
			else:
				print "La pagina con mayor numero de coincidencias es: "
				print self.pagina2
				print "La cantidad de coincidencias es de: %s"%(contar_pagina2)

hola=encontrar()
hola.busqueda()
