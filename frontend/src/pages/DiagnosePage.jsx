import React, { useState } from 'react';
import styles from './DiagnosePage.module.css';
import ImageUpload from '../components/ImageUpload';
import DiagnosisResult from '../components/DiagnosisResult';
import AdvisoryPanel from '../components/AdvisoryPanel';
import { uploadImageForDiagnosis, getAdvisory } from '../api';
import { useNavigate } from 'react-router-dom';
import { pendingFile, setPendingFile } from '../sharedState';

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
    <div className={styles.container}>
      <div className={styles.leftPanel}>
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
            className={`btn-primary ${styles.analyseBtn}`}
            onClick={handleAnalyse}
            disabled={!file || loading}
          >
            {loading ? 'Analysing...' : 'Analyse'}
          </button>
        </div>
      </div>
      
      <div className={styles.rightPanel}>
        {!loading && !error && !diagnosisData && (
          <div className={styles.placeholder}>
            Upload an image and click Analyse to see results here.
          </div>
        )}

        {loading && (
          <div className={styles.skeleton}>
            <div className={styles.skeletonImg}></div>
            <div className={styles.skeletonText}></div>
            <div className={styles.skeletonText}></div>
            <div className={styles.skeletonText}></div>
          </div>
        )}

        {error && (
          <div className={styles.errorState}>
            <p>Couldn't reach the server — try again.</p>
            <button className="btn-primary" onClick={handleAnalyse}>Retry</button>
          </div>
        )}

        {diagnosisData && !loading && (
          <div className={styles.results}>
            <DiagnosisResult data={diagnosisData} />
            {advisoryData ? (
              <>
                <AdvisoryPanel data={advisoryData} />
                <button className={`btn-primary ${styles.chatBtn}`} onClick={startChat}>
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
