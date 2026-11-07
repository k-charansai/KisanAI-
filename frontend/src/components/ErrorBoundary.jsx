import React from 'react';

export class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('ErrorBoundary caught an error:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div style={{
          minHeight: '100vh',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          padding: '2rem',
          backgroundColor: '#1b1e19',
          color: '#ffffff',
          fontFamily: 'system-ui, -apple-system, sans-serif',
          textAlign: 'center'
        }}>
          <h1 style={{ fontSize: '1.8rem', marginBottom: '0.8rem', color: '#86efac' }}>
            Something went wrong
          </h1>
          <p style={{ maxWidth: '480px', color: '#cbd5e1', marginBottom: '1.5rem', lineHeight: '1.5' }}>
            An unexpected error occurred while rendering the page.
          </p>
          <pre style={{
            background: '#0f172a',
            color: '#f87171',
            padding: '1rem',
            borderRadius: '8px',
            fontSize: '0.85rem',
            maxWidth: '600px',
            overflowX: 'auto',
            textAlign: 'left',
            marginBottom: '1.5rem'
          }}>
            {this.state.error?.message || String(this.state.error)}
          </pre>
          <button
            onClick={() => window.location.assign('/')}
            style={{
              padding: '0.6rem 1.4rem',
              backgroundColor: '#22c55e',
              color: '#ffffff',
              border: 'none',
              borderRadius: '6px',
              fontSize: '1rem',
              cursor: 'pointer',
              fontWeight: 500
            }}
          >
            Reload Home
          </button>
        </div>
      );
    }
    return this.props.children;
  }
}

export default ErrorBoundary;
