import axios from 'axios';

const API_URL = import.meta.env.VITE_BACKEND_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_URL,
});

export async function uploadImageForDiagnosis(file) {
  const formData = new FormData();
  formData.append('file', file);

  const res = await api.post('/diagnose', formData);
  return res.data;
}

export async function getAdvisory(disease, location) {
  const res = await api.post('/advise', { disease, location });
  return res.data;
}

export async function sendChatMessage(sessionId, message) {
  const res = await api.post('/chat', { session_id: sessionId, message });
  return res.data;
}
