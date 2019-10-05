import { shallow } from 'enzyme';
import React from 'react';
import SwapLanguageButton from './SwapLanguageButton';

it('renders without crashing', () => {
  const div = document.createElement('div');
  shallow(<SwapLanguageButton />, div);
});
