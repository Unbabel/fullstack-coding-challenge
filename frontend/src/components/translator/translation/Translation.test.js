import { shallow } from 'enzyme';
import React from 'react';
import Translation from './Translation';

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

describe('<Translation/>', () => {
  it('renders without crashing', () => {
    shallow(<Translation translation={translation}></Translation>);
  });

  it('is deleted properly on click', () => {
    const mockOnClick = jest.fn();
    const wrapper = shallow(
      <Translation
        translation={translation}
        deleteTranslation={mockOnClick}
      ></Translation>
    );
    const button = wrapper.find('button[data-test="delete-translation"]');
    button.simulate('click');
    expect(mockOnClick.mock.calls.length).toEqual(1);
    expect(mockOnClick).toBeCalledWith(translation.uid);
  });

  it('shows delete button on mouseover', () => {
    const wrapper = shallow(
      <Translation translation={translation}></Translation>
    );
    const button = wrapper.find('button[data-test="delete-translation"]');
    wrapper.simulate('mouseEnter');
    expect(button.hasClass('opacity-100')).toBe(true);

    wrapper.simulate('mouseLeave');
    expect(button.hasClass('opacity-0')).toBe(true);
  });
});
