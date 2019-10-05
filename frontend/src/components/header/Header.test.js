import { shallow } from 'enzyme';
import React from 'react';
import Header from './Header';

it('renders without crashing', () => {
  const div = document.createElement('div');
  shallow(<Header />, div);
});
