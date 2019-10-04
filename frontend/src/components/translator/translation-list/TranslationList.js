import PropTypes from 'prop-types';
import React from 'react';
import PulseLoader from 'react-spinners/PulseLoader';
import Translation from '../translation/Translation';

const TranslationList = ({ loading, translations }) => {
  const allTranslations = translations.map(translation => (
    <Translation key={translation.uid} translation={translation}></Translation>
  ));
  return (
    <React.Fragment>
      <div
        className={`flex justify-center items-center p-6 ${
          loading ? 'opacity-100' : 'hidden'
        }`}
      >
        <PulseLoader sizeUnit="px" size={5} color="#5a67d8" loading={loading} />
      </div>
      <div
        className={`flex flex-col bg-gray-100 lg:shadow-xl transition transition-slower lg:rounded lg:overflow-hidden ${
          loading ? 'opacity-0' : 'opacity-100'
        }`}
      >
        <div
          className={`flex justify-between bg-white px-4 py-3 border border-l-0 border-r-0 lg:border-t-0 text-sm text-gray-600 transition transition-slower ${
            loading ? 'opacity-0' : 'opacity-100'
          }`}
        >
          <div>{allTranslations.length} translations</div>
          <button
            type="button"
            className="block transition text-gray-500 hover:text-gray-700 focus:outline-none"
          >
            Clear all
          </button>
        </div>
        {allTranslations}
      </div>
    </React.Fragment>
  );
};

TranslationList.propTypes = {
  translations: PropTypes.array,
  loading: PropTypes.bool,
};

export default TranslationList;
