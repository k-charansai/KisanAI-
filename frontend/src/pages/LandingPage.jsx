import React, { useState, useEffect } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import './LandingPage.css';
import farmerImg from '../assets/farmer-planting-seedling.jpg';
import riceImg from '../assets/farmers-rice-field.jpg';
import { fadeInUp, leafGrow, pulse } from '../utils/animations';

export default function LandingPage() {
  const navigate = useNavigate();
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll);
    // Initial call in case page loads mid-scroll
    handleScroll();
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handleScanClick = () => {
    navigate('/diagnose');
  };

  return (
    <>
      {/* Navbar */}
      <nav className={\
av \\}>
        <div className=\"nav-inner\">
          <div className=\"nav-logo\">
            <div className=\"nav-logo-mark\">🌱</div>
            <div className=\"nav-logo-text\">KisanAI</div>
          </div>
          <div className=\"nav-links\" role=\"navigation\">
            <a href=\"#hero\">Home</a>
            <a href=\"#how-it-works\">How It Works</a>
            <a href=\"#scan\">Scan</a>
            <a href=\"#features\">Features</a>
          </div>
          <button 
            className=\"nav-cta\" 
            onClick={handleScanClick}
          >
            Get Started
          </button>
          <button 
            className=\"mobile-menu-btn\" 
            onClick={() => setIsMenuOpen(!isMenuOpen)}
            aria-label=\"Toggle mobile menu\"
          >
            ☰
          </div>
        </div>
        
        {/* Mobile menu */}
        {isMenuOpen && (
          <div className=\"nav-links mobile-menu\" onClick={() => setIsMenuOpen(false)}>
            <a href=\"#hero\">Home</a>
            <a href=\"#how-it-works\">How It Works</a>
            <a href=\"#scan\">Scan</a>
            <a href=\"#features\">Features</a>
            <button 
              className=\"nav-cta\" 
              onClick={handleScanClick}
              style={{ marginTop: '1rem' }}
            >
              Get Started
            </button>
          </div>
        )}
      </nav>

      {/* Hero Section */}
      <section id=\"hero\" className=\"hero\">
        <div className=\"hero-grid-bg\"></div>
        <div className=\"container\">
          <div className=\"hero-content\">
            <div className=\"hero-text\">
              <div className=\"hero-tag\">
                <span className=\"pulse-dot\" aria-hidden=\"true\"></span>
                Plant Health Assistant
              </div>
              <h1>Instantly <em>diagnose</em> crop diseases<br/>with AI-powered leaf analysis</h1>
              <p className=\"hero-desc\">
                Simply upload a photo of any affected leaf and get instant disease identification, 
                treatment recommendations, and preventive advice tailored to your location.
              </p>
              <div className=\"hero-actions\">
                <Link to=\"/diagnose\" className=\"btn btn-dark\">
                  Scan Your Plant <span aria-hidden=\"true\">→</span>
                </Link>
                <a href=\"#how-it-works\" className=\"btn btn-outline\">
                  How It Works
                </a>
              </div>
              <div className=\"hero-stats\">
                <div>
                  <div className=\"hero-stat-val\">94%</div>
                  <div className=\"hero-stat-label\">Accuracy</div>
                </div>
                <div>
                  <div className=\"hero-stat-val\">150+</div>
                  <div className=\"hero-stat-label\">Diseases Covered</div>
                </div>
                <div>
                  <div className=\"hero-stat-val\">10K+</div>
                  <div className=\"hero-stat-label\">Farmers Helped</div>
                </div>
              </div>
            </div>
            <div className=\"hero-visual\">
              <div className=\"hero-phone\">
                <div className=\"phone-screen\">
                  <div className=\"phone-header\">
                    <div className=\"phone-header-dot\" aria-hidden=\"true\"></div>
                    <span>Diagnosis Result</span>
                  </div>
                  <div className=\"phone-image-box\">
                    <span>🌿</span>
                  </div>
                  <div className=\"phone-result\">
                    <div className=\"phone-result-top\">
                      <span className=\"phone-result-disease\">Leaf Blight</span>
                      <span className=\"phone-result-badge\">High Risk</span>
                    </div>
                    <div className=\"phone-result-bar\">
                      <div className=\"phone-result-bar-fill\" style={{ width: '94%' }}></div>
                    </div>
                  </div>
                </div>
              </div>
              {/* Floating cards */}
              <div className=\"float-card float-card-1\">
                <div className=\"float-card-icon green\">📊</div>
                <span>94% Accurate</span>
              </div>
              <div className=\"float-card float-card-2\">
                <div className=\"float-card-icon amber\">⚡</div>
                <span>Instant Results</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Gallery Section */}
      <section className=\"gallery-section\">
        <div className=\"container\">
          <div className=\"section-head\">
            <p className=\"section-eyebrow\">Real Farmer Imagery</p>
            <h2>See how our AI works in real field conditions</h2>
            <p className=\"section-header-p\">
              Our model is trained on diverse, real-world agricultural imagery 
              to ensure accurate diagnosis across different lighting, angles, and backgrounds.
            </p>
          </div>
          <div className=\"gallery-grid\">
            <div className=\"gallery-item\">
              <img src={farmerImg} alt=\"Farmer examining rice leaf in field\" />
              <div className=\"gallery-caption\">
                <div className=\"gallery-caption-eyebrow\">Field Diagnosis</div>
                <h4>Early detection saves crops</h4>
              </div>
            </div>
            <div className=\"gallery-item\">
              <img src={riceImg} alt=\"Close-up of diseased rice leaf showing lesions\" />
              <div className=\"gallery-caption\">
                <div className=\"gallery-caption-eyebrow\">Disease Details</div>
                <h4>Clear lesion patterns guide treatment</h4>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* How It Works Section */}
      <section id=\"how-it-works\" className=\"how-section\">
        <div className=\"container\">
          <div className=\"section-head\">
            <p className=\"section-eyebrow\">Simple Process</p>
            <h2>How KisanAI Works</h2>
            <p className=\"section-header-p\">
              Get accurate diagnosis and treatment advice in just three simple steps.
            </p>
          </div>
          <div className=\"steps-row\">
            <div className=\"step\">
              <div className=\"step-num\">1</div>
              <div className=\"step-icon-wrap\">📸\</div>
              <h3>Upload Leaf Photo</h3>
              <p>Take or upload a clear photo of the affected plant leaf showing symptoms.</p>
            </div>
            <div className=\"step\">
              <div className=\"step-num\">2</div>
              <div className=\"step-icon-wrap\">🔬\</div>
              <h3>AI Analysis</h3>
              <p>Our AI analyzes the image within seconds to identify disease patterns and severity.</p>
            </div>
            <div className=\"step\">
              <div className=\"step-num\">3</div>
              <div className=\"step-icon-wrap\">📋\</div>
              <h3>Get Treatment Plan</h3>
              <p>Receive detailed diagnosis, organic/chemical treatment options, and preventive advice.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Scan Section */}
      <section id=\"scan\" className=\"scan-section\">
        <div className=\"container\">
          <div className=\"section-head\">
            <p className=\"section-eyebrow\">Ready to Scan?</p>
            <h2>Start diagnosing your crops today</h2>
            <p className=\"section-header-p\">
              Upload a leaf photo to get instant disease identification and treatment recommendations.
            </p>
          </div>
          <div className=\"upload-area\" onClick={handleScanClick}>
            <div className=\"upload-illustration\">
              <i className=\"fas fa-leaf\"></i>
              <div className=\"ring\" aria-hidden=\"true\"></div>
            </div>
            <h3>Scan Your Plant</h3>
            <p className=\"sub\">Drag & drop or click to upload</p>
            <div className=\"format-pills\">
              <span className=\"format-pill\">JPG</span>
              <span className=\"format-pill\">PNG</span>
              <span className=\"format-pill\">WEBP</span>
            </div>
          </div>
        </div>
      </section>

      {/* Results Section (Preview) */}
      <section id=\"results\" className=\"results-section\">
        <div className=\"container\">
          <div className=\"result-header\">
            <div className=\"check-circle\" aria-hidden=\"true\">✓</div>
            <h2>See What Results Look Like</h2>
            <p>Get comprehensive diagnosis and actionable advice in seconds</p>
          </div>
          <div className=\"diagnosis-box\">
            <div className=\"diagnosis-top\">
              <div className=\"diagnosis-icon\">🌾\</div>
              <div className=\"diagnosis-info\">
                <h3>Leaf Blight</h3>
                <div className=\"latin\">(Xanthomonas oryzae)</div>
                <div className=\"severity-chip medium\">Medium Risk</div>
              </div>
            </div>
            <div className=\"confidence-row\">
              <div className=\"confidence-labels\">
                <span>Confidence</span>
                <span>94%\</span>
              </div>
              <div className=\"confidence-track\">
                <div className=\"confidence-fill\" style={{ width: '94%' }}></div>
              </div>
            </div>
            <p className=\"diagnosis-desc\">
              Bacterial leaf blight appears as yellow-to-white lesions with wavy edges 
              that eventually turn brown and cause leaf wilting. <em>Early detection is crucial</em> 
              for effective management.
            </p>
          </div>
          <div className=\"advice-title\">
            <i className=\"fas fa-prescription-bottle\"></i>
            Recommended Treatment Plan
          </div>
          <div className=\"advice-grid\">
            <div className=\"advice-card\">
              <div className=\"advice-card-head\">
                <div className=\"advice-card-icon treat\">💊\</div>
                <h4>Immediate Treatment</h4>  
              </div>
              <ul className=\"advice-list\">
                <li><span className=\"check\" aria-hidden=\"true\">✓\</span>Apply copper-based bactericide</li>
                <li><span className=\"check\" aria-hidden=\"true\">✓\</span>Remove and destroy infected leaves</li>
                <li><span className=\"check\" aria-hidden=\"true\">✓\</span>Avoid overhead irrigation</li>
              </ul>
            </div>
            <div className=\"advice-card\">
              <div className=\"advice-card-head\">
                <div className=\"advice-card-icon prevent\">🛡️\</div>
                <h4>Prevention</h4>
              </div>
              <ul className=\"advice-list\">
                <li><span className=\"check\" aria-hidden=\"true\">✓\</span>Use disease-resistant varieties</li>
                <li><span className=\"check\" aria-hidden=\"true\">✓\</span>Practice crop rotation</li>
                <li><span className=\"check\" aria-hidden=\"true\">✓\</span>Ensure proper plant spacing</li>
              </ul>
            </div>
          </div>
          <div className=\"reset-wrap\">
            <button className=\"btn btn-outline\">Scan Another Leaf</button>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id=\"features\" className=\"features-section\">
        <div className=\"container\">
          <div className=\"section-head\">
            <p className=\"section-eyebrow\">Why Farmers Choose Us</p>
            <h2>Key Features</h2>
            <p className=\"section-header-p\">
              Purpose-built for agricultural diagnosis with features designed for real-world farming needs.
            </p>
          </div>
          <div className=\"features-grid\">
            <div className=\"feature-card\">
              <div className=\"feature-card-icon\">🌱\</div>
              <h3>Disease Identification</h3>
              <p>Accurately identifies 150+ plant diseases across 30+ crop types with detailed pathology information.</p>
            </div>
            <div className=\"feature-card\">
              <div className=\"feature-card-icon\">📍\</div>
              <h3>Location-Specific Advice</h3>
              <p>Treatment recommendations adapted to your local climate, growing conditions, and regulations.</p>
            </div>
            <div className=\"feature-card\">
              <div className=\"feature-card-icon\">📅\</div>
              <h3>Seasonal Alerts</h3>
              <p>Get timely warnings about disease outbreaks in your area based on weather patterns and regional reports.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Crops Ticker */}
      <section className=\"ticker-section\">
        <div className=\"container\">
          <div className=\"ticker-track\">
            <div className=\"ticker-item\><span className=\"emoji\">🌾\</span> Rice</div>
            <div className=\"ticker-item\><span className=\"emoji\">🌽\</span> Maize</div>
            <div className=\"ticker-item\><span className=\"emoji\">🍅\</span> Tomato</div>
            <div className=\"ticker-item\><span className=\"emoji\">🥔\</span> Potato</div>
            <div className=\"ticker-item\><span className=\"emoji\">🥬\</span> Lettuce</div>
            <div className=\"ticker-item\><span className=\"emoji\">🍎\</span> Apple</div>
            <div className=\"ticker-item\><span className=\"emoji\">🍊\</span> Orange</div>
            <div className=\"ticker-item\><span className=\"emoji\">🥕\</span> Carrot</div>
            <div className=\"ticker-item\><span className=\"emoji\">🌰\</span> Walnut</div>
            <div className=\"ticker-item\><span className=\"emoji\">🌻\</span> Sunflower</div>
            {/* Duplicate for seamless loop */}
            <div className=\"ticker-item\><span className=\"emoji\">🌾\</span> Rice</div>
            <div className=\"ticker-item\><span className=\"emoji\">🌽\</span> Maize</div>
            <div className=\"ticker-item\><span className=\"emoji\">🍅\</span> Tomato</div>
            <div className=\"ticker-item\><span className=\"emoji\">🥔\</span> Potato</div>
            <div className=\"ticker-item\><span className=\"emoji\">🥬\</span> Lettuce</div>
            <div className=\"ticker-item\><span className=\"emoji\">🍎\</span> Apple</div>
            <div className=\"ticker-item\><span className=\"emoji\">🍊\</span> Orange</div>
            <div className=\"ticker-item\><span className=\"emoji\">🥕\</span> Carrot</div>
            <div className=\"ticker-item\><span className=\"emoji\">🌰\</span> Walnut</div>
            <div className=\"ticker-item\><span className=\"emoji\">🌻\</span> Sunflower</div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className=\"cta-section\">
        <div className=\"container\">
          <h2>Join thousands of farmers protecting their crops with AI</h2>
          <p>Start scanning today - no expertise required. Get instant diagnosis and treatment advice in seconds.</p>
          <Link to=\"/diagnose\" className=\"btn btn-white\">
            Start Scanning Now
          </Link>
        </div>
      </section>

      {/* Footer */}
      <footer>
        <div className=\"container\">
          <div className=\"footer-inner\">
            <div className=\"footer-brand\">KisanAI</div>
            <div className=\"footer-links\">
              <a href=\"#\">How It Works</a>
              <a href=\"#\">Blog</a>
              <a href=\"#\">Contact</a>
            </div>
            <div className=\"footer-copy\">
              © 2026 KisanAI. All rights reserved. | 
              <a href=\"#\" style={{ color: 'var(--stone-400)' }}>Privacy Policy</a> | 
              <a href=\"#\" style={{ color: 'var(--stone-400)' }}>Terms of Service</a>
            </div>
          </div>
        </div>
      </footer>
    </>
  );
}
