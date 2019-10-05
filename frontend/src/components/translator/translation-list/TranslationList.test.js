import { shallow } from 'enzyme';
import React from 'react';
import TranslationList from './TranslationList';

it('renders without crashing', () => {
  const div = document.createElement('div');
  shallow(<TranslationList />, div);
});
