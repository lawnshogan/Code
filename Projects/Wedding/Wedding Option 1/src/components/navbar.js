import React from 'react';
import styled from 'styled-components';

const StyledNav = styled.div`
  color: var(--white);
  box-sizing: border-box;
  border-bottom: 3rem solid #274355;

  .logo {
    height: 3rem;
  }

  .nav-list {
    background: white;
    margin: 0;
    padding: 1rem 0;
    border-radius: 2px;
    display: flex;
    justify-content: flex-end;
    align-items: center;
  }

  .nav-item {
    list-style: none;
    margin-right: 0.75rem;
  }

  .nav-item a {
    border: none;
    background: none;
    color: var(--white);
    /* text-shadow: 2px 3px 5px rgba(0, 0, 0, 0.5); */
    font-size: 1rem;
    font-weight: bold;
    text-decoration: none;
  }

  .nav-item a:hover {
    color: #bcbdc2;
    transition: all 200ms ease-in;
  }

  .nav-item:first-child {
    margin-right: auto;
    margin-left: 1.3rem;
  }

  @media (max-width: 600px) {
    .nav-list {
      height: 20px;
    }
    .nav-item {
      opacity: 0;
    }
    .nav-item:first-child {
      opacity: 1;
    }

    .nav-list {
      display: none;
    }
  }
`;

export default function Navbar() {
  return (
    <StyledNav>
      <ul className="nav-list nav">
        <li className="nav-item ">
          <img className="logo" src="images/logo.png" alt="" />
        </li>
        <li className="nav-item nav">
          <a href="#story">Our Story</a>
        </li>
        <li className="nav-item nav">
          <a href="#rsvp">RSVP</a>
        </li>
        <li className="nav-item nav">
          <a href="#gallery">Gallery</a>
        </li>
        <li className="nav-item nav">
          <a
            href="https://www.vogue.com/article/best-wedding-registries-list"
            target="_blank"
            rel="noopener noreferrer"
          >
            Resistry
          </a>
        </li>
      </ul>
    </StyledNav>
  );
}
