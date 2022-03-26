import React from 'react'
import './styles/footer.css'
import { FiTwitter, FiGithub } from 'react-icons/fi'


export default function Footer() {
  return (
    <div className='footer-contaienr'>
      <div className='inner-footer-contaienr'>

        <div className='copy-right-container'>
            <h5> &copy; تواصل 2022 </h5>
        </div>
        <div className='social-media-footer-container'>
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
        
      </div>
    </div>
  )
}
