import React from 'react';
import styles from './DiagnosisResult.module.css';

export default function DiagnosisResult({ data }) {
  if (!data) return null;

  const { display_name, confidence, is_healthy, gradcam_overlay_base64 } = data;
  const confPercent = Math.round(confidence * 100);
  
  return (
    <div className={`card ${styles.container}`}>
      {gradcam_overlay_base64 && (
        <img 
          src={`data:image/jpeg;base64,${gradcam_overlay_base64}`} 
          alt="Grad-CAM Heatmap Overlay" 
          className={styles.overlayImage} 
        />
      )}
      
      <div className={styles.header}>
        <h2 className={styles.diseaseName}>{display_name}</h2>
        <span className={`${styles.badge} ${is_healthy ? styles.badgeHealthy : styles.badgeSick}`}>
          {confPercent}% Confidence
        </span>
      </div>
    </div>
  );
}
