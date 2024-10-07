from fastapi import FastAPI, Request
import yt_dlp
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.post("/descargar-audio")
async def descargar_audio(request: Request):
    # Recibe el JSON con la URL
    data = await request.json()
    url = data.get("url")

    # Configuración para descargar el mejor audio disponible en formato m4a si es posible
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestaudio/best',  # Descargar el mejor audio disponible en .m4a si es posible
        'outtmpl': '/tmp/%(title)s.%(ext)s',  # Guardar en /tmp (importante para Railway)
    }

    try:
        # Descargar el audio con yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            archivo = ydl.prepare_filename(info)

        # Verificar si el archivo existe
        if os.path.exists(archivo):
            return FileResponse(archivo, filename=os.path.basename(archivo))
        else:
            return {"error": "No se pudo encontrar el archivo descargado"}

    except Exception as e:
        return {"error": str(e)}
    