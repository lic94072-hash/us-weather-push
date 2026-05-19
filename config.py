# 美国各区域代表城市配置
# 每个区域选2个代表城市，经纬度用于调用 NWS API

REGIONS = {
    "东北部": {
        "states": ["NY", "MA", "PA", "NJ", "CT"],
        "cities": [
            {"name": "纽约", "en": "New York", "lat": 40.7128, "lon": -74.0060},
            {"name": "波士顿", "en": "Boston", "lat": 42.3601, "lon": -71.0589},
        ],
    },
    "东南部": {
        "states": ["FL", "GA", "SC", "NC"],
        "cities": [
            {"name": "迈阿密", "en": "Miami", "lat": 25.7617, "lon": -80.1918},
            {"name": "亚特兰大", "en": "Atlanta", "lat": 33.7490, "lon": -84.3880},
        ],
    },
    "南部": {
        "states": ["TX", "LA", "MS", "AL"],
        "cities": [
            {"name": "休斯顿", "en": "Houston", "lat": 29.7604, "lon": -95.3698},
            {"name": "新奥尔良", "en": "New Orleans", "lat": 29.9511, "lon": -90.0715},
        ],
    },
    "中部": {
        "states": ["IL", "MO", "KS", "IA", "NE"],
        "cities": [
            {"name": "芝加哥", "en": "Chicago", "lat": 41.8781, "lon": -87.6298},
            {"name": "堪萨斯城", "en": "Kansas City", "lat": 39.0997, "lon": -94.5786},
        ],
    },
    "西部": {
        "states": ["CA", "OR", "WA"],
        "cities": [
            {"name": "洛杉矶", "en": "Los Angeles", "lat": 34.0522, "lon": -118.2437},
            {"name": "旧金山", "en": "San Francisco", "lat": 37.7749, "lon": -122.4194},
        ],
    },
    "西南部": {
        "states": ["AZ", "NM", "NV"],
        "cities": [
            {"name": "凤凰城", "en": "Phoenix", "lat": 33.4484, "lon": -112.0740},
            {"name": "拉斯维加斯", "en": "Las Vegas", "lat": 36.1699, "lon": -115.1398},
        ],
    },
    "西北部": {
        "states": ["WA", "OR", "ID", "MT"],
        "cities": [
            {"name": "西雅图", "en": "Seattle", "lat": 47.6062, "lon": -122.3321},
            {"name": "波特兰", "en": "Portland", "lat": 45.5152, "lon": -122.6784},
        ],
    },
    "中西部山地": {
        "states": ["CO", "UT", "WY"],
        "cities": [
            {"name": "丹佛", "en": "Denver", "lat": 39.7392, "lon": -104.9903},
            {"name": "盐湖城", "en": "Salt Lake City", "lat": 40.7608, "lon": -111.8910},
        ],
    },
}

# 天气状况英文 → 中文翻译
WEATHER_CN = {
    "Sunny": "晴天", "Clear": "晴朗", "Mostly Sunny": "大部晴朗",
    "Mostly Clear": "大部晴朗", "Partly Sunny": "局部多云",
    "Partly Cloudy": "局部多云", "Cloudy": "多云", "Overcast": "阴天",
    "Light Rain": "小雨", "Rain": "雨", "Heavy Rain": "大雨",
    "Rain Showers": "阵雨", "Thunderstorms": "雷暴",
    "Severe Thunderstorms": "强雷暴", "Snow": "雪", "Light Snow": "小雪",
    "Heavy Snow": "大雪", "Blizzard": "暴风雪", "Sleet": "雨夹雪",
    "Freezing Rain": "冻雨", "Fog": "雾", "Haze": "霾",
    "Windy": "大风", "Breezy": "微风", "Hot": "炎热",
    "Cold": "寒冷", "Fair": "晴好",
}

# NWS 预警类型英文 → 中文
ALERT_CN = {
    "Tornado Warning": "龙卷风警告",
    "Tornado Watch": "龙卷风警戒",
    "Severe Thunderstorm Warning": "强雷暴警告",
    "Severe Thunderstorm Watch": "强雷暴警戒",
    "Flash Flood Warning": "山洪警告",
    "Flash Flood Watch": "山洪警戒",
    "Flood Warning": "洪水警告",
    "Flood Watch": "洪水警戒",
    "Flood Advisory": "洪水预警",
    "Hurricane Warning": "飓风警告",
    "Hurricane Watch": "飓风警戒",
    "Tropical Storm Warning": "热带风暴警告",
    "Tropical Storm Watch": "热带风暴警戒",
    "Winter Storm Warning": "冬季风暴警告",
    "Winter Storm Watch": "冬季风暴警戒",
    "Blizzard Warning": "暴风雪警告",
    "Ice Storm Warning": "冰暴警告",
    "Heavy Snow Warning": "大雪警告",
    "Freeze Warning": "霜冻警告",
    "Frost Advisory": "霜冻预警",
    "Wind Chill Warning": "寒潮警告",
    "Wind Chill Advisory": "寒潮预警",
    "Heat Advisory": "高温预警",
    "Excessive Heat Warning": "极端高温警告",
    "Excessive Heat Watch": "极端高温警戒",
    "Red Flag Warning": "火灾危险警告",
    "Fire Weather Watch": "火灾天气警戒",
    "High Wind Warning": "大风警告",
    "Wind Advisory": "大风预警",
    "Dense Fog Advisory": "浓雾预警",
    "Dust Storm Warning": "沙尘暴警告",
    "Severe Weather Statement": "恶劣天气通报",
    "Special Weather Statement": "特殊天气通报",
    "Coastal Flood Advisory": "沿海洪水预警",
    "Coastal Flood Warning": "沿海洪水警告",
    "Rip Current Statement": "离岸流预警",
    "Air Quality Alert": "空气质量预警",
    "Hard Freeze Warning": "严重霜冻警告",
    "Freeze Watch": "霜冻警戒",
}

# 预警严重等级中文
SEVERITY_CN = {
    "Extreme": "极端",
    "Severe": "严重",
    "Moderate": "中等",
    "Minor": "轻微",
    "Unknown": "未知",
}

# 只推送 Moderate 及以上级别的预警
MIN_SEVERITY = "Moderate"

# 预报天数（NWS 最多 7 天）
FORECAST_DAYS = 7

# 美国州名英文全称 → 中文
STATE_FULL_CN = {
    "Alabama": "阿拉巴马", "Alaska": "阿拉斯加", "Arizona": "亚利桑那",
    "Arkansas": "阿肯色", "California": "加利福尼亚", "Colorado": "科罗拉多",
    "Connecticut": "康涅狄格", "Delaware": "特拉华", "Florida": "佛罗里达",
    "Georgia": "佐治亚", "Hawaii": "夏威夷", "Idaho": "爱达荷",
    "Illinois": "伊利诺伊", "Indiana": "印第安纳", "Iowa": "爱荷华",
    "Kansas": "堪萨斯", "Kentucky": "肯塔基", "Louisiana": "路易斯安那",
    "Maine": "缅因", "Maryland": "马里兰", "Massachusetts": "马萨诸塞",
    "Michigan": "密歇根", "Minnesota": "明尼苏达", "Mississippi": "密西西比",
    "Missouri": "密苏里", "Montana": "蒙大拿", "Nebraska": "内布拉斯加",
    "Nevada": "内华达", "New Hampshire": "新罕布什尔", "New Jersey": "新泽西",
    "New Mexico": "新墨西哥", "New York": "纽约", "North Carolina": "北卡罗来纳",
    "North Dakota": "北达科他", "Ohio": "俄亥俄", "Oklahoma": "俄克拉荷马",
    "Oregon": "俄勒冈", "Pennsylvania": "宾夕法尼亚", "Rhode Island": "罗德岛",
    "South Carolina": "南卡罗来纳", "South Dakota": "南达科他", "Tennessee": "田纳西",
    "Texas": "德克萨斯", "Utah": "犹他", "Vermont": "佛蒙特",
    "Virginia": "弗吉尼亚", "Washington": "华盛顿", "West Virginia": "西弗吉尼亚",
    "Wisconsin": "威斯康星", "Wyoming": "怀俄明",
    "District of Columbia": "华盛顿特区",
}

# 美国州代码 → 中文
STATE_CN = {
    "AL": "阿拉巴马", "AK": "阿拉斯加", "AZ": "亚利桑那", "AR": "阿肯色",
    "CA": "加利福尼亚", "CO": "科罗拉多", "CT": "康涅狄格", "DE": "特拉华",
    "FL": "佛罗里达", "GA": "佐治亚", "HI": "夏威夷", "ID": "爱达荷",
    "IL": "伊利诺伊", "IN": "印第安纳", "IA": "爱荷华", "KS": "堪萨斯",
    "KY": "肯塔基", "LA": "路易斯安那", "ME": "缅因", "MD": "马里兰",
    "MA": "马萨诸塞", "MI": "密歇根", "MN": "明尼苏达", "MS": "密西西比",
    "MO": "密苏里", "MT": "蒙大拿", "NE": "内布拉斯加", "NV": "内华达",
    "NH": "新罕布什尔", "NJ": "新泽西", "NM": "新墨西哥", "NY": "纽约",
    "NC": "北卡罗来纳", "ND": "北达科他", "OH": "俄亥俄", "OK": "俄克拉荷马",
    "OR": "俄勒冈", "PA": "宾夕法尼亚", "RI": "罗德岛", "SC": "南卡罗来纳",
    "SD": "南达科他", "TN": "田纳西", "TX": "德克萨斯", "UT": "犹他",
    "VT": "佛蒙特", "VA": "弗吉尼亚", "WA": "华盛顿", "WV": "西弗吉尼亚",
    "WI": "威斯康星", "WY": "怀俄明", "DC": "华盛顿特区",
}

# 区域描述常用词英文 → 中文
AREA_TERM_CN = {
    "Northern": "北部", "Southern": "南部", "Eastern": "东部", "Western": "西部",
    "North": "北", "South": "南", "East": "东", "West": "西",
    "Northeast": "东北", "Northwest": "西北", "Southeast": "东南", "Southwest": "西南",
    "North Central": "中北部", "South Central": "中南部",
    "East Central": "中东", "West Central": "中西",
    "Central": "中部", "Upper": "上游", "Lower": "下游",
    "Interior": "内陆", "Coastal": "沿海", "Coast": "海岸",
    "Greater": "大", "Metro": "都市区", "Metropolitan": "都市区",
    "Surrounding": "周边", "Including": "包括",
    "Valley": "谷地", "Valleys": "谷地",
    "Mountains": "山区", "Mountain": "山",
    "Plains": "平原", "Plateau": "高原",
    "Peninsula": "半岛", "Panhandle": "柄地",
    "Island": "岛", "Islands": "群岛",
    "County": "县", "Counties": "各县",
    "Region": "地区", "Area": "区域", "Zone": "地带",
    "Waters": "水域", "Coastal Waters": "近海水域",
    "Offshore": "近海", "Nearshore": "近岸",
    "Portions of": "部分地区", "Parts of": "部分地区",
}

# 所有涉及州（用于全局极端天气扫描）
ALL_STATES = []
for _r in REGIONS.values():
    for _s in _r["states"]:
        if _s not in ALL_STATES:
            ALL_STATES.append(_s)
