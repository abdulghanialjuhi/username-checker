import React, { useEffect, useState } from 'react';
import { Portal } from 'react-portal';
import './styles/tools.css'

export default function Modal({ children, setOpenModal, openModal }) {

  const [transtion, setTranstion] = useState(false)

  useEffect(() => {
    if (openModal === false) {
      document.body.classList.remove('modal-open');

      setTimeout(() => setTranstion(false), 500)
      
    } else if (openModal === true) {
      document.body.classList.add('modal-open');
      setTranstion(true)
    }

  },[openModal])

  return (
    <>
      {
      transtion && <Portal node={document && document.getElementById('root')} >
        <div onClick={() =>  setOpenModal(false)} className={openModal ? 'full-payload' :  'full-payload hide-modal'}>
            {children}
        </div>
        </Portal>
        }
      </>
    );
}
