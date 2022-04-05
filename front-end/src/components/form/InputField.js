import React, { useState } from 'react'

export default function InputField({ inputRef, placeHolder, required = false }) {

  const [animateText, setAnimateText] = useState(false)

  const handleOnBlur = () => {
    if (!inputRef.current.value > 0) {
        setAnimateText(false)
    }
  }

  const handleOnFocus = () => {
    setAnimateText(true)
  }

  return (
    <div className={`input-container ${animateText && 'show'}`}>   
      <h6 className={animateText ? 'animate-place-holder' : 'place-holder'} > {placeHolder} </h6>
          <input ref={inputRef} required={required} type="text" onChange={handleOnFocus} onBlur={handleOnBlur} onFocus={handleOnFocus} />
    </div>
  )
}
