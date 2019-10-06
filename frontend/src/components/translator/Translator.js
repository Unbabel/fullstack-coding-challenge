import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { Flipper } from 'react-flip-toolkit';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { sortByTranslatedText } from '../../utilities';
import LanguageBar from './language-bar/LanguageBar';
import TranslationList from './translation-list/TranslationList';
import TranslatorText from './translator-text/TranslatorText';

const eventSource =
  new EventSource('http://localhost:5000/translations/stream') || undefined;

const Translator = () => {
  const [loadingTranslations, setLoadingTranslations] = useState(true);
  const [loadingNewTranslation, setLoadingNewTranslation] = useState(false);
  const [sourceLanguage, setSourceLanguage] = useState('en');
  const [targetLanguage, setTargetLanguage] = useState('es');
  const [translationText, setTranslationText] = useState('');
  const [translationList, setTranslationList] = useState([]);
  const [deleteLoading, setDeleteLoading] = useState(false);

  const notify = message => toast(`${message}`, { type: 'error' });

  const swapLanguage = () => {
    const source = sourceLanguage;
    const target = targetLanguage;
    setSourceLanguage(target);
    setTargetLanguage(source);
  };

  const handleTextChange = event => {
    if (event.target.value.length > 5000) {
      return;
    }
    setTranslationText(event.target.value);
  };

  const handleTextSubmit = async event => {
    event.preventDefault();
    if (!translationText) {
      return;
    }
    setLoadingNewTranslation(true);

    try {
      const response = await axios.post('/translations/', {
        text: translationText,
        source_language: sourceLanguage,
        target_language: targetLanguage,
      });
      const newTranslation = response.data;

      setTranslationText('');
      setTranslationList(oldList =>
        [newTranslation, ...oldList].sort(sortByTranslatedText)
      );
    } catch (error) {
      notify('Could not submit translation!');
    }
    setLoadingNewTranslation(false);
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

  const deleteTranslation = async translationUid => {
    setDeleteLoading(true);
    const response = await axios.delete(
      `/translations/delete/${translationUid}`
    );

    if (response.data.message === 'success') {
      setTranslationList(oldList =>
        [...oldList].filter(translation => translation.uid !== translationUid)
      );
    } else {
      notify('Could not delete translation!');
    }
    setDeleteLoading(false);
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
    if (eventSource) {
      eventSource.onmessage = event => {
        upsertTranslations(JSON.parse(event.data));
      };
    }
  }, [translationList]);

  useEffect(() => {
    let didCancel = false;

    async function fetchTranslations() {
      try {
        const response = await axios.get('/translations/');
        if (!didCancel) {
          // Ignore if we started fetching something else
          setTranslationList(response.data.sort(sortByTranslatedText));
        }
      } catch (error) {
        notify('Could not fetch translations!');
      }
    }

    fetchTranslations();
    setLoadingTranslations(false);
    return () => {
      didCancel = true;
    };
  }, []);

  return (
    <React.Fragment>
      <div className="lg:max-w-3xl w-full lg:rounded lg:overflow-hidden lg:mt-10 lg:shadow-xl">
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
          loading={loadingNewTranslation}
        ></TranslatorText>
      </div>
      <div className="lg:max-w-3xl w-full lg:my-10">
        <Flipper
          flipKey={translationList.map(translation => translation.uid).join('')}
        >
          <TranslationList
            loading={loadingTranslations}
            translations={translationList}
            deleteTranslation={deleteTranslation}
            deleteLoading={deleteLoading}
          ></TranslationList>
        </Flipper>
      </div>
      <ToastContainer
        position="top-center"
        autoClose={5000}
        hideProgressBar={false}
        newestOnTop
        closeOnClick
        rtl={false}
        pauseOnVisibilityChange
        draggable
        pauseOnHover
      />
    </React.Fragment>
  );
};

export default Translator;
