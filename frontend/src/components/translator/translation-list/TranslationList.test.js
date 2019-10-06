import { shallow } from 'enzyme';
import React from 'react';
import TranslationList from './TranslationList';

const translation = {
  created_at: '2019-10-05T22:12:33.323691',
  source_language: 'en',
  status: 'completed',
  target_language: 'es',
  text: 'Test',
  text_format: 'text',
  translated_text: 'Prueba',
  uid: '5d4747be79',
  updated_at: '2019-10-05T22:12:50.846814',
};

describe('<TranslationList/>', () => {
  it('renders without crashing', () => {
    const wrapper = shallow(
      <TranslationList translations={[translation]}></TranslationList>
    );
    const button = wrapper.find('button');
    expect(button.text()).toEqual('Clear all');
  });
});
