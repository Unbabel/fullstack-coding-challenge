import React from 'react';

const TranslatorText = () => (
  <div className="shadow flex px-4 py-3 h-32">
    <textarea
      placeholder="Translate..."
      className="text-grey-darkest text-xl flex-1 p-2 m-1 bg-transparent resize-none max-h-full"
    >
      Hello, World!
    </textarea>
    <div className="ml-1 flex items-start">
      <button type="button" className="block">
        X
      </button>
    </div>
  </div>
);

export default TranslatorText;
