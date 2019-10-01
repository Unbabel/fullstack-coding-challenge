import React from 'react';
import { shortnameToName } from '../../utils';

const Translation = props => {
  const translatedText = props.translatedText
    ? props.translatedText
    : 'Translating...';
  return (
    <div className="px-4 py-3 flex flex-col bg-white hover:bg-gray-100 border border-l-0 border-r-0 border-t-0">
      <div className="flex items-baseline justify-between">
        <span className="text-gray-500 text-sm">
          {shortnameToName(props.sourceLanguage)} &rarr;{' '}
          {shortnameToName(props.targetLanguage)}
        </span>
        <span className={`badge ${props.badgeClass}`}>{props.status}</span>
      </div>
      <div className="mt-2">
        <div className="text-gray-600">{props.originalText}</div>
        <div className="mt-2 text-indigo-700">{translatedText}</div>
      </div>
    </div>
  );
};

export default Translation;
