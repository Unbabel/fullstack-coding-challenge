import PropTypes from 'prop-types';
import React from 'react';
import BarLoader from 'react-spinners/BarLoader';

const TranslatorText = ({
  handleChange,
  handleClear,
  handleKeyDown,
  handleSubmit,
  loading,
  translationText,
}) => (
  <div className="shadow bg-white flex pt-3 h-40 flex flex-col">
    <form className="flex w-full h-full px-4" onSubmit={handleSubmit}>
      <textarea
        placeholder="Translate..."
        className="text-gray-800 text-xl flex-1 p-2 m-1 bg-transparent resize-none max-h-full focus:outline-none"
        value={translationText}
        onChange={handleChange}
        disabled={loading}
        onKeyDown={event => {
          handleKeyDown(event);
        }}
      ></textarea>
      <div className="ml-1 flex flex-col items-center justify-between">
        {translationText.length ? (
          <button
            type="button"
            className="block transition text-gray-500 hover:text-gray-600 focus:outline-none"
            onClick={handleClear}
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              className="h-6 w-6 fill-current"
            >
              <path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z" />
              <path d="M0 0h24v24H0z" fill="none" />
            </svg>
          </button>
        ) : null}
        {translationText.length ? (
          <button
            type="submit"
            className="block transition text-gray-500 hover:text-gray-600 focus:outline-none"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              className="h-6 w-6 fill-current"
            >
              <path fill="none" d="M0 0h24v24H0V0z" />
              <path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" />
            </svg>
          </button>
        ) : null}
      </div>
    </form>
    <div className="flex text-sm text-gray-500 mt-3 mb-3 pr-4 justify-end">
      {translationText.length} / 5000
    </div>
    <div className={`w-full ${loading ? 'opacity-100' : 'opacity-0'}`}>
      <BarLoader color="#5a67d8" css="width: 100%" loading></BarLoader>
    </div>
  </div>
);

TranslatorText.propTypes = {
  handleChange: PropTypes.func,
  handleClear: PropTypes.func,
  handleKeyDown: PropTypes.func,
  handleSubmit: PropTypes.func,
  loading: PropTypes.bool,
  translationText: PropTypes.string,
};

export default TranslatorText;
