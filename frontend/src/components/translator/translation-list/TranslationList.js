import PropTypes from 'prop-types';
import React from 'react';
import Translation from '../translation/Translation';

const TranslationList = ({ translations }) => {
  const translationList = translations.map(translation => (
    <Translation key={translation.uid} translation={translation}></Translation>
  ));

  return (
    <div className="flex flex-col bg-gray-100">
      <div className="bg-white px-4 py-3 border border-l-0 border-r-0 lg:border-t-0 text-sm text-gray-600">
        {translationList.length} translations
      </div>
      {translationList}
    </div>
  );
};

TranslationList.propTypes = {
  translations: PropTypes.array,
};

export default TranslationList;
