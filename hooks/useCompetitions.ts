import { useEffect, useState } from 'react';

export function useCompetitions() {
  const [competitions, setCompetitions] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/competitions/')
      .then(response => response.json())
      .then(data => {
        setCompetitions(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching competitions:', error);
        setLoading(false);
      });
  }, []);

  return { competitions, loading };
}