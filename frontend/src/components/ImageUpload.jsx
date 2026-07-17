import React, { useRef, useState } from 'react';
import styles from './ImageUpload.module.css';

export default function ImageUpload({ file, setFile }) {
  const fileInputRef = useRef(null);
  const [preview, setPreview] = useState(null);
  const [dragActive, setDragActive] = useState(false);

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

  return (
    <div 
      className={`${styles.uploadZone} ${dragActive ? styles.dragActive : ''}`}
      onDragEnter={onDrag}
      onDragLeave={onDrag}
      onDragOver={onDrag}
      onDrop={onDrop}
      onClick={() => fileInputRef.current.click()}
    >
      <input 
        type="file" 
        ref={fileInputRef} 
        onChange={(e) => handleFile(e.target.files[0])} 
        accept="image/jpeg, image/png" 
        style={{ display: 'none' }} 
      />
      
      {preview ? (
        <img src={preview} alt="Preview" className={styles.previewImage} />
      ) : (
        <div className={styles.uploadPrompt}>
          <div className={styles.icon}>📷</div>
          <p>Drag & drop leaf image here</p>
          <span className={styles.muted}>or click to browse</span>
        </div>
      )}
    </div>
  );
}
