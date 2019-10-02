import React from 'react';
import logo from '../../assets/images/unbabel-logo.svg';

const Header = () => (
  <header className="bg-indigo-600 flex items-center justify-between px-4 py-3">
    <div>
      <button
        type="button"
        className="block text-gray-100 hover:text-white focus:outline-none"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          className="h-6 w-6 fill-current"
          viewBox="0 0 24 24"
        >
          <path d="M0 0h24v24H0z" fill="none" />
          <path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z" />
        </svg>
      </button>
    </div>
    <div>
      <img className="h-6" src={logo} alt="Unbabel"></img>
    </div>
  </header>
);

export default Header;
