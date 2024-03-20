/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let buy_index = 0
    let sell_index = 1
    let max_profit = 0
    while(sell_index < prices.length){
        let profit = prices[sell_index] - prices[buy_index]
        if(profit > max_profit){
            max_profit = profit
        }
        if(profit < 0){
            buy_index = sell_index
        }
        sell_index += 1
    }

    return max_profit
};