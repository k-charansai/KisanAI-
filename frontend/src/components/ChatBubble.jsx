import React from 'react';
import styles from './ChatBubble.module.css';

export default function ChatBubble({ role, text }) {
  const isUser = role === 'user';
  
  return (
    <div className={`${styles.bubbleWrapper} ${isUser ? styles.right : styles.left}`}>
      {!isUser && <div className={styles.icon}>🍃</div>}
      <div className={`${styles.bubble} ${isUser ? styles.userBubble : styles.botBubble}`}>
        {text}
      </div>
    </div>
  );
}
