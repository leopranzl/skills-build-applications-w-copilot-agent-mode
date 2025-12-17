import React, { useEffect, useState } from 'react';

const getApiUrl = () => {
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  return codespace
    ? `https://${codespace}-8000.app.github.dev/api/activities/`
    : '/api/activities/';
};

export default function Activities() {
  const [activities, setActivities] = useState([]);
  useEffect(() => {
    const url = getApiUrl();
    console.log('Fetching activities from:', url);
    fetch(url)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        console.log('Fetched activities:', results);
        setActivities(results);
      });
  }, []);
  return (
    <div>
      <h2>Activities</h2>
      <ul>
        {activities.map((a, i) => (
          <li key={i}>{a.user} - {a.workout} - {a.date} - {a.duration_minutes} min - {a.points} pts</li>
        ))}
      </ul>
    </div>
  );
}
