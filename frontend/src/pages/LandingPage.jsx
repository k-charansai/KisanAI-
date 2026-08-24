import React from 'react';
import { useNavigate } from 'react-router-dom';
import './LandingPage.css';
import farmerImg from '../assets/farmer-planting-seedling.jpg';
import riceImg from '../assets/farmers-rice-field.jpg';

export default function LandingPage() {
    const navigate = useNavigate();

    return (
        <div className="landing-wrapper">
            

  {/*  Navbar  */}
  <nav className="nav" id="nav">
    <div className="nav-inner">
      <a onClick={() => navigate('/diagnose')} className="nav-logo">
        <div className="nav-logo-mark">🌱</div>
        <span className="nav-logo-text">KisanAI</span>
      </a>
      <ul className="nav-links" id="navLinks">
        <li><a href="#how">How It Works</a></li>
        <li><a href="#scan">Scan Crop</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#scan" className="nav-cta">Try Free</a></li>
      </ul>
      <button className="mobile-menu-btn" id="menuBtn"><i className="fas fa-bars"></i></button>
    </div>
  </nav>

  {/*  Hero  */}
  <section className="hero">
    <div className="hero-grid-bg"></div>
    <div className="hero-content">
      <div className="hero-text">
        <div className="hero-tag">
          <span className="pulse-dot"></span>
          AI-Powered Crop Diagnosis
        </div>
        <h1>Know what's wrong with your crop — <em>instantly</em></h1>
        <p className="hero-desc">
          Take a photo of any infected leaf. KisanAI identifies the disease and gives you clear, actionable treatment advice in seconds.
        </p>
        <div className="hero-actions">
          <a href="#scan" className="btn btn-dark"><i className="fas fa-camera"></i> Scan a Crop</a>
          <a href="#how" className="btn btn-outline"><i className="fas fa-play"></i> How It Works</a>
        </div>
        <div className="hero-stats">
          <div>
            <div className="hero-stat-val" data-count="50">0</div>
            <div className="hero-stat-label">Diseases detected</div>
          </div>
          <div>
            <div className="hero-stat-val" data-count="98" data-suffix="%">0</div>
            <div className="hero-stat-label">Accuracy rate</div>
          </div>
          <div>
            <div className="hero-stat-val" data-count="10" data-suffix="s">0</div>
            <div className="hero-stat-label">Avg scan time</div>
          </div>
        </div>
      </div>

      <div className="hero-visual">
        <div className="hero-phone">
          <div className="phone-screen">
            <div className="phone-header">
              <span className="phone-header-dot"></span>
              <span>KisanAI</span>
            </div>
            <div className="phone-image-box">🍃</div>
            <div className="phone-result">
              <div className="phone-result-top">
                <span className="phone-result-disease">Leaf Blight Detected</span>
                <span className="phone-result-badge">94%</span>
              </div>
              <div style={{ 'fontSize': '0.75rem', 'color': '#6b7280', 'marginBottom': '0.25rem' }}>Confidence Score</div>
              <div className="phone-result-bar">
                <div className="phone-result-bar-fill"></div>
              </div>
            </div>
          </div>
        </div>

        <div className="float-card float-card-1">
          <div className="float-card-icon green"><i className="fas fa-check"></i></div>
          <div>
            <div style={{ 'fontSize': '0.7rem', 'color': 'var(--stone-400)' }}>Treatment</div>
            <div>Mancozeb 75% WP</div>
          </div>
        </div>

        <div className="float-card float-card-2">
          <div className="float-card-icon amber"><i className="fas fa-exclamation-triangle"></i></div>
          <div>
            <div style={{ 'fontSize': '0.7rem', 'color': 'var(--stone-400)' }}>Severity</div>
            <div>High — Act Now</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  {/*  Gallery  */}
  <section className="gallery-section">
    <div className="container">
      <div className="gallery-grid">
        <div className="gallery-item fade-up">
          <img src={riceImg} alt="Farmers transplanting rice seedlings in a paddy field" />
          <div className="gallery-caption">
            <div className="gallery-caption-eyebrow">In the field</div>
            <h4>Built alongside the people who work the land</h4>
          </div>
        </div>
        <div className="gallery-item fade-up d1">
          <img src={farmerImg} alt="Hands cupping soil around a young plant seedling" />
          <div className="gallery-caption">
            <div className="gallery-caption-eyebrow">Growing forward</div>
            <h4>Every scan starts with a seed worth protecting</h4>
          </div>
        </div>
      </div>
    </div>
  </section>

  {/*  How It Works  */}
  <section className="how-section" id="how">
    <div className="container">
      <div className="section-head">
        <div className="section-eyebrow">How It Works</div>
        <h2>Three steps. Ten seconds.</h2>
        <p>No jargon, no appointments. Just snap, scan, and act.</p>
      </div>

      <div className="steps-row">
        <div className="step fade-up">
          <div className="step-num">1</div>
          <div className="step-icon-wrap">📸</div>
          <h3>Take a Photo</h3>
          <p>Point your camera at the infected leaf or stem. Works best in natural light.</p>
        </div>
        <div className="step fade-up d1">
          <div className="step-num">2</div>
          <div className="step-icon-wrap">🔍</div>
          <h3>Let AI Analyze</h3>
          <p>Our model scans the image for disease patterns, spots, and discoloration.</p>
        </div>
        <div className="step fade-up d2">
          <div className="step-num">3</div>
          <div className="step-icon-wrap">💊</div>
          <h3>Get a Plan</h3>
          <p>Receive specific treatment, prevention, and care instructions you can follow today.</p>
        </div>
      </div>
    </div>
  </section>

  {/*  Scan Section  */}
  <section className="scan-section" id="scan">
    <div className="container-narrow">
      <div className="section-head">
        <div className="section-eyebrow">Disease Detection</div>
        <h2>Scan your crop</h2>
        <p>Upload a photo of an infected leaf for an instant diagnosis.</p>
      </div>

      <div className="upload-area" id="uploadArea" onClick={() => navigate('/diagnose')} style={{ cursor: 'pointer' }}>
        {/*  Default state  */}
        <div className="upload-default" id="uploadDefault">
          <div className="upload-illustration">
            <div className="ring"></div>
            <i className="fas fa-cloud-arrow-up"></i>
          </div>
          <h3>Drop your crop photo here</h3>
          <p className="sub">or click to browse your device</p>
          <div className="format-pills">
            <span className="format-pill">JPG</span>
            <span className="format-pill">PNG</span>
            <span className="format-pill">WEBP</span>
            <span className="format-pill">Max 10MB</span>
          </div>
        </div>

        {/*  Preview state  */}
        <div className="preview-state" id="previewState">
          <div className="preview-img-wrap">
            <img id="previewImg" src="" alt="Preview" />
          </div>
          <div className="preview-meta">
            <i className="fas fa-image"></i>
            <div>
              <div className="name" id="fileName">photo.jpg</div>
              <div className="size" id="fileSize">2.1 MB</div>
            </div>
          </div>
          <button className="btn btn-green" id="analyzeBtn" onClick="startScan()">
            <i className="fas fa-magnifying-glass"></i> Analyze Crop
          </button>
        </div>

        {/*  Scanning state  */}
        <div className="scanning-state" id="scanState">
          <div className="scan-visual">
            <img id="scanImg" src="" alt="Scanning" />
            <div className="scan-beam"></div>
            <div className="scan-grid-overlay"></div>
          </div>
          <div className="scan-progress-track">
            <div className="scan-progress-fill" id="progressFill"></div>
          </div>
          <div className="scan-text">
            <span id="scanMsg">Preparing image</span>
            <span className="dots"><span></span><span></span><span></span></span>
          </div>
        </div>
      </div>

      <input type="file" id="fileInput" accept="image/*" hidden />
    </div>
  </section>

  {/*  Results  */}
  <section className="results-section" id="results">
    <div className="container">
      <div className="result-header">
        <div className="check-circle"><i className="fas fa-check"></i></div>
        <h2>Diagnosis complete</h2>
        <p>Here's what we found and what to do next.</p>
      </div>

      <div className="diagnosis-box" id="diagnosisBox">
        <div className="diagnosis-top">
          <div className="diagnosis-icon" id="dIcon">🦠</div>
          <div className="diagnosis-info">
            <h3 id="dName">Late Blight</h3>
            <div className="latin" id="dCrop">Potato / Tomato — Phytophthora infestans</div>
          </div>
          <span className="severity-chip high" id="dSeverity">High Severity</span>
        </div>

        <div className="confidence-row">
          <div className="confidence-labels">
            <span>Confidence</span>
            <span id="dConf">94%</span>
          </div>
          <div className="confidence-track">
            <div className="confidence-fill" id="confFill"></div>
          </div>
        </div>

        <p className="diagnosis-desc" id="dDesc">
          Late blight is a potentially devastating disease of tomato and potato, caused by the fungus-like organism <em>Phytophthora infestans</em>. It spreads rapidly in cool, wet conditions and can destroy entire fields within days if left untreated.
        </p>
      </div>

      <div className="advice-title"><i className="fas fa-clipboard-list"></i> Recommended Actions</div>

      <div className="advice-grid" id="adviceGrid">
        <div className="advice-card fade-up">
          <div className="advice-card-head">
            <div className="advice-card-icon treat"><i className="fas fa-pills"></i></div>
            <h4>Treatment</h4>
          </div>
          <ul className="advice-list" id="adviceTreat"></ul>
        </div>
        <div className="advice-card fade-up d1">
          <div className="advice-card-head">
            <div className="advice-card-icon prevent"><i className="fas fa-shield-halved"></i></div>
            <h4>Prevention</h4>
          </div>
          <ul className="advice-list" id="advicePrevent"></ul>
        </div>
        <div className="advice-card fade-up d2">
          <div className="advice-card-head">
            <div className="advice-card-icon feed"><i className="fas fa-seedling"></i></div>
            <h4>Nutrition</h4>
          </div>
          <ul className="advice-list" id="adviceFeed"></ul>
        </div>
        <div className="advice-card fade-up d3">
          <div className="advice-card-head">
            <div className="advice-card-icon water"><i className="fas fa-droplet"></i></div>
            <h4>Watering</h4>
          </div>
          <ul className="advice-list" id="adviceWater"></ul>
        </div>
      </div>

      <div className="reset-wrap">
        <button className="btn btn-outline" onClick="resetAll()">
          <i className="fas fa-arrow-rotate-left"></i> Scan Another Crop
        </button>
      </div>
    </div>
  </section>

  {/*  Features  */}
  <section className="features-section" id="features">
    <div className="container">
      <div className="section-head">
        <div className="section-eyebrow">Why KisanAI</div>
        <h2>Built for the field, not the lab</h2>
        <p>Tools that actually help farmers, not just impress investors.</p>
      </div>

      <div className="features-grid">
        <div className="feature-card fade-up">
          <div className="feature-card-icon"><i className="fas fa-bolt"></i></div>
          <h3>Instant diagnosis</h3>
          <p>Results in under 10 seconds. No labs, no waiting — just your phone camera.</p>
        </div>
        <div className="feature-card fade-up d1">
          <div className="feature-card-icon"><i className="fas fa-brain"></i></div>
          <h3>Trained on real data</h3>
          <p>Over 100,000 images of real crop diseases across 50+ crops and counting.</p>
        </div>
        <div className="feature-card fade-up d2">
          <div className="feature-card-icon"><i className="fas fa-language"></i></div>
          <h3>Speaks your language</h3>
          <p>Advice in Hindi, Marathi, Tamil, Telugu, and 10+ regional languages.</p>
        </div>
        <div className="feature-card fade-up d3">
          <div className="feature-card-icon"><i className="fas fa-wifi-slash"></i></div>
          <h3>Works offline</h3>
          <p>Core detection runs on-device. Sync when you're back in range.</p>
        </div>
        <div className="feature-card fade-up d4">
          <div className="feature-card-icon"><i className="fas fa-clock-rotate-left"></i></div>
          <h3>Scan history</h3>
          <p>Track every scan over the season. Spot trends before they become problems.</p>
        </div>
        <div className="feature-card fade-up d5">
          <div className="feature-card-icon"><i className="fas fa-user-doctor"></i></div>
          <h3>Expert connect</h3>
          <p>Reach local agricultural officers and KVK experts for complex cases.</p>
        </div>
      </div>
    </div>
  </section>

  {/*  Ticker  */}
  <section className="ticker-section">
    <div className="ticker-track">
      <div className="ticker-item"><span className="emoji">🌾</span> Wheat</div>
      <div className="ticker-item"><span className="emoji">🍚</span> Rice</div>
      <div className="ticker-item"><span className="emoji">🌽</span> Maize</div>
      <div className="ticker-item"><span className="emoji">🥔</span> Potato</div>
      <div className="ticker-item"><span className="emoji">🍅</span> Tomato</div>
      <div className="ticker-item"><span className="emoji">🌶️</span> Chili</div>
      <div className="ticker-item"><span className="emoji">🥒</span> Cucumber</div>
      <div className="ticker-item"><span className="emoji">🫛</span> Soybean</div>
      <div className="ticker-item"><span className="emoji">🧅</span> Onion</div>
      <div className="ticker-item"><span className="emoji">🍇</span> Grapes</div>
      <div className="ticker-item"><span className="emoji">🍎</span> Apple</div>
      <div className="ticker-item"><span className="emoji">🍊</span> Orange</div>
      <div className="ticker-item"><span className="emoji">🥭</span> Mango</div>
      <div className="ticker-item"><span className="emoji">🍌</span> Banana</div>
      <div className="ticker-item"><span className="emoji">🌿</span> Cotton</div>
      <div className="ticker-item"><span className="emoji">☕</span> Coffee</div>
      {/*  duplicate for seamless loop  */}
      <div className="ticker-item"><span className="emoji">🌾</span> Wheat</div>
      <div className="ticker-item"><span className="emoji">🍚</span> Rice</div>
      <div className="ticker-item"><span className="emoji">🌽</span> Maize</div>
      <div className="ticker-item"><span className="emoji">🥔</span> Potato</div>
      <div className="ticker-item"><span className="emoji">🍅</span> Tomato</div>
      <div className="ticker-item"><span className="emoji">🌶️</span> Chili</div>
      <div className="ticker-item"><span className="emoji">🥒</span> Cucumber</div>
      <div className="ticker-item"><span className="emoji">🫛</span> Soybean</div>
      <div className="ticker-item"><span className="emoji">🧅</span> Onion</div>
      <div className="ticker-item"><span className="emoji">🍇</span> Grapes</div>
      <div className="ticker-item"><span className="emoji">🍎</span> Apple</div>
      <div className="ticker-item"><span className="emoji">🍊</span> Orange</div>
      <div className="ticker-item"><span className="emoji">🥭</span> Mango</div>
      <div className="ticker-item"><span className="emoji">🍌</span> Banana</div>
      <div className="ticker-item"><span className="emoji">🌿</span> Cotton</div>
      <div className="ticker-item"><span className="emoji">☕</span> Coffee</div>
    </div>
  </section>

  {/*  CTA  */}
  <section className="cta-section">
    <h2>Your crops can't wait. <span className="serif" style={{ 'fontStyle': 'italic' }}>Neither should you.</span></h2>
    <p>One photo is all it takes to know exactly what's wrong and how to fix it.</p>
    <a href="#scan" className="btn btn-white"><i className="fas fa-camera"></i> Scan Your First Crop</a>
  </section>

  {/*  Footer  */}
  <footer>
    <div className="footer-inner">
      <div className="footer-brand">🌱 KisanAI</div>
      <div className="footer-links">
        <a onClick={() => navigate('/diagnose')}>About</a>
        <a onClick={() => navigate('/diagnose')}>Contact</a>
        <a onClick={() => navigate('/diagnose')}>Privacy</a>
        <a onClick={() => navigate('/diagnose')}>Terms</a>
      </div>
      <div className="footer-copy">© 2026 KisanAI. All rights reserved.</div>
    </div>
  </footer>

  {/*  Toast  */}
  <div className="toast" id="toast">
    <i className="fas fa-circle-check"></i>
    <span id="toastText">Done</span>
  </div>

  

        </div>
    );
}
