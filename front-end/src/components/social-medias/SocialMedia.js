import React from 'react'
import './styles/social.css'
import ParagraphSec from './ParagraphSec';
import ShowUsername from './ShowUsername';


export default function SocialMedia({ inputRef, showSocial }) {
  return (
    <section className='section'> 
     {showSocial ? <ShowUsername username={inputRef.current.value} /> :
     <ParagraphSec inputRef={inputRef} />
      }
    </section>
  )
}
