import React, { useState } from 'react';
import LanguageBar from './language-bar/LanguageBar';
import TranslatorText from './translator-text/TranslatorText';

const Translator = () => {
  const [sourceLanguage, setSourceLanguage] = useState('en');
  const [targetLanguage, setTargetLanguage] = useState('es');
  const [translationText, setTranslationText] = useState('');

  const swapLanguage = () => {
    const source = sourceLanguage;
    const target = targetLanguage;
    setSourceLanguage(target);
    setTargetLanguage(source);
  };

  const handleTextChange = event => {
    setTranslationText(event.target.value);
  };

  const handleTextSubmit = event => {
    event.preventDefault();
    if (!translationText) {
      return;
    }
    alert(`Translation for text "${translationText}" was submitted.`);
  };

  const handleTextClear = event => {
    event.preventDefault();
    if (!translationText) {
      return;
    }
    setTranslationText('');
  };

  return (
    <div>
      <LanguageBar
        sourceLanguage={sourceLanguage}
        targetLanguage={targetLanguage}
        onClick={swapLanguage}
      ></LanguageBar>
      <TranslatorText
        translationText={translationText}
        handleChange={handleTextChange}
        handleSubmit={handleTextSubmit}
        handleClear={handleTextClear}
      ></TranslatorText>
    </div>
  );
};

export default Translator;
