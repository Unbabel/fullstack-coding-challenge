import React from 'react';

const SwapLanguageButton = props => (
  <button onClick={props.onClick} type="button" className="block text-gray-600">
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

export default SwapLanguageButton;
