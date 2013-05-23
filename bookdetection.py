from Tkinter import *
from tkFileDialog import askopenfilename
from pytesser import *
from squares import *
from filters_methods import *
import Image, ImageTk, webbrowser

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title('Book detection')
        self.root.resizable(width=False, height=False)

        self.labeltext = StringVar()
        self.labeltext.set('No hay imagen seleccionada')
        self.label = Label(self.root, textvariable=self.labeltext).grid(row=0, column=1, columnspan=3)
        self.label = Label(self.root, text='Vista previa:').grid(row=1, column=0)

        self.button_search = Button(text='Seleccionar Archivo', width=15, command=self.select_file).grid(row=0, column=0)
        self.button_detect = Button(text='Abrir', width=12, command=self.openit).grid(row=1, column=1)
        self.button_detect = Button(text='Detectar', width=12, command=self.action).grid(row=1, column=2)
        self.button_exit = Button(text='Salir', width=12, command=self.root.destroy).grid(row=1, column=3)

    def select_file(self):
        self.filename = askopenfilename(filetypes=[('allfiles', '*'), ('images', '*.jpg')])
        self.labeltext.set(self.filename)

    def openit(self):
        image = Image.open(self.filename)
        image = image.resize((140, 140), Image.ANTIALIAS)
        self.imagetk = ImageTk.PhotoImage(image)
        self.labelimage = Label(self.root, image=self.imagetk).grid(row=2, column=0)

    def action(self):
        squares = search(self.filename)
        booksdetected = self.cut(self.filename, squares)

        image = Image.open('preview.png')
        image = image.resize((140, 140), Image.ANTIALIAS)
        self.imagetk = ImageTk.PhotoImage(image)
        self.labelimage = Label(self.root, image=self.imagetk).grid(row=2, column=0)

        r = 2
        c = 0
        self.bookimagetk = [1, 2, 3, 4]
        self.bookimage = [1, 2, 3, 4]
        for num in booksdetected:
            bookfile = 'frontbook-%d.png' % num
            image = Image.open(bookfile)
            image = image.resize((140, 140), Image.ANTIALIAS)
            self.bookimagetk[c] = ImageTk.PhotoImage(image)
            self.bookimage[c] = Label(self.root, image=self.bookimagetk[c]).grid(row=r, column=1, columnspan=2)

            imagefortext = Image.open(bookfile)
            imagefortext = grayscale(imagefortext)
            imagefortext = binarization(imagefortext, 40)
            imagefortext.save('frontbook-%d.png' % num)
            text = image_file_to_string(bookfile)
            text = text[:36]

            self.linkimage = Label(text=text, foreground='#00f')
            self.linkimage.bind('<1>', lambda event, text=text: self.click_link(event, text))
            self.linkimage.grid(row=r, column=3)
            r += 1
            c += 1

    def click_link(self, event, text):
        google_link = 'http://www.google.es/search?btnG=Buscar+libros&tbm=bks&tbo=1&hl=es&oq=ma&q=' + text
        webbrowser.open(google_link)

    def cut(self, image, squares):
        image = Image.open(image)
        width, height = image.size

        frontcount = 0
        space = 60
        lastsizes = []
        repeated = []
        for square in squares:
            p1 = square[0]
            p2 = square[1]
            p3 = square[2]
            p4 = square[3]

            pixels = image.load()
            an = (p3[0]-p1[0])
            al = (p3[1]-p1[1])

            for size in lastsizes:
                w, h = size
                if an > w-space and an < w+space and al > h-space and al < h+space:
                    if frontcount in repeated:
                        pass
                    else:
                        repeated.append(frontcount)
                    
            if an > (width*0.1) and al > (height*0.1) and an < (width*0.9) and al < (height*0.9):
                lastsizes.append((an, al))
                newimage = Image.new('RGB', (an, al), (255, 255, 255))
                pix = newimage.load()
                x = 0
                y = 0
                for i in range(p1[0], p3[0]):
                    for j in range(p1[1], p3[1]):
                        pix[x, y] = pixels[i, j]
                        y += 1
                    x += 1
                    y = 0
                imagename = 'frontbook-%d.png' % frontcount
                frontcount += 1
                newimage.save(imagename)

        booksdetected = []
        for element in range(frontcount-1):
            if element not in repeated:
                booksdetected.append(element)
        return booksdetected

def main():
    root = Tk()
    app = Interface(root)
    root.mainloop()

if __name__ == '__main__':
    main()

