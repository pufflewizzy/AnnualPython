from tkinter import BooleanVar, Button, Checkbutton, IntVar, Tk, mainloop, simpledialog, Label, PhotoImage
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import requests
from random import uniform 

# Menu
def menuWindow(previousWindow = None):
	# opens menu and hides previous window
	menu = Tk()
	menu.geometry('600x210')
	menu.title('Menu')
	menu.configure(bg='light cyan')
	label = Label(menu, text = 'Effects of COVID-19\nBy Aaron Hsu, Ella Krechmer,\nSasha Motiellal, Maret Aulenbach,\nLogan Byers, and Israel Pina',
              bd = 1,
              relief = 'solid',
              font = 'Times 12',
              width = 30,
              height = 4,
                      bg='white')
	label.pack()
	if previousWindow is not None:
		previousWindow.withdraw()

	# creates buttons for each section
	pricesButton = Button(menu, text = 'Changes in Cost of Items', command = lambda:pricesWindow(menu), bg = 'white')
	pollutionButton = Button(menu, text = 'Changes in Pollution Levels', command = lambda:pollutionWindow(menu), bg='white')
	deathsButton = Button(menu, text = 'Death Count', command = lambda:deathWindow(menu), bg='white')
	pricesButton.place(x=70, y=125)
	pollutionButton.place(x=370, y=125)
	deathsButton.place(x=255, y = 125)

# Prices
def pricesWindow(previousWindow):
	# closes menu and opens prices window
	pricesSelection = Tk()
	previousWindow.withdraw()
	pricesSelection.configure(bg='light cyan')
	pricesSelection.title('Prices of Items')
	label = Label(pricesSelection, text = 'Select item(s):',
              bd = 1,
              relief = 'solid',
              width = 15,
              height = 2,
                      bg='white')
	label.pack()
	
	# values of checkbox variables
	toiletPaperS = BooleanVar()
	toiletPaperL = BooleanVar()
	handSanitizerS = BooleanVar()
	handSanitizerL = BooleanVar()
	waterGal = BooleanVar()
	waterBot = BooleanVar()
	wipesS = BooleanVar()
	wipesL = BooleanVar()

	# checkboxes
	Checkbutton(pricesSelection, text = 'Toilet Paper (Small Pack, 12)', variable = toiletPaperS, onvalue = 1, offvalue = 0, bg='light cyan').pack()
	Checkbutton(pricesSelection, text = 'Toilet Paper (Bulk, 24)', variable = toiletPaperL, onvalue = 1, offvalue = 0, bg='light cyan').pack()
	Checkbutton(pricesSelection, text = 'Hand Sanitizer (travel size, 2 fl. oz.)', variable = handSanitizerS, onvalue = 1, offvalue = 0, bg='light cyan').pack()
	Checkbutton(pricesSelection, text = 'Hand Sanitizer (medium size, 12 fl. oz.)', variable = handSanitizerL, onvalue = 1, offvalue = 0, bg='light cyan').pack()
	Checkbutton(pricesSelection, text = 'Poland Spring Water Jug (1 Gallon)', variable = waterGal, onvalue = 1, offvalue = 0, bg='light cyan').pack()
	Checkbutton(pricesSelection, text = 'Poland Spring Pack (24 Bottles)', variable = waterBot, onvalue = 1, offvalue = 0, bg='light cyan').pack()
	Checkbutton(pricesSelection, text = 'Heavy Duty Wipes (30 ct)', variable = wipesS, onvalue = 1, offvalue = 0, bg='light cyan').pack()
	Checkbutton(pricesSelection, text = 'Heavy Duty Wipes (60 ct)', variable = wipesL, onvalue = 1, offvalue = 0, bg='light cyan').pack()

	# button that creates graph
	graphPrices = Button(pricesSelection, text = 'Graph', bg='white', command = lambda:pricesData([toiletPaperS, toiletPaperL, handSanitizerS, handSanitizerL, waterGal, waterBot, wipesS, wipesL]))
	graphPrices.pack()

	# return to menu button
	menuButton = Button(pricesSelection, text = 'Return to Menu', command = lambda:menuWindow(pricesSelection), bg='white')
	menuButton.pack()

def pricesData(checkboxes):
	data = {'Items': [],
        'Price Before Corona': [],
        'Price After Corona': [],
        'Inflation %': []}

    # reading file and parsing data
	with open('D://Coding/Python/AnnualPython/Data Analysis Project/prices.csv', 'r') as f:
		read = f.readlines()
    
	for i in range(len(read)):
		read[i] = read[i].split(', ')
		read[i][1] = float(read[i][1])
		read[i][2] = float(read[i][2])
		read[i][3] = float(read[i][3])
    
    
    # determines which items to graph
	requested = []
	for i in range(len(checkboxes)):
		if checkboxes[i].get(): requested.append(i)

    # adds requested data to the data variable
	for i in requested:
		data['Items'].append(read[i][0])
		data['Price Before Corona'].append(read[i][1])
		data['Price After Corona'].append(read[i][2])
		data['Inflation %'].append(read[i][3])

	# graphing function
	graphPrices(data)

def graphPrices(data):
	# Maret and Logan can implement graph
	# data = {'Items': [], 'Price Before Corona': [], 'Price After Corona': [], 'Inflation %': []}
	print('graphed')


# Pollution
def pollutionWindow(previousWindow):
	# closes menu and opens pollution window
	pollutionSelection = Tk()
	previousWindow.withdraw()
	pollutionSelection.geometry('300x200')
	pollutionSelection.configure(bg='light cyan')
	pollutionSelection.title('Pollution Levels')
	label = Label(pollutionSelection, text='Choose an option:',
                      bd = 1,
                      relief = 'solid',
                      width = 15,
                      height = 2,
                      bg='white')
	label.pack()

	# Graph two countries
	graphSpecific = Button(pollutionSelection, text = 'Choose certain countries to compare', command = lambda:compareWindow(pollutionSelection), bg='white')
	graphSpecific.place(x=50, y=60)
	# Graph all
	graphAll = Button(pollutionSelection, text = 'Graph all', command = lambda:pollutionData(), bg='white')
	graphAll.place(x=120, y=95)
	# return to menu button
	menuButton = Button(pollutionSelection, text = 'Return to Menu', command = lambda:menuWindow(pollutionSelection), bg='white')
	menuButton.place(x=102, y=130)

def compareWindow(previousWindow):
	# closes menu and opens pollution window
	countrySelection = Tk()
	previousWindow.withdraw()
	countrySelection.configure(bg='light cyan')
	label = Label(countrySelection, text='Select countries:',
                      bd = 1,
                      relief = 'solid',
                      width = 15,
                      height = 2,
                      bg='white')
	label.pack()

	china = BooleanVar()
	unitedStates = BooleanVar()
	india = BooleanVar()
	glob = BooleanVar()

	Checkbutton(countrySelection, text = 'China', variable = china, onvalue = True, offvalue = False, bg='light cyan').pack()
	Checkbutton(countrySelection, text = 'United States', variable = unitedStates, onvalue = True, offvalue = False, bg='light cyan').pack()
	Checkbutton(countrySelection, text = 'India', variable = india, onvalue = True, offvalue = False, bg='light cyan').pack()
	Checkbutton(countrySelection, text = 'Global', variable = glob, onvalue = True, offvalue = False, bg='light cyan').pack()

	# button that creates graph
	graphPrices = Button(countrySelection, text = 'Graph', command = lambda:pollutionData([china, unitedStates, india, glob]), bg='white')
	graphPrices.pack()

	# return to menu button
	menuButton = Button(countrySelection, text = 'Return to Menu', command = lambda:menuWindow(countrySelection), bg='white')
	menuButton.pack()



def pollutionData(checkboxes = None):
	with open('D://Coding/Python/AnnualPython/Data Analysis Project/pollution.csv', 'r') as f:
		read = f.readlines()
	
	data = {'Countries': [], 
			'Pollution estimate before': [], 
			'Pollution estimate after': []}

	for i in range(len(checkboxes)):
		print(checkboxes[i].get())

	for i in range(len(read)):
		read[i] = read[i].split(',')
		read[i][1] = float(read[i][1])
		read[i][2] = float(read[i][2][:-2])

	if checkboxes is not None:
		# if user decides to only graph certain countries
		requested = []
		for i in range(len(checkboxes)):
			if bool(checkboxes[i].get()): requested.append(i)
		
		print(requested)
		for i in requested:
			data['Countries'].append(read[i][0])
			data['Pollution estimate before'].append(read[i][1])
			data['Pollution estimate after'].append(read[i][2])
	else:
		# user wants all data
		for i in range(len(read)):
			data['Countries'].append(read[i][0])
			data['Pollution estimate before'].append(read[i][1])
			data['Pollution estimate after'].append(read[i][2])

	graphPollution(data)

def graphPollution(data):
	print(data)


# Deaths
def deathWindow(previousWindow):
        # closes menu and prompts user for a country
        previousWindow.withdraw()


        # asks user to input country
        unformattedCountry = simpledialog.askstring('Country', 'Insert Country (ex: South Africa):')
        if unformattedCountry is None:
                menuWindow()

        # formats the userinput to work with API
        formattedCountry = ''
        for i in unformattedCountry.split(' '):
                formattedCountry += i.lower()
                formattedCountry += '-'
        formattedCountry = formattedCountry[:-1]


        # asks user to input date
        unformattedDate = simpledialog.askstring('Date', 'Insert Date (ex: 4/23):')
        if unformattedDate is None:
                menuWindow()
        unformattedDate1 = simpledialog.askstring('Date', 'Insert Date (ex: 5/1):')
        temp_dict = {}
        # creates two variables that symbolize the start and end of temp_dict. The second variable will be added to the dictionary where it says "here"
        for i in unformattedDate:
                if i == "/":
                        startpoint = int(unformattedDate[:unformattedDate.find(i)])
                        temp_var = unformattedDate[unformattedDate.find(i)+1:]
                        temp_var = int(temp_var)
                        temp_dict[1] = [startpoint,temp_var]
                        startpoint = startpoint*100 + temp_var
                        startpoint1 = startpoint
        for i in unformattedDate1:
                if i == "/":
                        endpoint = int(unformattedDate1[:unformattedDate1.find(i)])
                        temp_var1 = unformattedDate1[unformattedDate1.find(i)+1:]
                        temp_var1 = int(temp_var1)
                        endpoint = endpoint*100 + temp_var1
        arr = []
        a = 2
        startpoint += 7
        # this gets all the dates in intervals of one week
        while True:
                if startpoint%100 > 30:
                        startpoint += 70
                if startpoint >= endpoint:
                        break
                temp_dict[a] = [startpoint//100,startpoint%100]
                a += 1
                startpoint += 7
        # here
        endpoint = int(unformattedDate1[:unformattedDate1.find("/")])
        temp_dict[a] = [endpoint,temp_var1]
        # formats the userinput to work with API
        formattedList = []
        for j in temp_dict.values():
                if int(j[1]) < 10:
                        formattedDate = "0" + str(j[0]) + "-0" + str(j[1])
                else:
                        formattedDate = "0" + str(j[0]) + "-" + str(j[1])
                formattedList.append(formattedDate)

        # calls formatting data
        deathData(formattedCountry,formattedList,a)

# parses everything
def searcher(string,element):
        temp_string = string
        output = 0
        placeholder = temp_string.count(element)
        for i in range(placeholder):
                starter = temp_string.find(element)+3+len(element)
                temp_string1 = temp_string[starter:ender(temp_string,starter)]
                temp_string.replace(element,"",1)
                output += int(temp_string1)
        return output

# returns the position of the start of the numbers
def ender(string,start):
        return (start+string[start:].find(","))

# Logan you can use this to create a random color for each bar/line
def randomRGBA():
    r = uniform(0,1)
    b = uniform(0,1)
    g = uniform(0,1)
    a = uniform(0,1)
    rgb_value = [r, g, b, a]
    return rgb_value

def deathData(country,formattedList,distance):
        data = {}
        # grabs the data for all of the dates
        temp_storage_stuff = [""]
        for i in formattedList:
                print(i)
                url = "https://api.covid19api.com/live/country/" + country + "/status/confirmed/date/2020-" + i + "T13:13:30Z"
                payload = {}
                headers= {}
                response = requests.request("GET", url, headers=headers, data = payload)
                unformattedData = str(response.text.encode('utf8'))
                # Maret and Logan: 'unformattedData' is a string
                # data[date] = [country,confirmed,deaths,recovered,active]
                stuff1 = [country,searcher(unformattedData,"Confirmed"),searcher(unformattedData,"Deaths"),searcher(unformattedData,"Recovered"),searcher(unformattedData,"Active")]
                if stuff1 == temp_storage_stuff:
                        distance -= 1
                        continue
                else:
                        data[i] = stuff1
                temp_storage_stuff = data[i]
        # a total number of things equivalent to the variable distance (one of the inputs of this function) need to be graphed
        print(data)
        graphDeaths(data)

def graphDeaths(data):
        # graphs data for confired, deaths, active, and recovery
        print(data)
        deaths = []
        confirmed = []
        recovered = []
        active = []
        country = []
        menuWindow()
        count = []
        s = 0
        for i in data:
                count.append(s)
                s += 1
                
        for i in data:
                country.append(data[i][0])
        for i in data:
                deaths.append(data[i][1])
        for i in data:
                confirmed.append(data[i][2])
        for i in data:
                recovered.append(data[i][3])
        for i in data:
                active.append(data[i][4]) 
                
        x1 = count
        y1 = deaths
        x2 = count
        y2 = confirmed
        x3 = count
        y3 = recovered
        x4 = count
        y4 = active
        
        plt.plot (x1,y1,
                  label = 'Confirmed')
        plt.plot (x2,y2,
                  label = 'Deaths')
        plt.plot (x3,y3,
                  label = 'Recovered')
        plt.plot (x4,y4,
                  label = 'Active')
        
        plt.title(country[0])
        plt.ylabel('People')
        plt.xlabel('Weeks since initial date')

        plt.legend()
        plt.grid(True, color = 'k')
        plt.show()

# starts program
menuWindow()

mainloop()

