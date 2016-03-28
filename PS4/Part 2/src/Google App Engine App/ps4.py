import cgi
import datetime
import webapp2
import json
import jinja2


from google.appengine.ext import ndb
from google.appengine.api import users

#jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


ps4_key = ndb.Key('wireless-ps-4', 'default_ps4')

#Define Model for Google App Engine's NDB datastore

class TemperatureData(ndb.Model):
  temperature = ndb.TextProperty()
  humidity = ndb.TextProperty()
  heatIndex = ndb.TextProperty()
  date = ndb.DateTimeProperty(auto_now_add=True)

# Controller for end point to get Temperature data which will be used to plot graphs and display table
class Temperature(webapp2.RequestHandler):
  def get(self):

    # get Historical temperature and humidity data
    data = ndb.gql('SELECT * '
                        'FROM TemperatureData '
                        'WHERE ANCESTOR IS :1 '
                        'ORDER BY date DESC',
                        ps4_key)
    
    tempArray=[]
    humidityArray=[]
    heatIndexArray=[]
    timeArray=[]
    for d in data:

      tempArray.append(float(cgi.escape(d.temperature)))
      humidityArray.append(float(cgi.escape(d.humidity)))
      heatIndexArray.append(float(cgi.escape(d.heatIndex)))
      timeArray.append(str(d.date.time()))

    returnJson={}
    returnJson['temperature']= tempArray
    returnJson['humidity']= humidityArray
    returnJson['heatIndex']= heatIndexArray
    returnJson['time']= timeArray
    self.response.headers['Content-Type'] = 'application/json'   
    self.response.out.write(json.dumps(returnJson))


# Landing Page Controller
class MainPage(webapp2.RequestHandler):
  def get(self):


    self.response.out.write('<html> <head> <script src="https://code.jquery.com/jquery-1.12.2.js"   integrity="sha256-VUCyr0ZXB5VhBibo2DkTVhdspjmxUgxDGaLQx7qb7xY="   crossorigin="anonymous"></script> <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/1.0.2/Chart.min.js"></script>')
    self.response.out.write('  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.5/css/materialize.min.css" /> <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.5/js/materialize.min.js"></script>')
    self.response.out.write('</head> <body>')


    data = ndb.gql('SELECT * '
                        'FROM TemperatureData '
                        'WHERE ANCESTOR IS :1 '
                        'ORDER BY date DESC',
                        ps4_key)
    
    # renders table

    self.response.out.write('<center> <table class="responsive-table centered highlight" style="width:60%;"> <thead> <tr> <td>Temperature</td> <td>Humidity</td> <td>Heat Index</td> </tr> </thead> ')
    for d in data:

      self.response.out.write("<tr>")
      self.response.out.write('<td>%s</td>' %
                              cgi.escape(d.temperature))
      self.response.out.write('<td>%s</td>' %
                              cgi.escape(d.humidity))
      self.response.out.write('<td>%s</td>' %
                              cgi.escape(d.heatIndex))
      self.response.out.write('</tr>')
    
    self.response.out.write('</table>')

# renders graphs
    self.response.out.write(' <canvas id="canvas" width="400" height="400"></canvas>  <div id="legendDiv">  </div> </center>')
    self.response.out.write('<script type="text/javascript"> $( document ).ready(function() { var dataToBePlotted; $.getJSON("http://wireless-ps-4.appspot.com/temperature", function(data) { dataToBePlotted = data.temperature; dataToBePlottedHumidity = data.humidity; dataToBePlottedHeatIndex = data.heatIndex; chartLabel = data.time; console.log(data.temperature);  var ctx = document.getElementById("canvas").getContext("2d"); var data = { labels:chartLabel ,datasets: [{label: "Temperature",fillColor: "rgba(220,220,220,0.2)",strokeColor: "rgba(220,220,220,1)", pointColor: "rgba(220,220,220,1)", pointStrokeColor: "#fff", pointHighlightFill: "#fff", pointHighlightStroke: "rgba(220,220,220,1)", data: dataToBePlotted },{ label: "Humidity", fillColor: "rgba(151,187,205,0.2)",strokeColor: "rgba(151,187,205,1)", pointColor: "rgba(151,187,205,1)", pointStrokeColor: "#fff", pointHighlightFill: "#fff", pointHighlightStroke: "rgba(151,187,205,1)", data: dataToBePlottedHumidity},{ label: "Heat Index", fillColor: "rgba(120,197,205,0.2)",strokeColor: "rgba(120,197,205,1)", pointColor: "rgba(120,197,205,1)", pointStrokeColor: "#fff", pointHighlightFill: "#fff", pointHighlightStroke: "rgba(120,197,205,1)", data: dataToBePlottedHeatIndex}]};  var myLineChart = new Chart(ctx).Line(data); Chart.defaults.global.responsive = true; document.getElementById("legendDiv").innerHTML = myLineChart.generateLegend();});    }); </script>' )

#    self.response.out.write('<script type="text/javascript"> $( document ).ready(function() { var dataToBePlotted; $.getJSON("http://localhost:9080/temperature", function(data) { dataToBePlotted = data.temperature; dataToBePlottedHumidity = data.humidity; chartLabel = data.time; console.log(data.temperature);  var ctx = document.getElementById("canvas").getContext("2d"); var data = { labels:chartLabel ,datasets: [{label: "My First dataset",fillColor: "rgba(220,220,220,0.2)",strokeColor: "rgba(220,220,220,1)", pointColor: "rgba(220,220,220,1)", pointStrokeColor: "#fff", pointHighlightFill: "#fff", pointHighlightStroke: "rgba(220,220,220,1)", data: dataToBePlotted },{ label: "My Second dataset", fillColor: "rgba(151,187,205,0.2)",strokeColor: "rgba(151,187,205,1)", pointColor: "rgba(151,187,205,1)", pointStrokeColor: "#fff", pointHighlightFill: "#fff", pointHighlightStroke: "rgba(151,187,205,1)", data: dataToBePlottedHumidity}]};  var myLineChart = new Chart(ctx).Line(data); Chart.defaults.global.responsive = true; });    }); </script>' )

# Controller for endpoint for MT7688 to post data real time
class PostData(webapp2.RequestHandler):
  def post(self):
    temperaturedata = TemperatureData(parent=ps4_key)
    temperaturedata.temperature = self.request.get('temperature')
    temperaturedata.humidity= self.request.get('humidity')
    temperaturedata.heatIndex= self.request.get('heatindex')
    temperaturedata.put()
    self.redirect('/')

# Routes
app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/tempdata', PostData),
  ('/temperature', Temperature)
], debug=True)
