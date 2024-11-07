import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  // Handle form submit
  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await axios.post('http://127.0.0.1:5000/analyze', { text });
      setResult(response.data);
    } catch (error) {
      console.error("There was an error!", error);
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <h1>Sentiment Analysis</h1>

      <form onSubmit={handleSubmit}>
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter text for sentiment analysis"
          rows="5"
          cols="50"
        />
        <br />
        <button type="submit">Analyze</button>
      </form>

      {loading ? <p>Loading...</p> : result && (
        <div>
          <h3>Sentiment: {result.sentiment}</h3>
          <p>Confidence: {result.confidence.toFixed(2)}</p>
        </div>
      )}
    </div>
  );
}

export default App;
