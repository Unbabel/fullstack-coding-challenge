import React, { useState } from 'react';
import LanguageBar from './language-bar/LanguageBar';
import TranslatorText from './translator-text/TranslatorText';

const Translator = () => {
  const [sourceLanguage, setSourceLanguage] = useState('en');
  const [targetLanguage, setTargetLanguage] = useState('es');

  const swapLanguage = () => {
    const source = sourceLanguage;
    const target = targetLanguage;
    setSourceLanguage(target);
    setTargetLanguage(source);
  };
  return (
    <div>
      <LanguageBar
        sourceLanguage={sourceLanguage}
        targetLanguage={targetLanguage}
        onClick={swapLanguage}
      ></LanguageBar>
      <TranslatorText></TranslatorText>
    </div>
  );
};

export default Translator;
