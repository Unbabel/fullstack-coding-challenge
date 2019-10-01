import React from 'react';
import Translation from '../translation/Translation';

const statusMapper = {
  new: 'badge-pending',
  translating: 'badge-pending',
  canceled: 'badge-danger',
  failed: 'badge-danger',
  rejected: 'badge-danger',
  accepted: 'badge-success',
  completed: 'badge-success',
};

const TranslationList = props => {
  const translations = props.translations.map(translation => (
    <Translation
      status={translation.status}
      badgeClass={statusMapper[translation.badgeClass]}
      originalText={translation.originalText}
      translatedText={translation.translatedText}
      sourceLanguage={translation.sourceLanguage}
      targetLanguage={translation.targetLanguage}
    ></Translation>
  ));

  return (
    <div className="flex flex-col bg-gray-100">
      <div className="bg-white px-4 py-3 border border-l-0 border-r-0 text-sm text-gray-600">
        {translations.length} translations
      </div>
      {translations}
    </div>
  );
};

export default TranslationList;
