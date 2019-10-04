import PropTypes from 'prop-types';
import React from 'react';
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

const Translation = ({ translation }) => {
  const translatedText = translation.translated_text ? (
    translation.translated_text
  ) : (
    <PulseLoader sizeUnit="px" size={5} color="#5a67d8" loading />
  );
  return (
    <Flipped flipId={translation.uid}>
      <div className="flex flex-col bg-white hover:bg-gray-200 border border-l-0 border-r-0 border-t-0">
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
        <div className="flex flex-col lg:flex-row py-6 items-baseline leading-relaxed">
          <div className="flex-1 flex text-gray-600 px-5 lg:px-6 lg:mt-0">
            {translation.text}
          </div>
          <div
            className={`flex-1 flex items-center mt-6 text-gray-800 px-5 lg:mt-0 lg:px-6 ${
              !translation.translated_text ? 'justify-center' : ''
            }`}
          >
            {translatedText}
          </div>
        </div>
      </div>
    </Flipped>
  );
};

Translation.propTypes = {
  translation: PropTypes.object,
};

export default Translation;
