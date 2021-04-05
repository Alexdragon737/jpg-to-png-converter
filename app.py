import tkinter
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image



def import_JPG():
	global img
	import_path = filedialog.askopenfilename()
	img = Image.open(import_path)



def convert_file():
	global img
	export_path = filedialog.asksaveasfilename(extensions='.png')
	img.save(export_path)




box = tkinter.Tk()


canvas1 = tkinter.Canvas(box, bg="blue", height=300, width=300)
canvas1.pack()
label1 = tkinter.Label(box, text='JPG to PNG Converter', bg = 'hotpink')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

browseButton_JPG = tkinter.Button(text="      Import JPG File     ", command=import_JPG, bg='red', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_JPG)

saveAsButton_PNG = tkinter.Button(text='Convert JPG to PNG', command=convert_file, bg='red', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_PNG)




box.mainloop()