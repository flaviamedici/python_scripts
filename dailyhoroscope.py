import requests

SIGN = "gemini"  # change to your zodiac sign

BASE_URL = "https://freehoroscopeapi.com/api/v1/get-horoscope"


def fetch_horoscope(period):
    """
    period should be "daily", "weekly", or "monthly"
    """
    url = f"{BASE_URL}/{period}"
    params = {"sign": SIGN}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    
    data = response.json()
    # Return the horoscope text or a fallback message
    return data.get("horoscope", "No horoscope text in response.")


if __name__ == "__main__":
    try:
        daily_horoscope = fetch_horoscope("daily")
        weekly_horoscope = fetch_horoscope("weekly")
        
        print("\n🌟 DAILY HOROSCOPE 🌟")
        print(daily_horoscope)
        
        print("\n🌙 WEEKLY HOROSCOPE 🌙")
        print(weekly_horoscope)
        
    except Exception as e:
        print("Error fetching horoscope:", str(e))