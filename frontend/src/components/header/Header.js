import React from 'react';

const Header = () => (
  <header className="bg-indigo-600 flex items-center justify-between px-4 py-3">
    <div>
      <button type="button" className="block text-gray-100">
        <svg
          className="h-6 w-6 fill-current"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 20 20"
        >
          <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
        </svg>
      </button>
    </div>
    <div>
      <img className="h-8" src="/" alt="Unbabel"></img>
    </div>
  </header>
);

export default Header;
