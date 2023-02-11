# Live Project Summary
## Intro to Tech Academy Live Project

The final part of my Tech Academy bootcamp was a Live Project wtih a two week sprint to build a website utilizing the skills learned throughout the bootcamp. The website used the Django framework, with HTML and CSS on the front end and Python on the back end. Website functionality was built one story at at time, from creating the initial webpage up to displaying API data on the website. My Django app operated within a common main app which contained other students' apps; this provided a chance to practice using Git within Azure DevOps to integrate my code with other students'. 

The website created allowed a user to input ski objects and save relevant information, such as brand, length, width, color, etc. The back end stored each ski as an object created with via a Django model.  The front end provided a common theme across all pages, with shared table, button, and link styling. 


## Back End
* [Ski Object Creation](#ski-object-creation)
* [Weather API](#weather-api)
* [Display Weather](#display-weather)

### Ski Object Creation
Each Ski object created contained various attributes, and contained a verbose name which clarified the object when presented to the user. 

      class Ski(models.Model):
          brand = models.CharField(max_length=100)
          ski_model = models.CharField(max_length=30)
          ski_length = models.IntegerField()
          ski_width = models.IntegerField()
          terrain = models.CharField(max_length=30, choices=TERRAIN_TYPES)
          color = models.CharField(max_length=50, verbose_name='Color/Design')

          Skis = models.Manager()

          def __str__(self):
              return self.brand + ' ' + self.ski_model + ' ' + str(self.ski_length) + 's'
              
              
### Weather API
The weather API retrieves the forecast for Timberline Lodge from the National Weather Service's API. It stores the forecast time and forecast detail in a dictionary.

      # function to connect to national weather service's API, to look up weather for skiing at timberline lodge
      def check_weather(request):
          try:
              response = requests.get(location_1)
          except:
              raise APIException("The connection to the API failed! Ensure the URL is correct.")
          weather_data = response.json()
          # save all the time periods available
          weather = weather_data['properties']['periods']
          # create blank dictionary that we'll build with time periods as key and forecast as value
          wx_dict = {}
          for timePeriod in weather:
              # build dictionary with time period's name (today, tonight, tomorrow, etc) as key and forecast as value
              wx_dict[timePeriod['name']] = timePeriod['detailedForecast']
          # nws.gov weather api reference: https://www.weather.gov/documentation/services-web-api
          content = {'wx_dict': wx_dict}
          return render(request, 'Skis/weather_check.html', content)
          
          
### Display Weather
The weather data is displayed by retrieving it from the Python dictionary and displaying it in an HTML table.

            <!-- in dictionary, forecast period name (like today, tomorrow, Wednesday, etc) is key, and forecast is value -->
            {% for forecast_period, forecast in wx_dict.items %}
            <tr>
                <td>{{ forecast_period }}</td>
                <td>{{ forecast }}</td>
            </tr>
