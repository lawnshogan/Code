import React from 'react';
import styled from 'styled-components';

const StyledSpacer = styled.div`
  height: 15vh;
  width: 100vw;
  color: white;
  background-color: #274355;
  display: flex;
  justify-content: center;

  .title {
    display: grid;
    align-items: center;
    justify-content: center;
    text-align: center;
  }

  .title h1 {
    font-weight: normal;
    font-size: 2rem;
    color: #d9d9d9;
  }

  @media (max-width: 900px) {
    .title h1 {
      font-size: 1.5rem;
    }
  }
`;

export default function Spacer() {
  return (
    <StyledSpacer>
      <div className="title">
        <h1>Fuck Ya, We're Getting Married!</h1>
      </div>
    </StyledSpacer>
  );
}
