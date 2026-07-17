import React, { useState, useEffect, useRef } from 'react';
import { motion, useScroll, useTransform } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import { UploadCloud, CheckCircle, ArrowRight, ShieldCheck, Zap, Activity, Leaf } from 'lucide-react';
import styles from './LandingPage.module.css';
import { setPendingFile } from '../sharedState';
import farmersImg from '../assets/farmers.png';
import sproutImg from '../assets/sprout.png';

const presetCases = [
  {
    name: 'Tomato Late Blight',
    confidence: 92,
    steps: ['1. Apply Mancozeb 75% WP at 2.5g/L', '2. Improve airflow immediately', '3. Do not overwater canopy'],
    cost: '₹1200 - ₹1500',
    imgPlaceholder: 'bg-green-800'
  },
  {
    name: 'Tomato Spider Mites',
    confidence: 88,
    steps: ['1. Apply Oberon at 1.0ml/L', '2. Spray underside of leaves', '3. Wait 5 days between sprays'],
    cost: '₹1000 - ₹1600',
    imgPlaceholder: 'bg-yellow-700'
  },
  {
    name: 'Apple Scab',
    confidence: 95,
    steps: ['1. Apply Captan 50% WP at 2g/L', '2. Rake and burn fallen leaves', '3. Spray prior to rain events'],
    cost: '₹800 - ₹1100',
    imgPlaceholder: 'bg-red-800'
  }
];

const DiagnoseCard = () => {
  const [caseIndex, setCaseIndex] = useState(0);
  const [isScanning, setIsScanning] = useState(false);
  const [showResult, setShowResult] = useState(false);
  const currentCase = presetCases[caseIndex];
  const navigate = useNavigate();

  const handleAnalyse = () => {
    setIsScanning(true);
    setShowResult(false);
    setTimeout(() => {
      setIsScanning(false);
      setShowResult(true);
    }, 2000);
  };

  const handleNext = () => {
    setShowResult(false);
    setCaseIndex((prev) => (prev + 1) % presetCases.length);
  };

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      setPendingFile(e.target.files[0]);
      navigate('/diagnose');
    }
  };

  return (
    <motion.div 
      className={styles.diagnoseCard}
      animate={{ y: [-10, 10, -10] }}
      transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
    >
      <label className={styles.uploadZone} style={{ cursor: 'pointer' }}>
        <input 
          type="file" 
          accept="image/*"
          style={{ display: 'none' }} 
          onChange={handleFileChange} 
        />
        <UploadCloud className={styles.uploadIcon} size={40} />
        <p style={{ color: 'var(--text-faint)', fontSize: 13, marginBottom: 12, textAlign: 'center' }}>
          Drop diseased leaf photo here<br/>
          <span style={{ fontSize: 11 }}>(or click to upload & diagnose)</span>
        </p>
        
        {isScanning && (
          <motion.div 
            className={styles.scanline}
            initial={{ top: 0 }}
            animate={{ top: '100%' }}
            transition={{ duration: 2, ease: "linear" }}
          />
        )}
      </label>

      {!showResult && !isScanning && (
        <button className={styles.btnPrimary} style={{ width: '100%', justifyContent: 'center' }} onClick={handleAnalyse}>
          Analyse demo crop
        </button>
      )}

      {isScanning && (
        <button className={styles.btnSecondary} style={{ width: '100%', justifyContent: 'center' }} disabled>
          Processing...
        </button>
      )}

      {showResult && (
        <div className={styles.resultBox}>
          <h3 className={styles.diseaseName}>{currentCase.name}</h3>
          
          <div className={styles.confidenceWrap}>
            <div className={styles.confidenceLabel}>
              <span>Confidence</span>
              <span>{currentCase.confidence}%</span>
            </div>
            <div className={styles.confidenceBg}>
              <motion.div 
                className={styles.confidenceFill}
                initial={{ width: 0 }}
                animate={{ width: `${currentCase.confidence}%` }}
                transition={{ duration: 0.8, ease: "easeOut" }}
              />
            </div>
          </div>

          <div style={{ marginBottom: 16 }}>
            {currentCase.steps.map((step, idx) => (
              <motion.div 
                key={idx}
                className={styles.stepItem}
                initial={{ opacity: 0, x: -10 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: idx * 0.3 }}
              >
                <CheckCircle className={styles.stepIcon} size={16} />
                <span>{step}</span>
              </motion.div>
            ))}
          </div>

          <motion.div 
            className={styles.costWrap}
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 1 }}
          >
            <span>Est. Cost / Acre</span>
            <strong>{currentCase.cost}</strong>
          </motion.div>

          <button className={styles.btnSecondary} style={{ width: '100%', marginTop: 16, justifyContent: 'center' }} onClick={handleNext}>
            Try another crop
          </button>
        </div>
      )}
    </motion.div>
  );
};

const FadeIn = ({ children, delay = 0 }) => (
  <motion.div
    initial={{ opacity: 0, y: 24 }}
    whileInView={{ opacity: 1, y: 0 }}
    viewport={{ once: true }}
    transition={{ duration: 0.6, delay }}
  >
    {children}
  </motion.div>
);

const ParallaxImage = ({ src, alt }) => {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({ target: ref, offset: ["start end", "end start"] });
  const y = useTransform(scrollYProgress, [0, 1], ["-15%", "15%"]);
  
  return (
    <div ref={ref} style={{ width: '100%', height: '100%', overflow: 'hidden', borderRadius: 24, minHeight: 300 }}>
      <motion.img 
        src={src} 
        alt={alt} 
        style={{ y, width: '100%', height: '130%', objectFit: 'cover', display: 'block', marginTop: '-15%' }} 
      />
    </div>
  );
};

export default function LandingPage() {
  const navigate = useNavigate();

  return (
    <div className={styles.page}>
      <nav className={styles.navbar}>
        <h2 className={styles.logo}>Kisan<strong>AI</strong></h2>
        <div className={styles.navLinks}>
          <a href="#how-it-works">How it works</a>
          <a href="#features">Features</a>
          <a href="#about">About</a>
        </div>
        <button onClick={() => navigate('/diagnose')} className={styles.navCta}>
          Diagnose Now
        </button>
      </nav>

      <section className={styles.section}>
        <div className={styles.hero}>
          <FadeIn>
            <span className={styles.eyebrow}>AI Agronomist in your pocket</span>
            <h1 className={styles.heroTitle}>Stop guessing. Start <strong>healing</strong>.</h1>
            <p className={styles.heroDesc}>
              Upload a photo of a diseased leaf and instantly receive an India-registered, cost-estimated treatment plan powered by real agronomy data.
            </p>
            <div className={styles.heroBtns}>
              <button onClick={() => navigate('/diagnose')} className={styles.btnPrimary}>
                Start free diagnosis <ArrowRight size={18} />
              </button>
              <button className={styles.btnSecondary} onClick={() => document.getElementById('how-it-works').scrollIntoView({ behavior: 'smooth'})}>
                See how it works
              </button>
            </div>
          </FadeIn>
          <FadeIn delay={0.2}>
            <div className={styles.heroRight}>
              <DiagnoseCard />
            </div>
          </FadeIn>
        </div>
      </section>

      <section className={styles.section} style={{ paddingBottom: 0 }}>
        <FadeIn>
          <div className={styles.statsRow}>
            <div className={styles.statCell}>
              <div className={styles.statNum}>38</div>
              <div className={styles.statLabel}>Crop diseases identified</div>
            </div>
            <div className={styles.statCell}>
              <div className={styles.statNum}>95%</div>
              <div className={styles.statLabel}>Lab-validated accuracy</div>
            </div>
            <div className={styles.statCell}>
              <div className={styles.statNum}>2s</div>
              <div className={styles.statLabel}>Average diagnosis time</div>
            </div>
            <div className={styles.statCell}>
              <div className={styles.statNum}>100%</div>
              <div className={styles.statLabel}>Free for Indian farmers</div>
            </div>
          </div>
        </FadeIn>
      </section>

      <section className={styles.section} id="features">
        <FadeIn>
          <h2 style={{ fontSize: 36, marginBottom: 48, textAlign: 'center' }}>Enterprise-grade AI, <strong>accessible to all.</strong></h2>
          <div className={styles.featuresGrid}>
            <div className={styles.featureCell}>
              <ShieldCheck className={styles.featureIcon} size={40} />
              <h3 className={styles.featureTitle}>CIB&RC Compliant</h3>
              <p style={{ color: 'var(--text-muted)' }}>Every treatment plan strictly recommends pesticides officially registered for that specific crop and disease in India.</p>
            </div>
            <div className={styles.featureCell}>
              <Activity className={styles.featureIcon} size={40} />
              <h3 className={styles.featureTitle}>Resistance Management</h3>
              <p style={{ color: 'var(--text-muted)' }}>The AI automatically factors in chemical group rotation to prevent pathogens from developing resistance.</p>
            </div>
            <div className={styles.featureCell}>
              <Zap className={styles.featureIcon} size={40} />
              <h3 className={styles.featureTitle}>Edge-optimized Vision</h3>
              <p style={{ color: 'var(--text-muted)' }}>Our EfficientNet-B0 model runs extremely fast, even on heavily compressed photos sent over 3G rural networks.</p>
            </div>
            <div className={styles.featureCell}>
              <Leaf className={styles.featureIcon} size={40} />
              <h3 className={styles.featureTitle}>Organic Alternatives</h3>
              <p style={{ color: 'var(--text-muted)' }}>Not using synthetics? The system provides robust organic regimens like Trichoderma and Neem oil protocols.</p>
            </div>
          </div>
        </FadeIn>
      </section>

      <div className={styles.howBg} id="how-it-works">
        <div className={styles.howContainer}>
          <FadeIn>
            <h2 style={{ fontSize: 36, marginBottom: 16 }}>From photo to <strong>prescription</strong>.</h2>
            <p style={{ color: 'var(--text-muted)', fontSize: 18 }}>Four simple steps to protect your yield.</p>
            
            <div className={styles.howGrid}>
              <div className={styles.howStep}>
                <div className={styles.stepNum}>1</div>
                <div className={styles.stepLine} />
                <h4 style={{ fontSize: 18, marginBottom: 8 }}>Snap a photo</h4>
                <p style={{ color: 'var(--text-muted)', fontSize: 14 }}>Take a clear picture of the infected leaf.</p>
              </div>
              <div className={styles.howStep}>
                <div className={styles.stepNum}>2</div>
                <div className={styles.stepLine} />
                <h4 style={{ fontSize: 18, marginBottom: 8 }}>AI Analysis</h4>
                <p style={{ color: 'var(--text-muted)', fontSize: 14 }}>Our vision model identifies the exact pathogen.</p>
              </div>
              <div className={styles.howStep}>
                <div className={styles.stepNum}>3</div>
                <div className={styles.stepLine} />
                <h4 style={{ fontSize: 18, marginBottom: 8 }}>Weather Check</h4>
                <p style={{ color: 'var(--text-muted)', fontSize: 14 }}>Agent verifies local weather for safe spraying.</p>
              </div>
              <div className={styles.howStep}>
                <div className={styles.stepNum}>4</div>
                <div className={styles.stepLine} style={{ display: 'none' }} />
                <h4 style={{ fontSize: 18, marginBottom: 8 }}>Action Plan</h4>
                <p style={{ color: 'var(--text-muted)', fontSize: 14 }}>Receive a step-by-step chemical or organic plan.</p>
              </div>
            </div>
          </FadeIn>
        </div>
      </div>

      <section className={styles.section} id="about">
        <div className={styles.farmerSection}>
          <FadeIn>
            <ParallaxImage src={farmersImg} alt="Farmers planting rice" />
          </FadeIn>
          <FadeIn delay={0.2}>
            <div className={styles.quote}>
              "Technology shouldn't stay in the lab. It belongs in the field, helping the hands that feed the nation."
            </div>
            <p style={{ color: 'var(--text-muted)' }}>Built with ❤️ for Indian Agriculture.</p>
          </FadeIn>
        </div>
      </section>
      
      {/* Scrollable Animation Section per User Request */}
      <section className={styles.section} style={{ paddingTop: 0 }}>
        <FadeIn>
           <ParallaxImage src={sproutImg} alt="Hands holding soil and sprout" />
        </FadeIn>
      </section>

      <div className={styles.darkCta}>
        <FadeIn>
          <span className={styles.eyebrow} style={{ color: 'var(--green-light)' }}>Ready to protect your crop?</span>
          <h2>Don't wait until it's <strong>too late.</strong></h2>
          <button onClick={() => navigate('/diagnose')} className={styles.btnGreen}>
            Analyse my crop <ArrowRight size={20} />
          </button>
        </FadeIn>
      </div>

      <footer className={styles.footer}>
        <div style={{ display: 'flex', justifyContent: 'center', gap: 24, marginBottom: 24 }}>
          <a href="#" style={{ color: 'var(--text-muted)', textDecoration: 'none' }}>Privacy Policy</a>
          <a href="#" style={{ color: 'var(--text-muted)', textDecoration: 'none' }}>Terms of Service</a>
          <a href="#" style={{ color: 'var(--text-muted)', textDecoration: 'none' }}>Contact</a>
        </div>
        <p>© 2026 KisanAI. Built for portfolio demonstration.</p>
      </footer>
    </div>
  );
}
