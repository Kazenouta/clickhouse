-- stk_bar_1min
DROP TABLE IF EXISTS ark.b_stk_bar_1min;
CREATE TABLE ark.b_stk_bar_1min
(
	`symbol` String,
	`open`   Float32,
	`close`  Float32,
	`high`   Float32,
	`low`    Float32,
	`volume` Float32,
	`amount`  Float32,
	`s_time` DateTime,
	`t_date` DateTime,
	`change` Float32,
	`ret`    Float32,
	`e_time` DateTime
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(t_date)
ORDER BY (symbol, s_time)
SAMPLE BY symbol
SETTINGS index_granularity = 8192;

-- stk_bar_5min
DROP TABLE IF EXISTS ark.b_stk_bar_5min;
CREATE TABLE ark.b_stk_bar_5min
(
	`symbol` String,
	`t_date` DateTime,
	`s_time` DateTime,
	`e_time` DateTime,
	`open`   Float32,
	`high`   Float32,
	`low`    Float32,
	`close`  Float32,
	`volume` Float32,
	`amount`  Float32,
	`change` Float32,
	`ret`    Float32
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(t_date)
ORDER BY (symbol, s_time)
SAMPLE BY symbol
SETTINGS index_granularity = 8192;

-- b_trade
DROP TABLE IF EXISTS ark.b_trade;
CREATE TABLE ark.b_trade
(
	`symbol`        String,
	`trading_date`  Date,
	`trading_time`  DateTime64(3),
	`rec_id`        Int32,
	`trade_channel` Int16,
	`trade_price`   Float32,
	`trade_volume`  Float32,
	`trade_amount`  Float32,
	`unix`          Int64,
	`market`        String,
	`buy_rec_id`    Int32,
	`sell_rec_id`   Int32,
	`buy_sell_flag` String,
	`security_id`   Float64,
	`symbol_source` String
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(trading_date)
ORDER BY (trading_date, symbol)
SAMPLE BY symbol
SETTINGS index_granularity = 8192;

-- b_stk_orderbook
DROP TABLE IF EXISTS ark.b_stk_orderbook;
CREATE TABLE ark.b_stk_orderbook
(
  `symbol`                String,                        
  `trading_date`          Date,             
  `trading_time`          Datetime64(3),             
  `preclose_price`        Float32,         
  `open_price`            Float32,                 
  `high_price`            Float32,                 
  `low_price`             Float32,                   
  `last_price`            Float32,                 
  `trade_status`          String,  
  `ask_level_no`          Int8,             
  `bid_level_no`          Int8,              
  `total_no`              Int32,                     
  `trade_no`              Int32,                     
  `total_volume`          Int32,             
  `trade_volume`          Int32,             
  `total_amount`          Float32,             
  `trade_amount`          Float32,             
  `total_ask_order_volume`   Int32,   
  `total_bid_order_volume`   Int32,    
  `wt_avg_ask_price`      Float32,      
  `wt_avg_bid_price`      Float32,       
  `unix`                  Int64,                            
  `close_price`           Float32,               
  `market`                String,                        
  `price_up_limit`        Float32,          
  `price_down_limit`      Float32,      
  `security_id`           String,      
  `ask_price10`           Float32,     
  `ask_price09`           Float32,     
  `ask_price08`           Float32,     
  `ask_price07`           Float32,     
  `ask_price06`           Float32,     
  `ask_price05`           Float32,     
  `ask_price04`           Float32,     
  `ask_price03`           Float32,     
  `ask_price02`           Float32,     
  `ask_price01`           Float32,     
  `ask_volume10`          Int32,   
  `ask_volume09`          Int32,    
  `ask_volume08`          Int32,    
  `ask_volume07`          Int32,    
  `ask_volume06`          Int32,    
  `ask_volume05`          Int32,    
  `ask_volume04`          Int32,    
  `ask_volume03`          Int32,    
  `ask_volume02`          Int32,    
  `ask_volume01`          Int32,    
  `total_ask_order_no10`  Int32,  
  `total_ask_order_no09`  Int32,  
  `total_ask_order_no08`  Int32,  
  `total_ask_order_no07`  Int32,  
  `total_ask_order_no06`  Int32,  
  `total_ask_order_no05`  Int32,  
  `total_ask_order_no04`  Int32,  
  `total_ask_order_no03`  Int32,  
  `total_ask_order_no02`  Int32,  
  `total_ask_order_no01`  Int32,  
  `bid_price01`           Float32,    
  `bid_price02`           Float32,    
  `bid_price03`           Float32,    
  `bid_price04`           Float32,    
  `bid_price05`           Float32,    
  `bid_price06`           Float32,    
  `bid_price07`           Float32,    
  `bid_price08`           Float32,    
  `bid_price09`           Float32,    
  `bid_price10`           Float32,    
  `bid_volume01`          Int32,  
  `bid_volume02`          Int32,  
  `bid_volume03`          Int32,  
  `bid_volume04`          Int32,  
  `bid_volume05`          Int32,  
  `bid_volume06`          Int32,  
  `bid_volume07`          Int32,  
  `bid_volume08`          Int32,  
  `bid_volume09`          Int32,  
  `bid_volume10`          Int32,  
  `total_bid_order_no01`  Int32,  
  `total_bid_order_no02`  Int32,  
  `total_bid_order_no03`  Int32,  
  `total_bid_order_no04`  Int32,  
  `total_bid_order_no05`  Int32,  
  `total_bid_order_no06`  Int32,  
  `total_bid_order_no07`  Int32,  
  `total_bid_order_no08`  Int32,  
  `total_bid_order_no09`  Int32,  
  `total_bid_order_no10`  Int32   
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(trading_date)
ORDER BY (trading_date, symbol)
SAMPLE BY symbol
SETTINGS index_granularity = 8192;