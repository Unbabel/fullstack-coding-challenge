import { shallow } from 'enzyme';
import React from 'react';
import LanguageBar from './LanguageBar';

it('renders without crashing', () => {
  const div = document.createElement('div');
  shallow(<LanguageBar />, div);
});
