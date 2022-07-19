import React from "react"
import { priceStreamer, getTickerHistory } from '../api/endpoints'
import SymbolSelector from './SymbolSelector'
import { Get } from '../api/client'
import PriceChart from "./Charts"
import  { Spinner } from 'react-bootstrap'


class WsListener {
    constructor(onMessageCallback)
    {
        this.callback = onMessageCallback
        this.conn = null;

    }

    connect(ticker)
    {
        this.conn = new WebSocket(priceStreamer(ticker))
        this.conn.onmessage = (event) => {    
            try {
              const json = JSON.parse(event.data);
              this.callback(json)
            } catch (err) {
              console.log(err);
            }
          };
    }

    close(){
        this.conn.close()
    }

    isOpen(){
        return this.conn.OPEN
    }
}


class PriceApp extends React.Component {

    constructor()
    {
        super()
        this.state = {
            history: [],
            ticker: null,
            loading: false,
            limit: null
        }

        this.ws = null;
        this.prev_price =0;

        this.SelectorCallback = this.SelectorCallback.bind(this)
        this.wsCallback = this.wsCallback.bind(this)
        this.LimitChangeCallback = this.LimitChangeCallback.bind(this)
    }

    wsCallback(data){
      this.setState({history: [...this.state.history, data]})
    }

    SelectorCallback(ticker, limit=null){
        this.setState({loading: true, ticker: ticker});
        var url = getTickerHistory(ticker, limit);
        console.log(url, this.state.limit, this.state.ticker)
        Get(url, (rsp) => {this.setState({history: rsp.data, loading: false})})
            
        if(this.ws){
            this.ws.close();
        }
        this.ws = new WsListener(this.wsCallback);
        this.ws.connect(ticker)
    }

    LimitChangeCallback(limit){
        this.setState({limit: limit});
        this.SelectorCallback(this.state.ticker, limit);
    }

    render(){
        return (<div className="apprice">

            <SymbolSelector 
                callbackChange={this.SelectorCallback}
                changeLimitCallback={this.LimitChangeCallback} 
            />

            {this.state.history.length > 0 ? (<>
                {this.state.loading ? (
                <Spinner animation="grow" />
            ) : (<>
                    <PriceChart prices={this.state.history}/>
                </>
            )}
            </>) : (<div className="notifier">
                <h2>Please choose a Ticker</h2>
            </div>)}

           
            
        </div>)
    }
}

export default PriceApp;