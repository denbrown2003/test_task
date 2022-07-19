import './styles/App.css';
import { useState, useEffect } from 'react'
import { Button, Form } from 'react-bootstrap'
import { Get } from './api/client'
import { getAllTicker, priceStreamer } from './api/endpoints'
import SymbolSelector from './components/SymbolSelector'
import PriceApp from './components/PriceApp';


function App() {
  return (
    <div className="App">
      <div clasName="content">
          <PriceApp />
        </div>
    </div>
  );
}

export default App;
