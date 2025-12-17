import React, { useEffect, useState } from 'react';

const getApiUrl = () => {
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  return codespace
    ? `https://${codespace}-8000.app.github.dev/api/users/`
    : '/api/users/';
};

export default function Users() {
  const [users, setUsers] = useState([]);
  useEffect(() => {
    const url = getApiUrl();
    console.log('Fetching users from:', url);
    fetch(url)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        console.log('Fetched users:', results);
        setUsers(results);
      });
  }, []);
  return (
    <div>
      <h2>Users</h2>
      <ul>
        {users.map((u, i) => (
          <li key={i}>{u.name} - {u.email} - {u.team}</li>
        ))}
      </ul>
    </div>
  );
}
