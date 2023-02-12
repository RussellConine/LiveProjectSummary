# Live Project Summary
## Intro to Tech Academy Live Project

The final part of my Tech Academy bootcamp was a Live Project wtih a two week sprint to build a website utilizing the skills learned throughout the bootcamp. The website used the Django framework, with HTML and CSS on the front end and Python on the back end. Website functionality was built one story at at time, from creating the initial webpage up to displaying API data on the website. My Django app operated within a common main app which contained other students' apps; this provided a chance to practice using Git within Azure DevOps to integrate my code with other students'. 

The website created allowed a user to input skis and save relevant information, such as brand, length, width, color, etc. The back end stored each ski as an object created via a Django model.  The front end provided a common theme across all pages, with shared table, button, and link styling. 


## Back End
* [Ski Object Creation](#ski-object-creation)
* [Weather API](#weather-api)
* [Display Weather](#display-weather)

### Ski Object Creation
Each Ski object created contains various attributes and contains a verbose name which clarifies the object when presented to the user. 

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
            
            

## Front End
* [Table Content](#table-display)
* [Table Styling](#table-styling)

### Table Content
All tables receive their data from Django views. This data comes from either the database, or from the weather API. Below is an example of a table which contains data from the database, which is a reult of reading all Ski objects contained in the database. 

        <table class="table table-responsive" id="ski-table">
            <tr>
                <th>Brand</th>
                <th>Model</th>
                <th>Length</th>
                <th>Width</th>
                <th>Terrain</th>
                <th>View Ski Details</th>
            </tr>
            {% for e in entry %}
            <tr>
                <td>{{e.brand}}</td>
                <td>{{e.ski_model}}</td>
                <td>{{e.ski_length}}</td>
                <td>{{e.ski_width}}</td>
                <td>{{e.terrain}}</td>
                <td><a href="{% url 'details' e.id %}"><button type="button" class="classic-button">Details</button></a></td>
            </tr>
            {% endfor %}
        </table>


### Table Styling
The styling of all tables and their buttons was unified across the various pages on the website. 

      /* make every other row an alternating color */
      #ski-table tr:nth-child(even){
          background-color: rgb(255, 236, 220);
      }

      #ski-table th {
          background-color: rgb(255, 183, 142);
      }

      #ski-table tr:hover {
          background-color: white;
      }

      #ski-table tr {
          background-color: #a2a2a2;
      }

      #ski-table a:hover {
          text-decoration: none;
      }
      .classic-button, .details-button, .edit-button{
          border: none;
          background-color: var(--navbar-color);
          width: 100%;
          border-radius: 3px;
          color: white;
      }
