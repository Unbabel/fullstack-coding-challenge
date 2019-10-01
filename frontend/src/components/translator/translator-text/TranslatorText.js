import React from 'react';

const TranslatorText = props => (
  <div className="shadow flex px-4 py-3 h-32">
    <form className="flex w-full" onSubmit={props.handleSubmit}>
      <textarea
        placeholder="Translate..."
        className="text-grey-darkest text-xl flex-1 p-2 m-1 bg-transparent resize-none max-h-full"
        value={props.translationText}
        onChange={props.handleChange}
      ></textarea>
      <div className="ml-1 flex flex-col items-center justify-between">
        <button type="button" className="block" onClick={props.handleClear}>
          X
        </button>
        <button type="submit" className="block">
          >
        </button>
      </div>
    </form>
  </div>
);

export default TranslatorText;
