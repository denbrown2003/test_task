
const prefix = "/api";

export const getAllTicker = prefix + "/tickers";
export const getTickerHistory = (name, limit = null) => prefix + `/tickers/${name}/history${limit != null ? '?limit=' + limit : ""}`;
export const priceStreamer = (name) => `ws://localhost:8000/api/ticker/${name}/ws`;
