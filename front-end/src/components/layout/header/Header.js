import React, { useState } from 'react'
import './styles/header.css'
import { FiTwitter, FiInstagram } from 'react-icons/fi'
import HeaderBar from './HeaderBar'
import { useLocation } from 'react-router-dom'

export default function Header() {
  const [openBurger, SetOpenBurger] = useState(false)

  const location = useLocation();

  const homePage = location.pathname === '/home' ? true : false

  const getClassName = () => {
      if (homePage && openBurger) return 'header-container extend-header home-landing'
        else if (homePage && !openBurger) return 'header-container home-landing'
          else if (!homePage && openBurger) return 'header-container extend-header'
            else if (!homePage && !openBurger) return 'header-container'
  }

  return (
    <div className={getClassName()}>
        <div className='inner-header-container'>
            <div className={openBurger ? 'nav-bar-container extend-bar' : 'nav-bar-container'}>
                <HeaderBar SetOpenBurger={SetOpenBurger} openBurger={openBurger} />
            </div>
           {homePage && <div className='home-title-container'>
                <div className='inner-title-container'>
                    <h1> هوية واحدة لجميع منصاتك الإجتماعية </h1>
                    <div className='paragraph-container'>
                        <p> اجعل هويتك موحدة في جميع مواقع التواصل الإجتماعي بضغطة زر واحدة فقط </p>
                    </div>
                </div>
                    <FiTwitter strokeWidth='1' size='10%' className='twitter-icon' />
                    <FiInstagram strokeWidth='1' size='10%' className='instagram-icon' />
            </div>}
        </div>
    </div>
  )
}

