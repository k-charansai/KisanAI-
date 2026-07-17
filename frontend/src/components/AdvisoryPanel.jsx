import React from 'react';
import styles from './AdvisoryPanel.module.css';

export default function AdvisoryPanel({ data }) {
  if (!data) return null;

  return (
    <div className={`card ${styles.panel}`}>
      <p className={styles.summary}>{data.summary}</p>
      
      {data.weather_note && (
        <div className={styles.weatherCallout}>
          <span className={styles.icon}>⚠️</span>
          <p>{data.weather_note}</p>
        </div>
      )}

      {data.treatment_steps && data.treatment_steps.length > 0 && (
        <div className={styles.stepsContainer}>
          <h3>Treatment Steps</h3>
          <ol className={styles.stepsList}>
            {data.treatment_steps.map((step, idx) => (
              <li key={idx}>{step}</li>
            ))}
          </ol>
        </div>
      )}

      <div className={styles.footerInfo}>
        <p><strong>Estimated Cost:</strong> {data.estimated_cost_inr}</p>
        <p className={styles.disclaimer}>{data.disclaimer}</p>
      </div>
    </div>
  );
}
