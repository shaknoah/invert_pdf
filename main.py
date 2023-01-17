import customtkinter as tk
# import pypdfium2 as pdfium

import sys
import os
import tempfile
from PIL import Image, ImageOps, ImageEnhance
from pdf2image import convert_from_path


import pypdfium2 as pdfium
# import fitz
# pdffile = "my_pdf_file.pdf"
# doc = fitz.open(pdffile)
# zoom = 4
# mat = fitz.Matrix(zoom, zoom)
# count = 0
# # Count variable is to get the number of pages in the pdf
# for p in doc:
#     count += 1
# for i in range(count):
#     val = f"image_{i+1}.png"
#     page = doc.load_page(i)
#     pix = page.get_pixmap(matrix=mat)
#     pix.save(val)


def invert(filepath):
    with tempfile.TemporaryDirectory() as path:
        pdf = pdfium.PdfDocument(filepath)
        n_pages = len(pdf)
        black_and_white_images = []

        for im in range(n_pages):
            pil_image = pdf.get_page(im).render_topil( scale=3,
            rotation=0,
        # crop=(0, 0, 0, 0),
        # colour=(255, 255, 255, 255),
        # annotations=True,
        greyscale=False,
        optimise_mode=pdfium.OptimiseMode.PRINTING,)
            baw = pil_image.convert('RGB').convert('L')
            im_invert = ImageOps.invert(baw)
            enhancer = ImageEnhance.Contrast(im_invert)
            final_image = enhancer.enhance(7.0)
            black_and_white_images.append(final_image)
            # page = pdf.get_page(page_number)
            # pil_image = page.render_topil(
            # scale=1,
            # rotation=0,
            # crop=(0, 0, 0, 0),
            # colour=(255, 255, 255, 255),
            # annotations=True,
            # greyscale=False,
            # optimise_mode=pdfium.OptimiseMode.NONE,
            

        # # filepath = "tests/resources/multipage.pdf"
        # pdf = pdfium.PdfDocument(filepath)
        # page = pdf.get_page(0)
        # pil_image = page.render_to(pdfium.BitmapConv.pil_image,)
        # images_from_path = convert_from_path(pdf_path ,output_folder=path)
        # black_and_white_images = []
        # for im in images_from_path:
        #     baw = im.convert('RGB').convert('L')
        #     im_invert = ImageOps.invert(baw)
        #     enhancer = ImageEnhance.Contrast(im_invert)
        #     final_image = enhancer.enhance(7.0)
        #     black_and_white_images.append(final_image)
    black_and_white_images[0].save("r55.pdf", save_all=True, append_images=black_and_white_images[1:])

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")
root = tk.CTk()
root.geometry("500x350")
root.title("PDF INVERTER")



from PIL import Image
from tkinter import filedialog
def upload():
    filepath = filedialog.askopenfilename()
    invert(filepath)   
    label.config(text=filepath)

def submit():
    print("lo")

frame = tk.CTkFrame (master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

my_image = tk.CTkImage(light_image=Image.open("pngwing.com (1).png"),dark_image=Image.open("pngwing.com (1).png"),size=(150, 200))
button = tk.CTkButton(master=frame,image=my_image, text="",fg_color="transparent", command=upload )
button.pack(pady=1, padx=1,fill="both",expand=True)

button1=tk.CTkButton(master=frame,text="Submit",command=submit)
button1.pack(pady=25,padx=40,expand=True)

# label = tk.CTkLabel(master=frame, text="inverter")
# label.pack(pady=12, padx=10)
# label.pack()

root.mainloop()
