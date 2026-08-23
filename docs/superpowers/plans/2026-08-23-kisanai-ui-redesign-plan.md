# KisanAI UI Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign the KisanAI user interface with a nature-inspired organic approach, featuring interactive elements, motion graphics, and improved user flow while preserving core crop diagnosis functionality.

**Architecture:** Component-based redesign using React with Framer Motion for animations. Updates will be made to existing components in the frontend/src directory, adding new animation utilities and assets while maintaining compatibility with the existing backend API.

**Tech Stack:** React, Framer Motion, CSS Modules, JavaScript/ES6

## File Structure
- **frontend/src/pages/LandingPage.jsx** - Main landing page with animated hero section
- **frontend/src/pages/LandingPage.module.css** - Styling for landing page with nature-inspired design
- **frontend/src/pages/DiagnosePage.jsx** - Improved diagnosis flow with progressive disclosure
- **frontend/src/pages/DiagnosePage.module.css** - Styling for diagnosis page
- **frontend/src/components/ImageUpload.jsx** - Enhanced upload area with leaf interaction
- **frontend/src/components/ImageUpload.module.css** - Styling for upload component
- **frontend/src/components/DiagnosisResult.jsx** - Improved results display with emergence animation
- **frontend/src/components/DiagnosisResult.module.css** - Styling for results component
- **frontend/src/components/AdvisoryPanel.jsx** - Enhanced advisory panel with unfolding animation
- **frontend/src/components/AdvisoryPanel.module.css** - Styling for advisory panel
- **frontend/src/components/ChatBubble.jsx** - Minor animation enhancements
- **frontend/src/components/ChatBubble.module.css** - Styling for chat bubbles
- **frontend/src/components/ChatInput.jsx** - Minor animation enhancements
- **frontend/src/components/ChatInput.module.css** - Styling for chat input
- **frontend/src/utils/animations.js** - Custom animation utilities and presets
- **frontend/src/assets/illustrations/** - New directory for nature-inspired SVG illustrations
- **frontend/src/assets/icons/** - New directory for animated icons

## Global Constraints
- Must maintain compatibility with existing backend API endpoints
- Must preserve Grad-CAM overlay functionality
- Must preserve LangGraph agent advisory functionality
- Must maintain responsive design for mobile and desktop
- Must follow existing code conventions in the frontend/src directory
- Must not break existing functionality during implementation
- Should use accessible animation practices (respect prefers-reduced-motion)
- Should maintain or improve performance metrics

---

## Task 1: Project Setup and Animation Utilities

**Files:**
- Create: `frontend/src/utils/animations.js`
- Modify: `frontend/src/pages/LandingPage.jsx`
- Modify: `frontend/src/pages/LandingPage.module.css`

**Interfaces:**
- Consumes: None (foundational setup)
- Produces: Animation utility functions and landing page foundation

- [ ] **Step 1: Create animation utilities file**
  
```javascript
// frontend/src/utils/animations.js
export const fadeInUp = {
  initial: { y: 20, opacity: 0 },
  animate: { y: 0, opacity: 1, transition: { duration: 0.6, ease: "easeOut" } },
  exit: { y: 20, opacity: 0, transition: { duration: 0.3 } }
};

export const leafGrow = {
  initial: { scale: 0, opacity: 0 },
  animate: { scale: 1, opacity: 1, transition: { duration: 1.2, ease: "elasticOut" } },
};

export const pulse = {
  initial: { scale: 1 },
  animate: { 
    scale: [1, 1.05, 1], 
    transition: { duration: 2, repeat: Infinity, ease: "easeInOut" } 
  },
};

export const leafUnfold = {
  initial: { rotate: -90, opacity: 0 },
  animate: { rotate: 0, opacity: 1, transition: { duration: 0.8, ease: "easeOut" } },
};

export const waterDropFill = {
  initial: { height: 0 },
  animate: { height: "100%", transition: { duration: 1.5, ease: "easeOut" } },
};

export const pollenFloat = {
  initial: { y: 0, opacity: 0 },
  animate: { 
    y: [-20, -40], 
    opacity: [0, 0.8, 0],
    transition: { duration: 3, repeat: Infinity, ease: "easeInOut" } 
  },
};
```

- [ ] **Step 2: Run lint to verify no syntax errors**

Run: `npm run lint -- --fix frontend/src/utils/animations.js`
Expected: PASS

- [ ] **Step 3: Update LandingPage.jsx to import animations and set up basic structure**

```javascript
import React from 'react';
import { useNavigate } from 'react-router-dom';
import './LandingPage.css';
import farmerImg from '../assets/farmer-planting-seedling.jpg';
import riceImg from '../assets/farmers-rice-field.jpg';
import { fadeInUp, leafGrow, pulse } from '../utils/animations';
// Note: In actual implementation, we'd use framer-motion components
// For now, we'll set up the foundation

export default function LandingPage() {
  const navigate = useNavigate();

  return (
    <div className="landing-wrapper">
      {/* Will be implemented in subsequent tasks */}
    </div>
  );
}
```

- [ ] **Step 4: Run development server to verify no errors**

Run: `npm run dev` (in background, then check for errors)
Expected: No compilation errors

- [ ] **Step 5: Commit**

```bash
git add frontend/src/utils/animations.js frontend/src/pages/LandingPage.jsx
git commit -m "feat: create animation utilities and landing page foundation"
```

## Task 2: Landing Page Hero Section

**Files:**
- Modify: `frontend/src/pages/LandingPage.jsx`
- Modify: `frontend/src/pages/LandingPage.module.css`

**Interfaces:**
- Consumes: Animation utilities from Task 1
- Produces: Animated hero section with growing leaf and core messaging

- [ ] **Step 1: Implement hero section structure in LandingPage.jsx**
  
```javascript
import React from 'react';
import { useNavigate } from 'react-router-dom';
import './LandingPage.css';
import farmerImg from '../assets/farmer-planting-seedling.jpg';
import riceImg from '../assets/farmers-rice-field.jpg';
import { fadeInUp, leafGrow, pulse } from '../utils/animations';

export default function LandingPage() {
  const navigate = useNavigate();

  return (
    <div className="landing-wrapper">
      {/* Navbar */}
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

      {/* Hero Section */}
      <section className="hero">
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
```

- [ ] **Step 2: Add basic hero section styling to LandingPage.module.css**
  
```css
/* Hero Section */
.hero {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 64px;
  align-items: center;
  padding: 96px 5%;
  min-height: 80vh;
  position: relative;
  overflow: hidden;
}

.hero-text {
  text-align: left;
}

.hero-tag {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  font-weight: 600;
  color: #8FBC8F;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 16px;
}

.pulse-dot {
  width: 8px;
  height: 8px;
  background-color: #8FBC8F;
  border-radius: 50%;
  animation: pulse 2s infinite;
}

.hero h1 {
  font-size: 2.5rem;
  line-height: 1.1;
  margin-bottom: 1.5rem;
  color: #2D3748;
}

.hero-desc {
  font-size: 1.125rem;
  color: #4A5568;
  margin-bottom: 2rem;
  line-height: 1.6;
}

.hero-actions {
  display: flex;
  gap: 1rem;
  margin-bottom: 2.5rem;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  font-weight: 500;
  cursor: pointer;
  border: none;
  border-radius: 0.5rem;
  text-decoration: none;
  transition: all 0.2s ease;
}

.btn-dark {
  background-color: #2D3748;
  color: white;
  padding: 0.75rem 1.5rem;
  font-size: 0.875rem;
}

.btn-dark:hover {
  background-color: #1A202C;
  transform: translateY(-2px);
}

.btn-outline {
  border: 2px solid #2D3748;
  color: #2D3748;
  padding: 0.75rem 1.5rem;
  font-size: 0.875rem;
}

.btn-outline:hover {
  background-color: rgba(45, 55, 72, 0.05);
  transform: translateY(-2px);
}

.hero-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  margin-top: 2rem;
  text-align: center;
}

.hero-stat-val {
  font-size: 2rem;
  font-weight: 700;
  color: #8FBC8F;
  line-height: 1;
}

.hero-stat-label {
  font-size: 0.875rem;
  color: #6B7280;
  margin-top: 0.5rem;
}

/* Hero Visual */
.hero-visual {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero-leaf-placeholder {
  width: 200px;
  height: 200px;
  background-color: rgba(143, 188, 143, 0.1);
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 3rem;
}

/* Animations */
@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.1); }
}
```

- [ ] **Step 4: Commit**

```bash
git add frontend/src/pages/LandingPage.jsx frontend/src/pages/LandingPage.module.css
git commit -m "feat: implement landing page hero section with basic styling"
```

## Task 3: Landing Page Navbar and Mobile Menu

**Files:**
- Modify: `frontend/src/pages/LandingPage.jsx`
- Modify: `frontend/src/pages/LandingPage.module.css`

**Interfaces:**
- Consumes: Hero section structure from Task 2
- Produces: Functional navbar with mobile menu toggle

- [ ] **Step 1: Add mobile menu functionality to LandingPage.jsx**
  
```javascript
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './LandingPage.css';
import farmerImg from '../assets/farmer-planting-seedling.jpg';
import riceImg from '../assets/farmers-rice-field.jpg';
import { fadeInUp, leafGrow, pulse } from '../utils/animations';

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
            <div className="nav-logo-mark">🌱</div>
            <span className="nav-logo-text">KisanAI</span>
          </a>
          <ul className="nav-links" id="navLinks">
            <li><a href="#how">How It Works</a></li>
            <li><a href="#scan">Scan Crop</a></li>
            <li><a href="#features">Features</a></li>
            <li><a href="#scan" className="nav-cta">Try Free</a></li>
          </ul>
          <button className="mobile-menu-btn" id="menuBtn" onClick={toggleMenu}>
            <i className={isMenuOpen ? 'fas fa-times' : 'fas fa-bars'></i>}
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
            <div className="hero-leaf-placeholder">
              {/* Will be replaced with animated leaf in later task */}
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
```

- [ ] **Step 2: Add mobile menu styling to LandingPage.module.css**
  
```css
/* Navbar Styles */
.nav {
  position: sticky;
  top: 0;
  background-color: #ffffff;
  border-bottom: 1px solid #E2E8F0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 5%;
  z-index: 100;
  transition: background-color 0.3s ease;
}

.nav.scrolled {
  background-color: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
}

.nav-inner {
  display: flex;
  align-items: center;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
}

.nav-logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  text-decoration: none;
}

.nav-logo-mark {
  font-size: 1.5rem;
}

.nav-logo-text {
  font-size: 1.25rem;
  font-weight: 700;
  color: #2D3748;
}

.nav-links {
  display: flex;
  gap: 2rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-links a {
  color: #4A5568;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s ease;
  position: relative;
}

.nav-links a:hover {
  color: #2D3748;
}

.nav-links a::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 0;
  height: 2px;
  background-color: #8FBC8F;
  transition: width 0.3s ease;
}

.nav-links a:hover::after {
  width: 100%;
}

.nav-cta {
  background-color: #8FBC8F;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  font-weight: 600;
  transition: all 0.2s ease;
}

.nav-cta:hover {
  background-color: #6D8D6D;
  transform: translateY(-2px);
}

.mobile-menu-btn {
  display: none;
  flex-direction: column;
  justify-content: space-between;
  width: 1.5rem;
  height: 1.5rem;
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 0;
}

.mobile-menu-btn span,
.mobile-menu-btn i {
  display: block;
  width: 100%;
  height: 2px;
  background-color: #2D3748;
  transition: all 0.3s ease;
}

/* Mobile Menu Styles */
@media (max-width: 768px) {
  .nav-links {
    position: fixed;
    top: 4rem;
    right: 0;
    height: calc(100vh - 4rem);
    width: 250px;
    background-color: white;
    flex-direction: column;
    align-items: flex-start;
    padding: 2rem;
    box-shadow: -2px 0 10px rgba(0,0,0,0.1);
    transform: translateX(100%);
    transition: transform 0.3s ease;
  }
  
  .nav-open .nav-links {
    transform: translateX(0);
  }
  
  .nav-links li {
    margin: 1rem 0;
    width: 100%;
  }
  
  .nav-links a {
    font-size: 1.125rem;
    padding: 0.5rem 0;
  }
  
  .mobile-menu-btn {
    display: flex;
  }
}
```

- [ ] **Step 3: Test mobile menu functionality**

Run: `npm run dev` and test both desktop and mobile views
Expected: Menu toggles properly on mobile, navbar displays correctly on desktop

- [ ] **Step 4: Commit**

```bash
git add frontend/src/pages/LandingPage.jsx frontend/src/pages/LandingPage.module.css
git commit -m "feat: add responsive navbar with mobile menu toggle"
```

## Task 4: Enhance Landing Page Gallery Section

**Files:**
- Modify: `frontend/src/pages/LandingPage.jsx`
- Modify: `frontend/src/pages/LandingPage.module.css`

**Interfaces:**
- Consumes: Existing gallery section structure
- Produces: Enhanced gallery with nature-inspired hover effects and animations

- [ ] **Step 1: Identify gallery section in LandingPage.jsx**
  
```javascript
// Keep existing gallery section but enhance with animations
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
```

- [ ] **Step 2: Enhance gallery styling with nature-inspired hover effects**
  
```css
/* Gallery Section */
.gallery-section {
  padding: 96px 5%;
  background-color: #F8FAF5;
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 3rem;
}

.gallery-item {
  position: relative;
  overflow: hidden;
  border-radius: 1rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  transition: transform 0.4s ease, box-shadow 0.4s ease;
}

.gallery-item:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 20px rgba(0, 0, 0, 0.1);
}

.gallery-item img {
  width: 100%;
  height: auto;
  display: block;
  transition: transform 0.6s ease;
}

.gallery-item:hover img {
  transform: scale(1.05);
}

.gallery-caption {
  padding: 1.5rem;
}

.gallery-caption-eyebrow {
  display: inline-block;
  background-color: #8FBC8F;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.875rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 0.75rem;
}

.gallery-caption h4 {
  margin: 0;
  font-size: 1.25rem;
  color: #2D3748;
  line-height: 1.4;
}

/* Add subtle leaf vein pattern as background */
.gallery-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%239CAF88' fill-opacity='0.05'%3E%3Cpath d='M30 0l30 30H0z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
  opacity: 0;
  transition: opacity 0.3s ease;
}

.gallery-item:hover::before {
  opacity: 1;
}

/* Animation classes */
.fade-up {
  opacity: 0;
  transform: translateY(30px);
  animation: fadeUp 0.6s ease forwards;
}

.fade-up.d1 {
  animation-delay: 0.2s;
}

.fade-up.d2 {
  animation-delay: 0.4s;
}

@keyframes fadeUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

- [ ] **Step 3: Test gallery hover effects and animations**

Run: `npm run dev` and verify gallery items animate on scroll and respond to hover
Expected: Images lift slightly on hover, zoom in, and show subtle leaf pattern overlay

- [ ] **Step 4: Commit**

```bash
git add frontend/src/pages/LandingPage.jsx frontend/src/pages/LandingPage.module.css
git commit -m "feat: enhance gallery section with nature-inspired hover effects"
```

## Task 5: Enhance Landing Page How It Works Section

**Files:**
- Modify: `frontend/src/pages/LandingPage.jsx`
- Modify: `frontend/src/pages/LandingPage.module.css`

**Interfaces:**
- Consumes: Existing how it works section structure
- Produces: Enhanced how it works section with animated progress indicators

- [ ] **Step 1: Identify how it works section in LandingPage.jsx**
  
```javascript
// Keep existing how it works section but enhance with step animations
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
        <div className="step-progress">
          <div className="progress-circle"></div>
        </div>
      </div>
      <div className="step fade-up d1">
        <div className="step-num">2</div>
        <div className="step-icon-wrap">🔍</div>
        <h3>Let AI Analyze</h3>
        <p>Our model scans the image for disease patterns, spots, and discoloration.</p>
        <div className="step-progress">
          <div className="progress-circle"></div>
        </div>
      </div>
      <div className="step fade-up d2">
        <div className="step-num">3</div>
        <div className="step-icon-wrap">💊</div>
        <h3>Get a Plan</h3>
        <p>Receive specific treatment, prevention, and care instructions you can follow today.</p>
        <div className="step-progress">
          <div className="progress-circle"></div>
        </div>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 2: Enhance how it works styling with animated progress indicators**
  
```css
/* How It Works Section */
.how-section {
  padding: 96px 5%;
  background-color: #ffffff;
}

.section-head {
  text-align: center;
  margin-bottom: 3rem;
}

.section-eyebrow {
  display: inline-block;
  background-color: #8FBC8F;
  color: white;
  padding: 0.375rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.875rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 1rem;
}

.how-section h2 {
  font-size: 2rem;
  font-weight: 700;
  color: #2D3748;
  margin-bottom: 1.5rem;
}

.how-section p {
  color: #4A5568;
  max-width: 600px;
  margin: 0 auto 2rem;
  line-height: 1.6;
}

.steps-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.step {
  text-align: center;
  padding: 1.5rem;
  background-color: #F8FAF5;
  border-radius: 1rem;
  transition: all 0.3s ease;
}

.step:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
  background-color: #ffffff;
}

.step-num {
  width: 3rem;
  height: 3rem;
  background-color: #8FBC8F;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.25rem;
  margin: 0 auto 1rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.step-icon-wrap {
  font-size: 2rem;
  margin-bottom: 1rem;
  opacity: 0.8;
}

.step h3 {
  margin: 0 0 1rem 0;
  font-size: 1.25rem;
  color: #2D3748;
}

.step p {
  color: #4A5568;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.step-progress {
  width: 4rem;
  height: 4rem;
  margin: 0 auto;
  position: relative;
}

.progress-circle {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  border: 3px solid #E2E8F0;
  position: relative;
}

.progress-circle::before {
  content: '';
  position: absolute;
  top: -3px;
  left: -3px;
  right: -3px;
  bottom: -3px;
  border: 3px solid transparent;
  border-top-color: #8FBC8F;
  border-radius: 50%;
  animation: spin 2s linear infinite;
}

/* Water filling animation for progress */
.step:nth-child(1) .progress-circle::before {
  border-top-color: #8FBC8F;
  animation: waterFill1 2s ease-in-out infinite;
}

.step:nth-child(2) .progress-circle::before {
  border-top-color: #E27D60;
  animation: waterFill2 2s ease-in-out infinite;
}

.step:nth-child(3) .progress-circle::before {
  border-top-color: #FDD835;
  animation: waterFill3 2s ease-in-out infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

@keyframes waterFill1 {
  0%, 100% { 
    clip-path: polygon(50% 0%, 100% 0%, 100% 50%, 50% 100%, 0% 50%, 0% 0%);
  }
  50% { 
    clip-path: polygon(50% 0%, 100% 0%, 100% 100%, 50% 100%, 0% 100%, 0% 0%);
  }
}

@keyframes waterFill2 {
  0%, 100% { 
    clip-path: polygon(50% 0%, 100% 0%, 100% 50%, 50% 100%, 0% 50%, 0% 0%);
  }
  50% { 
    clip-path: polygon(50% 0%, 100% 0%, 100% 100%, 50% 100%, 0% 100%, 0% 0%);
  }
}

@keyframes waterFill3 {
  0%, 100% { 
    clip-path: polygon(50% 0%, 100% 0%, 100% 50%, 50% 100%, 0% 50%, 0% 0%);
  }
  50% { 
    clip-path: polygon(50% 0%, 100% 0%, 100% 100%, 50% 100%, 0% 100%, 0% 0%);
  }
}

/* Animation classes */
.fade-up {
  opacity: 0;
  transform: translateY(30px);
  animation: fadeUp 0.6s ease forwards;
}

.fade-up.d1 {
  animation-delay: 0.2s;
}

.fade-up.d2 {
  animation-delay: 0.4s;
}

@keyframes fadeUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

- [ ] **Step 3: Test how it works section animations**

Run: `npm run dev` and verify steps animate on scroll and progress indicators animate
Expected: Steps fade in on scroll, progress circles show animated water filling effect

- [ ] **Step 4: Commit**

```bash
git add frontend/src/pages/LandingPage.jsx frontend/src/pages/LandingPage.module.css
git commit -m "feat: enhance how it works section with animated progress indicators"
```

## Task 6: Enhance Landing Page Scan Section

**Files:**
- Modify: `frontend/src/pages/LandingPage.jsx`
- Modify: `frontend/src/pages/LandingPage.module.css`

**Interfaces:**
- Consumes: Existing scan section structure
- Produces: Enhanced scan section with interactive leaf upload area and scanning animations

- [ ] **Step 1: Identify scan section in LandingPage.jsx**
  
```javascript
// Enhance existing scan section with interactive elements
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
          <div className="leaf-silhouette">
            {/* Will be replaced with animated leaf */}
          </div>
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
```

- [ ] **Step 2: Enhance scan section styling with interactive leaf upload and scanning effects**
  
```css
/* Scan Section */
.scan-section {
  padding: 96px 5%;
  background-color: #ffffff;
}

.container-narrow {
  max-width: 500px;
  margin: 0 auto;
}

.section-head {
  text-align: center;
  margin-bottom: 3rem;
}

.section-eyebrow {
  display: inline-block;
  background-color: #8FBC8F;
  color: white;
  padding: 0.375rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.875rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 1rem;
}

.scan-section h2 {
  font-size: 2rem;
  font-weight: 700;
  color: #2D3748;
  margin-bottom: 1.5rem;
}

.scan-section p {
  color: #4A5568;
  max-width: 400px;
  margin: 0 auto 2rem;
  line-height: 1.6;
}

/* Upload Area */
.upload-area {
  position: relative;
  border: 2px dashed #8FBC8F;
  border-radius: 1.5rem;
  height: 400px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #F8FAF5;
  transition: all 0.3s ease;
  overflow: hidden;
  cursor: pointer;
}

.upload-area:hover {
  border-color: #6D8D6D;
  background-color: #F0F7F0;
  transform: scale(1.02);
}

.upload-area.drag-active {
  border-color: #E27D60;
  background-color: #FFF8F5;
  transform: scale(1.03);
}

.upload-default {
  text-align: center;
  padding: 2rem;
}

.upload-illustration {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 1.5rem;
  position: relative;
}

.leaf-silhouette {
  width: 80px;
  height: 80px;
  background-color: rgba(143, 188, 143, 0.2);
  border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
  margin-bottom: 1rem;
  position: relative;
  overflow: hidden;
}

.leaf-silhouette::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: 
    radial-gradient(circle at 30% 30%, rgba(143, 188, 143, 0.3) 0%, transparent 40%),
    radial-gradient(circle at 70% 70%, rgba(143, 188, 143, 0.3) 0%, transparent 40%);
  animation: leafPulse 3s ease-in-out infinite;
}

.ring {
  width: 60px;
  height: 60px;
  border: 2px dashed #8FBC8F;
  border-radius: 50%;
  margin-bottom: 1rem;
  animation: ringRotate 4s linear infinite;
}

.upload-icon {
  font-size: 2rem;
  color: #8FBC8F;
  margin-bottom: 1rem;
  animation: pulse 2s ease-in-out infinite;
}

.upload-default h3 {
  margin: 0 0 0.5rem 0;
  font-size: 1.25rem;
  color: #2D3748;
}

.upload-default .sub {
  color: #6B7280;
  font-size: 0.875rem;
}

.format-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 1.5rem;
}

.format-pill {
  background-color: #E2E8F0;
  color: #4A5568;
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.75rem;
  font-weight: 500;
}

/* Preview State */
.preview-state {
  display: none;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.preview-img-wrap {
  width: 200px;
  height: 200px;
  border-radius: 1rem;
  overflow: hidden;
  margin-bottom: 1rem;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.preview-img-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.preview-meta {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.preview-meta i {
  font-size: 1.25rem;
  color: #6B7280;
}

.preview-meta div {
  text-align: left;
}

.preview-meta .name {
  font-weight: 600;
  color: #2D3748;
}

.preview-meta .size {
  color: #6B7280;
  font-size: 0.875rem;
}

.btn-green {
  background-color: #8FBC8F;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  font-size: 0.875rem;
  font-weight: 600;
  border-radius: 0.5rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s ease;
}

.btn-green:hover {
  background-color: #6D8D6D;
  transform: translateY(-2px);
}

.btn-green:active {
  transform: scale(0.98);
}

/* Scanning State */
.scanning-state {
  display: none;
  text-align: center;
}

.scan-visual {
  position: relative;
  width: 200px;
  height: 200px;
  margin-bottom: 2rem;
}

.scan-visual img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 1rem;
}

.scan-beam {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(90deg, transparent, #8FBC8F, transparent);
  animation: beamMove 2s linear infinite;
}

.scan-grid-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("data:image/svg+xml,%3Csvg width='20' height='20' viewBox='0 0 20 20' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%238FBC8F' fill-opacity='0.05'%3E%3Cpath d='M0 0h20v20H0z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
  animation: gridMove 4s linear infinite;
}

.scan-progress-track {
  width: 100%;
  height: 8px;
  background-color: #E2E8F0;
  border-radius: 4px;
  overflow: hidden;
  margin-bottom: 1.5rem;
}

.scan-progress-fill {
  height: 100%;
  background: linear-gradient(to right, #8FBC8F, #E27D60, #FDD835);
  width: 0;
  transition: width 0.4s ease;
}

.scan-text {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

#scanMsg {
  font-size: 1rem;
  color: #4A5568;
}

.dots {
  display: flex;
  gap: 0.25rem;
}

.dots span {
  width: 4px;
  height: 4px;
  background-color: #6B7280;
  border-radius: 50%;
  animation: dotPulse 1.5s ease-in-out infinite;
}

.dots span:nth-child(2) {
  animation-delay: 0.2s;
}

.dots span:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes leafPulse {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 0.5; }
}

@keyframes ringRotate {
  to { transform: rotate(360deg); }
}

@keyframes beamMove {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
}

@keyframes gridMove {
  0% { transform: translate(0, 0); }
  100% { transform: translate(-20px, -20px); }
}

@keyframes dotPulse {
  0%, 100% { opacity: 0.3; transform: scale(0.8); }
  50% { opacity: 1; transform: scale(1.2); }
}

/* Responsive */
@media (max-width: 480px) {
  .scan-section {
    padding: 64px 5%;
  }
  
  .upload-area {
    height: 300px;
  }
  
  .scan-visual {
    width: 150px;
    height: 150px;
  }
}
```

- [ ] **Step 3: Test scan section interactions**

Run: `npm run dev` and test upload area hover effects, drag interactions, and scanning animations
Expected: Upload area responds to hover/drag, scanning animation shows moving beam and grid, progress bar fills

- [ ] **Step 4: Commit**

```bash
git add frontend/src/pages/LandingPage.jsx frontend/src/pages/LandingPage.module.css
git commit -m "feat: enhance scan section with interactive leaf upload and scanning animations"
```

## Task 7: Enhance Landing Page Results Section

**Files:**
- Modify: `frontend/src/pages/LandingPage.jsx`
- Modify: `frontend/src/pages/LandingPage.module.css`

**Interfaces:**
- Consumes: Existing results section structure
- Produces: Enhanced results section with nature-inspired emergence animation and diagnostic display

- [ ] **Step 1: Identify results section in LandingPage.jsx**
  
```javascript
// Enhance existing results section with emergence animations
{/*  Results  */}
<section className="results-section" id="results">
  <div className="container">
    <div className="result-header">
      <div className="check-circle">
        <i className="fas fa-seedling"></i>
      </div>
      <h2>Diagnosis complete</h2>
      <p>Here's what we found and what to do next.</p>
    </div>

    <div className="diagnosis-box" id="diagnosisBox">
      <div className="diagnosis-top">
        <div className="diagnosis-icon" id="dIcon">🌿</div>
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

    <div className="advice-title"><i className="fas fa-leaf"></i> Recommended Actions</div>

    <div className="advice-grid" id="adviceGrid">
      <div className="advice-card fade-up">
        <div className="advice-card-head">
          <div className="advice-card-icon treat"><i className="fas fa-flask"></i></div>
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
          <div className="advice-card-icon water"><i className="fas fa-tint"></i></div>
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
```

- [ ] **Step 2: Enhance results section styling with nature-inspired emergence effects**
  
```css
/* Results Section */
.results-section {
  padding: 96px 5%;
  background-color: #ffffff;
}

.result-header {
  text-align: center;
  margin-bottom: 3rem;
}

.result-header i {
  font-size: 2.5rem;
  color: #8FBC8F;
  background-color: #F0F7F0;
  width: 3rem;
  height: 3rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1rem;
  animation: seedlingGrow 1.5s ease-out;
}

.result-header h2 {
  font-size: 2rem;
  font-weight: 700;
  color: #2D3748;
  margin-bottom: 1.5rem;
}

.result-header p {
  color: #4A5568;
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.6;
}

.diagnosis-box {
  background-color: #F8FAF5;
  border-radius: 1.5rem;
  padding: 2rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
  position: relative;
  overflow: hidden;
  animation: diagnosisEmergence 0.8s ease-out;
}

.diagnosis-box::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(to right, #8FBC8F, #E27D60, #FDD835);
  animation: diagnosisGlow 2s ease-in-out infinite;
}

.diagnosis-top {
  display: flex;
  align-items: center;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.diagnosis-icon {
  font-size: 2.5rem;
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #E2E8F0;
  border-radius: 50%;
  animation: iconFloat 3s ease-in-out infinite;
}

.diagnosis-info {
  flex: 1;
  min-width: 150px;
}

.diagnosis-info h3 {
  margin: 0 0 0.5rem 0;
  font-size: 1.5rem;
  font-weight: 600;
  color: #2D3748;
}

.diagnosis-info .latin {
  font-size: 0.875rem;
  color: #6B7280;
  font-style: italic;
}

.severity-chip {
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.875rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.severity-chip.low {
  background-color: #C8E6C9;
  color: #2E7D32;
}

.severity-chip.medium {
  background-color: #FFF9C4;
  color: #F57F17;
}

.severity-chip.high {
  background-color: #FFCDD2;
  color: #C62828;
}

.confidence-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.confidence-labels {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.confidence-labels span {
  font-size: 0.875rem;
  font-weight: 500;
}

.confidence-labels span:first-child {
  color: #4A5568;
}

.confidence-labels span:last-child {
  font-weight: 600;
  color: #2D3748;
}

.confidence-track {
  width: 100%;
  height: 8px;
  background-color: #E2E8F0;
  border-radius: 4px;
  overflow: hidden;
  margin-bottom: 0.5rem;
}

.confidence-fill {
  height: 100%;
  background: linear-gradient(to right, #8FBC8F, #E27D60, #FDD835);
  width: 94%; /* This will be dynamically set */
  border-radius: 4px;
  transition: width 1.2s ease;
}

.diagnosis-desc {
  color: #4A5568;
  line-height: 1.7;
  margin-bottom: 2rem;
  font-size: 0.9375rem;
}

.advice-title {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 1.5rem;
  color: #2D3748;
  font-size: 1.25rem;
  font-weight: 600;
}

.advice-title i {
  font-size: 1.5rem;
  color: #8FBC8F;
}

.advice-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.advice-card {
  background-color: #ffffff;
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  transition: all 0.3s ease;
  border: 1px solid #F0F0F0;
}

.advice-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.08);
  border-color: #DFE9FF;
}

.advice-card-head {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
}

.advice-card-icon {
  width: 2.5rem;
  height: 2.5rem;
  background-color: #E2E8F0;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 1rem;
}

.advice-card-icon.treat {
  background-color: #FFEAA7;
}

.advice-card-icon.prevent {
  background-color: #BBDEFb;
}

.advice-card-icon.feed {
  background-color: #C8E6C9;
}

.advice-card-icon.water {
  background-color: #B3E5FC;
}

.advice-card-icon h4 {
  margin: 0;
  font-size: 1.125rem;
  font-weight: 600;
  color: #2D3748;
}

.advice-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.advice-list li {
  padding: 0.5rem 0;
  border-bottom: 1px solid #F0F0F0;
  color: #4A5568;
  font-size: 0.875rem;
}

.advice-list li:last-child {
  border-bottom: none;
}

.reset-wrap {
  text-align: center;
  margin-top: 2rem;
}

.btn-outline {
  border: 2px solid #8FBC8F;
  color: #8FBC8F;
  background: transparent;
  padding: 0.75rem 1.5rem;
  font-size: 0.875rem;
  font-weight: 600;
  border-radius: 0.5rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s ease;
}

.btn-outline:hover {
  background-color: rgba(143, 188, 143, 0.1);
  transform: translateY(-2px);
}

.btn-outline:active {
  transform: scale(0.98);
}

/* Animations */
@keyframes seedlingGrow {
  0% { transform: scale(0.3) rotate(-30deg); opacity: 0; }
  50% { transform: scale(1.1) rotate(10deg); }
  70% { transform: scale(0.9) rotate(-5deg); }
  100% { transform: scale(1) rotate(0deg); opacity: 1; }
}

@keyframes diagnosisEmergence {
  0% { opacity: 0; transform: translateY(30px); }
  100% { opacity: 1; transform: translateY(0); }
}

@keyframes diagnosisGlow {
  0%, 100% { opacity: 0.5; }
  50% { opacity: 0.8; }
}

@keyframes iconFloat {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
}

/* Animation classes */
.fade-up {
  opacity: 0;
  transform: translateY(30px);
  animation: fadeUp 0.6s ease forwards;
}

.fade-up.d1 {
  animation-delay: 0.2s;
}

.fade-up.d2 {
  animation-delay: 0.4s;
}

.fade-up.d3 {
  animation-delay: 0.6s;
}

@keyframes fadeUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Hide results section by default */
.results-section {
  display: none;
}

/* When results are active, show the section */
.results-section.active {
  display: block;
}
```

- [ ] **Step 3: Test results section animations and styling**

Run: `npm run dev` and verify results section appears with appropriate animations when activated
Expected: Results section emerges with seedling animation, diagnosis box grows in, confidence fill animates, icons float gently

- [ ] **Step 4: Commit**

```bash
git add frontend/src/pages/LandingPage.jsx frontend/src/pages/LandingPage.module.css
git commit -m "feat: enhance results section with nature-inspired emergence effects"
```

## Task 8: Enhance Landing Page Features Section

**Files:**
- Modify: `frontend/src/pages/LandingPage.jsx`
- Modify: `frontend/src/pages/LandingPage.module.css`

**Interfaces:**
- Consumes: Existing features section structure
- Produces: Enhanced features section with animated feature cards and nature-inspired icons

- [ ] **Step 1: Identify features section in LandingPage.jsx**
  
```javascript
// Enhance existing features section with animated cards
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
```

- [ ] **Step 2: Enhance features section styling with animated cards and nature-inspired elements**
  
```css
/* Features Section */
.features-section {
  padding: 96px 5%;
  background-color: #F8FAF5;
}

.section-head {
  text-align: center;
  margin-bottom: 3rem;
}

.section-eyebrow {
  display: inline-block;
  background-color: #8FBC8F;
  color: white;
  padding: 0.375rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.875rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 1rem;
}

.features-section h2 {
  font-size: 2rem;
  font-weight: 700;
  color: #2D3748;
  margin-bottom: 1.5rem;
}

.features-section p {
  color: #4A5568;
  max-width: 600px;
  margin: 0 auto 2rem;
  line-height: 1.6;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.feature-card {
  background-color: #ffffff;
  border-radius: 1.5rem;
  padding: 2rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  transition: all 0.4s ease;
  position: relative;
  overflow: hidden;
  border: 1px solid #F0F0F0;
}

.feature-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 20px rgba(0, 0, 0, 0.08);
  border-color: #DFE9FF;
}

.feature-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background: linear-gradient(to bottom, #8FBC8F, #E27D60, #FDD835);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.feature-card:hover::before {
  opacity: 1;
}

.feature-card-icon {
  width: 3rem;
  height: 3rem;
  background-color: #E2E8F0;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1.5rem;
  font-size: 1.5rem;
  transition: all 0.3s ease;
}

.feature-card-icon:hover {
  transform: scale(1.1) rotate(5deg);
  background-color: #BBDEFb;
}

.feature-card h3 {
  margin: 0 0 1rem 0;
  font-size: 1.25rem;
  font-weight: 600;
  color: #2D3748;
}

.feature-card p {
  color: #4A5568;
  line-height: 1.7;
}

/* Add subtle nature patterns to feature cards */
.feature-card:nth-child(1)::after {
  content: '';
  position: absolute;
  bottom: -10px;
  right: -10px;
  width: 60px;
  height: 60px;
  background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M30 0L45 30L30 60L15 30Z' fill='%238FBC8F' fill-opacity='0.1'/%3E%3C/svg%3E");
  opacity: 0;
  transition: opacity 0.3s ease;
}

.feature-card:nth-child(1):hover::after {
  opacity: 0.5;
}

.feature-card:nth-child(2)::after {
  content: '';
  position: absolute;
  bottom: -15px;
  left: -15px;
  width: 50px;
  height: 50px;
  background: url("data:image/svg+xml,%3Csvg width='50' height='50' viewBox='0 0 50 50' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='25' cy='25' r='20' fill='%23E27D60' fill-opacity='0.1'/%3E%3C/svg%3E");
  opacity: 0;
  transition: opacity 0.3s ease;
}

.feature-card:nth-child(2):hover::after {
  opacity: 0.4;
}

.feature-card:nth-child(3)::after {
  content: '';
  position: absolute;
  top: -10px;
  right: -10px;
  width: 40px;
  height: 40px;
  background: url("data:image/svg+xml,%3Csvg width='40' height='40' viewBox='0 0 40 40' xmlns='http://www.w3.org/2000/svg'%3E%3Crect width='40' height='40' fill='%23FDD835' fill-opacity='0.1'/%3E%3C/svg%3E");
  opacity: 0;
  transition: opacity 0.3s ease;
}

.feature-card:nth-child(3):hover::after {
  opacity: 0.3;
}

/* Repeat patterns for remaining cards */
.feature-card:nth-child(4)::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: -5px;
  width: 30px;
  height: 30px;
  background: url("data:image/svg+xml,%3Csvg width='30' height='30' viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 0h30v30H0z' fill='%238FBC8F' fill-opacity='0.05'/%3E%3C/svg%3E");
  opacity: 0;
  transition: opacity 0.3s ease;
}

.feature-card:nth-child(4):hover::after {
  opacity: 0.2;
}

.feature-card:nth-child(5)::after {
  content: '';
  position: absolute;
  top: -5px;
  right: -5px;
  width: 35px;
  height: 35px;
  background: url("data:image/svg+xml,%3Csvg width='35' height='35' viewBox='0 0 35 35' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 0h35v35H0z' fill='%23E27D60' fill-opacity='0.05'/%3E%3C/svg%3E");
  opacity: 0;
  transition: opacity 0.3s ease;
}

.feature-card:nth-child(5):hover::after {
  opacity: 0.2;
}

.feature-card:nth-child(6)::after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: -8px;
  width: 45px;
  height: 45px;
  background: url("data:image/svg+xml,%3Csvg width='45' height='45' viewBox='0 0 45 45' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 0h45v45H0z' fill='%23FDD835' fill-opacity='0.05'/%3E%3C/svg%3E");
  opacity: 0;
  transition: opacity 0.3s ease;
}

.feature-card:nth-child(6):hover::after {
  opacity: 0.2;
}

/* Animation classes */
.fade-up {
  opacity: 0;
  transform: translateY(30px);
  animation: fadeUp 0.6s ease forwards;
}

.fade-up.d1 {
  animation-delay: 0.2s;
}

.fade-up.d2 {
  animation-delay: 0.4s;
}

.fade-up.d3 {
  animation-delay: 0.6s;
}

.fade-up.d4 {
  animation-delay: 0.8s;
}

.fade-up.d5 {
  animation-delay: 1.0s;
}

.fade-up.d6 {
  animation-delay: 1.2s;
}

@keyframes fadeUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Feature card entrance stagger */
.feature-card {
  animation-fill-mode: both;
}
```

- [ ] **Step 3: Test features section animations and hover effects**

Run: `npm run dev` and verify feature cards animate on scroll and respond to hover
Expected: Cards fade in with staggered delay, lift slightly on hover, show growing side border, and icons animate slightly

- [ ] **Step 4: Commit**

```bash
git add frontend/src/pages/LandingPage.jsx frontend/src/pages/LandingPage.module.css
git commit -m "feat: enhance features section with animated cards and nature-inspired elements"
```

## Task 9: Enhance Landing Page Ticker, CTA, and Footer Sections

**Files:**
- Modify: `frontend/src/pages/LandingPage.jsx`
- Modify: `frontend/src/pages/LandingPage.module.css`

**Interfaces:**
- Consumes: Existing ticker, CTA, and footer sections
- Produces: Enhanced sections with subtle animations and nature-inspired styling

- [ ] **Step 1: Identify ticker, CTA, and footer sections in LandingPage.jsx**
  
```javascript
// Enhance ticker section with moving plant elements
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
```

- [ ] **Step 2: Enhance ticker, CTA, and footer sections with subtle animations**
  
```css
/* Ticker Section */
.ticker-section {
  background-color: #ffffff;
  overflow: hidden;
  padding: 2rem 5%;
  border-top: 1px solid #E2E8F0;
  border-bottom: 1px solid #E2E8F0;
}

.ticker-track {
  display: flex;
  width: max-content;
  animation: tickerMove 20s linear infinite;
}

.ticker-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  white-space: nowrap;
  font-size: 1rem;
  color: #4A5568;
}

.ticker-item .emoji {
  font-size: 1.25rem;
  animation: emojiFloat 3s ease-in-out infinite;
}

.ticker-item:nth-child(2n) .emoji {
  animation-delay: 1.5s;
}

@keyframes tickerMove {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

@keyframes emojiFloat {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-5px); }
}

/* CTA Section */
.cta-section {
  text-align: center;
  padding: 96px 5%;
  background-color: #F0F7F0;
}

.cta-section h2 {
  font-size: 2rem;
  font-weight: 700;
  color: #2D3748;
  margin-bottom: 1.5rem;
  position: relative;
  display: inline-block;
}

.cta-section h2::after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 4px;
  background-color: #8FBC8F;
  transition: width 0.3s ease;
}

.cta-section h2:hover::after {
  width: 50%;
}

.cta-section h2 .serif {
  font-family: 'Georgia', serif;
  font-style: italic;
}

.cta-section p {
  color: #4A5568;
  max-width: 600px;
  margin: 0 auto 2rem;
  line-height: 1.6;
}

.btn-white {
  background-color: white;
  color: #2D3748;
  border: 2px solid #2D3748;
  padding: 0.75rem 1.5rem;
  font-size: 0.875rem;
  font-weight: 600;
  border-radius: 0.5rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s ease;
}

.btn-white:hover {
  background-color: #2D3748;
  color: white;
  transform: translateY(-2px);
}

.btn-white:active {
  transform: scale(0.98);
}

/* Footer Section */
footer {
  background-color: #2D3748;
  color: #E2E8F0;
  padding: 3rem 5%;
  margin-top: 4rem;
}

.footer-inner {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 1.5rem;
}

.footer-brand {
  font-size: 1.5rem;
  font-weight: 700;
  color: #8FBC8F;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.footer-brand i {
  font-size: 2rem;
}

.footer-links {
  display: flex;
  gap: 1.5rem;
  flex-wrap: wrap;
  justify-content: center;
}

.footer-links a {
  color: #E2E8F0;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s ease;
  position: relative;
}

.footer-links a:hover {
  color: white;
}

.footer-links a::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 0;
  height: 2px;
  background-color: #8FBC8F;
  transition: width 0.3s ease;
}

.footer-links a:hover::after {
  width: 100%;
}

.footer-copy {
  font-size: 0.875rem;
  color: #A0AEC0;
  margin-top: 1rem;
}

/* Add subtle footer animation */
footer {
  position: relative;
  overflow: hidden;
}

footer::before {
  content: '';
  position: absolute;
  top: -50%;
  left: 0;
  width: 100%;
  height: 100%;
  background: url("data:image/svg+xml,%3Csvg width='100' height='100' viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 0 L100 100 M100 0 L0 100' stroke='%234A5568' stroke-width='1' stroke-opacity='0.05'/%3E%3C/svg%3E");
  animation: footerLines 20s linear infinite;
}

@keyframes footerLines {
  0% { transform: translateY(-100%); }
  100% { transform: translateY(0); }
}

/* Animation classes */
.fade-up {
  opacity: 0;
  transform: translateY(30px);
  animation: fadeUp 0.6s ease forwards;
}

.fade-up.d1 {
  animation-delay: 0.2s;
}

.fade-up.d2 {
  animation-delay: 0.4s;
}

/* Apply fade-up to sections as they enter viewport */
.ticker-section,
.cta-section,
footer {
  opacity: 0;
  transform: translateY(30px);
}

.ticker-section.visible,
.cta-section.visible,
footer.visible {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
```

- [ ] **Step 3: Test ticker, CTA, and footer animations**

Run: `npm run dev` and verify ticker moves smoothly, CTA header animates on hover, and footer shows subtle line animation
Expected: Ticker scrolls continuously, CTA header underline expands on hover, footer shows slow-moving diagonal lines

- [ ] **Step 4: Commit**

```bash
git add frontend/src/pages/LandingPage.jsx frontend/src/pages/LandingPage.module.css
git commit -m "feat: enhance ticker, cta, and footer sections with subtle animations"
```

## Task 10: Enhance Diagnose Page Layout and Styling

**Files:**
- Modify: `frontend/src/pages/DiagnosePage.jsx`
- Modify: `frontend/src/pages/DiagnosePage.module.css`

**Interfaces:**
- Consumes: Existing diagnose page structure
- Produces: Enhanced diagnose page with nature-inspired layout and styling

- [ ] **Step 1: Update DiagnosePage.jsx with improved layout**
  
```javascript
import React, { useState } from 'react';
import styles from './DiagnosePage.module.css';
import ImageUpload from '../components/ImageUpload';
import DiagnosisResult from '../components/DiagnosisResult';
import AdvisoryPanel from '../components/AdvisoryPanel';
import { uploadImageForDiagnosis, getAdvisory } from '../api';
import { useNavigate } from 'react-router-dom';
import { pendingFile, setPendingFile } from '../sharedState';
import { fadeInUp } from '../utils/animations';

export default function DiagnosePage() {
  const navigate = useNavigate();
  const [file, setFile] = useState(pendingFile || null);
  const [location, setLocation] = useState('');
  
  // Clear the global pending file so a refresh doesn't keep grabbing it
  React.useEffect(() => {
    if (pendingFile) setPendingFile(null);
  }, []);
  
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);
  
  const [diagnosisData, setDiagnosisData] = useState(null);
  const [advisoryData, setAdvisoryData] = useState(null);

  const handleAnalyse = async () => {
    if (!file) return;
    
    setLoading(true);
    setError(false);
    setDiagnosisData(null);
    setAdvisoryData(null);

    try {
      const diagRes = await uploadImageForDiagnosis(file);
      setDiagnosisData(diagRes);
      
      const advRes = await getAdvisory(diagRes.disease, location);
      setAdvisoryData(advRes);
      
    } catch (err) {
      setError(true);
    } finally {
      setLoading(false);
    }
  };

  const startChat = () => {
    const sessionId = Math.random().toString(36).substring(7);
    navigate(`/chat/${sessionId}`);
  };

  return (
    <div className={`${styles.container} animate-fade-in`}>
      <div className={`${styles.leftPanel} animate-slide-in-left`}>
        <div className="card">
          <h2>Diagnose Crop</h2>
          <ImageUpload file={file} setFile={setFile} />
          
          <div className={styles.inputGroup}>
            <label>Location (Optional)</label>
            <input 
              type="text" 
              placeholder="e.g. Pune, Maharashtra" 
              value={location}
              onChange={(e) => setLocation(e.target.value)}
              className={styles.input}
            />
          </div>
          
          <button 
            className={`${btn-primary} ${styles.analyseBtn} animate-pulse-on-hover`}
            onClick={handleAnalyse}
            disabled={!file || loading}
          >
            {loading ? 'Analysing...' : 'Analyse'}
          </button>
        </div>
      </div>
      
      <div className={`${styles.rightPanel} animate-slide-in-right`}>
        {!loading && !error && !diagnosisData && (
          <div className={styles.placeholder} animate-fade-in-delayed>
            Upload an image and click Analyse to see results here.
          </div>
        )}
        
        {loading && (
          <div className={styles.skeleton} animate-pulse>
            <div className={styles.skeletonImg}></div>
            <div className={styles.skeletonText}></div>
            <div className={styles.skeletonText}></div>
            <div className={styles.skeletonText}></div>
          </div>
        )}
        
        {error && (
          <div className={styles.errorState} animate-shake-on-error>
            <p>Couldn't reach the server — try again.</p>
            <button className="btn-primary" onClick={handleAnalyse}>Retry</button>
          </div>
        )}
        
        {diagnosisData && !loading && (
          <div className={styles.results} animate-fade-in-delayed>
            <DiagnosisResult data={diagnosisData} />
            {advisoryData ? (
              <>
                <AdvisoryPanel data={advisoryData} animate-fade-in-delayed/>
                <button className={`${btn-primary} ${styles.chatBtn} animate-pulse-on-hover`} onClick={startChat}>
                  Ask a follow-up question
                </button>
              </>
            ) : (
              <p>Loading advisory...</p>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
```

- [ ] **Step 2: Add animation utility imports and CSS classes**
  
```javascript
// Add to existing imports in DiagnosePage.jsx
import { fadeInUp } from '../utils/animations';
```

- [ ] **Step 3: Enhance DiagnosePage.module.css with nature-inspired styling**
  
```css
/* Diagnose Page Styles */
.container {
  display: flex;
  gap: 2rem;
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
}

.leftPanel {
  flex: 0 0 350px;
}

.rightPanel {
  flex: 1;
}

/* Card Styles */
.card {
  background-color: #ffffff;
  border-radius: 1.5rem;
  padding: 2rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  border: 1px solid #F0F0F0;
  position: relative;
  overflow: hidden;
}

.card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background: linear-gradient(to bottom, #8FBC8F, #E27D60, #FDD835);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.card:hover::before {
  opacity: 1;
}

.card h2 {
  margin: 0 0 1.5rem 0;
  font-size: 1.5rem;
  font-weight: 600;
  color: #2D3748;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.card h2::before {
  content: '🌱';
  font-size: 1.75rem;
}

/* Input Group Styles */
.inputGroup {
  margin-bottom: 1.5rem;
}

.inputGroup label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
  color: #4A5568;
}

.inputGroup input {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #E2E8F0;
  border-radius: 0.5rem;
  font-size: 0.875rem;
  transition: all 0.2s ease;
}

.inputGroup input:focus {
  outline: none;
  border-color: #8FBC8F;
  box-shadow: 0 0 0 3px rgba(143, 188, 143, 0.2);
}

.inputGroup input::placeholder {
  color: #9CA3AF;
}

/* Button Styles */
.btn-primary {
  background-color: #8FBC8F;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  font-size: 0.875rem;
  font-weight: 600;
  border-radius: 0.5rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
}

.btn-primary::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.2),
    transparent
  );
  transition: all 0.5s ease;
}

.btn-primary:hover::before {
  left: 100%;
}

.btn-primary:hover {
  background-color: #6D8D6D;
  transform: translateY(-2px);
}

.btn-primary:active {
  transform: scale(0.98);
}

/* Placeholder Styles */
.placeholder {
  text-align: center;
  padding: 3rem;
  color: #6B7280;
  font-size: 1.125rem;
}

/* Skeleton Styles */
.skeleton {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.skeletonImg {
  width: 100%;
  height: 200px;
  background-color: #E2E8F0;
  border-radius: 1rem;
}

.skeletonText {
  height: 1.5rem;
  background-color: #E2E8F0;
  border-radius: 0.5rem;
}

.skeletonText:first-child {
  width: 60%;
}

.skeletonText:nth-child(2) {
  width: 40%;
}

.skeletonText:nth-child(3) {
  width: 70%;
}

/* Error State Styles */
.errorState {
  text-align: center;
  padding: 2rem;
  background-color: #FFF0F0;
  border: 1px solid #FECACA;
  border-radius: 1rem;
}

.errorState p {
  color: #991B1B;
  margin-bottom: 1.5rem;
}

/* Results Styles */
.results {
  margin-top: 2rem;
}

/* Chat Button Styles */
.chatBtn {
  margin-top: 1.5rem;
  width: 100%;
  justify-content: center;
}

/* Animation Classes */
.animate-fade-in {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.6s ease forwards;
}

.animate-slide-in-left {
  opacity: 0;
  transform: translateX(-30px);
  animation: slideInLeft 0.6s ease forwards;
}

.animate-slide-in-right {
  opacity: 0;
  transform: translateX(30px);
  animation: slideInRight 0.6s ease forwards;
}

.animate-fade-in-delayed {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.6s ease forwards 0.2s;
}

.animate-pulse-on-hover {
  transition: all 0.2s ease;
}

.animate-pulse-on-hover:hover {
  transform: scale(1.02);
}

.animate-pulse {
  animation: pulse 2s ease-in-out infinite;
}

.animate-shake-on-error {
  animation: shake 0.6s ease-in-out;
}

/* Keyframes */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateX(30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.03); }
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  20% { transform: translateX(-5px); }
  40% { transform: translateX(5px); }
  60% { transform: translateX(-5px); }
  80% { transform: translateX(5px); }
  100% { transform: translateX(0); }
}

/* Responsive Design */
@media (max-width: 768px) {
  .container {
    flex-direction: column;
  }
  
  .leftPanel {
    flex: 0 0 auto;
    width: 100%;
    margin-bottom: 2rem;
  }
  
  .rightPanel {
    flex: 1;
    width: 100%;
  }
}
```

- [ ] **Step 3: Test diagnose page layout and animations**

Run: `npm run dev` and navigate to /diagnose to verify layout and animations
Expected: Page loads with fade-in animation, panels slide in from sides, buttons respond to hover, form fields animate on focus

- [ ] **Step 4: Commit**

```bash
git add frontend/src/pages/DiagnosePage.jsx frontend/src/pages/DiagnosePage.module.css
git commit -m "feat: enhance diagnose page with nature-inspired layout and animations"
```

## Task 11: Enhance Chat Page Layout and Styling

**Files:**
- Modify: `frontend/src/pages/ChatPage.jsx`
- Modify: `frontend/src/pages/ChatPage.module.css`

**Interfaces:**
- Consumes: Existing chat page structure
- Produces: Enhanced chat page with nature-inspired styling and animations

- [ ] **Step 1: Update ChatPage.jsx with improved layout and animations**
  
```javascript
import React, { useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import styles from './ChatPage.module.css';
import ChatBubble from '../components/ChatBubble';
import ChatInput from '../components/ChatInput';
import { sendChatMessage } from '../api';
import { fadeInUp } from '../utils/animations';

export default function ChatPage() {
  const { sessionId } = useParams();
  const [messages, setMessages] = useState([
    { role: 'assistant', text: 'Hello! Do you have any follow-up questions about the diagnosis or treatment?' }
  ]);
  const [loading, setLoading] = useState(false);

  const handleSend = async (text) => {
    if (!text.trim()) return;
    
    const newMessages = [...messages, { role: 'user', text }];
    setMessages(newMessages);
    setLoading(true);

    try {
      const res = await sendChatMessage(sessionId, text);
      setMessages([...newMessages, { role: 'assistant', text: res.reply }]);
    } catch (err) {
      setMessages([...newMessages, { role: 'assistant', text: "Sorry, I'm having trouble connecting right now." }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={`${styles.container} animate-fade-in`}>
      <header className={styles.header} animate-slide-down>
        <Link to="/diagnose" className={styles.backLink} animate-pulse-on-hover>&larr; Back to diagnosis</Link>
        <h2>Ask KisanAI</h2>
      </header>
      
      <div className={`${styles.chatArea} animate-fade-in-delayed`}>
        {messages.map((m, idx) => (
          <ChatBubble key={idx} role={m.role} text={m.text} className={`${m.role === 'user' ? 'animate-slide-in-right' : 'animate-slide-in-left'}`} />
        ))}
        {loading && <div className={styles.loading} animate-pulse>KisanAI is typing...</div>}
      </div>
      
      <ChatInput onSend={handleSend} disabled={loading} className={`${styles.chatInput} animate-fade-in-delayed`} />
    </div>
  );
}
```

- [ ] **Step 2: Enhance ChatPage.module.css with nature-inspired styling**
  
```css
/* Chat Page Styles */
.container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  max-width: 600px;
  margin: 0 auto;
  padding: 1rem;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border-bottom: 1px solid #E2E8F0;
  background-color: #ffffff;
}

.backLink {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #4A5568;
  text-decoration: none;
  font-weight: 500;
}

.backLink:hover {
  color: #2D3748;
}

.header h2 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 600;
  color: #2D3748;
}

.chatArea {
  flex: 1;
  overflow-y: auto;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.loading {
  text-align: center;
  padding: 1.5rem;
  color: #6B7280;
  font-style: italic;
}

.chatInput {
  padding: 1rem;
  border-top: 1px solid #E2E8F0;
  background-color: #ffffff;
}

/* Animation Classes */
.animate-fade-in {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.6s ease forwards;
}

.animate-slide-down {
  opacity: 0;
  transform: translateY(-20px);
  animation: slideDown 0.6s ease forwards;
}

.animate-fade-in-delayed {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.6s ease forwards 0.2s;
}

.animate-slide-in-left {
  opacity: 0;
  transform: translateX(-30px);
  animation: slideInLeft 0.6s ease forwards;
}

.animate-slide-in-right {
  opacity: 0;
  transform: translateX(30px);
  animation: slideInRight 0.6s ease forwards;
}

.animate-pulse-on-hover {
  transition: all 0.2s ease;
}

.animate-pulse-on-hover:hover {
  transform: scale(1.02);
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateX(30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Responsive Design */
@media (max-width: 480px) {
  .container {
    padding: 0.5rem;
  }
  
  .header {
    padding: 0.75rem;
  }
  
  .chatArea {
    padding: 1rem;
  }
}
```

- [ ] **Step 3: Test chat page layout and animations**

Run: `npm run dev` and navigate to a chat page to verify layout and animations
Expected: Page loads with fade-in animation, header slides down, chat bubbles slide in from sides, input fades in

- [ ] **Step 4: Commit**

```bash
git add frontend/src/pages/ChatPage.jsx frontend/src/pages/ChatPage.module.css
git commit -m "feat: enhance chat page with nature-inspired layout and animations"
```

## Task 12: Enhance Image Upload Component

**Files:**
- Modify: `frontend/src/components/ImageUpload.jsx`
- Modify: `frontend/src/components/ImageUpload.module.css`

**Interfaces:**
- Consumes: Existing image upload functionality
- Produces: Enhanced image upload with leaf-inspired interactions and animations

- [ ] **Step 1: Update ImageUpload.jsx with improved interactions**
  
```javascript
import React, { useRef, useState } from 'react';
import styles from './ImageUpload.module.css';
import { pulse, leafUnfold } from '../utils/animations';

export default function ImageUpload({ file, setFile }) {
  const fileInputRef = useRef(null);
  const [preview, setPreview] = useState(null);
  const [dragActive, setDragActive] = useState(false);
  const [hover, setHover] = useState(false);

  const handleFile = (selectedFile) => {
    if (selectedFile && (selectedFile.type === 'image/jpeg' || selectedFile.type === 'image/png')) {
      if (selectedFile.size > 10 * 1024 * 1024) {
        alert("File is too large (max 10MB)");
        return;
      }
      setFile(selectedFile);
      setPreview(URL.createObjectURL(selectedFile));
    } else {
      alert("Please upload a valid JPG or PNG image.");
    }
  };

  const onDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  };

  const onDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFile(e.dataTransfer.files[0]);
    }
  };

  const onFileSelect = (e) => {
    if (e.target.files && e.target.files[0]) {
      handleFile(e.target.files[0]);
    }
  };

  return (
    <div 
      className={`${styles.uploadZone} ${dragActive ? styles.dragActive : ''} ${hover ? styles.hover : ''}`}
      onDragEnter={onDrag}
      onDragLeave={onDrag}
      onDragOver={onDrag}
      onDrop={onDrop}
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      onClick={() => fileInputRef.current.click()}
    >
      <input 
        type="file" 
        ref={fileInputRef} 
        onChange={onFileSelect} 
        accept="image/jpeg, image/png" 
        style={{ display: 'none' }} 
      />
      
      {preview ? (
        <img 
          src={preview} 
          alt="Preview" 
          className={styles.previewImage}
          className={`${styles.previewImage} animate-fade-in`}
        />
      ) : (
        <div className={styles.uploadPrompt}>
          <div className={`${styles.icon} animate-pulse`}>🌱</div>
          <p className=${styles.promptText} animate-fade-in-delayed>Drop your crop photo here</p>
          <span className={styles.muted} animate-fade-in-delayed>or click to browse</span>
          <div className=${styles.leafDecoration} animate-leaf-grow>
            <div className="leaf-stem"></div>
            <div className="leaf-veins"></div>
          </div>
        </div>
      )}
    </div>
  );
}
```

- [ ] **Step 2: Enhance ImageUpload.module.css with nature-inspired styling**
  
```css
/* Image Upload Component Styles */
.uploadZone {
  border: 2px dashed #8FBC8F;
  border-radius: 1.5rem;
  min-height: 200px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #F8FAF5;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  cursor: pointer;
}

.uploadZone:hover {
  border-color: #6D8D6D;
  background-color: #F0F7F0;
  transform: scale(1.02);
}

.uploadZone.dragActive {
  border-color: #E27D60;
  background-color: #FFF8F5;
  transform: scale(1.03);
}

.uploadZone.hover {
  border-color: #6D8D6D;
  background-color: #F0F7F0;
}

.uploadPrompt {
  text-align: center;
  padding: 2rem;
}

.icon {
  font-size: 3rem;
  color: #8FBC8F;
  margin-bottom: 1.5rem;
  display: block;
}

.promptText {
  margin: 0 0 1rem 0;
  font-size: 1.25rem;
  color: #2D3748;
}

.muted {
  display: block;
  margin-bottom: 1.5rem;
  color: #6B7280;
  font-size: 0.875rem;
}

.previewImage {
  max-width: 100%;
  max-height: 300px;
  border-radius: 1rem;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

/* Leaf Decoration */
.leafDecoration {
  width: 60px;
  height: 60px;
  margin: 1rem auto;
  position: relative;
}

.leaf-stem {
  position: absolute;
  top: 10px;
  left: 50%;
  width: 2px;
  height: 40px;
  background-color: #8FBC8F;
  transform: translateX(-50%);
  border-radius: 1px;
  animation: stemGrow 1.5s ease-out;
}

.leaf-veins {
  position: absolute;
  top: 20px;
  left: 50%;
  width: 0;
  height: 0;
  border-left: 1px solid transparent;
  border-right: 1px solid transparent;
  border-bottom: 8px solid #8FBC8F;
  transform: translateX(-50%);
  animation: veinsGrow 1.5s ease-out 1s;
}

/* Animation Classes */
.animate-fade-in {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.6s ease forwards;
}

.animate-fade-in-delayed {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.6s ease forwards 0.2s;
}

.animate-pulse {
  animation: pulse 2s ease-in-out infinite;
}

.animate-leaf-grow {
  opacity: 0;
  transform: scale(0.5);
  animation: leafGrow 1.2s ease forwards;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.03); }
}

@keyframes leafGrow {
  from {
    opacity: 0;
    transform: scale(0.5);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes stemGrow {
  from {
    height: 0;
  }
  to {
    height: 40px;
  }
}

@keyframes veinsGrow {
  from {
    border-bottom-width: 0;
  }
  to {
    border-bottom-width: 8px;
  }
}

/* Responsive Design */
@media (max-width: 480px) {
  .uploadZone {
    min-height: 150px;
  }
  
  .icon {
    font-size: 2.5rem;
  }
  
  .promptText {
    font-size: 1.125rem;
  }
}
```

- [ ] **Step 3: Test image upload component interactions**

Run: `npm run dev` and navigate to /diagnose to test the upload component
Expected: Upload area responds to hover/drag/click, shows leaf animation when empty, displays preview when image selected

- [ ] **Step 4: Commit**

```bash
git add frontend/src/components/ImageUpload.jsx frontend/src/components/ImageUpload.module.css
git commit -m "feat: enhance image upload component with leaf-inspired interactions"
```

## Task 13: Enhance Diagnosis Result Component

**Files:**
- Modify: `frontend/src/components/DiagnosisResult.jsx`
- Modify: `frontend/src/components/DiagnosisResult.module.css`

**Interfaces:**
- Consumes: Existing diagnosis result data
- Produces: Enhanced diagnosis result with nature-inspired emergence animations

- [ ] **Step 1: Update DiagnosisResult.jsx with improved animations**
  
```javascript
import React from 'react';
import styles from './DiagnosisResult.module.css';
import { fadeInUp, pulse } from '../utils/animations';

export default function DiagnosisResult({ data }) {
  if (!data) return null;

  const { display_name, confidence, is_healthy, gradcam_overlay_base64 } = data;
  const confPercent = Math.round(confidence * 100);
  
  return (
    <div className={`${card ${styles.container} animate-fade-in-delayed`}>
      {gradcam_overlay_base64 && (
        <img 
          src={`data:image/jpeg;base64,${gradcam_overlay_base64}`} 
          alt="Grad-CAM Heatmap Overlay" 
          className={styles.overlayImage}
          className={`${styles.overlayImage} animate-leaf-unfold`}
        />
      )}
      
      <div className={styles.header} animate-fade-in>
        <h2 className={styles.diseaseName} animate-pulse-on-hover>{display_name}</h2>
        <span className={`${styles.badge} ${is_healthy ? styles.badgeHealthy : styles.badgeSick}`} animate-pulse>
          {confPercent}% Confidence
        </span>
      </div>
    </div>
  );
}
```

- [ ] **Step 2: Enhance DiagnosisResult.module.css with nature-inspired styling**
  
```css
/* Diagnosis Result Component Styles */
.container {
  background-color: #ffffff;
  border-radius: 1.5rem;
  padding: 2rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  border: 1px solid #F0F0F0;
  position: relative;
  overflow: hidden;
}

.container::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background: linear-gradient(to bottom, #8FBC8F, #E27D60, #FDD835);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.container:hover::before {
  opacity: 1;
}

.overlayImage {
  width: 100%;
  border-radius: 1rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.diseaseName {
  font-size: 1.5rem;
  font-weight: 600;
  color: #2D3748;
  flex: 1;
  min-width: 150px;
}

.badge {
  padding: 0.375rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.875rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  display: inline-block;
}

.badgeHealthy {
  background-color: #C8E6C9;
  color: #2E7D32;
}

.badgeSick {
  background-color: #FFCDD2;
  color: #C62828;
}

/* Animation Classes */
.animate-fade-in {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.6s ease forwards;
}

.animate-fade-in-delayed {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.6s ease forwards 0.2s;
}

.animate-pulse-on-hover {
  transition: all 0.2s ease;
}

.animate-pulse-on-hover:hover {
  transform: scale(1.02);
}

.animate-pulse {
  animation: pulse 2s ease-in-out infinite;
}

.animate-leaf-unfold {
  opacity: 0;
  transform: rotate(-90deg);
  animation: leafUnfold 0.8s ease forwards;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.03); }
}

@keyframes leafUnfold {
  from {
    opacity: 0;
    transform: rotate(-90deg);
  }
  to {
    opacity: 1;
    transform: rotate(0deg);
  }
}

/* Responsive Design */
@media (max-width: 480px) {
  .container {
    padding: 1.5rem;
  }
  
  .diseaseName {
    font-size: 1.25rem;
  }
  
  .badge {
    font-size: 0.75rem;
    padding: 0.25rem 0.5rem;
  }
}
```

- [ ] **Step 3: Test diagnosis result component animations**

Run: `npm run dev` and test with a sample diagnosis to verify animations
Expected: Component fades in with delay, image unfolds like a leaf, disease name pulses slightly on hover, badge pulses gently

- [ ] **Step 4: Commit**

```bash
git add frontend/src/components/DiagnosisResult.jsx frontend/src/components/DiagnosisResult.module.css
git commit -m "feat: enhance diagnosis result component with nature-inspired animations"
```

## Task 14: Enhance Advisory Panel Component

**Files:**
- Modify: `frontend/src/components/AdvisoryPanel.jsx`
- Modify: `frontend/src/components/AdvisoryPanel.module.css`

**Interfaces:**
- Consumes: Existing advisory panel data
- Produces: Enhanced advisory panel with nature-inspired styling and animations

- [ ] **Step 1: Update AdvisoryPanel.jsx with improved animations**
  
```javascript
import React from 'react';
import styles from './AdvisoryPanel.module.css';
import { fadeInUp, pulse } from '../utils/animations';

export default function AdvisoryPanel({ data }) {
  if (!data) return null;

  return (
    <div className={`${styles.panel} animate-fade-in-delayed`}>
      <p className={styles.summary} animate-fade-in>{data.summary}</p>
      
      {data.weather_note && (
        <div className={styles.weatherCallout} animate-pulse>
          <span className={styles.icon}>⚠️</span>
          <p>{data.weather_note}</p>
        </div>
      )}
      
      {data.treatment_steps && data.treatment_steps.length > 0 && (
        <div className={styles.stepsContainer} animate-fade-in-delayed>
          <h3>Treatment Steps</h3>
          <ol className={styles.stepsList}>
            {data.treatment_steps.map((step, idx) => (
              <li key={idx} className={`step-item animate-fade-in-delayed ${idx % 3 === 0 ? 'd1' : idx % 3 === 1 ? 'd2' : 'd3'}`}>
                {step}
              </li>
            ))}
          </ol>
        </div>
      )}
      
      <div className={styles.footerInfo} animate-fade-in-delayed>
        <p><strong>Estimated Cost:</strong> {data.estimated_cost_inr}</p>
        <p className={styles.disclaimer}>{data.disclaimer}</p>
      </div>
    </div>
  );
}
```

- [ ] **Step 2: Enhance AdvisoryPanel.module.css with nature-inspired styling**
  
```css
/* Advisory Panel Component Styles */
.panel {
  background-color: #ffffff;
  border-radius: 1.5rem;
  padding: 2rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  border: 1px solid #F0F0F0;
  position: relative;
  overflow: hidden;
}

.panel::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background: linear-gradient(to bottom, #8FBC8F, #E27D60, #FDD835);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.panel:hover::before {
  opacity: 1;
}

.summary {
  color: #4A5568;
  line-height: 1.7;
  margin-bottom: 1.5rem;
  font-size: 0.9375rem;
}

.weatherCallout {
  background-color: #FFF8F5;
  border: 1px solid #FFEAA7;
  border-radius: 0.75rem;
  padding: 1rem;
  margin: 1.5rem 0;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.weatherCallout .icon {
  font-size: 1.25rem;
  color: #F59E0B;
}

.weatherCallout p {
  margin: 0;
  color: #92400E;
  font-size: 0.875rem;
}

.stepsContainer {
  margin: 1.5rem 0;
}

.stepsContainer h3 {
  margin: 0 0 1rem 0;
  font-size: 1.25rem;
  font-weight: 600;
  color: #2D3748;
}

.stepsList {
  list-style: none;
  padding: 0;
  margin: 0;
}

.step-item {
  padding: 0.75rem 0;
  border-left: 2px solid #8FBC8F;
  padding-left: 1rem;
  margin-bottom: 0.75rem;
  color: #4A5568;
  font-size: 0.875rem;
}

.step-item.d1 {
  border-left-color: #E27D60;
}

.step-item.d2 {
  border-left-color: #FDD835;
}

.step-item.d3 {
  border-left-color: #8FBC8F;
}

.footerInfo {
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid #E2E8F0;
}

.footerInfo p {
  margin: 0 0 0.5rem 0;
  color: #6B7280;
  font-size: 0.875rem;
}

.footerInfo strong {
  color: #2D3748;
}

.disclaimer {
  font-size: 0.75rem;
  color: #9CA3AF;
  font-style: italic;
}

/* Animation Classes */
.animate-fade-in {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.6s ease forwards;
}

.animate-fade-in-delayed {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.6s ease forwards 0.2s;
}

.animate-pulse {
  animation: pulse 2s ease-in-out infinite;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.03); }
}

/* Responsive Design */
@media (max-width: 480px) {
  .panel {
    padding: 1.5rem;
  }
  
  .summary {
    font-size: 0.875rem;
  }
  
  .stepsContainer h3 {
    font-size: 1.125rem;
  }
  
  .step-item {
    font-size: 0.75rem;
    padding: 0.5rem 0;
  }
}
```

- [ ] **Step 3: Test advisory panel component animations**

Run: `npm run dev` and test with sample advisory data to verify animations
Expected: Panel fades in with delay, summary fades in, weather note pulses gently, treatment steps fade in with staggered delay, footer info fades in

- [ ] **Step 4: Commit**

```bash
git add frontend/src/components/AdvisoryPanel.jsx frontend/src/components/AdvisoryPanel.module.css
git commit -m "feat: enhance advisory panel component with nature-inspired animations"
```

## Task 15: Enhance Chat Bubble Component

**Files:**
- Modify: `frontend/src/components/ChatBubble.jsx`
- Modify: `frontend/src/components/ChatBubble.module.css`

**Interfaces:**
- Consumes: Existing chat bubble functionality
- Produces: Enhanced chat bubble with nature-inspired styling and animations

- [ ] **Step 1: Update ChatBubble.jsx with improved animations**
  
```javascript
import React from 'react';
import styles from './ChatBubble.module.css';
import { slideInLeft, slideInRight } from '../utils/animations';

export default function ChatBubble({ role, text }) {
  const isUser = role === 'user';
  
  return (
    <div className={`${styles.bubbleWrapper} ${isUser ? styles.right : styles.left} ${isUser ? 'animate-slide-in-right' : 'animate-slide-in-left'}`}>
      {!isUser && <div className={styles.icon} animate-pulse>🍃</div>}
      <div className={`${styles.bubble} ${isUser ? styles.userBubble : styles.botBubble}`} animate-fade-in>
        {text}
      </div>
    </div>
  );
}
```

- [ ] **Step 2: Enhance ChatBubble.module.css with nature-inspired styling**
  
```css
/* Chat Bubble Component Styles */
.bubbleWrapper {
  display: flex;
  margin: 0.5rem 0;
}

.right {
  justify-content: flex-end;
}

.left {
  justify-content: flex-start;
}

.bubble {
  max-width: 80%;
  padding: 0.75rem 1rem;
  border-radius: 1rem;
  font-size: 0.875rem;
  line-height: 1.5;
  position: relative;
}

.userBubble {
  background-color: #8FBC8F;
  color: white;
  margin-left: 2rem;
}

.botBubble {
  background-color: #F8FAF5;
  color: #2D3748;
  border: 1px solid #E2E8F0;
  margin-right: 2rem;
}

.icon {
  font-size: 1.25rem;
  margin-right: 0.5rem;
}

/* Add leaf-like details to bubbles */
.bubble::before {
  content: '';
  position: absolute;
  top: 10px;
  left: -8px;
  width: 0;
  height: 0;
  border-top: 6px solid transparent;
  border-bottom: 6px solid transparent;
  border-right: 8px solid;
}

.userBubble::before {
  border-right-color: #8FBC8F;
  left: auto;
  right: -8px;
  transform: rotate(180deg);
}

.botBubble::before {
  border-right-color: #E2E8F0;
}

/* Animation Classes */
.animate-fade-in {
  opacity: 0;
  transform: translateY(10px);
  animation: fadeInUp 0.3s ease forwards;
}

.animate-slide-in-left {
  opacity: 0;
  transform: translateX(-20px);
  animation: slideInLeft 0.3s ease forwards;
}

.animate-slide-in-right {
  opacity: 0;
  transform: translateX(20px);
  animation: slideInRight 0.3s ease forwards;
}

.animate-pulse {
  animation: pulse 2s ease-in-out infinite;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateX(20px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.03); }
}

/* Responsive Design */
@media (max-width: 480px) {
  .bubble {
    max-width: 85%;
    padding: 0.5rem 0.75rem;
    font-size: 0.75rem;
  }
  
  .userBubble {
    margin-left: 1rem;
  }
  
  .botBubble {
    margin-right: 1rem;
  }
}
```

- [ ] **Step 3: Test chat bubble component animations**

Run: `npm run dev` and send test messages to verify animations
Expected: User bubbles slide in from right, bot bubbles slide in from left, bubbles fade in, icons pulse gently

- [ ] **Step 4: Commit**

```bash
git add frontend/src/components/ChatBubble.jsx frontend/src/components/ChatBubble.module.css
git commit -m "feat: enhance chat bubble component with nature-inspired animations"
```

## Task 16: Enhance Chat Input Component

**Files:**
- Modify: `frontend/src/components/ChatInput.jsx`
- Modify: `frontend/src/components/ChatInput.module.css`

**Interfaces:**
- Consumes: Existing chat input functionality
- Produces: Enhanced chat input with nature-inspired styling and animations

- [ ] **Step 1: Update ChatInput.jsx with improved animations**
  
```javascript
import React, { useState } from 'react';
import styles from './ChatInput.module.css';

export default function ChatInput({ onSend, disabled }) {
  const [text, setText] = useState('');

  const handleSend = () => {
    if (text.trim() && !disabled) {
      onSend(text);
      setText('');
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className={`${styles.container} animate-fade-in`}>
      <textarea
        className={`${styles.textarea} ${disabled ? styles.disabled : ''} animate-pulse-on-focus`}
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder="Type a message..."
        rows={1}
        disabled={disabled}
      />
      <button 
        className={`btn-primary ${styles.sendBtn} ${disabled ? styles.disabled : ''} animate-pulse-on-hover`}
        onClick={handleSend}
        disabled={!text.trim() || disabled}
      >
        Send
      </button>
    </div>
  );
}
```

- [ ] **Step 2: Enhance ChatInput.module.css with nature-inspired styling**
  
```css
/* Chat Input Component Styles */
.container {
  display: flex;
  gap: 0.75rem;
  align-items: flex-end;
}

.textarea {
  flex: 1;
  min-height: 3rem;
  padding: 0.75rem;
  border: 2px solid #E2E8F0;
  border-radius: 0.5rem;
  font-size: 0.875rem;
  resize: vertical;
  transition: all 0.2s ease;
  font-family: inherit;
}

.textarea:focus {
  outline: none;
  border-color: #8FBC8F;
  box-shadow: 0 0 0 3px rgba(143, 188, 143, 0.2);
}

.textarea.disabled {
  background-color: #F3F4F6;
  border-color: #D1D5DB;
  color: #6B7280;
  cursor: not-allowed;
}

.sendBtn {
  background-color: #8FBC8F;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  font-size: 0.875rem;
  font-weight: 600;
  border-radius: 0.5rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s ease;
  position: relative;
  overflow: hidden;
}

.sendBtn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.2),
    transparent
  );
  transition: all 0.5s ease;
}

.sendBtn:hover::before {
  left: 100%;
}

.sendBtn:hover {
  background-color: #6D8D6D;
  transform: translateY(-2px);
}

.sendBtn:active {
  transform: scale(0.98);
}

.sendBtn.disabled {
  background-color: #9CA3AF;
  color: #F3F4F6;
  cursor: not-allowed;
}

/* Leaf icon on send button */
.sendBtn::after {
  content: '🌱';
  font-size: 1rem;
}

/* Animation Classes */
.animate-fade-in {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.6s ease forwards;
}

.animate-pulse-on-focus {
  transition: all 0.2s ease;
}

.animate-pulse-on-focus:focus-within {
  transform: scale(1.02);
}

.animate-pulse-on-hover {
  transition: all 0.2s ease;
}

.animate-pulse-on-hover:hover {
  transform: scale(1.02);
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Responsive Design */
@media (max-width: 480px) {
  .container {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .textarea {
    min-height: 2.5rem;
    font-size: 0.75rem;
  }
  
  .sendBtn {
    padding: 0.5rem 1rem;
    font-size: 0.75rem;
  }
}
```

- [ ] **Step 3: Test chat input component animations**

Run: `npm run dev` and test the chat input to verify animations
Expected: Input fades in, pulses when focused, send button pulses on hover and has leaf icon

- [ ] **Step 4: Commit**

```bash
git add frontend/src/components/ChatInput.jsx frontend/src/components/ChatInput.module.css
git commit -m "feat: enhance chat input component with nature-inspired animations"
```

## Task 17: Final Commit and Cleanup

**Files:**
- Modify: Various files as needed

**Interfaces:**
- Consumes: All completed tasks
- Produces: Final cleaned up codebase ready for testing

- [ ] **Step 1: Run ESLint to fix any code style issues**

Run: `npm run lint -- --fix`
Expected: No linting errors

- [ ] **Step 2: Run tests to ensure nothing is broken**

Run: `npm test` (if tests exist)
Expected: All tests pass

- [ ] **Step 3: Final commit with any remaining changes**

```bash
git add .
git commit -m "feat: complete KisanAI UI redesign with nature-inspired organic approach"
```