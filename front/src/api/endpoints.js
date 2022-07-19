
const prefix = "/api";

export const getAllTicker = prefix + "/tickers";
export const getTickerHistory = (name) => prefix + `/tickers/${name}/history`;
export const priceStreamer = (name) => `ws://localhost:8000/api/ticker/${name}/ws`;
