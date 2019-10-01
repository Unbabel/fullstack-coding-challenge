import React from 'react';
import Translation from '../translation/Translation';

const TranslationList = () => (
  <div className="flex flex-col bg-gray-100">
    <div className="bg-white px-4 py-3 border border-l-0 border-r-0 text-sm text-gray-600">
      3 translations
    </div>
    <Translation status="new" />
    <Translation status="translating" />
    <Translation status="completed" />
    <Translation status="failed" />
    <Translation status="canceled" />
    <Translation status="accepted" />
    <Translation status="rejected" />
  </div>
);

export default TranslationList;
