import { css } from '@emotion/react';
import React from 'react';

const App = () => {
  const buttonStyles = css`
    background-color: blue;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
  `;

  return (
    <div>
      <button css={buttonStyles}>Click me</button>
    </div>
  );
};

export default App;

// Define the CSS styles for the left-aligned header
const headerStyles = css`
  padding: 20px;
`;

// Apply the styles to the header element
const headerElement = document.querySelector('.column.is-one-quarter');
headerElement.setAttribute('css', headerStyles);

// Define the CSS styles for the main content
const mainContentStyles = css`
  padding: 20px;
`;

// Apply the styles to the main content element
const mainContentElement = document.querySelector('.main-content');
mainContentElement.setAttribute('css', mainContentStyles);