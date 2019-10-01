import React from 'react';
import Translation from '../translation/Translation';

const statusMapper = {
  new: 'badge-pending',
  translating: 'badge-pending',
  canceled: 'badge-danger',
  failed: 'badge-danger',
  rejected: 'badge-danger',
  accepted: 'badge-success',
  completed: 'badge-success',
};

const TranslationList = () => (
  <div className="flex flex-col bg-gray-100">
    <div className="bg-white px-4 py-3 border border-l-0 border-r-0 text-sm text-gray-600">
      7 translations
    </div>
    <Translation status="new" badgeClass={statusMapper.new} />
    <Translation status="translating" badgeClass={statusMapper.translating} />
    <Translation status="completed" badgeClass={statusMapper.completed} />
    <Translation status="failed" badgeClass={statusMapper.failed} />
    <Translation status="canceled" badgeClass={statusMapper.canceled} />
    <Translation status="accepted" badgeClass={statusMapper.accepted} />
    <Translation status="rejected" badgeClass={statusMapper.rejected} />
  </div>
);

export default TranslationList;
