import React, { useContext } from 'react'
import svg from '../../images/search.svg'
import Context from '../../context/Context';

export default function ParagraphSec({ inputRef }) {

  const { smoothScroll } = useContext(Context)

    const handleScrollUp = (e) => {

      e.preventDefault()

      smoothScroll('.header-container')
        inputRef.current.focus()
      }

  return (
    <div className='inner-section-container'>

    <div className='text-section-container'>
      <div className='section-title-container'>
        <h1> هل تبحث عن اسم مستخدم جديد في مواقع التواصل الاجتماعي ؟ </h1>
      </div>
        <div className='svg-small-container'>
          <img src={svg} alt='search' className='svg-small' />
        </div>
        <div className='section-paragraph-container'>
          <p> 
            إذا كنت تبحث عن اسم مستخدم جديد لجميع حساباتك في مواقع التواصل      الاجتماعي، او إذا كنت تبحث عن اسم مستخدم فريد و موحد لجميع المنصات الاجتماعية فأنت في المكان المناسب.
          </p>
          <p> هنا في تواصُل نوفر لك امكانية البحث عن اسمك الجديد او هويتك الجديدة في جميع المنصات الإجتماعية لتأتي بإسم فريد من مكان واحد فقط ليتسنى لك اختصار وقتك في البحث عن الاسم المناسب لك بإسرع وقت ممكن و بضغطة زر واحدة. </p>
        </div>
        <div className='button-section-container'>
          <div onClick={handleScrollUp}>
            <h4> ابحث الان </h4>
          </div>

        </div>
    </div>
    <div className='svg-container'>
      <img src={svg} alt='search' />
    </div>
</div>
  )
}
