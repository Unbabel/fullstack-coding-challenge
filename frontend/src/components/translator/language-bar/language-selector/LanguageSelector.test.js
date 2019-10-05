import { shallow } from 'enzyme';
import React from 'react';
import LanguageSelector from './LanguageSelector';

it('renders without crashing', () => {
  const div = document.createElement('div');
  shallow(<LanguageSelector />, div);
});
