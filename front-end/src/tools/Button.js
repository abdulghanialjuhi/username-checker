import React from 'react'

export default function Button({ text, onSubmit, loading=false }) {

  return (
    <div className='button-conatiner'>
        <input type="submit" disabled={loading} value={text} onSubmit={onSubmit} />
    </div>
  )
}
