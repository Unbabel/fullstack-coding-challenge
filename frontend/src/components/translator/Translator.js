import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { Flipper } from 'react-flip-toolkit';
import { sortByTranslatedText } from '../../utils';
import LanguageBar from './language-bar/LanguageBar';
import TranslationList from './translation-list/TranslationList';
import TranslatorText from './translator-text/TranslatorText';

const eventSource = new EventSource(
  'http://localhost:5000/translations/stream'
);

const Translator = () => {
  const [loading, setLoading] = useState(false);
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
    setLoading(true);
    setTranslationText('');

    const response = await axios.post('/translations/', {
      text: translationText,
      source_language: sourceLanguage,
      target_language: targetLanguage,
    });
    const newTranslation = response.data;

    setTranslationList(oldList =>
      [newTranslation, ...oldList].sort(sortByTranslatedText)
    );
    setLoading(false);
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
    const upsertTranslations = updatedTranslations => {
      const currentTranslations = [...translationList];
      updatedTranslations.forEach(updatedTranslation => {
        const translationIndex = currentTranslations.findIndex(
          x => x.uid === updatedTranslation.uid
        );
        currentTranslations[translationIndex] = updatedTranslation;
      });
      setTranslationList([...currentTranslations].sort(sortByTranslatedText));
    };
    eventSource.onmessage = event => {
      upsertTranslations(JSON.parse(event.data));
    };
  }, [translationList]);

  useEffect(() => {
    let didCancel = false;

    async function fetchTranslations() {
      const response = await axios.get('/translations/');
      if (!didCancel) {
        // Ignore if we started fetching something else
        setTranslationList(response.data.sort(sortByTranslatedText));
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
          loading={loading}
        ></TranslatorText>
      </div>
      <div>
        <Flipper
          flipKey={translationList.map(translation => translation.uid).join('')}
        >
          <TranslationList translations={translationList}></TranslationList>
        </Flipper>
      </div>
    </React.Fragment>
  );
};

export default Translator;
