Proyecto demo1 — sitio "La Capa de Ozono"

Cómo ejecutar localmente

1) Crear un virtualenv y activar (Windows PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2) Exportar la API key de OpenWeather (opcional, `weather.py` tiene un fallback):

```powershell
$env:OPENWEATHER_API_KEY = "tu_api_key_aqui"
```

3) Ejecutar la app:

```powershell
python app.py
```

La app se sirve por defecto en http://0.0.0.0:8080

Deploy

- Para deploys simples en servicios como Heroku/GitHub Actions, asegúrate de setear `OPENWEATHER_API_KEY` como secret en la plataforma.
