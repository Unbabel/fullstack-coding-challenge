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
