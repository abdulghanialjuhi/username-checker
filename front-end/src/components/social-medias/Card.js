import React from 'react'
import Loader from '../../tools/Loader'

export default function Card({ platform, username }) {

  return (
    <div className={`social-media-card  ${platform.status === false ? 'unavalible' : platform.status && 'avalible'} `}>
        <div className='brand-contaienr'>
        <div className='logo-container'>
            {platform.logo}
        </div>
            {platform.name}
        </div>
        <div className='username-container'>
            <div>
            <h4>  {username} </h4>
            </div>
        </div>
        <div className='username-status-container'>
            {platform.reason !== null ? (
                <h5> {platform.reason} </h5>
            ) : (
                <Loader />
            )} 
        </div>
    </div>
  )
}
