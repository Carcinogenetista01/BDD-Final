import streamlit as st
import os
import requests

# URL del archivo en Google Drive
url = "https://drive.google.com/uc?id=1o3GrCxuBIUmiOaKKrmQM7zja7LQpfS9z"
local_path = "archivo_grande.zip"

# Descarga el archivo si no existe localmente
if not os.path.exists(local_path):
    st.write("Descargando el archivo grande desde Google Drive, por favor espera...")
    with open(local_path, "wb") as f:
        response = requests.get(url, stream=True)
        total = int(response.headers.get("content-length", 0))
        with st.progress(0) as progress:
            for data in response.iter_content(chunk_size=1024):
                f.write(data)
                progress.progress(f.tell() / total)
    st.write("Descarga completada.")
else:
    st.write("El archivo ya está disponible localmente.")

# Aquí puedes añadir el resto de tu app, que use el archivo descargado
st.write("¡App funcionando!")
