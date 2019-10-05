import { shallow } from 'enzyme';
import React from 'react';
import TranslatorText from './TranslatorText';

it('renders without crashing', () => {
  const div = document.createElement('div');
  shallow(<TranslatorText />, div);
});
