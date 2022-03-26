import React from 'react'
import { GiHamburgerMenu } from 'react-icons/gi'
import { useNavigate, useLocation } from 'react-router-dom'

export default function HeaderBar({ SetOpenBurger, openBurger }) {

  const handleOpenBurger = () => {
    SetOpenBurger(!openBurger)
  }

  const location = useLocation();
  const isContact = location.pathname === '/contact' ? true : false
  const navigate = useNavigate()

  return (
    <>
      <div className='inner-container-div'>
        <div onClick={() => navigate('/home')} className='home-brand-container'>
          <h5>تواصُل</h5>    
        </div>
        <div className='burger-icon-container'>
          <div className='icon-container' onClick={handleOpenBurger}>
            <GiHamburgerMenu size={22} />
          </div>
        </div>
      </div>

      <div className='tool-bar-container'>
        <div 
        className={isContact ? 'header-bar-container activa-bar' : 'header-bar-container'} 
        onClick={() => navigate('/contact')}>
            <h4> تواصَل </h4>
        </div>
      </div>
    </>
  )
}
