import axios from 'axios';
import React, { useEffect, useState } from 'react';
import TranslationList from '../translation-list/TranslationList';
import LanguageBar from './language-bar/LanguageBar';
import TranslatorText from './translator-text/TranslatorText';

const Translator = () => {
  const [sourceLanguage, setSourceLanguage] = useState('en');
  const [targetLanguage, setTargetLanguage] = useState('es');
  const [translationText, setTranslationText] = useState('');
  const [translationList, setTranslationList] = useState([]);

  const swapLanguage = () => {
    const source = sourceLanguage;
    const target = targetLanguage;
    setSourceLanguage(target);
    setTargetLanguage(source);
  };

  const handleTextChange = event => {
    setTranslationText(event.target.value);
  };

  const handleTextSubmit = async event => {
    event.preventDefault();
    if (!translationText) {
      return;
    }
    const response = await axios.post('/translations/', {
      text: translationText,
      source_language: sourceLanguage,
      target_language: targetLanguage,
    });
    const newTranslation = response.data;

    setTranslationText('');
    setTranslationList(oldList => [newTranslation, ...oldList]);
  };

  const handleKeyDown = event => {
    if (event.key === 'Enter' && event.shiftKey === false) {
      event.preventDefault();
      handleTextSubmit(event);
    }
  };

  const handleTextClear = event => {
    event.preventDefault();
    if (!translationText) {
      return;
    }
    setTranslationText('');
  };

  useEffect(() => {
    let didCancel = false;

    async function fetchTranslations() {
      const response = await axios.get('/translations/');
      if (!didCancel) {
        // Ignore if we started fetching something else
        setTranslationList(response.data);
      }
    }

    fetchTranslations();
    return () => {
      didCancel = true;
    };
  }, []);

  return (
    <React.Fragment>
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
          handleKeyDown={handleKeyDown}
        ></TranslatorText>
      </div>
      <div>
        <TranslationList translations={translationList}></TranslationList>
      </div>
    </React.Fragment>
  );
};

export default Translator;
