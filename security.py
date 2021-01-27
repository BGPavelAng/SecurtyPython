#!/usr/bin/python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import asyncio


enmap = Gtk.Entry()
enmapa = Gtk.Entry()

ex4text = Gtk.Entry()

di1text = Gtk.Entry()
di2text = Gtk.Entry()
di3text = Gtk.Entry()

WP2text = Gtk.Entry()
WP3text = Gtk.Entry()

Nktext = Gtk.Entry()

HC1text = Gtk.Entry()
HC2text = Gtk.Entry()
HC3text = Gtk.Entry()

JN2text = Gtk.Entry()
JN3text = Gtk.Entry()

HY2text = Gtk.Entry()
HY3text = Gtk.Entry()
HY4text = Gtk.Entry()

async def run(cmd):
		proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
		stdout, stderr = await proc.communicate()

		if stdout:
			print(f'[Nmap]\n{stdout.decode()}')

		await proc.wait()

		if proc.returncode != 0:
			print("Error")
		else:
			print("Termino")

async def rundi(cmd):
		proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
		stdout, stderr = await proc.communicate()

		if stdout:
			print(f'[Dirb]\n{stdout.decode()}')

		await proc.wait()

		if proc.returncode != 0:
			print("Error")
		else:
			print("Termino")


async def runwp(cmd):
		proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
		stdout, stderr = await proc.communicate()

		if stdout:
			print(f'[WPScan]\n{stdout.decode()}')

		await proc.wait()

		if proc.returncode != 0:
			print("Error")
		else:
			print("Termino")	


async def runnk(cmd):
		proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
		stdout, stderr = await proc.communicate()

		if stdout:
			print(f'[WPScan]\n{stdout.decode()}')

		await proc.wait()

		if proc.returncode != 0:
			print("Error")
		else:
			print("Termino")

async def runhc(cmd):
		proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
		stdout, stderr = await proc.communicate()

		if stdout:
			print(f'[Hashcat]\n{stdout.decode()}')

		await proc.wait()

		if proc.returncode != 0:
			print("Error")
		else:
			print("Termino")

async def runjn(cmd):
		proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
		stdout, stderr= await proc.communicate()

		if stdout:
			print(f'[JOHN]\n{stdout.decode()}')

		await proc.wait()

		if proc.returncode != 0:
			print("Error")
		else:
			print("Termino")

async def runhy(cmd):
		proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
		stdout, stderr = await proc.communicate()

		if stdout:
			print(f'[Hydra]\n{stdout.decode()}')

		await proc.wait()

		if proc.returncode != 0:
			print("Error")
		else:
			print("Termino")


async def runex(cmd):
		proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
		stdout, stderr = await proc.communicate()

		if stdout:
			print(f'[Enum4Linux]\n{stdout.decode()}')

		await proc.wait()

		if proc.returncode != 0:
			print("Error")
		else:
			print("Termino")

class winini(Gtk.Window):
	"""docstring for winini"""
	def __init__(self):
		Gtk.Window.__init__(self, title="Red de Seguridad")
		self.set_default_size(400,0)

		layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(layout)
		#contenedor
		notebook = Gtk.Notebook()
		self.add(notebook)

		bnmap = Gtk.Button(label="NMAP")
		ex4but = Gtk.Button(label="Enum4Linux")
		dibut = Gtk.Button(label="dirb")
		WPbut = Gtk.Button(label="WPScan")
		Nkbut = Gtk.Button(label="Nikto")
		HCbut = Gtk.Button(label="Hashcat")
		JNbut = Gtk.Button(label="John")
		HYbut = Gtk.Button(label="Hydra")

		enmap.set_text("Scan IP") 
		enmapa.set_text("-Pn -A -sT -p-")

		ex4text.set_text("Parametros enum4linux") 

		di1text.set_text("IP")
		di2text.set_text("-w")
		di3text.set_text("/usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt")

		WP2text.set_text("--enumerate")
		WP3text.set_text("/usr/share/wordlists/")

		Nktext.set_text("Parametros Nikto")

		HC2text.set_text("Parametros")
		HC3text.set_text("/usr/share/wordlists/")

		JN2text.set_text("Parametros")
		JN3text.set_text("/usr/share/wordlists/")

		HY2text.set_text("-t 5 -s port")
		HY4text.set_text("-l username")
		HY3text.set_text("-P /usr/share/wordlists/")

		self.page1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.page1.set_border_width(10)
		self.page1.add(Gtk.new_with_label("Scan de ip"))
		self.page1.add(enmap)
		self.page1.add(enmapa)
		self.page1.add(bnmap)
		bnmap.connect("clicked", self.nmapbut)
		self.page1.add(Gtk.Separator())
		self.page1.add(ex4text)
		self.page1.add(ex4but)
		ex4but.connect("clicked", self.ex4but)
		self.page1.add(Gtk.Separator())
		self.page1.add(Gtk.Entry())
		self.page1.add(Gtk.Button(label="Netdiscover"))
		self.page1.add(Gtk.Separator())
		notebook.append_page(self.page1, Gtk.Label("Scan ip"))

		self.page2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.page2.set_border_width(10)
		self.page2.add(Gtk.Label("Scan de web"))
		self.page2.add(di1text)
		self.page2.add(di2text)
		self.page2.add(di3text)
		self.page2.add(dibut)
		dibut.connect("clicked", self.dibut)
		self.page2.add(Gtk.Separator())
		self.page2.add(WP2text)
		self.page2.add(WP3text)
		self.page2.add(WPbut)
		WPbut.connect("clicked", self.WPbut)
		self.page2.add(Gtk.Separator())
		self.page2.add(Nktext)
		self.page2.add(Nkbut)
		Nkbut.connect("clicked", self.Nkbut)
		notebook.append_page(self.page2, Gtk.Label("Scan web"))

		self.page3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.page3.set_border_width(10)
		self.page3.add(Gtk.Label("Crackeadores"))
		self.page3.add(HC1text)
		self.page3.add(HC2text)
		self.page3.add(HC3text)
		self.page3.add(HCbut)
		HCbut.connect("clicked", self.HCbut)
		self.page3.add(JN2text)
		self.page3.add(JN3text)
		self.page3.add(JNbut)
		JNbut.connect("clicked", self.JNbut)
		self.page3.add(HY2text)
		self.page3.add(HY4text)
		self.page3.add(HY3text)
		self.page3.add(HYbut)
		HYbut.connect("clicked", self.HYbut)
		notebook.append_page(self.page3, Gtk.Label("Cracks"))

		self.page4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.page4.set_border_width(10)
		self.page4.add(Gtk.Label("Base de datos"))
		self.page4.add(Gtk.Entry())
		self.page4.add(Gtk.Button(label="Sqlmap"))
		notebook.append_page(self.page4, Gtk.Label("Analisis web"))

		self.page5 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.page5.set_border_width(10)
		self.page5.add(Gtk.Label("Metasploit"))
		self.page5.add(Gtk.Entry())
		self.page5.add(Gtk.Button(label="Crear junk metasploit"))
		self.page5.add(Gtk.Button(label="Analizar junk metasploit"))
		self.page5.add(Gtk.Separator())
		self.page5.add(Gtk.Label("Terminal Metasploit"))
		self.page5.add(Gtk.Button(label="Activar DB Metasploit"))
		self.page5.add(Gtk.Button(label="Iniciar Metasploit"))
		notebook.append_page(self.page5, Gtk.Label("Metasploit"))

		main_menu_bar = Gtk.MenuBar()
		#drop
		file_menu = Gtk.Menu()
		file_drop = Gtk.MenuItem("Hash")

		#Subitems
		file_abrir = Gtk.MenuItem("Abrir")
		file_abrir.connect("activate", self.on_file_clicked)
		file_menu.append(Gtk.SeparatorMenuItem())
		file_cerrar = Gtk.MenuItem("Cerrar")

		file_drop.set_submenu(file_menu)
		file_menu.append(file_abrir)
		file_drop.set_submenu(file_menu)
		file_menu.append(file_cerrar)

		main_menu_bar.append(file_drop)

		layout.pack_start(main_menu_bar, True, True, 0)
		layout.pack_start(notebook, True, True, 0)

	def nmapbut(self, button):
		asyncio.run(run('nmap ' + enmapa.get_text() + ' ' + enmap.get_text()))

	def ex4but(self, button):
		asyncio.run(runex('enum4linux ' + enmap.get_text()))

	def dibut(self, button):
		asyncio.run(rundi('dirb ' + di1text.get_text() + ' ' + di2text.get_text() + ' ' + di3text.get_text()))

	def WPbut(self, button):
		asyncio.run(runwp('wpscan --update --url ' + di1text.get_text() + ' ' + WP2text.get_text() + ' ' + WP3text.get_text()))

	def Nkbut(self, button):
		asyncio.run(runnk('nikto -h ' + di1text.get_text()))

	def HCbut(self, button):
		asyncio.run(runhc('hashcat ' + HC1text.get_text()))

	def JNbut(self, button):
		asyncio.run(runjn('john ' + HC1text.get_text()))

	def HYbut(self, button):
		asyncio.run(runhy('hydra ' + HC1text.get_text() + ' ' + HY4text.get_text() + ' ' + HY3text.get_text() + ' ' + HY2text.get_text()))

	def on_file_clicked(self, widget):
		dialog = Gtk.FileChooserDialog(
			"Selecciona un archivo",
			self,
			Gtk.FileChooserAction.OPEN,
			(
				Gtk.STOCK_CANCEL,
				Gtk.ResponseType.CANCEL,
				Gtk.STOCK_OPEN,
				Gtk.ResponseType.OK,
				),
			)

		self.add_filters(dialog)

		resp = dialog.run()

		if resp == Gtk.ResponseType.OK:
			HC1text.set_text(dialog.get_filename())

		dialog.destroy()

	def add_filters(self, dialog):
		filter_text = Gtk.FileFilter()
		filter_text.set_name("hashfiles")
		filter_text.add_mime_type("text/plain")
		dialog.add_filter(filter_text)



win = winini()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
