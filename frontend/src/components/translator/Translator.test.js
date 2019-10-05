import { shallow } from 'enzyme';
import React from 'react';
import Translator from './Translator';

it('renders without crashing', () => {
  const div = document.createElement('div');
  shallow(<Translator />, div);
});
