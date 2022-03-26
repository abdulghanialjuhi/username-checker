import React, { useContext, useRef, useState } from 'react'
import LayOut from '../../tools/LayOut'
import UserForm from '../form/UserForm'
import './styles/home.css'
import SocialMedia from '../social-medias/SocialMedia'
import Context from '../../context/Context'
import Social from '../../images/social1.svg'

export default function Home() {

    const inputRef = useRef()
    const [showSocial, setShowSocial] = useState(false)

    const { smoothScroll, checkUserNames } = useContext(Context)
    
    const handleOnSubmit = (e) => {
      e.preventDefault()

      setShowSocial(true)
      checkUserNames(inputRef.current.value)
      
      smoothScroll('.section')
    }

  return (
    <LayOut>

        <div className='app-container'>
          <UserForm handleOnSubmit={handleOnSubmit} inputRef={inputRef} />
          <div className='search-svg-conatainer'>
            <img src={Social} alt="search" />
          </div>
        </div>
       <SocialMedia showSocial={showSocial} inputRef={inputRef} />

    </LayOut>
  )
}
