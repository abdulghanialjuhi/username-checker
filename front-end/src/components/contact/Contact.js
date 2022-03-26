import React from 'react'
import LayOut from '../../tools/LayOut'
import './styles/contact.css'
import { FiTwitter, FiGithub } from 'react-icons/fi'
import MailForm from './MailForm'
import emailSvg from '../../images/email.svg'

export default function Contact() {
   
  return (
      <LayOut>

        <div className='contact-main-conatainer'>
            <div className='contact-inner-container'>
                <div className='social-media-icons'>
                    <div>
                        <a href='https://twitter.com/abdulghani_18' target="_blank" rel="noreferrer" >
                            <FiTwitter strokeWidth={1} size={24} />
                        </a>
                    </div>
                    <div>
                        <a href= 'https://github.com/abdulghanialjuhi' target="_blank" rel="noreferrer" >
                            <FiGithub strokeWidth={1} size={24} />
                        </a>
                    </div>
                </div>
                <MailForm />
            </div>
            <div className='email-svg-container'>  
                <img src={emailSvg} alt='email-pic' />
            </div>
        </div>

      </LayOut>
  )
}
