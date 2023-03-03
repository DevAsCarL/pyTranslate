import tkinter as tk
from tkinter import filedialog, PhotoImage
from PIL import Image, ImageTk
import module.convert as convert
import module.transcript as transcript


convert = convert.MPEdit()
transcript = transcript.Transcript()

videoMP3 = 'generate/video.mp3'
file_path = ''
language_translate = 'es'


def open_file():
    global file_path, videoMP3
    file_path = filedialog.askopenfilename(filetypes=[['video','.mp4'],['audio','.mp3']])
    if file_path:
        label.configure(text=file_path)
        convert.convert_mp4_to_mp3(file_path, videoMP3)
        buttonTranscript.configure(state="normal")


def generate_transcript():
    global videoMP3, language_translate

    transcript.transcribe(videoMP3, language_translate)


width = 700
height = 500

root = tk.Tk()
root.title("Subir audio y transcribirlo")
root.geometry(f"{width}x{height}")
root.resizable(False, False)


img = Image.open('file.png')
img = img.resize((50, 25), Image.ANTIALIAS)  # Redimension (Alto, Ancho)
img = ImageTk.PhotoImage(img)


label = tk.Label(
    root, text="Seleccione un archivo de audio para transcribir:")
label.place(relx=0.6, rely=0.2, anchor="e")

button = tk.Button(root, image=img, command=open_file).place(
    relx=0.65, rely=0.2, anchor="w")

buttonTranscript = tk.Button(
    root, text="Generar Subtitulos", command=generate_transcript, state="disabled")
buttonTranscript.place(relx=0.5, anchor="center", rely=0.4)

root.mainloop()
