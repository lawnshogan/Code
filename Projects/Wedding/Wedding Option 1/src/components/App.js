import React from 'react';
import './App.css';
import Countdown from './countdown';
import Hero from './hero';
import NavBar from './navbar';
import OurStory from './ourStory';
import Spacer from './spacer';
import Gallery from './Gallery';
import Rsvp from './rsvp';

export default function App() {
  return (
    <div>
      <NavBar />
      <Hero />
      <Countdown />
      <OurStory />
      <Spacer />
      <Gallery />
      <Rsvp />
    </div>
  );
}
