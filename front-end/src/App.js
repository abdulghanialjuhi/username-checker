import './App.css';
import { Routes, Route, Navigate } from 'react-router-dom'
import Home from './components/home-page/Home';
import Context from './context/Context';
import useGlobal from './context/useGlobal';
import Contact from './components/contact/Contact';


function App() {

  const store = useGlobal()

  return (
    <Context.Provider value={store}>
      <Routes>
      <Route exact path="/" element={<Navigate to='/home' />} />
      <Route path="home" element={<Home />}/>
      <Route path="contact" element={<Contact />}/>
      {/* <Route path="*" element={<Navigate to='/' />} /> */}
      </Routes>
    </Context.Provider>
  );
}

export default App;
