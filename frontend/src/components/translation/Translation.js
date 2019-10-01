import React from 'react';

const Translation = props => (
  <div className="px-4 py-3 flex flex-col bg-white border border-l-0 border-r-0 border-t-0">
    <div className="flex items-baseline justify-between">
      <span className="text-gray-500 text-sm">English &rarr; Spanish</span>
      <span className="inline-block bg-teal-200 text-teal-800 text-xs px-2 rounded-full font-semibold">
        {props.status}
      </span>
    </div>
    <div className="mt-2">
      <div className="text-gray-600">Original text...</div>
      <div className="mt-2 text-indigo-700">Translated text...</div>
    </div>
  </div>
);

export default Translation;
