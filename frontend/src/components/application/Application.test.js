import { shallow } from 'enzyme';
import React from 'react';
import Application from './Application';

it('renders without crashing', () => {
  const div = document.createElement('div');
  shallow(<Application />, div);
});
