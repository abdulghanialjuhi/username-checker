import React, { useRef } from 'react'
import { useState } from 'react'
import Button from '../../tools/Button'
import httpRequest from '../../tools/httpRequest'
import Loader from '../../tools/Loader'
import Modal from '../../tools/Modal'
import InputField from '../form/InputField'

export default function MailForm() {

    const [animateText, setAnimateText] = useState(false)
    const [loading, setLoading] = useState(false)
    const [openModal, setOpenModal] = useState(false)

    const [responseState, setResponseState] = useState(null)
    const [responseError, setResponseError] = useState(null)

    const nameRef = useRef()
    const emailRef = useRef()
    const titleRef = useRef()
    const messageRef = useRef()

    const handleOnBlur = () => {
        if (!messageRef.current.value > 0) {
            setAnimateText(false)
        }
    }
    
    const handleOnFocus = () => {
        setAnimateText(true)
    }

    const  validateEmail = (mail) => {

        if (/^\w+([-]?\w+)*@\w+([-]?\w+)*(\.\w{2,3})+$/.test(mail)) {
            return true
        }

        setOpenModal(true)
        setResponseError('عذراً، الرجاء إدخال بريد إلكتروني صالح')
        return false
    }

    const handleSendEmail = (e) => {
        e.preventDefault()

        setResponseState(null)
        setResponseError(null)

        if (!validateEmail(emailRef.current.value.replace(/ /g, ""))){
            return false
        }

        setLoading(true)


        let fd = new FormData()

        fd.append('name', nameRef.current.value)
        fd.append('email', emailRef.current.value)
        fd.append('subject', titleRef.current.value)
        fd.append('message', messageRef.current.value)

        httpRequest.post('/send_email', fd)
        .then((res) => {
            setOpenModal(true)
            setResponseState(res.data)
            setLoading(false)
            nameRef.current.value = ''
            emailRef.current.value = ''
            titleRef.current.value = ''
            messageRef.current.value = ''
        })
        .catch((err) => {
            setOpenModal(true)
            setLoading(false)
            setResponseError(err.response.data)
            console.log(err)
        })
        
    }

  return (
    <div className='mail-form-container'>
        <div className='form-title'>
            <h3>تواصل معنا  </h3>
        </div>
        <div className='input-form-container'>
            <form onSubmit={handleSendEmail}>
            <div className='form-field-container'>
                <InputField required={true} inputRef={nameRef}  placeHolder='الاسم' />
            </div>

            <div className='form-field-container'>
                <InputField required={true}inputRef={emailRef}  placeHolder='البريد الإلكتروني' />
            </div>

            <div className='form-field-container'>
                <InputField  inputRef={titleRef}  placeHolder='العنوان' />
            </div>

            <div className={animateText ?'textarea-field-container show-textarea' : 'textarea-field-container'}>
                <h6 className={animateText ? 'animate-place-holder' : 'place-holder'} > الرسالة </h6>
                <textarea required ref={messageRef} rows="7" cols="70" onChange={handleOnFocus} onBlur={handleOnBlur} onFocus={handleOnFocus} />
                
            </div>

            <div className='email-submit-container'>
            {!loading ? <Button loading={loading} text='إرسال' onSubmit={handleSendEmail} />
                : <Loader />}
            </div>

            </form>
        </div>

        {/*  modal content  */}

        <Modal
         openModal={openModal}
        setOpenModal={setOpenModal}>
            <div onClick={(e) => e.stopPropagation()} className='modal-inner-conatiner'>
                <div className='modal-header-container'>
                    <h4> {responseState} {responseError} </h4>
                </div>
                {!responseError &&
                 <div className='body-modal-container'>
                    <h4>
                        شكراً لك على دعمك.
                    </h4>
                </div>}
            </div>
        </Modal>
    </div>
  )
}
