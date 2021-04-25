#!/usr/bin/python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import threading
import os



ips = Gtk.Entry()
dirs = Gtk.Entry()
wd = Gtk.Entry()
wdck = Gtk.Entry()
comm = Gtk.Entry()
comm2 = Gtk.Entry()


class winini(Gtk.Window):
	def __init__(self):

		self.timer=None
		self.event=None



		Gtk.Window.__init__(self, title="Red de seguridad")
		self.set_default_size(400,0)

		layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(layout)

		notebook = Gtk.Notebook()
		self.add(notebook)

		grid = Gtk.Grid()
		self.add(grid)

		grid2 = Gtk.Grid()
		self.add(grid2)

		main_menu_bar = Gtk.MenuBar()
		file_menu = Gtk.Menu()
		file_drop = Gtk.MenuItem(label="Archivo")


		file_abrir = Gtk.MenuItem(label="Abrir")
		file_abrir.connect("activate", self.on_file_clicked)
		file_menu.append(Gtk.SeparatorMenuItem())
		file_cerrar = Gtk.MenuItem(label="Cerrar")

		file_drop.set_submenu(file_menu)
		file_menu.append(file_abrir)
		file_drop.set_submenu(file_menu)
		file_menu.append(file_cerrar)


		main_menu_bar.append(file_drop)

		self.page1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.page1.set_border_width(10)
		self.page1.add(Gtk.Label(label="Scan ip"))
		self.page1.add(ips)
		self.page1.add(Gtk.Label(label="Comandos"))
		self.page1.add(comm)
		self.page1.add(Gtk.Label(label="Wordlist Web"))
		self.page1.add(wd)
		wd.set_text("/usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt")
		

		self.page2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.page2.set_border_width(10)
		self.page2.add(dirs)
		self.page2.add(Gtk.Label(label="Ruta del archivo"))
		self.page2.add(comm2)
		self.page2.add(Gtk.Label(label="Comandos"))


		button_nmap = Gtk.Button(label="Nmap")
		button_nmap.connect("clicked",self.start_nmap)

		button_nmap_def = Gtk.Button(label="Nmap (Default)")
		button_nmap_def.connect("clicked", self._start_nmap_def)


		button_gobuster = Gtk.Button(label="Gobuster")
		button_gobuster.connect("clicked", self.gobus)

		button_gobuster_def = Gtk.Button(label="Gobuster (Default)")
		button_gobuster_def.connect("clicked", self._gobus_def)

		button_nikto = Gtk.Button(label="Nikto")
		button_nikto.connect("clicked", self.nkt)

		button_nikto_def = Gtk.Button(label="Nikto (Default)")
		button_nikto_def.connect("clicked", self._nikto_def)

		button_steghide_def = Gtk.Button(label="Steghide")
		button_steghide_def.connect("clicked", self._steg_def)

		grid.add(button_nmap)
		grid.attach_next_to(button_nmap_def, button_nmap, Gtk.PositionType.RIGHT, 1, 1)
		grid.attach_next_to(button_gobuster, button_nmap_def, Gtk.PositionType.RIGHT,1,1)
		grid.attach_next_to(button_gobuster_def, button_gobuster, Gtk.PositionType.RIGHT,1,1)
		grid.attach_next_to(button_nikto, button_gobuster_def, Gtk.PositionType.RIGHT,1,1)
		grid.attach_next_to(button_nikto_def, button_nikto, Gtk.PositionType.RIGHT,1,1)

		grid2.add(button_steghide_def)

		notebook.append_page(self.page1, Gtk.Label(label="Analisis Web"))
		notebook.append_page(self.page2, Gtk.Label(label="Esteganografía"))



		layout.pack_start(main_menu_bar, True, True, 0)
		layout.pack_start(notebook, True, True, 0)
		layout.pack_start(grid, True, True, 0)
		layout.pack_start(grid2, True, True, 0)


	def on_file_clicked(self, widget):
			dialog = Gtk.FileChooserDialog("Seleccionar un archivo", self, Gtk.FileChooserAction.OPEN,(
				Gtk.STOCK_CANCEL,
				Gtk.ResponseType.CANCEL,
				Gtk.STOCK_OPEN,
				Gtk.ResponseType.OK,
				),
			)

			self.add_filters(dialog)

			resp = dialog.run()

			

			dialog.destroy()


	def add_filters(self, dialog):
			filter_text = Gtk.FileFilter()
			filter_text.set_name("Resultado")
			filter_text.add_mime_type("text/plain")
			dialog.add_filter(filter_text)

	def start_nmap(self, button):

		
		self.timer = threading.Thread(target=self.runmp)
		self.event = threading.Event()
		self.timer.daemon=True
		self.timer.start()

	def runmp(self): 

		print("[+] Inicio Nmap")

		ip_get = ips.get_text()
		comd = comm.get_text()
		pid = os.system("nmap " + comd + " " + ip_get + " " + ">" + " " + "Nmap.log")

		if(pid == 0):
			print("Terminado Nmap")

	def _start_nmap_def(self, button):
		
		self.timer = threading.Thread(target=self.runmp_def)
		self.event = threading.Event()
		self.timer.daemon = True
		self.timer.start()

	def runmp_def(self):

		print("[+] Inicio Nmap-default")

		ip_get = ips.get_text()
		pid2 = os.system("nmap -sT -A -p- --script=vulners --script=smb-vuln* '--script=banner,(ftp* or ssl*) and not (brute or external or dos or broadcast or fuzzer)' " + ip_get + " " + ">" + " " + "Nmap-default.log")

		if(pid2 == 0):
			print("Terminado Nmap default")

	def gobus(self, button):

		self.timer = threading.Thread(target=self.gbst)
		self.event = threading.Event()
		self.timer.daemon = True
		self.timer.start()

	def gbst(self):

		print("[+] Inicio Gobuster")

		ip_get = ips.get_text()
		comd = comm.get_text()
		wl = wd.get_text()
		pid3 = os.system("gobuster dir -u " + ip_get + " " + comd + " -w" + " " + wl + " " + ">" + " " + "Gobuster.log" )

		if(pid3 == 0):
			print("Terminado Gobuster")

	def _gobus_def(self, button):

		self.timer = threading.Thread(target=self.gbst_def)
		self.event = threading.Event()
		self.timer.daemon = True
		self.timer.start()

	def gbst_def(self):

		print("[+] Inicio Gobuster-default")

		ip_get = ips.get_text()
		
		pid4 = os.system("gobuster dir -u " + ip_get + " --no-progress --no-error -t 4 -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt" + " " + ">" + " " + "Gobuster-default.log")

		if(pid4 == 0):
			print("Terminado Gobuster default")


	def nkt(self, button):

		self.timer = threading.Thread(target=self.nk)
		self.event = threading.Event()
		self.timer.daemon = True
		self.timer.start()


	def nk(self):

		print("[+] Inicio Nikto")

		ip_get = ips.get_text()
		comd = comm.get_text()

		pid5 = os.system("nikto" + " " + comd + " " + ip_get + " " + ">" + " " + "Nikto.log")

		if(pid5 == 0):
			print("Terminado Nikto")


	def _nikto_def(self, button):

		self.timer = threading.Thread(target=self.nk_def)
		self.event = threading.Event()
		self.timer.daemon = True
		self.timer.start()

	def nk_def(self):

		print("[+] Inicio Nikto-default")

		ip_get = ips.get_text()

		pid6 = os.system("nikto -h " + ip_get + " " + ">" + " " + "Nikto-default.log")

		if(pid6 == 0):
			print("Terminado Nikto default")


	def _steg_def(self,button):
		self.timer = threading.Thread(target=self._steg_d)
		self.event = threading.Event()
		self.timer.daemon = True
		self.timer.start()


	def _steg_d(self):

		print("[+] Inicio steghide")

		rutfil = dirs.get_text()

		pid7 = os.system("steghide extract -sf" + " " + rutfil)

		if(pid7 == 0):
			print("Terminado steghide")
		



win = winini()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

