# 問題: match文を使った天気アドバイス
#
# 問題文:
# 天気を表す文字列（"sunny", "rainy", "cloudy", "snowy" など）を引数として受け取り、以下のようにアドバイスを返す関数 weather_advice(weather) を作成してください。
# match文を使用してください。
#
# "sunny" → "帽子を忘れずに！"
# "rainy" → "傘を持って行きましょう。"
# "cloudy" → "今日は曇りです。"
# "snowy" → "暖かくして出かけましょう。"
# その他 → "天気が分かりません。"

def weather_advice(weather: str):
    match weather:
        case "sunny":
            return "帽子を忘れずに！"
        case "rainy":
            return "傘を持っていきましょう。"
        case "cloudy":
            return "今日は曇りです。"
        case "snowy":
            return "暖かくして出かけましょう。"
        case _:
            return "天気が分かりません。"

if __name__ == '__main__':
    print(weather_advice("sunny"))
    print(weather_advice("rainy"))
    print(weather_advice("cloudy"))
    print(weather_advice("snowy"))
    print(weather_advice("unknown"))
    print(weather_advice(""))