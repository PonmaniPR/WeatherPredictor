import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url = "https://weather.com/en-IN/weather/today/l/Chennai+Tamil+Nadu?canonicalCityId=dab9026d4fcbbf18453a2c4da8a3d84003e5d213e619b6006e0e75d358b854e3"

master = Tk()
master.title("Weather App")
master.config(bg="lightblue")
img = Image.open("./weather.png")
img = img.resize((125, 125))
img = ImageTk.PhotoImage(img)


def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find(
        'h1', class_="CurrentConditions--location--kyTeL").text
    temperature = soup.find(
        'span', class_="CurrentConditions--tempValue--3a50n").text
    weatherPrediction = soup.find(
        'div', class_="CurrentConditions--phraseValue--2Z18W").text

    locationLabel.config(text=location)
    tempLabel.config(text=temperature)
    weatherPredictionLabel.config(text=weatherPrediction)

    tempLabel.after(60000, getWeather)
    master.update()


locationLabel = Label(master, font=("Calibri bold", 20), bg="lightblue")
locationLabel.grid(row=0, sticky="N", padx=100)

tempLabel = Label(master, font=("Calibri bold", 60), bg="lightblue")
tempLabel.grid(row=1, sticky="W", padx=60)

weatherPredictionLabel = Label(
    master, font=("Calibri bold", 25), bg="lightblue")
weatherPredictionLabel.grid(row=2, sticky="W", padx=25)

Label(master, image=img, bg="lightblue").grid(row=1, sticky="E")

getWeather()
master.mainloop()
