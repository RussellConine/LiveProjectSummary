# Live Project Summary
## Intro to Tech Academy Live Project

The final part of my Tech Academy bootcamp was a Live Project wtih a two week sprint to build a website utilizing the skills learned throughout the bootcamp. The website used the Django framework, with HTML and CSS on the front end and Python on the back end. Website functionality was built one story at at time, from creating the initial webpage up to displaying API data on the website. My Django app operated within a common main app which contained other students' apps; this provided a chance to practice using Git within Azure DevOps to integrate my code with other students'. 

The website created allowed a user to input ski objects and save relevant information, such as brand, length, width, color, etc. The back end stored each ski as an object created with via a Django model.  The front end provided a common theme across all pages, with shared table, button, and link styling. 

## Back End
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
