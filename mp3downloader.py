import sys
import subprocess

def descargar_audio(url):
    try:
        comando = [
            'yt-dlp',
            '-x', '--audio-format', 'mp3',
            '-o', '%(title)s.%(ext)s',
            url
        ]
        subprocess.run(comando, check=True)
        print("✅ Audio descargado correctamente.")
    except subprocess.CalledProcessError as e:
        print("❌ Error al ejecutar yt-dlp:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python descargar_audio.py <URL_YOUTUBE>")
    else:
        descargar_audio(sys.argv[1])
