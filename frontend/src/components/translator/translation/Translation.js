import PropTypes from 'prop-types';
import React, { useState } from 'react';
import { Flipped } from 'react-flip-toolkit';
import PulseLoader from 'react-spinners/PulseLoader';
import { shortnameToFlag, shortnameToName } from '../../../utilities';

const statusMapper = {
  new: 'badge-new',
  translating: 'badge-pending',
  canceled: 'badge-danger',
  failed: 'badge-danger',
  rejected: 'badge-danger',
  accepted: 'badge-success',
  completed: 'badge-success',
};

const Translation = ({ translation, deleteTranslation, deleteLoading }) => {
  const [showDelete, setShowDelete] = useState(false);

  const translatedText = translation.translated_text ? (
    translation.translated_text
  ) : (
    <PulseLoader sizeUnit="px" size={5} color="#5a67d8" loading />
  );

  return (
    <Flipped flipId={translation.uid}>
      <div
        onMouseEnter={() => setShowDelete(true)}
        onMouseLeave={() => setShowDelete(false)}
        className="flex flex-col transition transition-bg bg-white hover:bg-gray-200 border border-l-0 border-r-0 border-t-0"
      >
        <div className="px-4 py-3 flex items-baseline justify-between mb-1 bg-gray-100">
          <span className="text-gray-500 text-sm">
            <span className="mr-2 inline-block">
              {shortnameToFlag(translation.source_language)}
            </span>
            <span className="hidden lg:inline-block">
              {shortnameToName(translation.source_language)}
            </span>
            &rarr;
            <div className="mx-2 inline-block">
              {shortnameToFlag(translation.target_language)}
            </div>
            <span className="hidden lg:inline-block">
              {shortnameToName(translation.target_language)}
            </span>
          </span>
          <span className={`badge ${statusMapper[translation.status]}`}>
            {translation.status}
          </span>
        </div>
        <div className="flex flex-col relative lg:flex-row py-6 leading-relaxed px-5 lg:px-6">
          <div className="flex-1 flex text-gray-600 lg:mt-0 lg:mr-5">
            {translation.text}
          </div>
          <div
            className={`flex-1 flex items-center lg:ml-5 mt-6 text-gray-800 lg:mt-0 ${
              !translation.translated_text ? 'justify-center' : ''
            }`}
          >
            {translatedText}
          </div>
          <button
            type="button"
            onClick={() => deleteTranslation(translation.uid)}
            className={`transition block absolute right-0 px-3 py-2 bg-red-200 text-red-800 rounded -mt-4 mr-3 shadow-lg focus:outline-none hover:bg-red-300 active:shadow w-20 ${
              showDelete ? 'opacity-100' : 'opacity-0'
            }`}
          >
            {deleteLoading ? (
              <PulseLoader sizeUnit="px" size={5} color="#9b2c2c" loading />
            ) : (
              'Delete'
            )}
          </button>
        </div>
      </div>
    </Flipped>
  );
};

Translation.propTypes = {
  translation: PropTypes.object,
  deleteTranslation: PropTypes.func,
  deleteLoading: PropTypes.bool,
};

export default Translation;
