import React from 'react';
import HomeIcon from './icons/HomeIcon';
import SearchIcon from './icons/SearchIcon';
import AddIcon from './icons/AddIcon';
import HeartIcon from './icons/HeartIcon';
import PersonIcon from './icons/PersonIcon';

function Navbar() {
  return (
    <nav className="navbar navbar-dark bg-info navbar-expand fixed-bottom rounded mb-2 ms-3 me-3">
      <ul className="navbar-nav nav-justified w-100">
        <li className="nav-item">
          <a href="#" className="nav-link">
            <HomeIcon />
          </a>
        </li>
        <li className="nav-item">
          <a href="#" className="nav-link">
            <SearchIcon />
          </a>
        </li>
        <li className="nav-item">
          <a href="#" className="nav-link">
            <AddIcon />
          </a>
        </li>
        <li className="nav-item">
          <a href="#" className="nav-link">
            <HeartIcon />
          </a>
        </li>
        <li className="nav-item">
          <a href="#" className="nav-link">
            <PersonIcon />
          </a>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
