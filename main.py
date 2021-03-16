from tkinter import *
import requests
import json
import os # This is needed to import the api environment variable
my_api = os.environ.get('AIRNOW_API')
print(type(my_api))
root = Tk()
root.title('Weather app by AG')
root.configure(background='white')
root.geometry("400x100")

myLabel = Label(root)

# Create Zipcode Lookup function
def zipLookup():
    try:
        global myLabel
        myLabel.destroy()
        api_requests = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get()+ my_api)
        api = json.loads(api_requests.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        if category == 'Good':
            weather_color = '#00e400'
        elif category == "Moderate":
            weather_color = '#ffff00'
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = '#ff7e00'
        elif category == "Unhealthy":
            weather_color = '#ff0000'
        elif category == "Very Unhealthy":
            weather_color = '#8f3f97'
        elif category == "Hazardous":
            weather_color = '#7e0023'
        root.config(background=weather_color)
        myLabel = Label(root, text=city + "  Air Quality " + str(quality) + ' ' + category, font=("Helvetica", 20), background=weather_color)
        myLabel.grid(row=1, column =0, columnspan=2)
    except Exception as e:
        api = "404 Unable to load API"
        myLabel = Label(root, text=api, font=("Helvetica", 20))
        myLabel.grid(row=1, column =0, columnspan=2)



zip = Entry(root)
zip.grid(row=0, column=0)

zipButton = Button(root, text="Lookup Zipcode", command=zipLookup)
zipButton.grid(row=0, column=1)


root.mainloop()
