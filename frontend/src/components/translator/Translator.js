import React, { useState } from 'react';
import TranslationList from '../translation-list/TranslationList';
import LanguageBar from './language-bar/LanguageBar';
import TranslatorText from './translator-text/TranslatorText';

const translations = [
  {
    sourceLanguage: 'English',
    targetLanguage: 'Spanish',
    originalText: 'Original text...',
    translatedText: 'Translated text...',
    status: 'new',
    badgeClass: 'new',
  },
  {
    sourceLanguage: 'English',
    targetLanguage: 'Spanish',
    originalText: 'Original text...',
    translatedText: 'Translated text...',
    status: 'translating',
    badgeClass: 'translating',
  },
  {
    sourceLanguage: 'English',
    targetLanguage: 'Spanish',
    originalText: 'Original text...',
    translatedText: 'Translated text...',
    status: 'completed',
    badgeClass: 'completed',
  },
  {
    sourceLanguage: 'English',
    targetLanguage: 'Spanish',
    originalText: 'Original text...',
    translatedText: 'Translated text...',
    status: 'failed',
    badgeClass: 'failed',
  },
  {
    sourceLanguage: 'English',
    targetLanguage: 'Spanish',
    originalText: 'Original text...',
    translatedText: 'Translated text...',
    status: 'canceled',
    badgeClass: 'canceled',
  },
  {
    sourceLanguage: 'English',
    targetLanguage: 'Spanish',
    originalText: 'Original text...',
    translatedText: 'Translated text...',
    status: 'accepted',
    badgeClass: 'accepted',
  },
  {
    sourceLanguage: 'English',
    targetLanguage: 'Spanish',
    originalText: 'Original text...',
    translatedText: 'Translated text...',
    status: 'rejected',
    badgeClass: 'rejected',
  },
];

const Translator = () => {
  const [sourceLanguage, setSourceLanguage] = useState('en');
  const [targetLanguage, setTargetLanguage] = useState('es');
  const [translationText, setTranslationText] = useState('');
  const [translationList, setTranslationList] = useState(translations);

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
    const newTranslation = {
      originalText: translationText,
      translatedText: '...',
      status: 'new',
      badgeClass: 'new',
      sourceLanguage,
      targetLanguage,
    };

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
