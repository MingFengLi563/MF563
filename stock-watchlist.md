# 股票监控配置

## 关注的股票

```yaml
watchlist:
  # A 股
  - symbol: 000001.SZ
    name: 平安银行
    notes: 银行股
  - symbol: 600519.SS
    name: 贵州茅台
    notes: 白酒龙头
  - symbol: 000858.SZ
    name: 五粮液
    notes: 白酒
  - symbol: 300750.SZ
    name: 宁德时代
    notes: 新能源电池
  - symbol: 002594.SZ
    name: 比亚迪
    notes: 新能源汽车
```

## 监控设置

```yaml
alerts:
  price_change_threshold: 5  # 涨跌幅超过 5% 提醒
  volume_spike: true         # 成交量异动提醒
  technical_signals:         # 技术指标信号
    - RSI_overbought
    - RSI_oversold
    - MA_golden_cross
    - MA_death_cross
```

## 使用方式

向主代理发送以下指令：

- "分析一下 AAPL" - 分析特定股票
- "查看我的 watchlist" - 查看关注的股票
- "扫描热门股票" - 发现 trending stocks
- "检查投资组合" - 查看投资组合表现
- "设置 AAPL 价格提醒" - 设置价格预警

---

最后更新：2026-03-14
