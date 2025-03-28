import re

def convert_image_paths(html_content):
    # Регулярное выражение для поиска тегов img
    pattern = r'<img\s+src="images/([^"]+)"\s+alt="([^"]+)">'
    
    # Функция замены для каждого совпадения
    def replace_match(match):
        image_path = match.group(1)  # путь к изображению
        alt_text = match.group(2)    # текст alt
        new_path = f'<img src="{{% static \'images/{image_path}\' %}}" alt="{alt_text}">'
        return new_path
    
    # Выполняем замену для всех совпадений
    modified_html = re.sub(pattern, replace_match, html_content)
    return modified_html

# Пример использования
if __name__ == "__main__":
    # Тестовый HTML
    test_html = '''
{% load static %}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Alquiler de autocaravanas y campers de lujo en Marbella. Explore España con comodidad en nuestros vehículos con suspensión neumática. Alquiler directo, sin comisiones.">
    <meta name="keywords" content="alquiler autocaravana marbella, camper españa, autocaravana de lujo, suspensión neumática, alquiler caravana, viaje españa, camping marbella">
    <meta name="author" content="MarbellaCamper">
    <meta name="robots" content="index, follow">
    <link rel="icon" href="{% static 'marbell/images/logo/IMG_8475.png' %}" type="image/png">
    <title>MarbellaCamper</title>
    <link rel="canonical" href="https://marbellacamper.es">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'marbell/css/style.css' %}">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@8/swiper-bundle.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="https://mhkit.rometheme.pro/vantura/wp-content/plugins/elementskit-lite/modules/elementskit-icon-pack/assets/css/ekiticons.css">
    <link rel="stylesheet" href="https://mhkit.rometheme.pro/vantura/wp-content/plugins/elementor/assets/css/widget-icon-box.min.css">
    <script src="https://cdn.jsdelivr.net/npm/swiper@8/swiper-bundle.min.js" defer></script>
    <script src="{% static 'marbell/js/main.js' %}" defer></script>
    <style>
        @media (max-width: 768px) {
            .video-wrapper iframe {
                height: 280px;
                justify-content: center;
                border-radius: 5%;
            }
            
            /* Улучшенные стили для мобильного навбара */
            body .navbar .container .navbar-wrapper .navbar-menu.active {
                display: block !important;
            }
            
            body .navbar .container .navbar-wrapper .navbar-menu {
                display: none !important;
                position: fixed !important;
                top: 0 !important;
                left: 0 !important;
                width: 100% !important;
                height: 100vh !important;
                background: white !important;
                padding: 100px 0 20px !important;
                z-index: 1000 !important;
                overflow-y: auto !important;
            }
            
            body .navbar .container .navbar-wrapper .navbar-menu.active {
                display: block !important;
            }
            
            body .navbar .container .navbar-wrapper .navbar-menu .navbar-nav {
                display: flex !important;
                flex-direction: column !important;
                align-items: center !important;
                justify-content: center !important;
                width: 100% !important;
                padding: 0 !important;
                margin: 0 auto !important;
                text-align: center !important;
            }
            
            body .navbar .container .navbar-wrapper .navbar-menu .navbar-nav li {
                width: 100% !important;
                text-align: center !important;
                border-bottom: 1px solid #eaeaea !important;
                padding: 0 !important;
                margin: 0 !important;
            }
            
            body .navbar .container .navbar-wrapper .navbar-menu .navbar-nav li:last-child {
                border-bottom: none !important;
            }
            
            body .navbar .container .navbar-wrapper .navbar-menu .navbar-nav li .nav-link {
                display: block !important;
                text-align: center !important;
                padding: 15px 0 !important;
                font-size: 18px !important;
                width: 100% !important;
                color: #333 !important;
                margin: 0 auto !important;
            }
        }
        
        /* Убираем hover-эффект у кнопки в блоке с пневмоподвеской */
        .suspension-header .header-actions .btn-primary.lang-en:hover {
            background-color: #FFB800 !important;
            transform: none !important;
            box-shadow: none !important;
            opacity: 1 !important;
            cursor: default !important;
        }
         
    </style>
    <style>
        /* Полное удаление hover-эффектов для кнопок в блоке с пневмоподвеской */
        section#suspension .suspension-header .header-actions .btn-primary:hover,
        section#suspension .suspension-header .header-actions .btn-primary:active,
        section#suspension .suspension-header .header-actions .btn-primary:focus,
        .air-suspension .btn-primary:hover,
        .air-suspension .btn-primary:active,
        .air-suspension .btn-primary:focus {
            background-color: #FFB800 !important;
            color: #fff !important;
            transform: none !important;
            box-shadow: none !important;
            opacity: 1 !important;
            transition: none !important;
        }

        section#suspension .suspension-header .header-actions .btn-outline:hover,
        section#suspension .suspension-header .header-actions .btn-outline:active,
        section#suspension .suspension-header .header-actions .btn-outline:focus,
        .air-suspension .btn-outline:hover,
        .air-suspension .btn-outline:active,
        .air-suspension .btn-outline:focus {
            background: transparent !important;
            color: #333 !important;
            transform: none !important;
            box-shadow: none !important;
            border-color: #333 !important;
            transition: none !important;
        }
        
@media (max-width: 768px) {
    .features-side {
        margin-top: -120px;
        padding-right: 1rem;
        padding-left: 1rem;
    }
}
    </style>
    <style>
        .spec-item {
            background: #f8f9fa;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 15px;
        }
        @media (max-width: 768px) {
            .spec-label, .spec-value {
                display: block;
                text-align: center;
            }
            .spec-label {
                color: #666;
                margin-bottom: 8px;
                font-size: 14px;
            }
            .spec-value {
                color: #444;
                font-size: 14px;
                padding: 0 15px;
            }
            .spec-item {
                padding: 20px 15px;
            }
        }
    </style>
</head>
<body>
    <!-- Navbar -->
    <nav class="navbar">
        <div class="container">
            <div class="navbar-wrapper">
                <a class="navbar-brand">
                    <img src="../images/logo/IMG_8475.png" alt="MarbellaCamper" class="navbar-logo">
                </a>
                <div class="navbar-menu">
                    <ul class="navbar-nav">
                        <li><a href="#motorhomes" class="nav-link">Autocaravanas</a></li>
                        <li><a href="#about" class="nav-link">Sobre Nosotros</a></li>
                        <li><a href="#advantages" class="nav-link">Ventajas</a></li>
                        <li><a href="#reviews" class="nav-link">Opiniones</a></li>
                        <li><a href="#suspension" class="nav-link">Suspensión Neumática</a></li>
                        <li><a href="#contact" class="nav-link">Contacto</a></li>
                        <li><a href="#location" class="nav-link">Ubicación</a></li>
                        <li><a href="{% url 'main_page' %}" class="nav-link language-switch">English</a></li>
                    </ul>
                </div>
                <button class="navbar-toggle" aria-label="Alternar navegación">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <header class="hero">
        <div class="hero-background">
            <img src="../images/pictures/23F3D002-03E2-4570-BCCF-1375D8E4E83D.jpeg" class="hero-bg-image">
            <div class="overlay"></div>
        </div>
        <div class="container">
            <div class="hero-content">
                <span class="brand-name">MarbellaCamper</span>
                <h1 class="hero-title">¡Bienvenido a nuestro sitio web de <span class="highlight">alquiler de autocaravanas</span> en la soleada España!</h1>
                <p class="hero-subtitle">Estamos encantados de ofrecerle una oportunidad única para embarcarse en un viaje inolvidable a través de los pintorescos rincones de este increíble país. Nuestras autocaravanas modernas y cómodas le permitirán disfrutar de la libertad de movimiento, confort y comodidad en cualquier época del año.</p>
                <div class="hero-buttons">
                    <a href="#contact" class="btn btn-primary">Reserva Ahora</a>
                    <a href="#motorhomes" class="btn btn-view">Ver Nuestra Flota</a>
                </div>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main>
        <!-- Motorhomes Section -->
        <section id="motorhomes" class="section">
            <div class="container">
                <h2 class="section-title lang-en">Nuestras Autocaravanas</h2>
                <h2 class="section-title lang-es" style="display: none;">Nuestras Autocaravanas de Lujo</h2>
                <div class="motorhomes-grid">
                    <!-- Benimar Sport 323 -->
                    <div class="motorhome-card">
                        <div class="swiper motorhome-slider">
                            <div class="swiper-wrapper">                          
                                <div class="swiper-slide">
                                    <img src="../images/1 автодом/0042AAE5-1992-4109-80E4-EADD39269D9E.JPG" alt="Benimar Sport 323">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/1 автодом/IMG_7314.JPEG" alt="Benimar Sport 323">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/1 автодом/IMG_7320.jpg" alt="Benimar Sport 323">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/1 автодом/IMG_7322.JPEG" alt="Benimar Sport 323">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/1 автодом/IMG_7331.JPEG" alt="Benimar Sport 323">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/1 автодом/IMG_7333.JPEG" alt="Benimar Sport 323">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/1 автодом/IMG_7339.JPEG" alt="Benimar Sport 323">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/1 автодом/IMG_7342.jpg" alt="Benimar Sport 323">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/1 автодом/IMG_7344.jpg" alt="Benimar Sport 323">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/1 автодом/IMG_7350.JPEG" alt="Benimar Sport 323">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/1 автодом/IMG_7354.jpg" alt="Benimar Sport 323">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/1 автодом/IMG_7356.jpg" alt="Benimar Sport 323">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/1 автодом/IMG_7358.jpg" alt="Benimar Sport 323">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/1 автодом/IMG_7364.JPEG" alt="Benimar Sport 323">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/1 автодом/IMG_7365.JPEG" alt="Benimar Sport 323">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/1 автодом/IMG_7361 (1).JPEG" alt="Benimar Sport 323">
                                </div>

                                <div class="swiper-slide">
                                    <img src="../images/1 автодом/01772c07-72af-4655-8a92-6f94f929ec29.JPG" alt="Benimar Sport 323">
                                </div>
                                <div class="swiper-slide">
                                    <img src=" ../images/1 автодом/17A8465B-D8E0-4A49-96E9-627FDA693D2F.JPG" alt="Benimar Sport 323">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/1 автодом/80A219C2-15FC-4D24-B722-560D362C32C4.JPG" alt="Benimar Sport 323">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/1 автодом/F5D94B92-8146-4C30-A49A-5B7F231A5552.JPG" alt="Benimar Sport 323">
                                </div>
                            </div>
                            <div class="swiper-pagination"></div>
                            <div class="swiper-button-prev"></div>
                            <div class="swiper-button-next"></div>
                        </div>
                        <div class="motorhome-content">
                            <h3>Benimar Sport 323</h3>
                            <div class="features">
                               <p>Homologado para viajar/dormir 7 personas. Baño completo con ducha, cocina equipada con menaje, nevera grande con congelador, armario, ropa de cama y toallas, TV smart, Webasto calefacción, placa solar, mosquiteras, bombona de gas, cámara trasera, cierras exteriores y interiores para seguridad, mesa y sillas camping plegables, porta bicicletas para 3, toldo lateral. Química WC está incluida . Seguro con cobertura total con franquicia 900€. </p>
                            </div>
                            <div class="motorhome-footer">
                                <button class="btn btn-primary view-prices">Ver Precios</button>
                                <div class="price-info" style="display: none;">
                                    <div class="price-details">
                                            <h4>Precios:</h4>
                                            <ul>
                                                <li>temporada baja (1/11-31/03) 85€/día</li>
                                                <li>temporada media (1/04-30/06; 11/09-31/10) 115€/día</li>
                                                <li>temporada alta (1/07-10/09) 145€/día</li>
                                                <li>Navidad/Semana Blanca/Semana Santa 130€/día</li>
                                            </ul>
                                            <h4>Kilometraje:</h4>
                                            <ul>
                                                <li>150km/día incluidos</li>
                                                <li>250km/día 15€/día</li>
                                                <li>350km/día 25€/día</li>
                                                <li>Km ilimitados 35€/día</li>
                                                <li>0,25€/km extra</li>
                                            </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- McLouis MC4-60 -->
                    <div class="motorhome-card">
                        <div class="swiper motorhome-slider">
                            <div class="swiper-wrapper">                    
                                <div class="swiper-slide">
                                    <img src="../images/2 автодом/576B7770-C916-4A75-AD69-B2A114BEA05A.JPG" alt="McLouis MC4-60">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/2 автодом/IMG_6632.jpg" alt="McLouis MC4-60">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/2 автодом/IMG_6648.jpg" alt="McLouis MC4-60">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/2 автодом/IMG_6653.jpg" alt="McLouis MC4-60">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/2 автодом/IMG_6654.jpg" alt="McLouis MC4-60">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/2 автодом/IMG_6661.jpg" alt="McLouis MC4-60">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/2 автодом/IMG_6669.jpg" alt="McLouis MC4-60">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/2 автодом/IMG_6663.jpg" alt="McLouis MC4-60">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/2 автодом/IMG_6676.jpg" alt="McLouis MC4-60">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/2 автодом/IMG_6686.jpg" alt="McLouis MC4-60">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/2 автодом/IMG_6692.jpg" alt="McLouis MC4-60">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/2 автодом/IMG_6702.jpg" alt="McLouis MC4-60">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/2 автодом/IMG_6707.jpg" alt="McLouis MC4-60">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/2 автодом/IMG_6709.jpg" alt="McLouis MC4-60">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/2 автодом/IMG_6716.jpg" alt="McLouis MC4-60">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/2 автодом/IMG_6728.jpg" alt="McLouis MC4-60">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/2 автодом/IMG_6733.jpg" alt="McLouis MC4-60">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/2 автодом/IMG_6738.jpg" alt="McLouis MC4-60">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/2 автодом/IMG_6747.jpg" alt="McLouis MC4-60">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/2 автодом/3420df4d-9c90-4f6f-aa8c-58568b98fe59.JPG" alt="McLouis MC4-60">
                                </div>
            
                                <div class="swiper-slide">
                                    <img src="../images/2 автодом/606C6D84-B9B1-4C33-8E49-6F3016D0AB18.JPG" alt="McLouis MC4-60">
                                </div>
                            </div>
                            <div class="swiper-pagination"></div>
                            <div class="swiper-button-prev"></div>
                            <div class="swiper-button-next"></div>
                        </div>
                        <div class="motorhome-content">
                            <h3>McLouis MC4-60</h3>
                            <div class="features">
                              <p>Homologado para viajar/dormir 5 personas. Baño completo con ducha, cocina equipada con menaje, nevera grande con congelador, armario, ropa de cama y toallas, 2 televisores (1 TV Smart), Truma calefacción, placa solar, mosquiteras, 2 bombonas de gas, cámara trasera, cierras exteriores y interiores para seguridad, mesa y sillas camping plegables, gran maletero con zapateras, toldo lateral. Química WC está incluida . Seguro con cobertura total con franquicia 900€. </p>
                            </div>
                            <div class="motorhome-footer">
                                <button class="btn btn-primary view-prices">Ver Precios</button>
                                <div class="price-info" style="display: none;">
                                    <div class="price-details">
                                        <h4>Precios:</h4>
                                        <ul>
                                            <li>temporada baja (1/11-31/03) 85€/día</li>
                                            <li>temporada media (1/04-30/06; 11/09-31/10) 115€/día</li>
                                            <li>temporada alta (1/07-10/09) 145€/día</li>
                                            <li>Navidad/Semana Blanca/Semana Santa 130€/día</li>
                                        </ul>
                                        <h4>Kilometraje:</h4>
                                        <ul>
                                            <li>150km/día incluidos</li>
                                            <li>250km/día 15€/día</li>
                                            <li>350km/día 25€/día</li>
                                            <li>Km ilimitados 35€/día</li>
                                            <li>0,25€/km extra</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Iveco Daily -->
                    <div class="motorhome-card">
                        <div class="swiper motorhome-slider">
                            <div class="swiper-wrapper">
                                <div class="swiper-slide">
                                    <img src="../images/3 автодом/056E9CB5-D7A7-4EEA-95E7-AF3839EEC676.JPG" alt="Iveco Daily">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/3 автодом/IMG_7495.jpg" alt="Iveco Daily">
                                </div>   
                                <div class="swiper-slide">
                                    <img src="../images/3 автодом/IMG_7498.jpg" alt="Iveco Daily">
                                </div>   
                                <div class="swiper-slide">
                                    <img src="../images/3 автодом/IMG_7502.jpg" alt="Iveco Daily">
                                </div>   
                                <div class="swiper-slide">
                                    <img src="../images/3 автодом/IMG_7503.jpg" alt="Iveco Daily">
                                </div>   
                                <div class="swiper-slide">
                                    <img src="../images/3 автодом/IMG_7509.jpg" alt="Iveco Daily">
                                </div>   
                                <div class="swiper-slide">
                                    <img src="../images/3 автодом/IMG_7513.jpg" alt="Iveco Daily">
                                </div>   
                                <div class="swiper-slide">
                                    <img src="../images/3 автодом/IMG_7515.jpg" alt="Iveco Daily">
                                </div>   
                                <div class="swiper-slide">
                                    <img src="../images/3 автодом/IMG_7517.jpg" alt="Iveco Daily">
                                </div>   
                                <div class="swiper-slide">
                                    <img src="../images/3 автодом/IMG_7520.jpg" alt="Iveco Daily">
                                </div>   
                                <div class="swiper-slide">
                                    <img src="../images/3 автодом/IMG_7532.jpg" alt="Iveco Daily">
                                </div>  
                                 <div class="swiper-slide">
                                    <img src="../images/3 автодом/IMG_7551.jpg" alt="Iveco Daily">
                                </div>   
                                <div class="swiper-slide">
                                    <img src="../images/3 автодом/IMG_7559.jpg" alt="Iveco Daily">
                                </div>   
                                <div class="swiper-slide">
                                    <img src="../images/3 автодом/IMG_7562.jpg" alt="Iveco Daily">
                                </div>   
                                <div class="swiper-slide">
                                    <img src="../images/3 автодом/IMG_7589.jpg" alt="Iveco Daily">
                                </div>   
                                <div class="swiper-slide">
                                    <img src="../images/3 автодом/IMG_7594.jpg" alt="Iveco Daily">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/3 автодом/IMG_7602.jpg" alt="Iveco Daily">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/3 автодом/IMG_7604.jpg" alt="Iveco Daily">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/3 автодом/IMG_7611.jpg" alt="Iveco Daily">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/3 автодом/IMG_7623.jpg" alt="Iveco Daily">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/3 автодом/4B945A55-F325-4292-9BD5-70943B939187.JPG" alt="Iveco Daily">
                                </div>
                            </div>
                            <div class="swiper-pagination"></div>
                            <div class="swiper-button-prev"></div>
                            <div class="swiper-button-next"></div>
                        </div>
                        <div class="motorhome-content">
                            <h3>Iveco Daily</h3>
                            <div class="features">
                           <p>Homologado para viajar/dormir 5/4 personas (1 cama doble, 1 cama singular, 1,5 cama, posible adulto + niño). Baño completo con ducha, cocina equipada con menaje, nevera de compresor con un pequeño congelador, armario, ropa de cama y toallas, smart TV, calefacción, agua caliente, placa solar, mosquiteros, bombona de gas para cocina de gas, cámara de visión trasera, cerraduras exteriores y interiores para seguridad, mesa y sillas de camping plegables, maletero muy amplio, ducha exterior, toldo, WC químico incluido. Seguro con cobertura total con franquicia 800€.</p>
                            </div>
                            <div class="motorhome-footer">
                                <button class="btn btn-primary view-prices">Ver Precios</button>
                                <div class="price-info" style="display: none;">
                                    <div class="price-details">
                                        <h4>Precios:</h4>
                                        <ul>
                                            <li>temporada baja (1/11-31/03) 70€/día</li>
                                            <li>temporada media (1/04-30/06; 11/09-31/10) 90€/día</li>
                                            <li>temporada alta (1/07-10/09) 120€/día</li>
                                            <li>Navidad/Semana Blanca/Semana Santa 105€/día</li>
                                        </ul>
                                        <h4>Kilometraje:</h4>
                                        <ul>
                                            <li>150km/día incluidos</li>
                                            <li>250km/día 10€/día</li>
                                            <li>350km/día 15€/día</li>
                                            <li>Km ilimitados 25€/día</li>
                                            <li>0,25€/km extra</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- About Section -->
        <section id="about" class="section about-section">
            <div class="container">
                <span class="section-subtitle">NUESTRA GALERÍA</span>
                <h2 class="section-title">Galería de Nuestra Colección de Furgonetas</h2>
                <div class="about-content">
                    <div class="about-text">
                        <p>MarbellaCamper es su socio confiable en el mundo de las autocaravanas y los viajes en España. Ofrecemos autocaravanas de primera clase equipadas con todo lo necesario para una estancia confortable. Nuestra misión es hacer que su viaje sea inolvidable proporcionando un servicio de alta calidad y soporte profesional en todas las etapas de su aventura.</p>
                    </div>
                </div>
                <div class="gallery-slider">
                    <div class="swiper gallery-swiper">
                        <div class="swiper-wrapper">
                            <div class="swiper-slide">
                                <img src="../images/pictures/IMG_8312.JPEG" alt="MarbellaCamper Experience">
                            </div>
                            <div class="swiper-slide">
                                <img src="../images/pictures/IMG_8313.JPEG" alt="Luxury Motorhome">
                            </div>
                            <div class="swiper-slide">
                                <img src="../images/pictures/IMG_8677.JPEG" alt="Travel Experience">
                            </div>
                            <div class="swiper-slide">
                                <img src="../images/pictures/IMG_8822.JPEG" alt="Camping Life">
                            </div>
                            <div class="swiper-slide">
                                <img src="../images/pictures/IMG_8826.JPEG" alt="Adventure Time">
                            </div>
                            <div class="swiper-slide">
                                <img src="../images/pictures/IMG_8827.JPEG" alt="Scenic Views">
                            </div>
                        </div>
  
                    </div>
                </div>
            </div>
        </section>

        <!-- Why Choose Us Section -->
        <section class="why-choose-us" id="advantages">
            <div class="container">
                <span class="section-subtitle" style="color:#FFB800">POR QUÉ ELEGIRNOS</span>
                <h2 class="section-title">Ofrecemos el Mejor Vehículo para Tu Experiencia de Aventura</h2>
                <div class="why-choose-us-content">
                    <div class="video-side" style="margin-top: -50px;">
                        <div class="video-wrapper">
                            <iframe src="https://drive.google.com/file/d/1PmL-erxx0D-YbWvtOn9db-mn9b23ijDY/preview" 
                            width="1600"
                            height="900"
                            allow="autoplay"
                            allowfullscreen
                            style="width: 100%; border: none;">
                            </iframe>
                        </div>
                    </div>
                    <div class="features-side">
                        <div class="feature-item">
                            <div class="feature-icon">
                                <i class="fas fa-dollar-sign"></i>
                            </div>
                            <div class="feature-text">
                                <h3>Experiencia Desde 2022</h3>
                                <p>Comenzamos nuestra experiencia de alquiler de autocaravanas en 2022 y desde ese momento hemos tenido cientos de clientes satisfechos.</p>
                            </div>
                        </div>
                        <div class="feature-item">
                            <div class="feature-icon">
                                <i class="fas fa-headset"></i>
                            </div>
                            <div class="feature-text">
                                <h3>Soporte 24/7</h3>
                                <p>Estamos en contacto 24/7 para resolver cualquier duda y dar nuestras recomendaciones de rutas, campings y servicios para autocaravanas.</p>
                            </div>
                        </div>
                        <div class="feature-item">
                            <div class="feature-icon">
                                <i class="fas fa-tools"></i>
                            </div>
                            <div class="feature-text">
                                <h3>Flota Bien Mantenida</h3>
                                <p>Alquilamos nuestras propias autocaravanas, por lo que están muy bien mantenidas y equipadas para hacer que su viaje sea perfecto.</p>
                            </div>
                        </div>
                        <div class="feature-item">
                            <div class="feature-icon">
                                <i class="fas fa-tag"></i>
                            </div>
                            <div class="feature-text">
                                <h3>Alquiler Directo</h3>
                                <p>Alquilar directamente del propietario ayuda a evitar comisiones y hace que nuestros precios sean atractivos.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

       

        <!-- Reviews Section -->
        <section id="reviews" class="section testimonial">
            <div class="container">
                <div class="testimonial-wrapper">
                    <div class="testimonial-content">
                        <span class="section-subtitle">TESTIMONIOS</span>
                        <h2 class="section-title">Comentarios</h2>
                        <p class="section-description">Lee las experiencias de nuestros clientes satisfechos que han disfrutado de aventuras inolvidables en nuestras autocaravanas.</p>
                        <div class="swiper testimonial-slider">
                            <div class="swiper-wrapper">
                                <!-- Testimonial 1 -->
                                <div class="swiper-slide">
                                    <div class="testimonial-item">
                                        <div class="rating">
                                            <i class="fas fa-star"></i>
                                            <i class="fas fa-star"></i>
                                            <i class="fas fa-star"></i>
                                            <i class="fas fa-star"></i>
                                            <i class="fas fa-star"></i>
                                        </div>
                                        <h4 class="author-name">Michael y Sarah</h4>
                                        <p class="testimonial-text">"Increíble experiencia con MarbellaCamper! La casa rodante estaba impecablemente limpia y totalmente equipada con todo lo necesario. La suspensión neumática hizo que el viaje fuera increíblemente suave. Su apoyo las 24 horas del día fue fantástico; incluso recomendaron algunos hermosos campings en la costa del Sol. ¡Definitivamente volveré a alquilar con ellos otra vez!"</p>
                                    </div>
                                </div>
                                <!-- Testimonial 2 -->
                                <div class="swiper-slide">
                                    <div class="testimonial-item">
                                        <div class="rating">
                                            <i class="fas fa-star"></i>
                                            <i class="fas fa-star"></i>
                                            <i class="fas fa-star"></i>
                                            <i class="fas fa-star"></i>
                                            <i class="fas fa-star"></i>
                                        </div>
                                        <h4 class="author-name">Familia Thomas</h4>
                                        <p class="testimonial-text">"¡Vacaciones familiares perfectas! Alquilamos el Benimar Sport 323 durante dos semanas. La autocaravana era moderna, espaciosa y tenía todas las comodidades que podríamos pedir. A los niños les encantó, y el servicio del equipo de MarbellaCamper fue excepcional. El proceso de alquiler directo fue sencillo y también nos ahorró dinero!"</p>
                                    </div>
                                </div>
                                <!-- Testimonial 3 -->
                                <div class="swiper-slide">
                                    <div class="testimonial-item">
                                        <div class="rating">
                                            <i class="fas fa-star"></i>
                                            <i class="fas fa-star"></i>
                                            <i class="fas fa-star"></i>
                                            <i class="fas fa-star"></i>
                                            <i class="fas fa-star"></i>
                                        </div>
                                        <h4 class="author-name">Andreas y María</h4>
                                        <p class="testimonial-text">"¡Nuestro viaje por España fue inolvidable gracias a MarbellaCamper! El McLouis MC4-60 fue perfecto para nuestras necesidades: cómodo, bien mantenido y equipado con todo lo que necesitábamos. Los propietarios fueron increíblemente serviciales y proporcionaron excelentes consejos para nuestro viaje. ¡La suspensión de aire de la autocaravana hizo que conducir fuera un verdadero placer!"</p>
                                    </div>
                                </div>
                            </div>
                            <div class="swiper-pagination"></div>
                            <div class="swiper-button-prev"></div>
                            <div class="swiper-button-next"></div>
                        </div>
                    </div>
                    <div class="testimonial-image">
                        <img src="../images/pictures/IMG_9176.JPG" alt="Camper Experience">
                    </div>
                </div>
            </div>
        </section>

        <!-- Air Suspension Section -->
        <section id="suspension" class="section air-suspension" style="margin-top: -45px;"> 
            <div class="container">
                <h2 class="section-title lang-en">Sistemas de Suspensión Neumática</h2>
                <h2 class="section-title lang-es" style="display: none;">Sistemas de Suspensión Neumática</h2>
                <div class="suspension-card">
                    <div class="suspension-slider">
                        <div class="swiper suspension-swiper">
                            <div class="swiper-wrapper">
                                <div class="swiper-slide">
                                    <img src="../images/4 объявление продажа пневмоподвесок/snapedit_1742815922853.jpeg" alt="Air Suspension 1">
                                </div>
                                <div class="swiper-slide">
                                        <img src="../images/4 объявление продажа пневмоподвесок/snapedit_1742815953262.jpeg" alt="Air Suspension 2">
                                    </div>
                                <div class="swiper-slide">
                                    <img src="../images/4 объявление продажа пневмоподвесок/snapedit_1742815986065.jpeg" alt="Air Suspension 3">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/4 объявление продажа пневмоподвесок/snapedit_1742816041445.jpeg" alt="Air Suspension 4">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/4 объявление продажа пневмоподвесок/snapedit_1742816062354.jpeg" alt="Air Suspension 5">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/4 объявление продажа пневмоподвесок/snapedit_1742816165337.jpeg" alt="Air Suspension 6">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/4 объявление продажа пневмоподвесок/Airbrush-Image-Enhancer-no-bg-HD (carve.photos).png" alt="Air Suspension 7">
                                </div>
                                <div class="swiper-slide">
                                    <img src="../images/4 объявление продажа пневмоподвесок/snapedit_1742816186374.jpeg" alt="Air Suspension 7">
                                </div>
                            </div>
                            <div class="swiper-pagination"></div>
                            <div class="swiper-button-prev"></div>
                            <div class="swiper-button-next"></div>
                        </div>
                    </div>
                    
                    <div class="suspension-info">
                        <div class="suspension-header">
                            <div class="header-content">
                                <h3 class="lang-en">Suspensión Neumática Profesional</h3>
                                <h3 class="lang-es" style="display: none;">Sistema de Suspensión Neumática</h3>
                                
                                <p class="subtitle">
                                    <span class="highlight">Aprobado para FURGONETAS, CAMIONES y AUTOCARAVANAS</span> 
                                    sobre la plataforma FIAT DUCATO
                                </p>
                                
                                <div class="price-tag">
                                    <span class="price-amount">521€</span>
                                    <span class="price-label">OFERTA ESPECIAL</span>
                                </div>
                                </div>
                                <div class="header-actions" style="position: relative; top: 20px;">
                                    <a href="#contact" class="btn btn-primary lang-en">Solicitar Instalación</a>
                             
                                    <button class="btn btn-outline show-details" data-text-show="Ver Detalles" data-text-hide="Ocultar Detalles">Ver Detalles</button>

                            </div>
                        </div>

                        <div class="suspension-details" style="display: none;">
                            <div class="details-tabs">
                                <button class="tab-btn active" data-tab="specs">
                                    <i class="fas fa-cog"></i>
                                    <span>Especificaciones</span>
                                </button>
                                <button class="tab-btn" data-tab="compatibility">
                                    <i class="fas fa-check-circle"></i>
                                    <span>Compatibilidad</span>
                                </button>
                                <button class="tab-btn" data-tab="kit">
                                    <i class="fas fa-box-open"></i>
                                    <span>Contenido del Kit</span>
                                </button>
                            </div>

                            <div class="details-content">
                                <div class="tab-content active" id="specs">
                                    <div class="spec-item">
                                        <span class="spec-label">Tipo de Impulsión</span>
                                        <span class="spec-value">Tracción delantera (FWD)</span>
                                    </div>
                                    <div class="spec-item">
                                        <span class="spec-label">Configuración de<br> la Rueda Trasera</span>
                                        <span class="spec-value">Rueda simple (SW)</span>
                                    </div>
                                    <div class="spec-item">
                                        <span class="spec-label">Sistema de Control</span>
                                        <span class="spec-value">Panel de interruptores de paleta 2DB_E</span>
                                    </div>
                                </div>

                                <div class="tab-content" id="compatibility">
                                    <h4>Modelos FIAT</h4>
                                    <ul class="model-list">
                                        <li><strong>DUCATO X250-X295</strong> (2006+)</li>
                                        <li><strong>DUCATO X244</strong> (1994-2006)</li>
                                        <li><strong>DUCATO X230</strong> (1981-1994)</li>
                                        <li><strong>SCUDO</strong> (2016+)</li>
                                    </ul>

                                    <h4>Otras Marcas Compatibles</h4>
                                    <div class="brand-grid">
                                        <span>FORD</span>
                                        <span>IVECO</span>
                                        <span>VOLKSWAGEN</span>
                                        <span>MERCEDES</span>
                                        <span>RENAULT</span>
                                        <span>MAN</span>
                                        <span>OPEL</span>
                                        <span>CITROËN</span>
                                        <span>PEUGEOT</span>
                                        <span>NISSAN</span>
                                        <span>HYUNDAI</span>
                                    </div>
                                </div>

                                <div class="tab-content" id="kit">
                                    <div class="kit-grid">
                                        <div class="kit-item">
                                            <div class="kit-icon">
                                                <i class="fas fa-wind"></i>
                                            </div>
                                            <div class="kit-content">
                                                <h3 class="kit-title">2 × 170/2</h3>
                                                <p class="kit-subtitle">Muelles de Aire</p>
                                            </div>
                                        </div>

                                        <div class="kit-item">
                                            <div class="kit-icon">
                                                <i class="fas fa-arrow-up"></i>
                                            </div>
                                            <div class="kit-content">
                                                <h3 class="kit-title">2 × Superior</h3>
                                                <p class="kit-subtitle">Soportes de Montaje</p>
                                            </div>
                                        </div>

                                        <div class="kit-item">
                                            <div class="kit-icon">
                                                <i class="fas fa-arrow-down"></i>
                                            </div>
                                            <div class="kit-content">
                                                <h3 class="kit-title">2 × Inferior</h3>
                                                <p class="kit-subtitle">Soportes de Montaje</p>
                                            </div>
                                        </div>

                                        <div class="kit-item">
                                            <div class="kit-icon">
                                                <i class="fas fa-gauge"></i>
                                            </div>
                                            <div class="kit-content">
                                                <h3 class="kit-title">Dual</h3>
                                                <p class="kit-subtitle">Panel de Control de Presión</p>
                                            </div>
                                        </div>

                                        <div class="kit-item">
                                            <div class="kit-icon">
                                                <i class="fas fa-bolt"></i>
                                            </div>
                                            <div class="kit-content">
                                                <h3 class="kit-title">12V X100</h3>
                                                <p class="kit-subtitle">Compresor Potenciado</p>
                                            </div>
                                        </div>

                                        <div class="kit-item">
                                            <div class="kit-icon">
                                                <i class="fas fa-equals"></i>
                                            </div>
                                            <div class="kit-content">
                                                <h3 class="kit-title">2 × 9m</h3>
                                                <p class="kit-subtitle">Mangueras Neumáticas</p>
                                            </div>
                                        </div>

                                        <div class="kit-item">
                                            <div class="kit-icon">
                                                <i class="fas fa-wrench"></i>
                                            </div>
                                            <div class="kit-content">
                                                <h3 class="kit-title">Completo</h3>
                                                <p class="kit-subtitle">Kit de Montaje</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Contact Form Section -->
        <section id="contact" class="section contact-section" style="margin-top: -120px;">
            <div class="container">
                <span class="section-subtitle">CONTÁCTANOS</span>
                <h2 class="section-title">Ponte en Contacto Con Nosotros</h2>
                <p class="section-description">¿Tienes alguna pregunta o quieres reservar una autocaravana? ¡Estamos aquí para ayudar!</p>
                
                <div class="contact-form-wrapper">
                    <form id="contactForm">
                        <div class="form-row">
                            <div class="form-group half">
                                <input type="text" id="firstName" name="firstName" placeholder=" " required>
                                <label for="firstName">Nombre</label>
                            </div>
                            <div class="form-group half">
                                <input type="text" id="lastName" name="lastName" placeholder=" " required>
                                <label for="lastName">Apellido</label>
                            </div>
                        </div>
                        <div class="form-group">
                            <input type="email" id="email" name="email" placeholder=" " required>
                            <label for="email">Email</label>
                        </div>
                        <div class="form-group">
                            <input type="tel" id="phone" name="phone" placeholder=" " required>
                            <label for="phone">Número de Teléfono</label>
                        </div>
                        <div class="form-group">
                            <textarea id="message" name="message" placeholder=" " required></textarea>
                            <label for="message">Tu Mensaje</label>
                        </div>
                        <button type="submit" class="submit-button">Enviar Mensaje</button>
                    </form>
                </div>
            </div>
        </section>

        <!-- Map Section -->
        <section class="map-section" id="location">
            <div class="container">
                <span class="section-subtitle" style="color:#FFB800;  margin-top: 20px;">NUESTRA UBICACIÓN</span>
                <h2 class="section-title">Encuéntranos en Marbella</h2>
                <div class="map-wrapper">
                    <iframe 
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d791.7371095197774!2d-4.766027395892556!3d36.50505443927612!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd7321716071dc87%3A0xb79176a70a1cd0e5!2sMarbellaCamper!5e0!3m2!1ses!2ses!4v1711533892015!5m2!1ses!2ses"
                    width="100%"
                    height="450"
                    style="border:0;"
                    allowfullscreen=""
                    loading="lazy"
                    referrerpolicy="no-referrer-when-downgrade">
                </iframe>
                </div>
            </div>
        </section>

        <!-- Footer -->
        <footer class="footer">
            <div class="container">
                <div class="footer-content">
                    <div class="footer-col">
                        <div class="footer-logo-wrapper" style="background-color: #fff;">
                            <img src="../images/logo/IMG_8475.png" alt="Marbella Camper" class="footer-logo">
                        </div>
                        <p class="footer-description">
                            Experimenta la libertad del camping de lujo con nuestros alquileres de furgonetas camper premium en Marbella. Tu aventura comienza aquí.
                        </p>
                        </div>
                        <div class="footer-col">
                            <h4>Navegación</h4>
                            <ul>
                                <li><a href="#motorhomes">Autocaravanas</a></li>
                                <li><a href="#about">Acerca de</a></li>
                                <li><a href="#advantages">Ventajas</a></li>
                                <li><a href="#reviews">Opiniones</a></li>
                                <li><a href="#suspension">Suspensión de Aire</a></li>
                                <li><a href="#contact">Contacto</a></li>
                                <li><a href="#location">Ubicación</a></li>
                            </ul>
                        </div>
                        <div class="footer-col">
                            <h4>Contáctanos</h4>
                        <ul>
                            <li>
                                <i class="fas fa-map-marker-alt"></i>
                                <span>Marbella, Spain</span>
                            </li>
                            <li>
                                <i class="fas fa-envelope"></i>
                                <a href="mailto:irwin76@gmx.com">irwin76@gmx.com</a>
                            </li>
                            <li>
                                <i class="fas fa-phone"></i>
                                <a href="tel:+34602585897">+34 602 585 897</a>
                            </li>
                            <li>
                                <i class="fas fa-phone"></i>
                                <a href="tel:+34660953228">+34 660 953 228</a>
                            </li>
                            <li class="social-links">
                                <a href="https://www.facebook.com/share/1X7BHF6NeA/?mibextid=wwXIfr" target="_blank" class="social-link">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512" class="social-icon">
                                        <path fill="currentColor" d="M279.14 288l14.22-92.66h-88.91v-60.13c0-25.35 12.42-50.06 52.24-50.06h40.42V6.26S260.43 0 225.36 0c-73.22 0-121.08 44.38-121.08 124.72v70.62H22.89V288h81.39v224h100.17V288z"/>
                                    </svg>
                                </a>
                                <a href="https://www.instagram.com/marbella_camper?igshid=MTE0c2lucGZ2OWo0OQ==" target="_blank" class="social-link">
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" class="social-icon">
                                        <path fill="currentColor" d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"/>
                                    </svg>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="footer-bottom">
                    <p class="copyright">Copyright 2024 &copy; All Rights Reserved</p>
                </div>
            </div>
        </footer>

    </body>
</html>
    '''
    
    # Преобразуем HTML
    result = convert_image_paths(test_html)
    print("Преобразованный HTML:")
    print(result)