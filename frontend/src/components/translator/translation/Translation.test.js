import { shallow } from 'enzyme';
import React from 'react';
import Translation from './Translation';

it('renders without crashing', () => {
  const div = document.createElement('div');
  shallow(<Translation />, div);
});
