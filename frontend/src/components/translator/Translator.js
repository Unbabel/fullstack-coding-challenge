import React, { useState } from 'react';
import LanguageBar from './language-bar/LanguageBar';

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
    </div>
  );
};

export default Translator;
