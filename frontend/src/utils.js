const shortnameMapper = {
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

export const shortnameToName = shortname => shortnameMapper[shortname];

export const sortByTranslatedText = (a, b) => {
  if (!a.translated_text) {
    a.translated_text = '';
  }

  if (!b.translated_text) {
    b.translated_text = '';
  }

  return b.translated_text.length - a.translated_text.length;
};
