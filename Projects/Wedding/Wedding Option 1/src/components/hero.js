import React from 'react';

import styled from 'styled-components';

const StyledHero = styled.div`
  .bg-image {
    height: 80vh;
    width: 100vw;
    position: relative;
    background-size: cover;
    background-repeat: no-repeat;
    /* background-position: 50% 50%; */
    background-image: url('images/hero.jpg');
    background-position: top;
    background-attachment: fixed;
    z-index: 1000;
    border-bottom: 3rem solid #274355;
    /* border-top: 2rem solid #274355; */
  }

  .border {
    height: 20%;
    background-color: #274355;
    width: 100vw;
  }

  .overlay {
    position: absolute;
    height: 100%;
    width: 100%;
    top: 0;
    left: 0;
    background: rgba(0, 0, 0, 0.55);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
  }

  .overlay h1 {
    font-family: 'Old Standard TT', Serif;
    font-weight: normal;
    font-size: 4rem;
    transform: translateY(200px);
  }

  .words {
    transform: translateY(200px);
  }

  @media (max-width: 900px) {
    .bg-image {
      height: 35vh;
      position: relative;
      background-size: cover;
      background-position: 50% 50%;
      background-image: url('images/black-white.jpg');
      background-position: top;
      z-index: 1000;
      border-bottom: 3rem solid #274355;
      border-top: 2rem solid #274355;
    }
    .overlay {
      height: 30vh;
    }
    .overlay h1 {
      font-size: 1.5rem;
      transform: translateY(70px);
    }
    .words {
      transform: translateY(0);
    }
  }
`;

export default function Hero() {
  return (
    <StyledHero>
      <div className="border" />
      <div className="bg-image">
        <div className="overlay">
          <img className="words" src="images/dani-ethan.png" alt="" />
        </div>
      </div>
      <div className="border" />
    </StyledHero>
  );
}
