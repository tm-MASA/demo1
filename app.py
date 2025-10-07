from flask import Flask, request, redirect, url_for, render_template_string, render_template, flash
from weather import get_weather

app = Flask(__name__)
app.secret_key = "CLAVE_SECRETA_CAMBIAME"  # cambia esto en producción
ADMIN_PASSWORD = "admin"  # cambia la contraseña

# Contenido inicial
page_data = {
    "title": " ",
    "content": """ 
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>La Capa de Ozono: Monitoreo Global</title>
    
    <style>
        /* ==================================================== */
        /* ZONA DE EDICIÓN RÁPIDA DE ESTILOS CSS */
        /* ==================================================== */
        :root {
            /* Colores y Fuentes */
            --color-texto: #FFFFFF;       /* TEXTO: Blanco */
            --color-titulo: #D980F9;      /* TÍTULOS: Morado Claro (Lila) */
            --ancho-contenido: 900px;
            --fuente-principal: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

            /* ==================================================== */
            /* VARIABLES PARA CONTROLAR EL TAMAÑO DE LA IMAGEN */
            /* ==================================================== */
            --ancho-max-imagen: 500px; /* Ancho máximo que deseas para la imagen (o 100% si quieres que ocupe todo) */
            --alto-max-imagen: auto; /* Altura máxima (deja 'auto' para mantener proporciones) */
            /* ==================================================== */
        }

        body {
            font-family: var(--fuente-principal);
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: var(--color-texto);

            /* ESTILOS PARA LA IMAGEN DE FONDO */
            background-image: url('https://i.postimg.cc/vHkX3Pjv/Espacio-4k.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }
        
        /* Contenedor principal para centrar el contenido y darle un color de contraste suave */
        .contenedor {
            width: 90%;
            max-width: var(--ancho-contenido);
            margin: 40px auto;
            padding: 20px;
            background-color: rgba(0, 0, 0, 0.75); /* Fondo negro semitransparente */
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(224, 176, 255, 0.75);
        }

        /* Estilos de encabezado y logo */
        header {
            text-align: center;
            padding-bottom: 20px;
            border-bottom: 2px solid var(--color-titulo);
            margin-bottom: 30px;
        }

        #logo-placeholder img {
            max-width: 150px;
            height: auto;
            border-radius: 5px;
            margin-bottom: 10px;
        }

        /* Estilos de Títulos */
        h1 {
            color: var(--color-titulo);
            font-size: 2.5em;
            margin: 10px 0;
        }

        h2 {
            color: var(--color-titulo);
            margin-top: 35px;
            border-left: 5px solid var(--color-titulo);
            padding-left: 15px;
        }

        /* Estilos para el contenedor de elementos multimedia (mapa, video, imagen) */
        .media-container {
            margin: 40px 0;
            padding: 20px;
            background-color: rgba(44, 44, 44, 0.8);
            border-radius: 6px;
            text-align: center;
            overflow: hidden;
        }
        
        /* Estilos para los iframes (mapa y video) */
        .marco-media {
            width: 100%;
            height: 500px;
            border: 3px solid var(--color-titulo);
            border-radius: 6px;
            margin-bottom: 15px;
            display: flex;
            justify-content: center;
            align-items: center;
            color: grey;
            font-style: italic;
        }

        /* Estilos para la imagen individual (AJUSTADO) */
        .marco-imagen {
            /* Aquí puedes editar el padding si quieres más espacio alrededor de la imagen */
            padding: 10px; 
            
            /* Usamos 'auto' en height para que el contenedor se ajuste a la altura de la imagen */
            height: auto !important; 
        }

        /* Estilos para la etiqueta <img> dentro del contenedor (AJUSTADO) */
        .marco-imagen img {
            /* Usamos las variables definidas en :root para el control de tamaño */
            max-width: var(--ancho-max-imagen); 
            max-height: var(--alto-max-imagen);
            
            width: 100%; /* Asegura que la imagen sea responsiva dentro del marco-media */
            height: auto;
            
            display: block;
            margin: 0 auto;
            border: 3px solid var(--color-titulo);
            border-radius: 6px;
            
            /* Asegura que la imagen no exceda el ancho del contenedor padre (.media-container) */
            box-sizing: border-box; 
        }

        /* Estilos para las listas de puntos */
        ul {
            list-style: disc;
            margin-left: 25px;
            padding-left: 0;
        }
        ul li {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>

    <div class="contenedor">

        <header>
            
            <div id="logo-placeholder">
                <img src= "https://i.postimg.cc/x1G6Fjnz/mi-logo.png" alt="Logo de la Capa de Ozono">
                <p style="font-size: 0.9em; color: white;">"Cocinando el Código para las MASAS mas grandes".</p>
            </div>
            <h1>LA CAPA DE OZONO</h1>
            <p>Nuestro protector invisible contra la radiación UV.</p>
        </header>

        <section>
            <h2>1. El Escudo de la Tierra</h2>
            <p>La Capa de Ozono se encuentra en la *estratosfera*, esta capa absorbe casi el 100% de lo que son los rayos UV (radiación del sol que daña a diversas circunstancias en la vida del planeta) por lo que "La Capa de Ozono" es una pieza fundamental que ayuda a vivir la vida con menos límites de riesgos y no solo a nosotros los seres humanos, si no a todos aquellos seres que habitan la tierra.</p>
        </section>

        <section>
            <h2>2. Comienzo del Deterioro</h2>
            <p>A lo largo de la vida de los seres en este planeta, se ha presentado una gran cantidad de contaminacion ambiental gracias a que, en la prehistoria los humanos al ser nomadas dejaban una acumulación de desechos biodegradables (viviendas, herramientas de madera y piedra, etc.), que como tal no fueron tan impactantes en el medio ambiente como lo son los desechos actuales.</p>
            Con los avances del ser humano en consntante avance y la invensión de la pólvora se crearon las armas, y con esto las guerras empezaron a difundir temor por las calles de todo el mundo, y gracias a las guerras la producción de armas en masa fue inmensa, lo que ha logrado una gran cantidad de pérdidas y una gran contaminación dentro de poco tiempo, algunas guerras que sucedieron en un lapso corto de tiempo son:</p>
            <ul>
                <li>Primera y Segunda Guerra Mundial.</li>
                <li>Guerra Fría.</li>
                <li>Guerra de Corea.</li>
                <li>Guerra de Vietnam.</li>
            </ul>
            <p>Estas guerras fueron las que más impacto tuvieron en el medio ambiente, ya que se usaron armas nucleares y químicas, que liberaron una gran cantidad de gases tóxicos a la atmósfera.</p>
        </section>
        <section class="media-container">
            <h2>3. ¿Cómo lo hace? </h2>
            <p>Debido a que hubieron muchas guerras seguidas y gracias a eso desencadeno una gran perdida del gas ozono y otra gran abundancia de gases invernaderos, lo cual destruye la capa, pero ¿Por qué todavía no se destruye?, bueno pues es un proceso fácil:
              <li> La molecula de ozono (O3) absorbe la radiación ultravioleta (UV) del sol, lo que provoca una de sus moléculas de oxígeno se libere, convirtiéndose en oxígeno molecular (O2) y un átomo de oxígeno libre (O).</li>
              <li> El átomo de oxígeno libre (O) puede reaccionar con otra molécula de ozono (O3) para formar dos moléculas de oxígeno molecular (O2).</li>
              <li> Este ciclo de destrucción y formación de ozono es continuo y ayuda a mantener un equilibrio en la concentración de ozono en la estratosfera.</li>
            </p>
            
            <div class="marco-imagen">
                <img src="https://i.postimg.cc/HW2Gx7nc/OMG.png" alt="Descripción de la imagen de la capa de ozono">
            </div>
            <p style="color: grey; font-style: italic; margin-top: 10px;">En la imagen se puede dar a conocer la densidad de la capa de ozono en el Planeta.</p>
        </section>

        <section class="media-container">
            <h2>4. ¿Qué pasa con la capa de ozono?</h2>
            <p>A continuación, se muestra el estado actual mas reciente de la Capa de Ozono usando datos satelitales, pero hay algo en lo que nos gustaría centrarnos un poco mas.
              <ul>
                <li> ¿Por qué hay un agujero en la capa de ozono en la parte sur del planeta?</li>
            Esto se debe a que en la Antártida, durante el invierno, las temperaturas son extremadamente bajas, lo que favorece la formación de nubes estratosféricas polares. Estas nubes proporcionan una superficie para que los compuestos de cloro y bromo, liberados por los CFCs (Clorofluorocarbonos, gases sintéticos de cloro, flúor y carbono que se usaron como refrigerantes, aerosoles y espumas, pero que destruyen la capa de ozono) y halones, se conviertan en formas reactivas que destruyen el ozono cuando la luz solar regresa en la primavera antártica. Este proceso es menos pronunciado en el Ártico debido a las temperaturas relativamente más altas y la mayor variabilidad meteorológica.
              </ul>
            </p>
            
            <div class="marco-media">
                <iframe 
                    width="100%" 
                    height="100%" 
                    src="https://www.youtube.com/embed/Zlfr9xQf_o8?start=3" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen
                ></iframe>
            </div>
            <p style="font-size: 0.85em; color: #aaa;">El mapa o video muestra la concentración de ozono. Los colores azules/púrpuras indican menor densidad.-</p>
            
        </section>

                <section>
                    <h2>5. Prueba TU Mismo</h2>
                    <p>A continuación te presentamos una página creada por nosotros para saber el clima en tu región y un link directo a un modelo 3D en tiempo real de la Capa de Ozono.</p>

                    <div class="weather-form" style="margin-top:20px;">
                        <form action="/weather" method="post">
                            <label for="city">Ingresa el nombre de la ciudad:</label><br>
                            <input type="text" id="city" name="city" placeholder="Ej: Santiago" required style="width:60%;padding:8px;margin:8px 0;">
                            <button type="submit" style="padding:8px 16px;">Consultar Clima</button>
                        </form>
                    </div>

                    <div style="margin-top:18px;">
                        <label class="form-label mb-3">Capa de ozono:</label>
                        <a href="https://eyes.nasa.gov/apps/earth/#/vital-signs/ozone/omps-atmosphere-daily" class="btn btn-info">Ver datos de ozono en NASA Earth</a>
                    </div>

                </section>
        
        
        <section>
            <h2>6. ¿Y Qué nos Espera a Nosotros?</h2>
            <p>Si seguimos con el cuidado tan malo de la capa de ozono desencadenara muchos problemas que ya no podremos solucionar nosotros, simplemente tendremos que esperar a que un milagro pase, y en caso de que esto se salga de nuestras manos, se empezaran a demostrar estos casos con mas frecuencia:</p>
            <ul>
                <li>Aumento de enfermedades relacionadas con la piel, como el cáncer de piel y las cataratas asi como un envejencimiento prematuro, arrugas, manchas que ya no sera reversible.</li>
                <li>Sistema inmunológivo debilitado, que provocara mayor vulnerabiliad a enfermedades e infecciones.</li>
            </ul>
        </section>
        
        <section>
            <h2>7. ¿Y Los Animalitos?</h2>
            <p>Asi como a nosotros nos van a pasar cosas feas, lamentablemente ellos tampoco quedan exentados:</p>
            <ul>
                <li>Animales marinos: La radiación UV puede afectar el fitoplancton, que es la base de la cadena alimentaria marina, lo que puede tener efectos en cascada en los ecosistemas marinos.</li>
                <li>Animales terrestres: La radiación UV puede afectar a los animales terrestres, causando daños en la piel y los ojos, y afectando su comportamiento y reproducción.</li>
            </ul>
        </section>
        
        <section>
            <h2>8. ¿Ahora que comeré?</h2>
            <p>Pues si no quedaste contento con perder a los animalitos bellos, tambien muchos nutrientes de las frutas y verduras no podras consumirlo mas por las siguiente razones:</p>
            <ul>
                <li>Reducción de cultivos: La radiación UV puede afectar el crecimiento y la productividad de los cultivos, lo que puede llevar a una reducción en la disponibilidad de alimentos.</li>
                <li>Calidad nutricional: La radiación UV puede afectar la calidad nutricional de los alimentos, reduciendo su contenido de vitaminas y otros nutrientes esenciales.</li>
            </ul>
        </section>  
       
        <section>
            <h2>9.¿Recuerdas donde vivimos?</h2>
            <p>Ya para terminar con este tema, los efectos climáticos y ambientales gracias a no cuidar nuestro cielito lindo:</p>
            <ul>
                <li>Cambio climático: La destrucción de la capa de ozono puede contribuir al cambio climático, ya que algunos de los gases que destruyen el ozono también son gases de efecto invernadero.</li>
                <li>Alteración de ecosistemas: La radiación UV puede afectar a los ecosistemas terrestres y acuáticos, alterando las interacciones entre especies y afectando la biodiversidad.</li>
            </ul>
        
        <section>
            <h2>10.¡Se parte de nosotros!</h2>
            <p>Para difundir nuestro objetivo hacia las masas dimos a la tarea de hacer un cuestionario para que las personas nos demuestren su reacción hacia el problema presentado. Por ejemplo, "¿Usan Bloqueador?", "¿Qué tan frecuente lo usas?", ect.</p>
            <ul>
                <li>Acontinuacion las gráficas que demuestran nuestro formulario.</li>
            </ul>
            <div class="marco-imagen">
                <img src="https://i.postimg.cc/1R2Jkztc/image.png" alt="Descripción de la imagen de la capa de ozono">
            </div>
            <p style="color: grey; font-style: italic; margin-top: 10px;">Gráfica de "Género" : 94 Mujeres, 61 Hombres.</p>
            </ul>
                        <div class="marco-imagen">
                <img src="https://i.postimg.cc/V63nVdRh/image.png" alt="Descripción de la imagen de la capa de ozono">
            </div>
            <p style="color: grey; font-style: italic; margin-top: 10px;">Gráfica de "¿Utilizas Bloqueador?": 119 Si, 37 No.</p>       
            </ul>
                        <div class="marco-imagen">
                <img src="https://i.postimg.cc/zfvhDn2c/image.png" alt="Descripción de la imagen de la capa de ozono">
            </div>
            <p style="color: grey; font-style: italic; margin-top: 10px;">Gráfica de "¿Cuántas veces?" : No utilizo- 37 personas, 1- 10 personas, 2- 6 personas, 3- 6 personas, 4- 11 personas, 5- 25 personas, 6- 6 personas, 7- 55 personas.</p>       
            </ul>
                        <div class="marco-imagen">
                <img src="https://i.postimg.cc/9F1z4D7q/image.png" alt="Descripción de la imagen de la capa de ozono">
            </div>
            <p style="color: grey; font-style: italic; margin-top: 10px;">Gráfica de "Frecuencia de Reaplicacion": Cada 1-2 hrs- 4 personas, Cada 3-4 hrs- 26 personas, Una vez al día- 97 personas, No utilizo- 29 personas.</p>
                        <div class="marco-imagen">
                <img src="https://i.postimg.cc/Qdz0gx7V/image.png" alt="Descripción de la imagen de la capa de ozono">
            </div>
            <p style="color: grey; font-style: italic; margin-top: 10px;">Gráfica de "Factor de Protección Solar": No Utilizo- 37 personas, FPS 15-29- 10 personas, FPS 30-50- 45 personas, FPS 50+ - 63 personas.</p>
            </ul>
            <div class="marco-imagen">
                <img src="https://i.postimg.cc/GtLdrjz5/image.png" alt="Descripción de la imagen de la capa de ozono">
            </div>
            <p style="color: grey; font-style: italic; margin-top: 10px;">Gráfica de "Crees que se necesita protección UV en días nublados": "Si Siempre"- 113 personas, "No, solo días nublados"- 22 personas, "Depnde de la época del año"- 21 personas.</p>      
            </ul>
            <p> Esperamos que con estas gráficas se den cuenta de la importancia de usar bloqueador y cuidar nuestra piel, ya que es el órgano más grande que tenemos y debemos cuidarlo.</p>
            </ul>
            
        </section>
                    
        </section>        
        
        <section>
            <h2>11.¿Quien se cuida MAS?</h2>
            <p>Siguiendo las estadísticas obetenidas respecto la encuesta, concluimos que entre las mujeres y los hombres, las mujeres se cuidan más, en estos resultados fueron muy parejos, aunque los hombres hayan sido menos personas que hayan contestado la encuesta no pudieron batir a las mujeres y las siguientes gráficas lo representan.</p>
            <div class="marco-imagen">
                <img src="https://i.postimg.cc/jSdqD1Dt/image.png" alt="Descripción de la imagen de la capa de ozono">
            </div>      
            </ul>
            <div class="marco-imagen">
                <img src="https://i.postimg.cc/hvyyph1Y/image.png" alt="Descripción de la imagen de la capa de ozono">
            </div>     
            </ul>
        </section>

        <section class="media-container">
            <h2>12. Saber mas...</h2>
            <p>Para entender un poco mas sobre este tema, te dejamos un video explicativo que habla un poco mas a detalle sobre la capa de ozono y su importancia.</p>
            <div class="marco-media">
                <iframe 
                    width="100%" 
                    height="100%" 
                    src="https://www.youtube.com/embed/aU6pxSNDPhs"
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen
                ></iframe>
            </div>
        </section>
        
         <section>
            <h2>13. Soluciones y Medidas de Prevención</h2>
            <p>La capa de ozono es como el protector solar natural del planeta. Cuando se debilita, deja pasar más radiación ultravioleta (UV) del Sol, y eso nos afecta directamente, sobre todo a la piel. Por eso, las medidas para ayudarla y para protegernos van de la mano. Cómo Ayudar a la Capa de OzonoLa clave está en evitar ciertos químicos que la dañan, especialmente los gases que se encuentran en equipos viejos. Asegúrate de que tu aire acondicionado, refrigerador o congelador, si son antiguos, no tengan fugas de gas. Si notas algo raro, llama a un técnico que sepa manipular esos gases de forma segura, sin liberarlos al aire. Evita también comprar desodorantes o insecticidas en spray que no indiquen claramente que son "libres de CFC" (clorofluorocarbonos), que son gases muy dañinos; lo mejor es usar productos en barra, crema o con bomba manual. Además, usa la bicicleta, camina o toma el transporte público. Menos coches en la calle significan menos gases contaminantes que terminan afectando la atmósfera. Si puedes, compra productos que se hicieron cerca de ti, ya que esto reduce el transporte y, por lo tanto, la emisión de gases contaminantes.</p>
            <ul>
            <p> ¿Cómo Proteger tu Piel del Sol? Dado que la radiación UV es más fuerte hoy, es fundamental que te protejas todos los días. Evita el sol cuando está más fuerte, que generalmente es entre las 11 de la mañana y las 3 o 4 de la tarde. Si tienes que estar fuera, ¡quédate bajo la sombra! Es crucial que te apliques una crema con Factor de Protección Solar (FPS) de 30 o más que te proteja contra los rayos UVA y UVB. Ponte una buena cantidad en toda la piel expuesta y vuelve a aplicarlo cada dos horas, o si nadas o sudas mucho. Además, usa un sombrero de ala ancha para cubrir bien tu cara y cuello, y ponte gafas de sol que bloqueen la mayoría de los rayos UV. También puedes usar ropa de manga larga y colores oscuros o de tejido tupido para una protección extra. Al tomar estas sencillas decisiones en casa y en la calle, estás ayudando a que la capa de ozono se recupere lentamente y, al mismo tiempo, ¡estás cuidando tu salud!
            <ul>
        </section> 
        
        <section>
            <h2>14. REFERENCIAS</h2>
            <p>citas bibliograficas. (s. f.). Google Docs. https://docs.google.com/document/d/1whPbbnyqfXV6yuvoc-yXasV-Oj3HfJIdJW8Zlf-_jxg/edit?usp=sharing</p>
        </section> 
        
    </div>

    <footer>
        <p style="text-align: center; color: #555; font-size: 0.8em; padding: 15px 0;">
            &copy; 2025. Información y datos sobre la protección ambiental.
        </p>
    </footer>

</body>
</html>
  """
}

# --- Plantillas incrustadas ---
index_tpl = """
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ title }}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        :root { --brand: #d980f9; }
        .modal-header, .btn-primary { background: var(--brand); border-color: var(--brand); }
        .modal-title { color: #fff; }
        .btn-primary { color: #fff; }
        .flash-message { color: #fff; background: rgba(217,128,249,0.9); padding: 10px; border-radius: 6px; }
    </style>
</head>
<body>
    <div class="container py-4">
        <div class="d-flex justify-content-between align-items-center mb-3">
            <h1>{{ title }}</h1>
            <a class="btn btn-sm btn-outline-light" href="{{ url_for('edit') }}">Editar</a>
        </div>

        {% with messages = get_flashed_messages() %}
            {% if messages %}
                {% for msg in messages %}
                    <div class="flash-message mb-3">{{ msg }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        <div id="content-area">
            {{ content|safe }}
        </div>

        <!-- Auto-refresh controls -->
        <div class="d-flex align-items-center mb-3 mt-3">
            <div class="form-check form-switch me-3">
                <input class="form-check-input" type="checkbox" id="autoRefreshToggle">
                <label class="form-check-label" for="autoRefreshToggle">Auto-actualizar</label>
            </div>
            <label style="margin-right:8px;">Intervalo (s):</label>
            <input type="number" id="autoRefreshInterval" value="60" min="5" style="width:100px" class="form-control form-control-sm me-2">
            <button id="refreshNow" class="btn btn-sm btn-outline-light">Actualizar ahora</button>
        </div>

        <div id="liveWeather" class="mt-3"></div>

        <!-- Result Modal -->
        <div class="modal fade" id="resultModal" tabindex="-1" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Resultado - <span id="modalCity"></span></h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <ul class="list-group mb-2" id="modalBodyList"></ul>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
                    </div>
                </div>
            </div>
        </div>

    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        // Helper: fetch weather via AJAX with cache-busting
        let pollTimer = null;

        function fetchWeatherForCity(city) {
            const url = '/weather' + (location.search.includes('t=') ? '&' : '?') + 't=' + Date.now();
            const fd = new FormData();
            fd.append('city', city);
            return fetch(url, { method: 'POST', body: fd, headers: { 'X-Requested-With': 'XMLHttpRequest', 'Cache-Control': 'no-cache', 'Pragma': 'no-cache' }, cache: 'no-store' })
                .then(r => r.json());
        }

        function updateLiveWeather(json) {
            const container = document.getElementById('liveWeather');
            if (!json || json.error) {
                container.innerHTML = '<div class="alert alert-warning text-dark">No hay datos disponibles.</div>';
                return;
            }
            const w = json.weather || {};
            container.innerHTML = `
                <div class="card bg-light text-dark">
                    <div class="card-body">
                        <h5 class="card-title">${json.city || ''}</h5>
                        <p class="card-text">${w.description || ''} — ${w.temperature != null ? w.temperature + ' °C' : ''}</p>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item">Humedad: ${w.humidity != null ? w.humidity + ' %' : 'No disponible'}</li>
                            <li class="list-group-item">Presión: ${w.pressure != null ? w.pressure + ' hPa' : 'No disponible'}</li>
                            <li class="list-group-item">Viento: ${w.wind_speed != null ? w.wind_speed + ' m/s' : 'No disponible'}</li>
                            <li class="list-group-item">Índice UV: ${w.uv_index != null ? w.uv_index : 'No disponible'}</li>
                        </ul>
                    </div>
                </div>`;
        }

        function startPolling(intervalSeconds) {
            stopPolling();
            const cityInput = document.querySelector('form[action="/weather"] input[name="city"]');
            if (!cityInput || !cityInput.value.trim()) {
                alert('Ingresa una ciudad para iniciar auto-actualización');
                document.getElementById('autoRefreshToggle').checked = false;
                return;
            }
            // immediate update
            fetchWeatherForCity(cityInput.value.trim()).then(json => updateLiveWeather(json)).catch(err => console.error(err));
            pollTimer = setInterval(() => {
                const cityNow = cityInput.value.trim();
                if (cityNow) fetchWeatherForCity(cityNow).then(json => updateLiveWeather(json)).catch(err => console.error(err));
            }, intervalSeconds * 1000);
        }

        function stopPolling() {
            if (pollTimer) { clearInterval(pollTimer); pollTimer = null; }
        }

        document.addEventListener('DOMContentLoaded', () => {
            const toggle = document.getElementById('autoRefreshToggle');
            const intervalInput = document.getElementById('autoRefreshInterval');
            const refreshNowBtn = document.getElementById('refreshNow');

            if (toggle) toggle.addEventListener('change', (e) => {
                const enabled = e.target.checked;
                const interval = parseInt(intervalInput.value) || 60;
                if (enabled) startPolling(interval); else stopPolling();
            });

            if (refreshNowBtn) refreshNowBtn.addEventListener('click', () => {
                const cityInput = document.querySelector('form[action="/weather"] input[name="city"]');
                const city = cityInput ? cityInput.value.trim() : '';
                if (!city) { alert('Ingresa una ciudad para actualizar'); return; }
                fetchWeatherForCity(city).then(json => updateLiveWeather(json)).catch(err => console.error(err));
            });
        });

        // Existing submit handler (keeps modal behavior)
        document.addEventListener('submit', function(e){
            const form = e.target;
            if (form && form.matches && form.matches('form[action="/weather"]')) {
                e.preventDefault();
                const data = new FormData(form);
                const submitBtn = form.querySelector('button[type="submit"]');
                const originalBtnHTML = submitBtn ? submitBtn.innerHTML : null;
                if (submitBtn) {
                    submitBtn.disabled = true;
                    submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm text-white" role="status" aria-hidden="true"></span> Cargando...';
                }
                // cache-busting: evitar caches intermedios
                const url = form.action + (form.action.includes('?') ? '&' : '?') + 't=' + Date.now();
                // mostrar modal con spinner mientras carga
                const list = document.getElementById('modalBodyList');
                list.innerHTML = '<li class="list-group-item text-center"><div class="spinner-border text-secondary" role="status"><span class="visually-hidden">Cargando...</span></div></li>';
                document.getElementById('modalCity').textContent = 'Cargando...';
                var modal = new bootstrap.Modal(document.getElementById('resultModal'));
                modal.show();
                fetch(url, { method: 'POST', body: data, headers: { 'X-Requested-With': 'XMLHttpRequest', 'Cache-Control': 'no-cache', 'Pragma': 'no-cache' }, cache: 'no-store' })
                    .then(r => r.json())
                    .then(json => {
                        if (json.error) {
                            // show flash-like message and close modal
                            alert(json.error);
                            modal.hide();
                            return;
                        }
                        const city = json.city || '';
                        list.innerHTML = '';
                        const items = [
                            ['Temperatura', json.weather.temperature + ' °C'],
                            ['Humedad', json.weather.humidity + ' %'],
                            ['Presión', json.weather.pressure + ' hPa'],
                            ['Viento', json.weather.wind_speed + ' m/s'],
                            ['Descripción', json.weather.description || 'No disponible'],
                            ['Índice UV', (json.weather.uv_index || 'No disponible')]
                        ];
                        items.forEach(([k,v]) => {
                            const li = document.createElement('li');
                            li.className = 'list-group-item';
                            li.textContent = k + ': ' + v;
                            list.appendChild(li);
                        });
                        document.getElementById('modalCity').textContent = city;
                    }).catch(err => { alert('Error al obtener datos'); console.error(err); modal.hide(); })
                    .finally(() => {
                        if (submitBtn) {
                            submitBtn.disabled = false;
                            submitBtn.innerHTML = originalBtnHTML;
                        }
                    });
            }
        });
    </script>
</body>
</html>
"""

edit_tpl = """
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Editar página</title>
</head>
<body>
  <h1>Editor</h1>
  {% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
      {% for category, msg in messages %}
        <p style="color:red">{{ msg }}</p>
      {% endfor %}
    {% endif %}
  {% endwith %}

  <form method="post">
    <label>Título:</label><br>
    <input type="text" name="title" value="{{ title }}" required><br><br>

    <label>Contenido (HTML):</label><br>
    <textarea name="content" rows="10" cols="50">{{ content }}</textarea><br><br>

    <label>Contraseña:</label><br>
    <input type="password" name="password" required><br><br>

    <button type="submit">Guardar</button>
  </form>

  <p><a href="{{ url_for('index') }}">Volver</a></p>
</body>
</html>
"""

# --- Rutas ---
@app.route("/")
def index():
    return render_template_string(index_tpl, title=page_data["title"], content=page_data["content"])

@app.route("/edit", methods=["GET", "POST"])
def edit():
    global page_data
    if request.method == "POST":
        if request.form.get("password") != ADMIN_PASSWORD:
            flash("Contraseña incorrecta")
            return redirect(url_for("edit"))

        page_data["title"] = request.form.get("title", page_data["title"])
        page_data["content"] = request.form.get("content", page_data["content"])
        flash("Página actualizada con éxito")
        return redirect(url_for("index"))

    return render_template_string(edit_tpl, title=page_data["title"], content=page_data["content"])


@app.route('/weather', methods=['POST'])
def masa_weather():
    city = request.form.get('city')
    if not city:
        return redirect(url_for('index'))
    weather_data = get_weather(city)
    # Si la petición es AJAX (fetch), devolver JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.is_json:
        if not weather_data:
            from flask import make_response, jsonify
            resp = make_response(jsonify({ 'error': f"No se encontraron datos para la ciudad '{city}'." }), 200)
            resp.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
            return resp
        from flask import make_response, jsonify
        resp = make_response(jsonify({ 'city': city, 'weather': weather_data }), 200)
        resp.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        return resp

    # petición normal: render HTML
    if not weather_data:
        flash(f"No se encontraron datos para la ciudad '{city}'. Por favor verifica el nombre e intenta de nuevo.")
        return redirect(url_for('index'))
    return render_template('weather.html', weather=weather_data, city=city)





if __name__ == "__main__":
    app.run(debug=True, port=8080)
