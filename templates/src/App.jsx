import axios from 'axios';
import React, { useState } from 'react';
import './App.css';

function App() {
  
  const [news, SetNews] = useState({newsTitle : "", newsSubtitle:"", newsDate:"", newsImage:""})

  async function addNewEvent() {
    // сюда кидай ссылку где добавлять или изменять данные
    axios.put(`http://127.0.0.1:8000/admin/dataKeeper/testnews/`, {
        
    }).then(response => {
        console.log(response.data)
    }).catch(function (error) {
        console.log(error);
    })
}
  

  const [file, setFile] = useState();
    function handleChange(e) {
        console.log(e.target.files);
        setFile(URL.createObjectURL(e.target.files[0]));
    }
  return (
    <>
      <div className='Example_container'>
        <div className='img__block'>
          <img src={file} alt="" className='img'/>
          <input type="file" value={news.image} onChange={e => setFile({...news, newsImage: e.target.value})} onClick={handleChange} className='input_img'/>
          <button className='Apply_button' onClick={addNewEvent}>Сохранить</button>
        </div>
        <div className='News_block'>
          <input type="text" placeholder='Title News' className='input_txt' value={news.title} onChange={e => SetNews({...news, newsTitle: e.target.value})}/>
          <input type="text" placeholder='Subtitle News' className='input_txt' value={news.subtitle} onChange={e => SetNews({...news, newsSubtitle: e.target.value})}/>
          <input type="text" placeholder='Date of News' className='input_txt' value={news.date} onChange={e => SetNews({...news, newsDate: e.target.value})}/>
        </div>
      </div>
    </>
  )
}

export default App;
