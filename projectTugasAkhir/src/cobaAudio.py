from gtts import gTTS
import playsound
import os
import time  # <-- Tambah ini

def bicara(teks):
    tts = gTTS(teks, lang="id")
    tts.save("output.mp3")
    playsound.playsound("output.mp3")
    time.sleep(1)  # Tunggu 1 detik biar file ga kehapus terlalu cepat
    os.remove("output.mp3")

bicara("Hai, namaku Iyan")
bicara("Kalau nama kamu, siapa?")  # Sekarang aman!