#Librerias
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
import time
import os
import sys
#Listas

articulos=[]
fuente='Helvetica'
w, h = A4
cliente=[]
#Funciones
def convertir(dato):
	try:
		dato = int(dato)
		return dato
	except ValueError:
		try:
			dato = float(dato)
			return dato
		except ValueError:
			return messagebox.showerror(title="¡Error!", message="Error al convertir")

#def convertirString(dato):
	

def salir():
	respuesta = messagebox.askokcancel(title="Pregunta", message="¿Desea salir?")
	if respuesta:
		sys.exit()
		
def informacion():
	messagebox.showinfo(title="Información", message="Presupuesto v2, programa realizado por Nicolas Gonzalez. Mail: nicolasgonzalez470@gmail.com")

def agregarArticulos(lista=articulos):
	cant=entradaCant.get()
	cant=convertir(cant)
	nombre=entradaNomArt.get()
	ancho=entradaAncho.get()
	ancho=convertir(ancho)
	alto=entradaAlto.get()
	alto=convertir(alto)
	precioU=entradaPrecioU.get()
	precioU=convertir(precioU)
	if cant=='ok' or ancho=='ok' or alto=='ok' or precioU=='ok' or nombre=='ok':
		messagebox.showerror("Error", "Faltan datos del cliente")
		pass
	else:
		sup=ancho*alto
		precioTotal=cant*precioU
		lista.append((cant,nombre,ancho,alto,sup,precioU,precioTotal))
		string=f'Se ha agregado el articulo {nombre}.'
		campoTexto=str(cant)+'\t'+str(nombre)+'\t\t'+str(ancho)+'\t'+str(alto)+'\t'+str(precioU)+'\n'
		campo.insert(tk.END,campoTexto)
		messagebox.showinfo(message=string, title="Articulo agregado")
		entradaCant.delete(0, tk.END)
		entradaNomArt.delete(0, tk.END)
		entradaAncho.delete(0, tk.END)
		entradaAlto.delete(0, tk.END)
		entradaPrecioU.delete(0, tk.END)
	
	
	
def agregarCliente():
	if len(cliente)==1:
		messagebox.showerror("Error", "Ya agregaste los datos de un cliente")
		pass
	else:
		numPresupuesto=entradaNumPres.get()
		numPresupuesto=convertir(numPresupuesto)
		numCliente=entradaNumCliente.get()
		#numCliente=convertir(numCliente)
		nombreCliente=entradaNomCliente.get()
		nombreCliente=str(nombreCliente)
		apelCliente=entradaApelCliente.get()
		apelCliente=str(apelCliente)
		if numPresupuesto=='ok' or numCliente=='ok' or nombreCliente=='ok' or apelCliente=='ok':
			messagebox.showerror("Error", "Faltan datos del cliente")
			pass
		else:
			cliente.append((numPresupuesto,numCliente,nombreCliente,apelCliente))
			messagebox.showinfo(title="Agregado", message='Se agrego los datos del cliente exitosamente.')
			entradaNumPres.delete(0, tk.END)
			entradaNumCliente.delete(0, tk.END)
			entradaNomCliente.delete(0, tk.END)
			entradaApelCliente.delete(0, tk.END)
		
		
		
		

def crearPDF():
	w, h = A4
	variable=checkbutton_estado.get()
	numPresupuesto,numCliente,nombreCliente,apelCliente=cliente[0]
	direct=os.getcwd()
	local="\Presupuestos-PDF"
	direct+=local
	if os.path.exists(direct)==False:
		os.mkdir(direct)
	numPresupuesto1=str(numPresupuesto)+'.pdf'
	nomArch=direct+'/'+numPresupuesto1
	c = canvas.Canvas(nomArch, pagesize=A4)
	logo(c)
	fecha(c)
	textoPresupuesto(numPresupuesto, c)
	datoCliente(numCliente,nombreCliente,apelCliente,c)
	dibujarLinea(h - 150,c)
	categorias(c)
	imprimirArticulos(articulos,variable,c)
	messagebox.showinfo(title="Archivo creado", message=f"Se ha creado satisfactoriamente el archivo {numPresupuesto}.pdf")
	c.save()
	

def logo(c):
	email='E-Mail de contacto: info.ventas.decorglass@gmail.com'
	c.drawImage("decorglass.jpg", 20, 700, width=150, height=150)
	#E-Mail
	textEmail=c.beginText(w-315,720)
	textEmail.setFont(fuente,12)
	textEmail.textLine(email)
	c.drawText(textEmail)	

def fecha(c):
	named_tuple = time.localtime() 
	time_string = time.strftime("%d/%m/%Y   %H:%M", named_tuple)

	textDate=c.beginText(470,700)
	textDate.setFont(fuente,12)
	textDate.textLine(time_string)
	c.drawText(textDate)
	
def textoPresupuesto(numPresupuesto, c):
	presupuesto='PRESUPUESTO   #   '+str(numPresupuesto)
	textPres = c.beginText(200, 790)
	textPres.setFont(fuente, 15)
	textPres.textLine(presupuesto)
	c.drawText(textPres)

def datoCliente(nroCliente,nomCliente,apelCliente,c):
	nomCliente=nomCliente.upper()
	apelCliente=apelCliente.upper()
	name=apelCliente+' '+nomCliente
	cliente='CLIENTE: '+str(nroCliente)+'-'+name
	textCliente=c.beginText(20,700)
	textCliente.setFont(fuente,12)
	textCliente.textLine(cliente)
	c.drawText(textCliente)

def dibujarLinea(y,c):
	x = 20
	c.line(x, y, w-x, y)

def categorias(c):
	#CANTIDAD
	cantidadCat='Cantidad'
	textCantidadCat=c.beginText(30,h-170)
	textCantidadCat.setFont(fuente,12)
	textCantidadCat.textLine(cantidadCat)
	c.drawText(textCantidadCat)
	#DESCRIPCION
	descripcionCat='Descripción'
	textDescripcionCat=c.beginText(140,h-170)
	textDescripcionCat.setFont(fuente,12)
	textDescripcionCat.textLine(descripcionCat)
	c.drawText(textDescripcionCat)
	#MEDIDAS
	medidasCat='Medidas'
	textMedidasCat=c.beginText(w-330,h-170)
	textMedidasCat.setFont(fuente,12)
	textMedidasCat.textLine(medidasCat)
	c.drawText(textMedidasCat)
	#SUPERFICIE
	superficieCat='Superficie'
	textSuperficieCat=c.beginText(w-260,h-170)
	textSuperficieCat.setFont(fuente,12)
	textSuperficieCat.textLine(superficieCat)
	c.drawText(textSuperficieCat)
	#TOTAL UNIDAD
	uniCat='Precio por U.'
	textUniCat=c.beginText(w-190,h-170)
	textUniCat.setFont(fuente,12)
	textUniCat.textLine(uniCat)
	c.drawText(textUniCat)
	#TOTAL
	totalCat='Total'
	textTotalCat=c.beginText(w-60,h-170)
	textTotalCat.setFont(fuente,12)
	textTotalCat.textLine(totalCat)
	c.drawText(textTotalCat)

def imprimirArticulos(lista,opc,c):
	precioTotal=0
	superficieTotal=0
	x=27
	y=h-200
	for i in range(len(lista)):
		cantidad,nombre,ancho,alto,sup,precio,total=lista[i]
		precioTotal+=total
		superficieTotal+=sup
		#CANTIDAD
		textCantT=c.beginText(x+10,y)
		textCantT.setFont(fuente,12)
		textCantT.textLine(str(cantidad))
		c.drawText(textCantT)
		#NOMBRE
		textNom=c.beginText(x+50,y)
		if len(nombre)<25:
			textNom.setFont(fuente,12)
		else:
			textNom.setFont(fuente,10)
		textNom.textLine(nombre)
		c.drawText(textNom)
		#MEDIDAS
		medida=f'{ancho} X {alto}'
		textMed=c.beginText(x+233,y)
		textMed.setFont(fuente,12)
		textMed.textLine(str(medida))
		c.drawText(textMed)
		#SUPERFICIE
		superficie=f'{sup}  M2'
		textSup=c.beginText(w-260,y)
		textSup.setFont(fuente,12)
		textSup.textLine(str(superficie))
		c.drawText(textSup)
		#PRECIO UNIDAD
		textPrec=c.beginText(w-160,y)
		textPrec.setFont(fuente,12)
		textPrec.textLine(str(precio))
		c.drawText(textPrec)
		#PRECIO TOTAL
		total=round(total,2)
		textPT=c.beginText(w-60,y)
		textPT.setFont(fuente,12)
		textPT.textLine(str(total))
		c.drawText(textPT)
		#Cambio
		y=y-20
	#Sup Total
	superficieTotal=str(superficieTotal)+' M2 '
	textSuperficie=c.beginText(w-260,y)
	textSuperficie.setFont(fuente,12)
	textSuperficie.textLine(superficieTotal)
	c.drawText(textSuperficie)
	#Barra
	y-=10
	dibujarLinea(y,c)
	precioTotal=round(precioTotal,2)
	if opc==True:
		totalIva=precioTotal*1.21
		totalIva=round(totalIva,2)
		IVA=precioTotal*0.21
		IVA=round(IVA,2)
	else:
		totalIva=precioTotal
		IVA=0	
	y-=15
	labelSubtotal='SUBTOTAL'
	textLSubt=c.beginText(w-250,y)
	textLSubt.setFont(fuente,12)
	textLSubt.textLine(labelSubtotal)
	c.drawText(textLSubt)
	#Precio TOTAL
	textTotalP=c.beginText(w-60,y)
	textTotalP.setFont(fuente,12)
	textTotalP.textLine(str(precioTotal))
	c.drawText(textTotalP)
	#Label TOTAL IVA
	y-=30
	labelIva='IVA'
	textImp=c.beginText(w-250,y)
	textImp.setFont(fuente,12)
	textImp.textLine(labelIva)
	c.drawText(textImp)
	#IVA
	precioConIva=str(IVA)
	textTotIva=c.beginText(w-60,y)
	textTotIva.setFont(fuente,12)
	textTotIva.textLine(precioConIva)
	c.drawText(textTotIva)
	#Label Precio Total con IVA
	y-=15
	labelTtlIva='TOTAL'
	textLabelImp=c.beginText(w-250,y)
	textLabelImp.setFont(fuente,12)
	textLabelImp.textLine(labelTtlIva)
	c.drawText(textLabelImp)
	#Precio con IVA
	textIva=c.beginText(w-60,y)
	textIva.setFont(fuente,12)
	textIva.textLine(str(totalIva))
	c.drawText(textIva)
	#Rectangulo
	y-=30
	rectangulo(y,c)
	texto_rectangulo(y,c)
	

def rectangulo(y,c):
	c.rect(25, y, 290, 80)

def texto_rectangulo(y,c):
	y+=71
	parr1='SR CLIENTE: El Presupuesto refleja el valor correspondiente al material solicitado con las'
	textParr1=c.beginText(27,y)
	textParr1.setFont(fuente,7)
	textParr1.textLine(parr1)
	c.drawText(textParr1)
	y-=10
	parr2='medidas provistas por usted o recomendadas por nuestros técnicos. Es IMPORTANTE que'
	textParr2=c.beginText(27,y)
	textParr2.setFont(fuente,7)
	textParr2.textLine(parr2)
	c.drawText(textParr2)
	y-=10
	parr3='revise el presupuesto ya que su aprobación es compromiso de producción del mismo.'
	textParr3=c.beginText(27,y)
	textParr3.setFont(fuente,7)
	textParr3.textLine(parr3)
	c.drawText(textParr3)
	y-=10
	parr4='La empresa no se hará responsable por diferencias que puedan producirse por este motivo.'
	textParr4=c.beginText(27,y)
	textParr4.setFont(fuente,7)
	textParr4.textLine(parr4)
	c.drawText(textParr4)
	y-=10
	parr5='Este presupuesto está sujeto a posibles aumentos. El precio definitivo de las mercaderías '
	textParr5=c.beginText(27,y)
	textParr5.setFont(fuente,7)
	textParr5.textLine(parr5)
	c.drawText(textParr5)
	y-=10
	parr6='presupuestadas se fijara en el momento de su efectivo pago.'
	textParr6=c.beginText(27,y)
	textParr6.setFont(fuente,7)
	textParr6.textLine(parr6)
	c.drawText(textParr6)

#Main



root = tk.Tk()
root.title("Presupuestos v2.0")
root.config(width=700, height=500)

#Cabecera
logoEmpresa = ttk.Label(root, text='DecorGlass')
logoEmpresa.place(x=10,y=10)

#Datos del cliente

tituloCliente=ttk.Label(root, text='Datos del cliente').place(x=15,y=30)
	#Numero de presupuesto
etiquetaNumPres=ttk.Label(root, text='N° de presupuesto: ').place(x=15,y=55)
entradaNumPres=ttk.Entry()
entradaNumPres.place(x=15, y=75)
	#Numero de Cliente
etiquetaNumCliente=ttk.Label(root, text='Nombre/s: ').place(x=15,y=100)
entradaNomCliente=ttk.Entry()
entradaNomCliente.place(x=15, y=120)
	#Nombre Cliente
etiqNomCliente=ttk.Label(root, text='N° de cliente: ').place(x=250,y=55)
entradaNumCliente=ttk.Entry()
entradaNumCliente.place(x=250,y=75)
	#Apellido Cliente
etiqApelCliente=ttk.Label(root, text=' Apellido/s: ').place(x=250,y=100)
entradaApelCliente=ttk.Entry()
entradaApelCliente.place(x=250,y=120)
	#Boton agregar cliente
botonAgrCli=ttk.Button(text='Agregar cliente', command=agregarCliente).place(x=400,y=120)
#Datos de articulos

tituloArticulos=ttk.Label(root, text='Datos del articulo').place(x=15,y=150)
	#Cantidad
etiquetaCant=ttk.Label(root, text='Cantidad: ').place(x=15,y=175)
entradaCant=ttk.Entry()
entradaCant.place(x=15,y=195)
	#Nombre del articulo
etiquetaNomArt=ttk.Label(root, text='Nombre: ').place(x=250,y=175)
entradaNomArt=ttk.Entry()
entradaNomArt.place(x=250,y=195)
	#Ancho
etiquetaAncho=ttk.Label(root, text='Ancho: ').place(x=15,y=220)
entradaAncho=ttk.Entry()
entradaAncho.place(x=15,y=240)
	#Alto
etiquetaAlto=ttk.Label(root, text='Largo: ').place(x=250,y=220)
entradaAlto=ttk.Entry()
entradaAlto.place(x=250,y=240)
	#Precio x u.
etiquetaPrecioU=ttk.Label(root,text='Precio por Unidad: ').place(x=15,y=265)
entradaPrecioU=ttk.Entry()
entradaPrecioU.place(x=15,y=285)

#Campo de texto

campo=tk.Text()
campo.place(x=15, y=315, height=135)
encabezado='Cant\tNombre\t\tAlto\tAncho\tPrecio por Unidad\n'
campo.insert(tk.END,encabezado)

#Botones
checkbutton_estado = tk.BooleanVar()
checkbutton = ttk.Checkbutton(text="IVA", variable=checkbutton_estado)
checkbutton.place(x=250,y=285)
botonInfo=ttk.Button(text='Informacion', command=informacion).place(x=15,y=460)
botonAgrArt=ttk.Button(text='Agregar art.', command=agregarArticulos).place(x=182.5,y=460)
botonCrear=ttk.Button(text='Crear PDF', command=crearPDF).place(x=350,y=460)
botonSalir=ttk.Button(text='Salir', command=salir).place(x=571.5,y=460)


root.mainloop()


