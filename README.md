# AutoOKX2NFK Northflank 部署指南

## 1. 环境变量配置
在 Northflank 服务的"环境变量"界面，添加如下变量（按实际账户数量增减）：
- OKX_API_KEY、OKX_SECRET_KEY、OKX_PASSPHRASE、OKX_FLAG、OKX_ACCOUNT_NAME
- OKX_API_KEY1、OKX_SECRET_KEY1、OKX_PASSPHRASE1、OKX_FLAG1、OKX_ACCOUNT_NAME1
- BARK_KEY、BARK_GROUP

## 2. 定时任务（账户查询）
在 Northflank 的"计划任务"中，添加如下 cron 表达式：
- `0 9 * * *`（UTC 9:00 = 北京时间 17:00）
- 任务命令：`python okx_account_balance.py`

## 3. 网页访问
- 部署后，访问 Northflank 分配的服务 URL，即可通过网页控制和查看运行结果。
- 页面自适应手机，风格类似 GitHub。

## 4. 本地开发
```bash
pip install -r requirements.txt
python main.py
```

## 5. 其他
- 代码推送到 GitHub 后，Northflank 可自动构建并部署。