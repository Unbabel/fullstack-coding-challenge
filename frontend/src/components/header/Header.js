import React from 'react';
import logo from '../../assets/images/unbabel-logo.svg';

const Header = () => (
  <header className="bg-indigo-600 flex items-center justify-baseline px-4 py-3 w-full">
    <div>
      <img className="h-6" src={logo} alt="Unbabel"></img>
    </div>
  </header>
);

export default Header;
