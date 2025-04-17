while True:
    try:
        age = int(input("Units of time alive calculator! Enter your age in years, great alpha: ")) 
        if age == 0:
            print("lol ok")
            break
    except ValueError:
        print("nah.")
        
#picoseconds of life in a desired age.
    sump = (31557600000000000000 * age)
    print ("amount of picoseconds in")
    print (age)
    print ("years of life!")
    print (sump)
    print ("-------------")
    print ("-------------")     
#seconds of life in a desired age.
    sumsec = (60 * 60 * 24 * 365.2425 * age)
    print ("amount of seconds in")
    print (age)
    print ("years of life!")
    print (sumsec)
    print ("-------------")
    print ("-------------")
# minutes of life in a desired age.
    summin = (525600 * age)
    print ("amount of minutes in")
    print (age)
    print ("years of life!")
    print (summin)
    print ("-------------")
    print ("-------------")
#hours of life in a desired age.
    sumh = (8760 * age)
    print ("amount of hours in")
    print (age)
    print ("years of life!")
    print (sumh)
    print ("-------------")
    print ("-------------")
#days of life in a desired age.
    sumd = (365.2425 * age)
    print ("amount of days in")
    print (age)
    print ("years of life!")
    print (sumd)
    print ("-------------")
    print ("-------------")
#weeks of life in a desired age.
    sumw = (52 * age)
    print ("amount of weeks in")
    print (age)
    print ("years of life!")
    print (sumw)
    print ("-------------")
    print ("-------------")
#months of life in a desired age.
    summ = (12 * age)
    print ("amount of months in")
    print (age)
    print ("years of life!")
    print (summ)
    print ("-------------")
    print ("-------------")
#years of life in a desired age.
    sumy = (age)
    print ("and of course, naturally, how many years in")
    print (age)
    print ("years of life!")
    print (sumy)
