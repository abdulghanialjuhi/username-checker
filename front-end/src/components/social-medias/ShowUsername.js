import React, { useContext } from 'react'
import Card from './Card'
import Context from '../../context/Context'


export default function ShowUsername({ username }) {

    const { platforms } = useContext(Context)

  return (
    <div className='social-username-conainer'>
        <div className='display-platform'>
          <div className='inner-platform-container'>
            {platforms.map((platform) => (
              <Card key={platform.name} platform={platform} username={username} />
            ))}
          </div>
        </div>
    </div>
  )
}
