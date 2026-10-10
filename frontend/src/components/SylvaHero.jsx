import React from 'react';
import './SylvaHero.css';

export function SylvaHero() {
  return (
    <div className="sylva-hero-frame">
      <iframe
        src="/landing-pages/inner-green-3d.html"
        title="Sylva Hero — Into the living fields"
        className="sylva-hero-iframe"
        allow="autoplay; fullscreen"
      />
    </div>
  );
}

export default SylvaHero;
