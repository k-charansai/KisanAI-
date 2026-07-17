import React, { useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import styles from './ChatPage.module.css';
import ChatBubble from '../components/ChatBubble';
import ChatInput from '../components/ChatInput';
import { sendChatMessage } from '../api';

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
    <div className={styles.container}>
      <header className={styles.header}>
        <Link to="/diagnose" className={styles.backLink}>&larr; Back to diagnosis</Link>
        <h2>Ask KisanAI</h2>
      </header>
      
      <div className={styles.chatArea}>
        {messages.map((m, idx) => (
          <ChatBubble key={idx} role={m.role} text={m.text} />
        ))}
        {loading && <div className={styles.loading}>KisanAI is typing...</div>}
      </div>

      <ChatInput onSend={handleSend} disabled={loading} />
    </div>
  );
}
