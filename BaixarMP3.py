"""
pyinstaller --> Transformar um arquivo python em exe (Mesmo sem o Python)

Terminal    --> pyinstaller --onefile <file>
            --> pyinstaller --onefile --noconsoler <file>
"""

from PySimpleGUI import PySimpleGUI as sg
from pytube import YouTube
import moviepy.editor as mp
import re
import os

# Layout
sg.theme("Reddit")

layout = [
    [sg.Text("Link:   "), sg.Input(key="link", default_text="youtube.com")],
    [sg.Text("Caminho:"), sg.Input(key="caminho", default_text="Informar a pasta")],
    [sg.Checkbox("Salvar Caminho?", key="salvar")],
    [sg.Button("Baixar")],
]

# Window
janela = sg.Window("BaixarMP3 - Youtube", layout)

# Ler os Eventos
while True:
    eventos, valores = janela.read()
    link = str(valores["link"])
    path = str(valores["caminho"])

    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == "Baixar":
        yt = YouTube(link)

        # Efetuar Download
        print("Baixando...")
        yt = yt.streams.filter(only_audio=True).first().download(path)
        print("Download completo!")

        # Converte MP4 para MP3
        print("Convertendo arquivo...")
        for file in os.listdir(path):
            if re.search("mp4", file):
                mp4_path = os.path.join(path, file)
                mp3_path = os.path.join(path, os.path.splitext(file)[0] + ".mp3")
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)
        print("Sucesso!")
