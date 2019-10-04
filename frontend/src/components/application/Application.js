import React from 'react';
import Header from '../header/Header';
import Translator from '../translator/Translator';

const Application = () => (
  <div className="bg-gray-200 h-full flex flex-col items-center min-h-screen">
    <Header></Header>
    <Translator></Translator>
  </div>
);

export default Application;
