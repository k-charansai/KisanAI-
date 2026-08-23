import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './LandingPage.css';
import farmerImg from '../assets/farmer-planting-seedling.jpg';
import riceImg from '../assets/farmers-rice-field.jpg';
import { fadeInUp, leafGrow, pulse } from '../utils/animations';
// Note: In actual implementation, we'd use framer-motion components
// For now, we'll set up the foundation

export default function LandingPage() {
  const navigate = useNavigate();
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => setIsMenuOpen(!isMenuOpen);

  return (
    <div className="landing-wrapper">
      {/* Navbar */}
      <nav className={`nav ${isMenuOpen ? 'nav-open' : ''}`} id="nav">
        <div className="nav-inner">
          <a onClick={() => navigate('/diagnose')} className="nav-logo">
            <div className="nav-logo-mark">&gt;</div>
            <span className="nav-logo-text">KisanAI</span>
          </a>
          <ul className="nav-links" id="navLinks">
            <li><a href="#how">How It Works</a></li>
            <li><a href="#scan">Scan Crop</a></li>
            <li><a href="#features">Features</a></li>
            <li><a href="#scan" className="nav-cta">Try Free</a></li>
          </ul>
          <button className="mobile-menu-btn" id="menuBtn" onClick={toggleMenu}>
            <i className={isMenuOpen ? 'fas fa-times' : 'fas fa-bars'}></i>
          </button>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="hero">
        <div className="hero-content">
          <div className="hero-text">
            <div className="hero-tag">
              <span className="pulse-dot"></span>
              AI-Powered Crop Diagnosis
            </div>
            <h1>Know what's wrong with your crop - <em>instantly</em></h1>
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
            {/* Placeholder for animated leaf - will be implemented with framer-motion */}
            <div className="hero-leaf-placeholder">
              {/* This will be replaced with actual animated leaf */}
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}