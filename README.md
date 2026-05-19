# 美国天气预报 - 每日自动邮件推送

每天自动获取美国 8 大区域 16 个城市的天气预报和恶劣天气预警，推送到你的邮箱。

## 覆盖区域

| 区域 | 城市 | 州 |
|------|------|-----|
| 东北部 | 纽约、波士顿 | NY, MA, PA, NJ, CT |
| 东南部 | 迈阿密、亚特兰大 | FL, GA, SC, NC |
| 南部 | 休斯顿、新奥尔良 | TX, LA, MS, AL |
| 中部 | 芝加哥、堪萨斯城 | IL, MO, KS, IA, NE |
| 西部 | 洛杉矶、旧金山 | CA, OR, WA |
| 西南部 | 凤凰城、拉斯维加斯 | AZ, NM, NV |
| 西北部 | 西雅图、波特兰 | WA, OR, ID, MT |
| 中西部山地 | 丹佛、盐湖城 | CO, UT, WY |

数据来源：美国国家气象局（NWS），完全免费，无需 API Key。

## 3 步开始使用

### 第 1 步：Fork 本仓库

点击本页面右上角 **Fork** 按钮，把代码复制到你自己的 GitHub 账号下。

### 第 2 步：开启 QQ 邮箱 SMTP 服务

1. 电脑浏览器打开 [QQ 邮箱](https://mail.qq.com) 并登录
2. 点顶部「设置」→「账户」
3. 往下翻，找到 **IMAP/SMTP 服务**，点「开启」
4. 按提示用手机发短信验证
5. 验证通过后会得到一个 **16 位授权码**（只显示一次，记好）

### 第 3 步：配置 Secrets

在你 Fork 的仓库页面：

1. 点 **Settings**（设置）
2. 左侧找 **Secrets and variables** → **Actions**
3. 点 **New repository secret**，逐个添加以下 5 个：

| Name | Value（填什么） | 示例 |
|------|-----------------|------|
| `EMAIL_SMTP` | 固定填 | `smtp.qq.com` |
| `EMAIL_PORT` | 固定填 | `465` |
| `EMAIL_SENDER` | 你的 QQ 邮箱 | `123456789@qq.com` |
| `EMAIL_PASSWORD` | 第 2 步获取的授权码 | `abcdefghijklmnop` |
| `EMAIL_RECEIVER` | 接收邮件的邮箱 | `123456789@qq.com` |

> 发件和收件可以是同一个邮箱，自己发给自己。

### 完成！

现在有两种方式触发：

- **自动**：每天北京时间 7:30 自动推送
- **手动**：仓库页面 → **Actions** → **US Weather Push** → **Run workflow** → 立即推送

## 推送效果

邮件内容示例：

```
📍 东北部
   州: NY, MA, PA, NJ, CT

  纽约(New York)
    今天: 晴天 32°C 13~24km/h 3~4级
    今晚: 局部多云 23°C 19~24km/h 3~4级
    星期三: 晴天 31°C 16~26km/h 3~4级
    星期三晚: 雷暴 16°C 19~24km/h 3~4级
    星期四: 晴天 18°C 11~21km/h 2~4级
    星期四晚: 多云 13°C 3~13km/h 1~3级

  !! 预警(NY):
    [中等] Heat Advisory
```

## 修改推送时间

编辑 `.github/workflows/weather-push.yml`，修改 cron 表达式：

```yaml
schedule:
  - cron: '30 23 * * *'  # 北京时间 7:30
```

换算：北京时间 = UTC + 8，所以北京时间 8:00 = UTC 0:00 = `0 0 * * *`

## 自定义城市

编辑 `config.py`，可以增删区域和城市：

```python
REGIONS = {
    "你想叫的名字": {
        "states": ["CA"],
        "cities": [
            {"name": "洛杉矶", "en": "Los Angeles", "lat": 34.0522, "lon": -118.2437},
        ],
    },
}
```

## 其他推送方式

除了邮件，还支持企业微信、飞书、钉钉。在 Secrets 里对应添加即可：

| 方式 | Secret 名 | 获取方式 |
|------|-----------|----------|
| 企业微信 | `WECOM_WEBHOOK` | 群机器人 Webhook 地址 |
| 飞书 | `FEISHU_WEBHOOK` | 群机器人 Webhook 地址 |
| 钉钉 | `DINGTALK_WEBHOOK` | 群机器人 Webhook 地址 |

## 费用

全部免费：
- NWS 天气 API：免费，无需 Key
- GitHub Actions：免费额度（每月 2000 分钟）
- QQ 邮箱 SMTP：免费
