import PropTypes from 'prop-types';
import React from 'react';

const SwapLanguageButton = ({ onClick }) => (
  <button
    onClick={onClick}
    type="button"
    className="block text-gray-600 flex justify-center items-center hover:text-gray-700 focus:outline-none"
  >
    <svg className="h-6 w-6 fill-current">
      <defs>
        <path id="a" d="M0 0h24v24H0V0z" />
      </defs>
      <clipPath id="b">
        <use xlinkHref="#a" overflow="visible" />
      </clipPath>
      <path
        clipPath="url(#b)"
        d="M9.01 14H2v2h7.01v3L13 15l-3.99-4v3zm5.98-1v-3H22V8h-7.01V5L11 9l3.99 4z"
      />
    </svg>
  </button>
);

SwapLanguageButton.propTypes = {
  onClick: PropTypes.func,
};

export default SwapLanguageButton;
