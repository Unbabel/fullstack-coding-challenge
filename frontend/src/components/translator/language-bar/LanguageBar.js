import React from 'react';
import LanguageSelector from './language-selector/LanguageSelector';
import SwapLanguageButton from './swap-language-button/SwapLanguageButton';

const languageMap = {
  es: 'spanish',
  en: 'english',
};

const LanguageBar = props => (
  <div className="flex bg-indigo-100 justify-between items-center py-3">
    <LanguageSelector>{languageMap[props.sourceLanguage]}</LanguageSelector>
    <SwapLanguageButton onClick={props.onClick}></SwapLanguageButton>
    <LanguageSelector>{languageMap[props.targetLanguage]}</LanguageSelector>
  </div>
);

export default LanguageBar;
