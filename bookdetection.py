from Tkinter import *
from tkFileDialog import askopenfilename
from pytesser import *
import Image, ImageTk, webbrowser

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title('Book detection')
        self.root.resizable(width=False, height=False)

        self.labeltext = StringVar()
        self.labeltext.set('Selecciona una imagen')
        self.label = Label(self.root, textvariable=self.labeltext)
        self.label.pack(side=TOP)

        self.button_search = Button(text='Buscar Archivo', width=10, command=self.select_file).pack(side=TOP)
        self.button_detect = Button(text='Abrir', width=10, command=self.openit).pack(side=TOP)
        self.button_detect = Button(text='Detectar', width=10, command=self.action).pack(side=TOP)
        self.button_exit = Button(text='Salir', width=10, command=self.root.destroy).pack(side=TOP)

    def select_file(self):
        self.filename = askopenfilename(filetypes=[('allfiles', '*'), ('images', '*.jpg')])
        self.labeltext.set(self.filename)

    def openit(self):
        image = Image.open(self.filename)
        image = image.resize((400, 400), Image.ANTIALIAS)
        self.imagetk = ImageTk.PhotoImage(image)
        self.labelimage = Label(self.root, image=self.imagetk)
        self.labelimage.pack(side=LEFT)

    def action(self):
        text = image_file_to_string(self.filename)
        text = text[:24]
        self.labelimage = Label(text=text, foreground='#00f')
        self.labelimage.bind('<1>', lambda event, text=text: self.click_link(event, text))
        self.labelimage.pack()

    def click_link(self, event, text):
        google_link = 'http://www.google.es/search?btnG=Buscar+libros&tbm=bks&tbo=1&hl=es&oq=ma&q=' + text
        webbrowser.open(google_link)

def main():
    root = Tk()
    app = Interface(root)
    root.mainloop()

if __name__ == '__main__':
    main()

