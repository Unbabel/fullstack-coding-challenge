import React from 'react';
import Translation from '../translation/Translation';

const TranslationList = props => {
  const translations = props.translations.map(translation => (
    <Translation key={translation.uid} translation={translation}></Translation>
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
