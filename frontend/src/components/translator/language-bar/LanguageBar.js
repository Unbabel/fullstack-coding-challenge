import PropTypes from 'prop-types';
import React from 'react';
import LanguageSelector from './language-selector/LanguageSelector';
import SwapLanguageButton from './swap-language-button/SwapLanguageButton';

const languageMap = {
  es: 'spanish',
  en: 'english',
};

const LanguageBar = ({ onClick, sourceLanguage, targetLanguage }) => (
  <div className="flex bg-indigo-100 justify-between items-center py-3">
    <LanguageSelector>{languageMap[sourceLanguage]}</LanguageSelector>
    <SwapLanguageButton onClick={onClick}></SwapLanguageButton>
    <LanguageSelector>{languageMap[targetLanguage]}</LanguageSelector>
  </div>
);

LanguageBar.propTypes = {
  onClick: PropTypes.func,
  sourceLanguage: PropTypes.string,
  targetLanguage: PropTypes.string,
};

export default LanguageBar;
