# Turtle trading notes
- Markets must be trending & liquid
- Trade several markets at once, as may not be opportunities in one market

### Position sizing
- Most important aspect of trading
- Normalise dollar vol of position by adjusting size vs. dollar vol of market
    - This allows different contracts in different markets to have same chance for dollar movement, increasing effectiveness of diversification
- Use Average True Range (ATR) as measure of volatility
    $ TR = max[(high - low), \; abs(high - close_{prev}), \; abs(low - close_{prev})] $
- Then take exponential moving average
    - Richard Dennis: 20 day
    - J Welles Wilder: 14 day
- ATR at time 
$ ATR_t = \frac{ATR_{t-1} \times (n-1) + TR_{t}}{n} $
- Initial ATR value is the arithmetic mean

$ ATR_{initial} = \frac{1}{n} \sum^n_{i=1}TR_i $

- Calculate dollar volatility:
    - Dollar vol = ATR x dollars per point
- Volatility-adjusted position units
    - 1 unit = 1% of account equity
    - .: Unit size per market = 1% of account / market dollar volatility
- Stops must be predefined

A complete trading system covers:
- Markets: what to buy or sell
    - Trade enough markets to catch trends
    - Don't trade low volume or non-trending markets
- Position sizing: How much to buy or sell
    - Single most important aspect of trading
    - Diversification: spreading risk across instruments / markets
    - Money management: controlling risk by retaining capital until good trends appear
- Entries: When to buy or sell
    - System generates entry signals
- Stops: When to get out of a losing position
    - Do not enter with out a stop in place
- Exits: When to get out of a winning position
    - Do not enter without an exit strategy
- Tactics: How to buy or sell
    - More important for larger accounts which can move the market

### Markets traded by turtles
- Mainly futures markets  commodities
- Liquidity key criterion for deciding whether to enter market
    - 10y US T
    - 30y US T
    - Coffee
    - Cocoa
    - Sugar
    - Cotton
    - CHF
    - GBP
    - JPY
    - CAD
    - SP500
    - Eurodollar
    - 90d US T
    - Gold
    - Silver
    - Copper
    - Crude oil
    - Heating oil
    - Unleaded petrol

### Position sizing:
- Normalised dollar volatility
  - Increases effectiveness of diversification
- Market dollar volatility = ATR x dollars per point

- Build positions in units, where 1 unit = 1% of account equity
  - 1 unit = 1% of account / market dollar volatility

- True diversification requires similar bets on different instruments

- Market volatility is the risk measurement for that market
- Build positions that represent consistent amounts of volatility (i.e. risk)
- Much easier and more effective with more capital

- Risk rules:
  - Max units in single market: 4
  - Closely correlated markets: 6
  - Loosely correlated markets: 10
  - Single direction (long or short): 12 

- Adjusting trading size
  - Must adapt trade size to remaining equity in the account
  - Turtles reduce notional equity size by 20% for a loss of 10% and reset - if another 10% loss is sustained, reduce notional equity size another 20%

- Entries
  - System 1: short term, 20 day breakout
  - System 2: long term, 55 day breakout
    - An x day breakout is when price > high of last x days

- System 1
  - Buy 1 unit when 20 day breakout occurs
  - Unless last breakout would have resulted in a winning trade
  - Losing breakout if price after date of breakout moved 2xATR against position before profitable 10 day exit occurred
  - If 20 day breakout skipped due to this rule, 55 day breakout trade made (to avoid missing major moves)

- System 2
  - Buy 1 unit when 55 day breakout occurs
  - Regardless of whether previous trade was a winner

- Most breakouts DO NOT RESULT IN TRENDS
- .: Most trades using this system result in losses

Add unit to positions at 0.5ATR:
- ATR = 2.5
- 55 day breakout = 310
- Price hits 310
  - Buy 1 unit
- Price hits 311.25 (310 + 0.5ATR)
  - Buy 1 unit
- Price hits 312.5 (311.25 + 0.5ATR)
  - Buy 1 unit

Large proportion of year's profits may come from 2/3 big trades, so it is critical to enter whenever signals dictate it.

- Stops
  - No trade can incur more than 2% risk
  - i.e. 2ATR
  - If additional units added, increase stop for all units by 0.5ATR
  - If price gaps up, add stop for that unit at 2ATR

- Whipsaw stop strategy
  - Each unit has its own stop @ 0.5ATR
  - Higher profits but lower win/loss ratio

Exits
- System 1
- 10 day low for long positions
- 10 day high for short positions
- Exit all units at this point

- System 2
- 20 day low for long positions
- 20 day high for short positions

- These exits are DIFFICULT
- Often see 20/40/100% of profits evaporate when holding for the big move

Tactics
- Watch market and place limit orders when appropriate, as limit orders offer a chance for better fills and less slippage than market orders
- Should be able to get better prices using limit orders placed near the market than market orders (somewhat mitigates random market movt. a.k.a bounce)
- If market moving very quickly, wait for it to stabilise and place limit order lest you place market order at worst time
  - In this instance, spread widens and liquidity dries up as sellers hold out for higher price
  - Then new sellers come in and price drops back a little
  - Market orders often get filled at top of run, just when new sellers come in i.e. before price drops back

- Lots of days will be boring and nothing will happen

- Buy strength, sell weakness
- If several signals come at once, buy strongest market and sell weakest
- Only enter strongest contract month per commodity
- Calculate strength by:
  - Number of ATR price has moved since breakout
  - (Current price - 3mo price ) / ATR = normalised price increase
- Rolling over expiring contracts
  - Do not roll over unless price action of new contract would have resulted in an existing position
  - Contracts should be rolled before vol and open interestin expiring contract decline too much
    - Usually a few weeks before expiration unless currently held contract preforuming significantly better than contract months further out


- Things to test
  - length of breakout periods
  - size of units
  - exit lengths
  - market vs limit (how to test this?)