import React from 'react'
import Footer from '../components/layout/footer/Footer'
import Header from '../components/layout/header/Header'


export default function LayOut({ children }) {


    return (
        <div className='root-container'>
            <header>
                <Header />
            </header>
            <main>
                {children}
            </main>
            <footer>
                <Footer />
            </footer>
        </div>
    )
}
