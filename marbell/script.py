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
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Premium motorhome and campervan rentals in Marbella, Spain. Explore Spain in comfort with our well-maintained RVs equipped with air suspension. Direct rentals, no commission.">
    <meta name="keywords" content="motorhome rental, campervan spain, RV rental marbella, air suspension motorhome, luxury campervan, spain travel, marbella camping">
    <meta name="author" content="MarbellaCamper">
    <meta name="robots" content="index, follow">
    <link rel="icon" href="{% static 'marbell/images/logo/IMG_8475.png' %}" type="image/png">
    <title>MarbellaCamper</title>
    <link rel="canonical" href="https://marbellacamper.com">
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
                margin-top: 50px;
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
                    
        /* Убираем hover-эффект у кнопки в блоке с пневмоподвеской */
        .suspension-header .header-actions .btn-primary.lang-en:hover {
            background-color: #FFB800 !important;
            transform: none !important;
            box-shadow: none !important;
            opacity: 1 !important;
            cursor: default !important;
        }
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
        margin-top: -60px;
        padding-right: 1rem;
        padding-left: 1rem;
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
                    <img src="images/logo/IMG_8475.png" alt="MarbellaCamper" class="navbar-logo">
                </a>
                <div class="navbar-menu">
                    <ul class="navbar-nav">
                        <li><a href="#motorhomes" class="nav-link">Motorhomes</a></li>
                        <li><a href="#about" class="nav-link">About</a></li>
                        <li><a href="#advantages" class="nav-link">Advantages</a></li>
                        <li><a href="#reviews" class="nav-link">Reviews</a></li>
                        <li><a href="#suspension" class="nav-link">Air Suspension</a></li>
                        <li><a href="#contact" class="nav-link">Contact</a></li>
                        <li><a href="#location" class="nav-link">Location</a></li>
                        <li><a href="es/index.html" class="nav-link language-switch">Spanish</a></li>
                    </ul>
                </div>
                <button class="navbar-toggle" aria-label="Toggle navigation">
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
            <img src="images/pictures/23F3D002-03E2-4570-BCCF-1375D8E4E83D.jpeg"  class="hero-bg-image">
            <div class="overlay"></div>
        </div>
        <div class="container">
            <div class="hero-content">
                <span class="brand-name">MarbellaCamper</span>
                <h1 class="hero-title">Welcome to our website for <span class="highlight">motorhome rentals</span> in sunny Spain!</h1>
                <p class="hero-subtitle">We are delighted to offer you a unique opportunity to embark on an unforgettable journey through the picturesque corners of this amazing country. Our modern and comfortable motorhomes will allow you to enjoy the freedom of movement, comfort, and coziness at any time of the year.</p>
                <div class="hero-buttons">
                    <a href="#contact" class="btn btn-primary">Book Now</a>
                    <a href="#motorhomes" class="btn btn-view">View Our Fleet</a>
                </div>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main>
        <!-- Motorhomes Section -->
        <section id="motorhomes" class="section">
            <div class="container">
                <h2 class="section-title lang-en">Motorhomes</h2>
                <h2 class="section-title lang-es" style="display: none;">Nuestras Autocaravanas de Lujo</h2>
                <div class="motorhomes-grid">
                    {% for house in houses %}
                        <div class="motorhome-card">
                            <div class="swiper motorhome-slider">
                                <div class="swiper-wrapper">
                                    {% for photo in house.photos %}
                                        <div class="swiper-slide">
                                            <img src="{{ photo.photo.url }}" alt="{{ house.name }}">
                                        </div>
                                    {% empty %}
                                        <div class="swiper-slide">
                                            <img src="{% static 'marbell/images/no_photo.jpg' %}" alt="No Photo Available">
                                        </div>
                                    {% endfor %}
                                </div>
                                <div class="swiper-pagination"></div>
                                <div class="swiper-button-prev"></div>
                                <div class="swiper-button-next"></div>
                            </div>
                            <div class="motorhome-content">
                                <h3>{{ house.name }}</h3>
                                <div class="features">
                                    <p>{{ house.description }}</p>
                                </div>
                                <div class="motorhome-footer">
                                    <button class="btn btn-primary view-prices">View Prices</button>
                                    <div class="price-info" style="display: none;">
                                        <div class="price-details">
                                            <h4>Prices:</h4>
                                            <ul>
                                                {% for price in house.prices %}
                                                    <li>{{ price }}</li>
                                                {% endfor %}
                                            </ul>
                                            <h4>Mileage:</h4>
                                            <ul>
                                                {% for mile in house.mileage %}
                                                    <li>{{ mile }}</li>
                                                {% endfor %}
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    {% empty %}
                        <p>No motorhomes available.</p>
                    {% endfor %}
                </div>
            </div>
        </section>

        <!-- About Section -->
        <section id="about" class="section about-section">
            <div class="container">
                <span class="section-subtitle">OUR GALLERY</span>
                <h2 class="section-title">Gallery Of Our Van Collection</h2>
                <div class="about-content">
                    <div class="about-text">
                        <p>MarbellaCamper is your reliable partner in the world of motorhomes and travel in Spain. We offer first-class motorhomes equipped with everything necessary for a comfortable stay. Our mission is to make your trip unforgettable by providing high-quality service and professional support at all stages of your adventure.</p>
                    </div>
                </div>
                <div class="gallery-slider">
                    <div class="swiper gallery-swiper">
                        <div class="swiper-wrapper">
                            <div class="swiper-slide">
                                <img src="images/pictures/IMG_8312.JPEG" alt="MarbellaCamper Experience">
                            </div>
                            <div class="swiper-slide">
                                <img src="images/pictures/IMG_8313.JPEG" alt="Luxury Motorhome">
                            </div>
                            <div class="swiper-slide">
                                <img src="images/pictures/IMG_8677.JPEG" alt="Travel Experience">
                            </div>
                            <div class="swiper-slide">
                                <img src="images/pictures/IMG_8822.JPEG" alt="Camping Life">
                            </div>
                            <div class="swiper-slide">
                                <img src="images/pictures/IMG_8826.JPEG" alt="Adventure Time">
                            </div>
                            <div class="swiper-slide">
                                <img src="images/pictures/IMG_8827.JPEG" alt="Scenic Views">
                            </div>
                        </div>
                        <div class="swiper-pagination"></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Why Choose Us Section -->
        <section class="why-choose-us" id="advantages">
            <div class="container">
                <span class="section-subtitle" style="color:#FFB800">WHY CHOOSE US</span>
                <h2 class="section-title">We Provide Best Vehicle For Your Adventure Experience</h2>
                <div class="why-choose-us-content">
                    <div class="video-side" style="margin-top: -100px;">
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
                                    <h3>Easy Booking</h3>
                                    <p>We started our experience of renting the motorhomes in 2022 and from that moment we have hundreds of satisfied customers.</p>
                                </div>
                            </div>
                            <div class="feature-item">
                                <div class="feature-icon">
                                    <i class="fas fa-headset"></i>
                                </div>
                                <div class="feature-text">
                                    <h3>24/7 Support</h3>
                                    <p>We are in contact 24/7 for resolution of any doubt and give our recommendations of routes, campsites and services for motorhomes.</p>
                                </div>
                            </div>
                            <div class="feature-item">
                                <div class="feature-icon">
                                    <i class="fas fa-tools"></i>
                                </div>
                                <div class="feature-text">
                                    <h3>Fully Insured</h3>
                                    <p>We rent our own motorhomes, so they are very well maintained and equipped to make your trip perfect.</p>
                                </div>
                            </div>
                            <div class="feature-item">
                                <div class="feature-icon">
                                    <i class="fas fa-tag"></i>
                                </div>
                                <div class="feature-text">
                                    <h3>Affordable Pricing</h3>
                                    <p>Rent directly from the owner helps avoid commissions and makes our prices competitive.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Reviews Section -->
        <section id="reviews" class="section testimonial" >
            <div class="container">
                <div class="testimonial-wrapper">
                    <div class="testimonial-content">
                        <span class="section-subtitle">TESTIMONIALS</span>
                        <h2 class="section-title">What Our Clients Say</h2>
                        <p class="section-description">Read the experiences of our satisfied customers who have enjoyed unforgettable adventures in our motorhomes.</p>
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
                                        <h4 class="author-name">Michael and Sarah</h4>
                                        <p class="testimonial-text">"Amazing experience with MarbellaCamper! The motorhome was spotlessly clean and fully equipped with everything we needed. The air suspension made the journey incredibly smooth. Their 24/7 support was fantastic - they even recommended some beautiful campsites along the Costa del Sol. Will definitely rent from them again!"</p>
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
                                        <h4 class="author-name">Thomas Family</h4>
                                        <p class="testimonial-text">"Perfect family vacation! We rented the Benimar Sport 323 for two weeks. The motorhome was modern, spacious, and had all the amenities we could ask for. The kids loved it, and the service from the MarbellaCamper team was exceptional. The direct rental process was straightforward and saved us money too!"</p>
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
                                        <h4 class="author-name">Andreas & Maria</h4>
                                        <p class="testimonial-text">"Our trip through Spain was unforgettable thanks to MarbellaCamper! The McLouis MC4-60 was perfect for our needs - comfortable, well-maintained, and equipped with everything we needed. The owners were incredibly helpful and provided excellent tips for our journey. The motorhome's air suspension made driving a real pleasure!"</p>
                                    </div>
                                </div>
                            </div>
                            <div class="swiper-pagination"></div>
                            <div class="swiper-button-prev"></div>
                            <div class="swiper-button-next"></div>
                        </div>
                    </div>
                    <div class="testimonial-image">
                        <img src="images/pictures/IMG_9176.JPG" alt="Camper Experience">
                    </div>
                </div>
            </div>
        </section>

        <!-- Air Suspension Section -->
        <section id="suspension" class="section air-suspension" style="margin-top: -45px;">
            <div class="container">
                <h2 class="section-title lang-en">Air Suspension Systems</h2>
                <h2 class="section-title lang-es" style="display: none;">Sistemas de Suspensión Neumática</h2>
                <div class="suspension-card">
                    <div class="suspension-slider">
                        <div class="swiper suspension-swiper">
                            <div class="swiper-wrapper">
                                <div class="swiper-slide">
                                    <img src="images/4 объявление продажа пневмоподвесок/snapedit_1742815922853.jpeg" alt="Air Suspension 1">
                                </div>
                                <div class="swiper-slide">
                                        <img src="images/4 объявление продажа пневмоподвесок/snapedit_1742815953262.jpeg" alt="Air Suspension 2">
                                    </div>
                                <div class="swiper-slide">
                                    <img src="images/4 объявление продажа пневмоподвесок/snapedit_1742815986065.jpeg" alt="Air Suspension 3">
                                </div>
                                <div class="swiper-slide">
                                    <img src="images/4 объявление продажа пневмоподвесок/snapedit_1742816041445.jpeg" alt="Air Suspension 4">
                                </div>
                                <div class="swiper-slide">
                                    <img src="images/4 объявление продажа пневмоподвесок/snapedit_1742816062354.jpeg" alt="Air Suspension 5">
                                </div>
                                <div class="swiper-slide">
                                    <img src="images/4 объявление продажа пневмоподвесок/snapedit_1742816165337.jpeg" alt="Air Suspension 6">
                                </div>
                                <div class="swiper-slide">
                                    <img src="images/4 объявление продажа пневмоподвесок/Airbrush-Image-Enhancer-no-bg-HD (carve.photos).png" alt="Air Suspension 7">
                                </div>
                                <div class="swiper-slide">
                                    <img src="images/4 объявление продажа пневмоподвесок/snapedit_1742816186374.jpeg" alt="Air Suspension 7">
                                </div>
                            </div>
                            <div class="swiper-pagination"></div>
                            <div class="swiper-button-prev"></div>
                            <div class="swiper-button-next"></div>
                        </div>
                    </div>
                    
                    <div class="suspension-info">
                        <div class="suspension-header" >
                            <div class="header-content">
                                <h3 class="lang-en">Professional Air Suspension</h3>
                                <h3 class="lang-es" style="display: none;">Sistema de Suspensión Neumática</h3>
                                
                                <p class="subtitle">
                                    <span class="highlight">Approved for VANS, TRUCKS, and MOTORHOMES</span> 
                                    on the FIAT DUCATO platform
                                </p>
                                
                                <div class="price-tag">
                                    <span class="price-amount">521€</span>
                                    <span class="price-label">SPECIAL OFFER</span>
                                </div>
                            </div>
                            <div class="header-actions">
                                <a href="#contact" class="btn btn-primary lang-en">Request Installation</a>
                             
                                <button class="btn btn-outline show-details" data-text-show="View Details" data-text-hide="Hide Details">View Details</button>
                              
                            </div>
                        </div>

                        <div class="suspension-details" style="display: none;">
                            <div class="details-tabs">
                                <button class="tab-btn active" data-tab="specs">
                                    <i class="fas fa-cog"></i>
                                    <span>Specifications</span>
                                </button>
                                <button class="tab-btn" data-tab="compatibility">
                                    <i class="fas fa-check-circle"></i>
                                    <span>Compatibility</span>
                                </button>
                                <button class="tab-btn" data-tab="kit">
                                    <i class="fas fa-box-open"></i>
                                    <span>Kit Contents</span>
                                </button>
                            </div>

                            <div class="details-content">
                                <div class="tab-content active" id="specs">
                                    <div class="spec-item">
                                        <span class="spec-label">Drive Type</span>
                                        <span class="spec-value">Front-wheel drive (FWD)</span>
                                    </div>
                                    <div class="spec-item">
                                        <span class="spec-label">Rear Wheel Configuration</span>
                                        <span class="spec-value">Single wheel (SW)</span>
                                    </div>
                                    <div class="spec-item">
                                        <span class="spec-label">Control System</span>
                                        <span class="spec-value">2DB_E paddle switch panel</span>
                                    </div>
                                </div>

                                <div class="tab-content" id="compatibility">
                                    <h4>FIAT Models</h4>
                                    <ul class="model-list">
                                        <li><strong>DUCATO X250-X295</strong> (2006+)</li>
                                        <li><strong>DUCATO X244</strong> (1994-2006)</li>
                                        <li><strong>DUCATO X230</strong> (1981-1994)</li>
                                        <li><strong>SCUDO</strong> (2016+)</li>
                                    </ul>

                                    <h4>Other Compatible Brands</h4>
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
                                            <i class="fas fa-wind"></i>
                                            <span><strong>2 × 170/2</strong> Air Springs</span>
                                        </div>
                                        <div class="kit-item">
                                            <i class="fas fa-arrows-alt-v"></i>
                                            <span><strong>2 ×</strong> Upper Mounts</span>
                                        </div>
                                        <div class="kit-item">
                                            <i class="fas fa-arrows-alt-v"></i>
                                            <span><strong>2 ×</strong> Lower Mounts</span>
                                        </div>
                                        <div class="kit-item">
                                            <i class="fas fa-tachometer-alt"></i>
                                            <span><strong>Dual Pressure</strong> Gauge Panel</span>
                                        </div>
                                        <div class="kit-item">
                                            <i class="fas fa-bolt"></i>
                                            <span><strong>12V X100</strong> Boosted Compressor</span>
                                        </div>
                                        <div class="kit-item">
                                            <i class="fas fa-grip-lines"></i>
                                            <span><strong>2 × 9m</strong> Pneumatic Hoses</span>
                                        </div>
                                        <div class="kit-item">
                                            <i class="fas fa-tools"></i>
                                            <span>Complete Mounting Hardware</span>
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
        <section id="contact" class="section contact-section">
            <div class="container">
                <span class="section-subtitle">CONTACT US</span>
                <h2 class="section-title">Get In Touch With Us</h2>
                <p class="section-description">Have a question or want to book a motorhome? We're here to help!</p>
                
                <div class="contact-form-wrapper">
                    <form id="contactForm" method="post" action="{% url 'main_page' %}">
                        {% csrf_token %}
                        {% if form.errors %}
                            <div class="errors alert alert-danger">
                                {{ form.errors }}
                            </div>
                        {% endif %}
                        <div class="form-row">
                            <div class="form-group half">
                                {{ form.first_name }}
                                <label for="{{ form.first_name.id_for_label }}">First Name</label>
                            </div>
                            <div class="form-group half">
                                {{ form.last_name }}
                                <label for="{{ form.last_name.id_for_label }}">Last Name</label>
                            </div>
                        </div>
                        <div class="form-group">
                            {{ form.email_address }}
                            <label for="{{ form.email_address.id_for_label }}">Email Address</label>
                        </div>
                        <div class="form-group">
                            {{ form.phone_number }}
                            <label for="{{ form.phone_number.id_for_label }}">Phone Number</label>
                        </div>
                        <div class="form-group">
                            {{ form.message }}
                            <label for="{{ form.message.id_for_label }}">Your Message</label>
                        </div>
                        <button type="submit" class="submit-button">Send Message</button>
                    </form>
                    {% if success %}
                        <p class="alert alert-success">Thank you! Your message has been sent.</p>
                    {% endif %}
                </div>
            </div>
        </section>

        <!-- Map Section -->
        <section class="map-section" id="location">
            <div class="container">
                <span class="section-subtitle" style="color:#FFB800; margin-top: 20px;">OUR LOCATION</span>
                <h2 class="section-title">Find Us in Marbella</h2>
                <div class="map-wrapper">
                    <iframe 
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d791.7371095197774!2d-4.766027395892556!3d36.50505443927612!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd7321716071dc87%3A0xb79176a70a1cd0e5!2sMarbellaCamper!5e0!3m2!1sen!2ses!4v1711533892015!5m2!1sen!2ses"
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
                            <img src="images/logo/IMG_8475.png" alt="Marbella Camper" class="footer-logo">
                        </div>
                        <p class="footer-description">
                            Experience the freedom of luxury camping with our premium camper van rentals in Marbella. Your adventure starts here.
                        </p>
                    </div>
                    <div class="footer-col">
                        <h4>Navigation</h4>
                        <ul>
                            <li><a href="#motorhomes">Motorhomes</a></li>
                            <li><a href="#about">About</a></li>
                            <li><a href="#advantages">Advantages</a></li>
                            <li><a href="#reviews">Reviews</a></li>
                            <li><a href="#suspension">Air Suspension</a></li>
                            <li><a href="#contact">Contact</a></li>
                            <li><a href="#location">Location</a></li>
                        </ul>
                    </div>
                    <div class="footer-col">
                        <h4>Get In Touch</h4>
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