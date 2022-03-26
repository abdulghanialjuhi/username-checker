import React from 'react'
import Button from '../../tools/Button'
import InputField from './InputField'
import './styles/form.css'

export default function UserForm({ handleOnSubmit, inputRef }) {

  return (
    <form onSubmit={handleOnSubmit}>
        <div className='form-container'>
            <div className='input-field-container'>
                <InputField required={true} inputRef={inputRef} placeHolder='ابحث عن اسم المستخدم' />
            </div>
            <div className='submit-button'>
               <Button text=' بحث ' onSubmit={handleOnSubmit} />
            </div>
        </div>
    </form>
  )
}
