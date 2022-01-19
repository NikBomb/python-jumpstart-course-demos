import collections
import requests


UserInput = collections.namedtuple("UserInput", "city, state, country")

def main():
    printHeader()
    userInp = getInput()
    url = buildUrl(userInp)
    resp = requests.get(url)
    if resp.status_code != 200:
        print(resp.reason)
        return

    rawWeather = resp.json()

    print(f"The weather in  {rawWeather['location']['city']} is {rawWeather['weather']['description']}, with a "
          f"temperature of {rawWeather['forecast']['temp']} C.")


def buildUrl(userInp):
    url = f"https://weather.talkpython.fm/api/weather?city={userInp.city}&country={userInp.country}&units=metric"
    if userInp.state:
        url += f"&state={userInp.state}"
    return url


def printHeader():
    print("--------------------------------")
    print("---------- WEATHER APP ---------")
    print("--------------------------------")

def getInput():
    city = ""
    state = ""
    country = "IT"

    raw = input("Where would you like the check the weather? (City, [State], [Country = IT])")
    splitInp = raw.split(",")
    if len(splitInp) == 1:
        city = splitInp[0].strip().lower()
    elif len(splitInp) == 2:
        city = splitInp[0].strip().lower()
        country = splitInp[1].strip().lower()
    if len(splitInp) == 3:
        city = splitInp[0].strip().lower()
        state = splitInp[1].strip().lower()
        country = splitInp[2].strip().lower()
    return UserInput(city=city.replace(" ", "+"), state=state, country=country)

if __name__ == "__main__":
    main()