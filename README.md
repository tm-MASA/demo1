# tm-MASA (GitHub Pages)

Este repositorio está configurado para GitHub Pages con una versión estática (`index.html`) que funciona sin servidor. Si quieres la app completa (con Flask), debes desplegarla en un servicio que ejecute Python (Render, Railway, etc.).

Cómo activar Pages para este repo:

1. Entra en https://github.com/tu-usuario/tu-repo (en este caso: https://github.com/tm-MASA/tm-MASA.github.io).
2. Ve a Settings → Pages.
3. En "Source" selecciona la rama `main` y la carpeta `/ (root)`, guarda.
4. Espera unos segundos/minutos y abre: https://tm-MASA.github.io

Si quieres que te guíe para desplegar la app Flask (backend) en Render o Railway, dime y lo hacemos paso a paso.

---

## Automatización: construir y publicar imagen Docker automáticamente

He añadido un workflow de GitHub Actions que construye y publica la imagen Docker a Docker Hub cuando hagas push a `main`. Para que funcione necesitas crear dos secrets en tu repo:

- `DOCKERHUB_USERNAME` — tu usuario de Docker Hub
- `DOCKERHUB_TOKEN` — un token de acceso (o tu password) de Docker Hub

Pasos rápidos para activar la automatización:

1. Ve a tu repo en GitHub → Settings → Secrets and variables → Actions → New repository secret
2. Crea `DOCKERHUB_USERNAME` y `DOCKERHUB_TOKEN` con los valores correspondientes.
3. Haz push a `main` y GitHub Actions construirá y empujará la imagen a `<usuario>/tm-masa:latest`.

También añadí dos scripts en `scripts/` para uso local:

- `build_and_run.ps1` — construye la imagen y la ejecuta localmente
- `push_to_dockerhub.ps1` — etiqueta y sube la imagen a Docker Hub (te pedirá usuario y credenciales)

Usa PowerShell para ejecutarlos:

```powershell
# Construir y ejecutar
.\scripts\build_and_run.ps1

# Subir a Docker Hub
.\scripts\push_to_dockerhub.ps1
```

