import React, {useState, useEffect} from "react"
import { Get } from '../api/client'
import { getAllTicker } from '../api/endpoints'
import { Form } from 'react-bootstrap'


import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';




const SymbolSelector = ({callbackChange, ...props}) => {
    const[tickers, setTickers] = useState([])

    useEffect(_=>{
      Get(getAllTicker, (resp) => setTickers(resp.data.active), () => setTickers([]))
    }, [])

    const renderItems = () => tickers.map((el, idx) => (<option value={el} key={idx}>{el}</option>))

    return (
        <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
          <Container>
            <Navbar.Brand href="#home">Price Renderer</Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav" />
            <Navbar.Collapse id="responsive-navbar-nav">
              <Nav className="lg">
                <div className="selector">
                <div className="symbols">
                  <Form.Select 
                      aria-label="Ticker"
                      onChange={e=>{callbackChange(e.target.value)}}
                      >
                        <option value="" selected disabled hidden>Choose Ticker</option>
                    {renderItems()}
                </Form.Select>
                  </div>
              </div>

              </Nav>
              <Nav>
                
              </Nav>
            </Navbar.Collapse>
          </Container>
        </Navbar>
    )
}

export default SymbolSelector