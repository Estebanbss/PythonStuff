"""
This program converts a YouTube video to MP3.
To use it, you need to install the moviepy and pytube libraries.

"""

import os
from pytube import YouTube
from moviepy.editor import VideoFileClip

def convertir_a_mp3():
    # Solicitar la URL del video de YouTube
    url = input("Ingresa la URL del video de YouTube: ")

    # Descargar el video de YouTube
    youtube = YouTube(url)
    video = youtube.streams.first()
    video.download()

    # Extraer el audio y guardarlo como MP3
    video_filename = video.default_filename
    mp4_video = VideoFileClip(video_filename)
    mp3_audio = mp4_video.audio

    # Solicitar la ruta de destino para el archivo MP3
    ruta_destino = input("Ingresa la ruta de destino para el archivo MP3: ")
    mp3_filename = os.path.join(ruta_destino, video_filename.split('.')[0] + '.mp3')
    mp3_audio.write_audiofile(mp3_filename)

    # Eliminar el archivo de video descargado
    mp4_video.close()
    mp3_audio.close()
    mp4_video.reader.close()
    mp4_video.audio.reader.close_proc()
    os.remove(video_filename)

    print("El video se ha convertido a MP3 con éxito.")
    print(f"El archivo MP3 se ha guardado en: {os.path.abspath(mp3_filename)}")

# Llamar a la función de conversión
convertir_a_mp3()