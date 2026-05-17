import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,QLineEdit, QPushButton,QVBoxLayout)

from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name:",self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather",self)
        self.temperature_label =QLabel(self)
        self.emoji_label =QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox )

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family:calibri;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size:75px;
            }
            QLabel#emoji_label{
                font-size:100px;
                font-family:Segoe UI emoji;

            }
            QLabel#description_label{
                font-size:50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)
    def get_weather(self):

        api_key = "HERE ENTER THE API KEY FROM WEATHER.ORG"
        city = self.city_input.text()
        url = f"You enter the url here and replace with the correct variables"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)
            
        except requests.exceptions.HTTPError:
            match response.status_code:

                case 400:
                    self.display_error("⚠️ Bad Request: Please enter a valid city name.")

                case 401:
                    self.display_error("🔑 Unauthorized: Check your API key.")

                case 403:
                   self.display_error("🚫 Forbidden: Access denied.")

                case 404:
                    self.display_error("🌍 City not found.")

                case 500:
                    pself.display_error("💥 Internal Server Error: Server problem.")

                case 502:
                    self.display_error("🌐 Bad Gateway: Invalid server response.")

                case 503:
                    self.display_error("⏳ Service Unavailable: Server is temporarily down.")

                case 504:
                    self.display_error("⌛ Gateway Timeout: Server took too long to respond.")

                case _:
                    self.display_error("❌ An unexpected error occurred.")
        
        except requests.exceptions.ConnectionError:
            self.display_error("connection Error:'\n Check your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("TimeoutError\nThe request Timed out")
            pass
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects\n Check the URL")
        

        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

        
        
    def display_error(self,message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self,data):
        self.temperature_label.setStyleSheet("font-size: 75px;")
        temperature_k = data["main"]["temp"]
        print(temperature_k)
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_k * 9/5) - 459.67
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]



        self.temperature_label.setText(f"{temperature_f:.0f} F")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)
    @staticmethod
    def get_weather_emoji(weather_id):
        
        if 200 <= weather_id <= 232:
            return "⛈️"   # Thunderstorm

        elif 300 <= weather_id <= 321:
            return "🌦️"   # Drizzle

        elif 500 <= weather_id <= 531:
            return "🌧️"   # Rain

        elif 600 <= weather_id <= 622:
            return "❄️"   # Snow

        elif 701 <= weather_id <= 741:
            return "🌫️"   # Fog / Mist

        elif weather_id == 771:
            return "💨"   # Strong wind

        elif weather_id == 781:
            return "🌪️"   # Tornado

        elif weather_id == 800:
            return "☀️"   # Clear sky

        elif 801 <= weather_id <= 804:
            return "☁️"   # Clouds

        else:
            return "❓"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())