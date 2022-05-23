import tkinter
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image


# Functia care importa imaginea
# Initial se declara o variabila globala `img`, dupa care se preia calea imaginii pentru care se doreste convertirea printr-un file dialog.
# Folosind calea luata in `import_path`, se deschide imaginea aflata la calea respectiva.
def import_JPG():
	global img
	import_path = filedialog.askopenfilename()
	img = Image.open(import_path)


# Functia care exporta imaginea in noul format
# Se foloseste, la fel ca in cazul `import_JPG`, o variabila globala.
# Se foloseste un file dialog pentru ca utilizatorul sa fie intrebat la ce cale va fi salvata imaginea convertita. Aceasta cale este memorata in `export_path`
# Se salveaza imaginea la calea specificata
def convert_file():
	global img
	export_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=(("Image Files(PNG Only)", "*.png"),("All Files", "*.*")))
	img.save(export_path)



# Se declara o 'cutie' folosind functia Tk din libraria tkinter.
box = tkinter.Tk()

# Se definesc parametrii pentru cutia care reprezinta fereastra.
# In cazul de fata avem o fereastra cu dimensiunea 300x480
canvas1 = tkinter.Canvas(box, bg="white", height=300, width=480)
canvas1.pack()

# Se definesc, pe rand, celalalte elemente grafice precum titlul si butoanele ce trebuie sa actioneze functiile definite anterior
label1 = tkinter.Label(box, text='Convert from JPG to PNG', bg = '#fca103')
label1.config(font=('Times New Roman', 20))
canvas1.create_window(250, 60, window=label1)

browseButton_JPG = tkinter.Button(text="1. Import JPG File", command=import_JPG, bg='green', fg='white', font=('Times New Roman', 12, 'bold'))
canvas1.create_window(250, 130, window=browseButton_JPG)

saveAsButton_PNG = tkinter.Button(text='2. Convert JPG to PNG', command=convert_file, bg='green', fg='white', font=('Times New Roman', 12, 'bold'))
canvas1.create_window(250, 180, window=saveAsButton_PNG)

exit_button = tkinter.Button(text='3. Exit', command=exit, bg='red',fg='white',font =('Times New Roman', 12, 'bold'))
canvas1.create_window(250,230, window=exit_button)

# Se apeleaza functia `mainloop` din libraria tkinter, prin intermediul careia este mentinuta rularea programului.
box.mainloop()