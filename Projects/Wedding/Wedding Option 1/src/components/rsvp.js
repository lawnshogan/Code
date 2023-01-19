/* eslint-disable jsx-a11y/label-has-associated-control */
import React from 'react';
import styled from 'styled-components';

const StyledRsvp = styled.div`
  @import url('https://fonts.googleapis.com/css?family=Old+Standard+TT:400i|Rubik" rel="stylesheet');

  height: 100vh;
  width: 100vw;
  /* margin: 0;
  padding: 0; */
  background-color: #bdc3c7;

  .top {
    background-color: #264356;
    height: 20vh;
    margin: 0;
    padding: 0;
    box-shadow: 2px 2px 4px rgb(0, 0, 0, 0.25);
  }

  .form {
    height: 80vh;
    width: 45vw;
    background-color: #fff;
    margin: -80px auto;
    border-radius: 10px;
    color: #666;
    padding: 0px 0px;
    box-shadow: 2px 2px 4px rgb(0, 0, 0, 0.25);
  }

  .info {
    padding: 10px;
  }

  h1,
  h2,
  p {
    text-align: center;
    padding: 0px;
    margin: 5px 5px;
  }

  h2 {
    font-family: 'Great Vibes', cursive;
    font-weight: 100;
  }

  p.line {
    margin: 0px auto 20px auto;
    color: #999;
  }

  .form input {
    font-size: 1rem;
    color: #666;
    padding: 3px;
    margin: 1rem auto 1rem;
    display: block;
    width: 75%;
  }

  input:focus {
    outline: 0;
  }

  .button button {
    /* display: inline-block; */
    /* width: 400px; */
  }
  button {
    color: #264356;
    background-color: #83a8d4;
    border: none;
    font-family: 'Raleway';
    font-size: 1rem;
    font-weight: 600;
    padding: 0.75rem 1rem;
    width: 22.5vw;
    margin: auto;
    transform: translateY(4rem);
  }

  button.accept {
    border-radius: 0px 0px 0px 10px;
    border-right: solid 1px #bdd9f2;
    float: left;
  }

  button.regret {
    border-radius: 0px 0px 10px 0px;
    float: right;
  }

  button:hover {
    background-color: #cc919a;
    transition: 0.5s;
  }

  @media (max-width: 900px) {
    button {
      transform: translateY(0);
    }
  }
`;

export default function Rsvp() {
  return (
    <StyledRsvp>
      <div className="top" id="rsvp" />
      <form className="form">
        <div className="info">
          <h1>RSVP</h1>
          <h2>for the wedding of</h2>
          <h1>Ethan & Dani</h1>
          <p className="line">________________________________________</p>
          <h2>The Details</h2>
          <p>Saturday, October 16, 2021</p>
          <p>5:00 PM</p>
          <br />
          <h2>Ceremony & Reception</h2>
          <p>The Lodge at Malibou Lake</p>
          <p>29022 Lake Vista Dr, Angoura Hills, CA 91301</p>
          <p className="line">________________________________________</p>
          <input type="text" placeholder="Name" />
          <input type="number" placeholder="# of Guests" />
        </div>
        <button className="accept" type="button">
          Accept
        </button>
        <button className="regret" type="button">
          Regret
        </button>
      </form>
    </StyledRsvp>
  );
}
