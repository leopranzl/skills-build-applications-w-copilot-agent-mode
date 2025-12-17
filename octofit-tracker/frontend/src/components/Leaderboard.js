import React, { useEffect, useState } from 'react';

const getApiUrl = () => {
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  return codespace
    ? `https://${codespace}-8000.app.github.dev/api/leaderboard/`
    : '/api/leaderboard/';
};

export default function Leaderboard() {
  const [items, setItems] = useState([]);
  useEffect(() => {
    const url = getApiUrl();
    console.log('Fetching leaderboard from:', url);
    fetch(url)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        console.log('Fetched leaderboard:', results);
        setItems(results);
      });
  }, []);
  return (
    <div>
      <h2>Leaderboard</h2>
      <ul>
        {items.map((item, i) => (
          <li key={i}>{item.team} - {item.total_points} pts</li>
        ))}
      </ul>
    </div>
  );
}
