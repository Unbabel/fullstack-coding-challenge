import PropTypes from 'prop-types';
import React from 'react';

const LanguageSelector = ({ children }) => (
  <div className="text-gray-700 flex text-center items-center justify-center w-1/2 uppercase font-medium tracking-normal truncate">
    {children}
  </div>
);

LanguageSelector.propTypes = {
  children: PropTypes.string,
};

export default LanguageSelector;
