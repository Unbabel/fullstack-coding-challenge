import PropTypes from 'prop-types';
import React from 'react';
import { Flipped } from 'react-flip-toolkit';
import PulseLoader from 'react-spinners/PulseLoader';
import { shortnameToName } from '../../../utilities';

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
      <div className="px-4 py-3 flex flex-col bg-white hover:bg-gray-100 border border-l-0 border-r-0 border-t-0">
        <div className="flex items-baseline justify-between mb-1">
          <span className="text-gray-500 text-sm">
            {shortnameToName(translation.source_language)} &rarr;{' '}
            {shortnameToName(translation.target_language)}
          </span>
          <span className={`badge ${statusMapper[translation.status]}`}>
            {translation.status}
          </span>
        </div>
        <div className="mt-2">
          <div className="text-gray-600">{translation.text}</div>
          <div className="mt-2 text-indigo-700">{translatedText}</div>
        </div>
      </div>
    </Flipped>
  );
};

Translation.propTypes = {
  translation: PropTypes.object,
};

export default Translation;
