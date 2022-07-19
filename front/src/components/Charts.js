import { LineChart, Line, CartesianGrid, XAxis, YAxis } from 'recharts';


const PriceChart = ({prices, ...props}) => {
    var max = Number(Math.max(...prices.map(o => o.price)) * 1.2).toFixed(0)
    var min = Number(Math.min(...prices.map(o => o.price)) * 0.8).toFixed(0)

    prices.forEach(el => {
        var date = new Date(el.timestamp * 1000);
        el.time = date.toLocaleTimeString()
    })
    console.log(prices)
    const renderCurrentPrice = () => {
        var lastPrice = prices[prices.length - 1]
        
        if (lastPrice !== undefined)
        {
            var price = lastPrice.price
            return (<div className='currentPrice'>{`Current Price: ${price}`}</div>)
        }
    }

    return (<div className="pricer">

        {renderCurrentPrice()}
        <div className="chart">
            
            <LineChart width={window.screen.width - 500} height={window.screen.height - 400} data={prices} margin={{ top: 20, right: 50, bottom: 50, left: 50 }}>
                <Line type="monotone" dataKey="price" stroke="#000caf" isAnimationActive={false} dot={false}/>
                <CartesianGrid stroke="#828af5" strokeDasharray="5 5" />
                <XAxis dataKey="time" angle={-45} dy={20} stroke="#000"/>
                <YAxis domain={[min, max]}  stroke="#000"/>
            </LineChart>
        </div>
    </div>
    );
}

export default PriceChart
