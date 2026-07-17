import { Routes, Route } from 'react-router-dom'
import LandingPage from './pages/LandingPage'
import DiagnosePage from './pages/DiagnosePage'
import ChatPage from './pages/ChatPage'

function App() {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/diagnose" element={<DiagnosePage />} />
      <Route path="/chat/:sessionId" element={<ChatPage />} />
    </Routes>
  )
}

export default App
