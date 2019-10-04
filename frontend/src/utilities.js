import React from 'react';
import ReactCountryFlag from 'react-country-flag';

const shortnameToNameMapper = {
  pt: 'Portuguese',
  en: 'English',
  fr: 'French',
  es: 'Spanish',
  'zh-CN': 'Chinese (simplified)',
  ru: 'Russian',
  ar: 'Arabic',
  de: 'German',
  ja: 'Japanese',
  tr: 'Turkish',
  it: 'Italian',
  nl: 'Dutch',
  hi: 'Hindi',
  'es-latam': 'Spanish(Latam)',
};

const shortnameToFlagMapper = {
  en: (
    <ReactCountryFlag
      code="gb-eng"
      svg
      styleProps={{
        width: '17px',
        height: '17px',
      }}
    ></ReactCountryFlag>
  ),
  es: (
    <ReactCountryFlag
      code="es"
      svg
      styleProps={{
        width: '17px',
        height: '17px',
      }}
    ></ReactCountryFlag>
  ),
};

export const shortnameToFlag = shortname => shortnameToFlagMapper[shortname];

export const shortnameToName = shortname => shortnameToNameMapper[shortname];

export const sortByTranslatedText = (a, b) => {
  if (!a.translated_text) {
    a.translated_text = '';
  }

  if (!b.translated_text) {
    b.translated_text = '';
  }

  return b.translated_text.length - a.translated_text.length;
};
