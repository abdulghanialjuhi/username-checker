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
      if (homePage && openBurger) return 'extend-header home-landing'
      else if (homePage && !openBurger) return 'home-landing'
      else if (!homePage && openBurger) return 'extend-header'
      
      return null
  }

  return (
    <div className={`header-container ${getClassName()}`}>
        <div className='inner-header-container'>
            <div className={`nav-bar-container ${openBurger && 'extend-bar'}`}>
                <HeaderBar SetOpenBurger={SetOpenBurger} openBurger={openBurger} />
            </div>

           {homePage && 
              <div className='home-title-container'>
                    <div className='inner-title-container'>
                        <h1> هوية واحدة لجميع منصاتك الإجتماعية </h1>
                        <div className='paragraph-container'>
                            <p> اجعل هويتك موحدة في جميع مواقع التواصل الإجتماعي بضغطة زر واحدة فقط </p>
                        </div>
                    </div>
                        <FiTwitter strokeWidth='1' size='10%' className='twitter-icon' />
                        <FiInstagram strokeWidth='1' size='10%' className='instagram-icon' />
                </div>
            }

        </div>
    </div>
  )
}

