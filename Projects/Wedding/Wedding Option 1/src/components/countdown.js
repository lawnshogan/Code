import React, { useState, useEffect } from 'react';
import './countdown.css';

export default function Countdown() {
  const [timeRemaining, setTimeRemaining] = useState(null);

  // You'll need to replace this date with the date of your wedding
  const weddingDate = new Date('April 1, 2022 00:00:00').getTime();

  useEffect(() => {
    const intervalId = setInterval(() => {
      const currentTime = new Date().getTime();
      const timeUntilWedding = weddingDate - currentTime;

      if (timeUntilWedding < 0) {
        clearInterval(intervalId);
        setTimeRemaining(null);
        return;
      }

      const days = Math.floor(timeUntilWedding / (1000 * 60 * 60 * 24));
      const hours = Math.floor((timeUntilWedding % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((timeUntilWedding % (1000 * 60 * 60)) / (1000 * 60));

      setTimeRemaining({ days, hours, minutes });
    }, 1000);

    return () => clearInterval(intervalId);
  }, [weddingDate]);

  if (!timeRemaining) {
    return <div>MARRIED</div>;
  }

  return (
    <div className="countdown">
      <p>
        <span className="highlight">{timeRemaining.days}</span> DAYS
      </p>
      <hr />
      <p>
        <span className="highlight">{timeRemaining.hours}</span> HOURS
      </p>
      <hr />
      <p>
        <span className="highlight">{timeRemaining.minutes}</span> MINUTES
      </p>
    </div>
  );
}
