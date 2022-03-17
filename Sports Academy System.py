#Brian Joseph Keyrupan
#TP060173

#Login function
def login(user,txtfile,nextfunc,previousfunc):
    print ("\n\n\t*************Real Champions Sport Academy**************\n"+user+" Login")
    #check in the txt file
    valid=False
    yon=''
    while not valid:
        f=open(txtfile,'r')
        filelist=f.readlines()
        f.close()
        #enter username
        username=(input('Enter your Username: '))
        #enter password
        password=(input('Enter your Password: '))
        for datalist in filelist:
            data=datalist.split('\t')
            if username==data[0] and password==data[1]:
                print('Logged in')
                valid=True
                user=data #the data list of the user will be from 'student' to the user's login data itself
                break #break from the forelseloop when found username because every username is unique
        else:
            print('\nIncorrect Username or Password\nTry again?')
            yon=input("Enter 'y' for Yes to try again, 'n' for No to go back: ")
            while yon!='y' and yon!='n':
                yon=input("Incorrect input\nEnter 'y' for Yes to try again, 'n' for No to go back: ")
            if yon=='y':
                pass
            else:
                valid=True
    if yon=='n':
        previousfunc()
    else:
        nextfunc(user)

#register GENDER
def enter_gender():
    gender=input("\nEnter your Gender\n'm' for Male, 'f' for Female: ")
    while gender!='m' and gender!='f':
        gender=input("\nIncorrect input\nEnter 'm' for Male, 'f' for Female: ")
    if gender=='m':
        gender='Male'
    else:gender="Female"
    return gender
#register PHONE NUMBER
def enter_phone():
    phone=input("\nEnter Phone Number: ")
    valid=False
    while valid==False:
        for i in phone:
            if i!='1' and i!='2' and i!='3' and i!='4' and i!='5' and i!='6' and i!='7' and i!='8' and i!='9' and i!='0':
                phone=input('\nIncorect Input\nEnter Phone Number: ')
                break
        else:
            valid=True
    return phone
    pass
#register EMAIL
def enter_email():
    email=input('\nEnter your Email Address: ')
    valid=False
    while valid==False:
        for i in email:
            if i=='@':
                valid=True
                break
        else:
            email=input('\nInvalid email\nPlease enter your correct Email Address: ')
    return email
#register DATE OF BIRTH
def enter_dob():
    print('\nEnter your date of birth, dd/mm/yyyy')
    day=input('Enter day of birth (dd): ')
    nums=[]
    for i in range(1,32):
        if i<10:
            a='0'+str(i)
        else:a=str(i)
        nums.append(a)
    while day not in nums:
        day=input('\nIncorrect input, Please enter day of birth (dd): ')

    print('\nYour date of birth, '+day+'/mm/yyyy')
    month=input('Enter month of birth (mm): ')
    nums=[]
    for i in range(1,13):
        if i<10:
            a='0'+str(i)
        else:a=str(i)
        nums.append(a)
    while month not in nums:
        month=input('\nIncorrect input, Please enter month of birth (mm): ')

    print('\nYour date of birth, '+day+'/'+month+'/yyyy')
    year=input('Enter year of birth (yyyy): ')
    nums=[]
    for i in range(1900,2500):
        a=str(i)
        nums.append(a)
    while year not in nums:
        year=input('\nIncorrect input, Please enter year of birth (yyyy): ')

    date=str(day+'/'+month+'/'+year)
    return date
#REGISTER DATA
def enter_data():
    #enter full name
    name=input("\nEnter your Fullname: ")
    while name=='' or name==' ':
        name=input("\nInvalid Input\nEnter your Fullname: ")
    name=name[0].upper()+name[1:]
    #enter gender
    gender=enter_gender()
    #enter phone number
    phone=enter_phone()
    #email email address
    email=enter_email()
    #enter address
    address=input('\nEnter your Address: ')
    while address=='' and address==' ':
        address=input("\nInvalid Input\nEnter your Address: ")
    #enter dob
    dob=enter_dob()
    return name,gender,dob,phone,email,address
#confirm/change data
def confirm_data(name,gender,dob,phone,email,address):
    confirm=False
    while confirm==False:
        print('\n1. Name          : '+name+
            '\n2. Gender        : '+gender+
            '\n3. Date of Birth : '+dob+
            '\n4. Phone Number  : '+phone+
            '\n5. Email         : '+email+
            '\n6. Address       : '+address)
        yon=input("To confirm your data\nEnter 'y' for YES, 'n' for NO: ")
        while yon!='y' and yon!='n':
            yon=input("Incorrect input!\nTo confirm your data\nEnter 'y' for YES, 'n' for NO to change: ")
        if yon=='y':
            confirm=True
        elif yon=='n':
            print('\n1. Name          : '+name+
            '\n2. Gender        : '+gender+
            '\n3. Date of Birth : '+dob+
            '\n4. Phone Number  : '+phone+
            '\n5. Email         : '+email+
            '\n6. Address       : '+address)
            fix=input("Which data would you like to change?\nEnter the number you'd like to change: ")
            while fix!='1' and fix!='2' and fix!='3' and fix!='4' and fix!='5' and fix!='6':
                print('\n1. Name          : '+name+
                '\n2. Gender        : '+gender+
                '\n3. Date of Birth : '+dob+
                '\n4. Phone Number  : '+phone+
                '\n5. Email         : '+email+
                '\n6. Address       : '+address)                
                print("Incorrect input, enter either '1', '2', '3', '4', '5', or'6'")
                fix=input("Which data would you like to change?\nEnter the number you'd like to change: ")
            if fix=='1':
                name=input("\nEnter your Fullname: ")
                while name=='' and name==' ':
                    name=input("\nInvalid Input\nEnter your Fullname: ")
                name=name[0].upper()+name[1:]
            elif fix=='2':
                gender=enter_gender()
            elif fix=='3':
                dob=enter_dob()
            elif fix=='4':
                phone=enter_phone()
            elif fix=='5':
                email=enter_email()
            else: 
                address=input('\nEnter your Address: ')
                while address=='' and address==' ':
                    address=input("\nInvalid Input\nEnter your Address: ")
    return name,gender,dob,phone,email,address

#register USERNAME
def enter_username(textfile):
    f=open(textfile,'r')
    filelist=f.readlines()
    f.close()
    usernamelist=[]
    for data in filelist:
        if data=='':
            break
        datalist=data.split('\t')
        usernamelist.append(datalist[0])

    valid=False
    username=input('\nEnter a Username: ')
    if (usernamelist==[]):
        while len(username)<5:
            username=input('\nUsername too short, it has to be at least 5 characters\nPlease enter a Username: ')
        valid=True
    #checks if username used
    while valid==False:
        for usernames in usernamelist:
            if len(username)<5:
                username=input('\nUsername too short, it has to be at least 5 characters\nPlease enter a Username: ')
                break
            elif username==usernames:
                username=input('\nUsername used, Please try a different Username\nEnter a Username: ')
                break
            else:
                valid=True
    return username
#register PASSWORD
def enter_password():
    valid=False
    while valid==False:
        password=input('\nEnter a Password: ')
        while len(password)<5:
            print('\nPassword too short, must be at least 5 characters')
            password=input('Enter a Password: ')
        cpass=input('Enter the same Password to confirm: ')
        if password!=cpass:
            print('\nPassword are not the same\nEnter again')
        else: valid=True
    return password
#confirm Username and Password
def confirm_up(username, password, textfile):
    confirm=False
    while confirm==False:
        print('\n1. Username: '+username+
            '\n2. Password: '+password+
            '\nConfirm password?')
        yon=input("To confirm your data\nEnter 'y' for YES, 'n' for NO to change: ")
        while yon!='y' and yon!='n':
            yon=input("Incorrect input!\nTo confirm your data\nEnter 'y' for YES, 'n' for NO to change: ")
        if yon=='y':
            confirm=True
        elif yon=='n':
            print('\n1. Username: '+username+
            '\n2. Password: '+password+
            "\nWhich data would you like to change?\nEnter the number you'd like to change: ")
            fix=input("Enter '1' for Username, '2' for Password: ")
            while fix!='1' and fix!='2':
                print('\n1. Username: '+username+'\n2. Password: '+password+
                "\nIncorrect input, enter either '1' or '2'\nWhich data would you like to change?\nEnter the number you'd like to change: ")
                fix=input("Enter '1' for Username, '2' for Password: ")
            if fix=='1':
                username=enter_username(textfile)
            elif fix=='2':
                password=enter_password()
    return username, password

#enter date
def enter_date(date):
    print('\nEnter Date Coach '+date+', dd/mm/yyyy')
    day=input('Enter day of date(dd): ')
    nums=[]
    for i in range(1,32):
        if i<10:
            a='0'+str(i)
        else:a=str(i)
        nums.append(a)
    while day not in nums:
        day=input('\nIncorrect input, Please enter day of date (dd): ')

    print('\nDate '+date+', '+day+'/mm/yyyy')
    month=input('Enter month of date (mm): ')
    nums=[]
    for i in range(1,13):
        if i<10:
            a='0'+str(i)
        else:a=str(i)
        nums.append(a)
    while month not in nums:
        month=input('\nIncorrect input, Please enter month of date (mm): ')

    print('\nDate '+date+', '+day+'/'+month+'/yyyy')
    year=input('Enter year of date (yyyy): ')
    nums=[]
    for i in range(1900,2500):
        a=str(i)
        nums.append(a)
    while year not in nums:
        year=input('\nIncorrect input, Please enter year of date (yyyy): ')

    date=str(day+'/'+month+'/'+year)
    return date
#register date join
def djoin():
    date='Join'
    datejoin=enter_date(date)
    return datejoin
#register date terminated
def dterminate():
    date='Terminate'
    dateterminate=enter_date(date)
    return dateterminate
#register hourly rate
def enter_hourly_rate():
    rate=input("\nEnter Coach Hourly Rate: ")
    valid=False
    while valid==False:
        for i in rate:
            if i!='1' and i!='2' and i!='3' and i!='4' and i!='5' and i!='6' and i!='7' and i!='8' and i!='9' and i!='0':
                rate=input('\nIncorect Input\nEnter Coach Hourly Rate: ')
                break
        else:
            valid=True
    return 'RM'+rate
#confirm date and rate
def confirm_date_rate(datejoin,dateterminate,rate):
    confirm=False
    while confirm==False:
        print('\nDate Joined: '+datejoin+'\nDate Terminated: '+dateterminate+'\nHourly Rate: '+rate)
        yon=input("To confirm the data\nEnter 'y' for YES, 'n' for NO to change: ")
        while yon!='y' and yon!='n':
            yon=input("Incorrect input!\nTo confirm the data\nEnter 'y' for YES, 'n' for NO to change: ")
        if yon=='y':
            confirm=True
        elif yon=='n':
            print('\n1. Date Joined: '+datejoin+'\n2. Date Terminated: '+dateterminate+'\n3. Hourly Rate: '+rate)
            fix=(input("Enter '1', '2', or '3': "))
            while fix!='1' and fix!='2' and fix!='3':
                print('\n1. Date Joined: '+datejoin+'\n2. Date Terminated: '+dateterminate+'\n3. Hourly Rate: '+rate)
                fix=(input("Incorrect Input\nEnter '1', '2', or '3': "))
            if fix=='1':
                datejoin=djoin()
            elif fix=='2':
                if dateterminate!='-':
                    yon=input("This coach has been terminated\nWould you like to delete termination\nEnter 'y' for yes, 'n' for No")
                    while yon!='y' and yon!='n':
                        yon=input("\nIncorrect input\nThis coach has been terminated\nWould you like to delete termination\nEnter 'y' for yes, 'n' for No")
                    if yon=='y':
                        dateterminate='-'
                else:
                    dateterminate=dterminate()
            else: rate=enter_hourly_rate()

    return datejoin,dateterminate,rate

#register sport center
def enter_sportcenter():
    print('\n1. Bukit Bintang\n2. Petaling Jaya\n3. Subang Jaya')
    sportcntr=input('Enter the Sport Center: ')
    while sportcntr!='1' and sportcntr!='2' and sportcntr!='3':
        print('\n1. Bukit Bintang\n2. Petaling Jaya\n3. Subang Jaya\nIncorrect Input')
        sportcntr=input("Please enter either '1', '2', or '3': ")
    if sportcntr=='1':
        sportcntr='BB'
    elif sportcntr=='2':
        sportcntr='PJ'
    else: sportcntr='SJ'
    return sportcntr
#register sport
def enter_sport():
    print("\n1. Archery\n2. Badminton\n3. Basketball\n4. Cricket\n5. Football\n6. Gymnastics\n7. Swimming\n8. Table Tennis\n9. Tennis\n10. Volleyball ")
    sport=input("Enter the Sport: ")
    while sport!='1' and sport!='2' and sport!='3' and sport!='4' and sport!='5' and sport!='6' and sport!='7' and sport!='8' and sport!='9' and sport!='10' :
        print("\n1. Archery\n2. Badminton\n3. Basketball\n4. Cricket\n5. Football\n6. Gymnastics\n7. Swimming\n8. Table Tennis\n9. Tennis\n10. Volleyball ")
        print('\nIncorrect input')
        sport=input("Please enter either '1', '2', '3', '4', '5', '6', '7', '8', '9' or '10': ")
    if sport=='1':
        sportid='ARC'
    elif sport=='2':
        sportid='BMT'
    elif sport=='3':
        sportid='BSK'
    elif sport=='4':
        sportid='CRT'
    elif sport=='5':
        sportid='FTB'
    elif sport=='6':
        sportid='GYM'
    elif sport=='7':
        sportid='SWM'
    elif sport=='8':
        sportid='TBL'
    elif sport=='9':
        sportid='TNS'
    else: sportid='VLB'
    return sportid
#center code to center converter
def center_decode(sportcntr):
    if sportcntr=='BB':
        return 'Bukit Bintang'
    elif sportcntr=='PJ':
        return 'Petaling Jaya'
    else: return 'Subang Jaya'
#sport code to sport coverter
def sport_decode(sportid):
    if sportid=='ARC':
        sport='Archery'
    elif sportid=='BMT':
        sport='Badminton'
    elif sportid=='BSK':
        sport='Basketball'
    elif sportid=='CRT':
        sport='Cricket'
    elif sportid=='FTB':
        sport='Football'
    elif sportid=='GYM':
        sport='Gymnastics'
    elif sportid=='SWM':
        sport='Swimming'
    elif sportid=='TBL':
        sport='Table Tennis'
    elif sportid=='TNS':
        sport='Tennis'
    else: sport='Volleyball'
    
    return sport
#confirm sportcenter and sport
def confirm_sport(sportid,sportcntr):
    sportname=sport_decode(sportid)
    center=center_decode(sportcntr)
    confirm=False
    while confirm==False:
        print('\n1. Sport         : '+sportname+
            '\n2. Sport Center  : '+center+
            '\nConfirm?')
        yon=input("To confirm data\nEnter 'y' for YES, 'n' for NO to change: ")
        while yon!='y' and yon!='n':
            yon=input("Incorrect input!\nTo confirm data\nEnter 'y' for YES, 'n' for NO to change: ")
        if yon=='y':
            confirm=True
        elif yon=='n':
            print('\n1. Sport         : '+sportname+'\n2. Sport Center  : '+center+
            "\nWhich data would you like to change?\nEnter the number you'd like to change: ")
            fix=input("Enter '1' for Sport, '2' for Sport Center: ")
            while fix!='1' and fix!='2':
                print('\n1. Sport         : '+sportname+'\n2. Sport Center  : '+center+
                "\nIncorrect input, enter either '1' or '2'\nWhich data would you like to change?\nEnter the number you'd like to change: ")
                fix=input("Enter '1' for Sport, '2' for Sport Center: ")
            if fix=='1':
                sportid=enter_sport()
                sportname=sport_decode(sportid)
            elif fix=='2':
                sportcntr=enter_sportcenter()
                center=center_decode(sportcntr)
    return sportid, sportcntr

#register studentID
def enter_student_id(textfile,dob):
    f=open(textfile,'r')
    filelist=f.readlines()
    f.close
    if filelist==[]:
        numid='1'
    else:
        laststudent=filelist[-1]
        getid=laststudent.split('\t')
        laststudentid=getid[2]
        x=len(laststudentid)
        num=laststudentid[:x-2]
        numid=int(num)+1
    dateid=dob[-2:]
    newid=str(numid)+dateid
    return newid
#Register a Student
def register_student(user,useradmin):
    print ("\n\n\t*************Real Champions Sport Academy**************\nRegister Student")
    #enter the data
    name,gender,dob,phone,email,address=enter_data()
    #confirm the data
    name,gender,dob,phone,email,address=confirm_data(name,gender,dob,phone,email,address)

    #username
    textfile='studentdata.txt'
    username=enter_username(textfile)
    #password
    password=enter_password()
    #confirm username and password
    username,password=confirm_up(username,password,textfile)

    #id
    textfile='studentdata.txt'
    studentid=enter_student_id(textfile,dob)

    #write the data into the txt file
    datalist=[username,password,studentid,name,gender,dob,phone,email,address]
    acc=''
    for i in datalist:
        if i==datalist[-1]:
            acc+=i+'\n'
        else:
            acc+=i+'\t'
    file=open('studentdata.txt','a')
    file.write(acc)
    file.close()
    print('\nStudentID created',studentid)
    ok=input('Enter anything to continue: ')
    if useradmin==True:
        #used user admin=True if it is registered by the admin
        #if the registration from admin go back to admin register function
        admin_register(user)
    else:
        #used if useradmin==False this is to check who registered admin/student
        #When done regestering go back to registered_student() to login
        registered_student()

#register coachID
def enter_coach_id(textfile,dob,sportcntr,sportid):
    f=open(textfile,'r')
    filelist=f.readlines()
    f.close()
    if filelist==[]:
        newsportnum='1'
        newcoachnum='1'
    else:
        lastcoach=filelist[-1]
        coachdata=lastcoach.split('\t')
        coachid=coachdata[0]

        #find the same sport
        sportcoachlist=[]
        for i in filelist:
            data=i.split('\t')
            datasportid= data[0]
            if datasportid[2:5]==sportid:
                sportcoachlist.append(datasportid)
        if sportcoachlist==[]:
            newsportnum='1'
        else:
            lastsportdata=sportcoachlist[-1]
            #ex. coach id=BBBMT20.1102
            sportlist=lastsportdata.split('.')
            sportnums=sportlist[0]
            #BBBMT20
            sportnum=sportnums[5:]
            newsportnum=int(sportnum)+1

        lastnumid=coachid.split('.')
        coachnums=lastnumid[1]
        #1102
        x=len(coachnums)
        coachnum=coachnums[:x-2]
        newcoachnum=int(coachnum)+1

    dateid=dob[-2:]

    newid=sportcntr+sportid+str(newsportnum)+'.'+str(newcoachnum)+dateid
    return newid
#Register a Coach
def register_coach(user):
    print ("\n\n\t*************Real Champions Sport Academy**************\nRegister Coach")
    #enter the data
    name,gender,dob,phone,email,address=enter_data()
    #confirm the data
    name,gender,dob,phone,email,address=confirm_data(name,gender,dob,phone,email,address)

    #enter date join
    datejoin=djoin()
    #enter date terminated:
    dateterminate='-'
    #enter hourly rate
    rate=enter_hourly_rate()
    #confirm date and rate
    datejoin,dateterminate,rate=confirm_date_rate(datejoin,dateterminate,rate)

    #enter sport center
    sportcntr=enter_sportcenter()
    #enter sport and sport center and id
    sportid=enter_sport()
    #confirm
    sportid,sportcntr=confirm_sport(sportid,sportcntr)

    #enter coach id
    textfile='coachdata.txt'
    coachid=enter_coach_id(textfile, dob, sportcntr, sportid)

    #enter rating
    rating='rating:0'

    datalist=[coachid,name,gender,dob,phone,email,address,datejoin,dateterminate,rate,rating]
    coachacc=''
    for i in datalist:
        if i==datalist[-1]:
            coachacc+=i+'\n'
        else:
            coachacc+=(i+'\t')

    file=open('coachdata.txt','a')
    file.write(coachacc)
    file.close()

    print('\nID: '+coachid)
    ok=input('This is the coach id created\nEnter anything to go back: ')
    admin_register(user)

#enter day
def register_day():
    days=['\n1. Monday','2. Tuesday','3. Wednesday','4. Thursday','5. Friday','6. Saturday','7. Sunday']
    for i in days:
        print(i)
    num=input('Enter the number of the day: ')
    while num!='1' and num!='2' and num!='3' and num!='4' and num!='5' and num!='6'and num!='7':
        num=input("Incorrect Input\nEnter '1','2','3','4','5','6', or '7'\nEnter the number of the day: ")
    if num=='1':
        day='Monday'
    elif num=='2':
        day='Tuesday'
    elif num=='3':
        day='Wednesday'
    elif num=='4':
        day='Thursday'
    elif num=='5':
        day='Friday'
    elif num=='6':
        day='Saturday'
    else: day='Sunday'
    return num,day
#decode from num to day
def day_decode(num):
    if num=='1':
        day='Monday'
    elif num=='2':
        day='Tuesday'
    elif num=='3':
        day='Wednesday'
    elif num=='4':
        day='Thursday'
    elif num=='5':
        day='Friday'
    elif num=='6':
        day='Saturday'
    else: day='Sunday'
    return day
#enter time
def register_time():
    print("\nEnter time of schedule (hh/mm)\nenter '07' for 7am and enter '14' for 2pm")
    hour=input('Enter the hour of time: ')

    valid=False
    while valid==False:
        while len(hour)!=2:
            hour=input("\nIncorect Input\nEnter '07' for 7am and enter '14' for 2pm\nEnter the hour of time: " )
        for i in hour:
            if i!='1' and i!='2' and i!='3' and i!='4' and i!='5' and i!='6' and i!='7' and i!='8' and i!='9' and i!='0':
                hour=input("\nIncorect Input\nEnter '07' for 7am and enter '14' for 2pm\nEnter the hour of time: " )
                break
        else:
            valid=True

    minute=input("\nEnter the minute of time: ")

    valid=False
    while valid==False:
        while len(minute)!=2:
            minute=input("\nIncorect Input\nEnter the minute of time: " )
        for i in minute:
            if i!='1' and i!='2' and i!='3' and i!='4' and i!='5' and i!='6' and i!='7' and i!='8' and i!='9' and i!='0':
                minute=input("\nIncorect Input\nEnter the minute of time: " )
                break
        else:
            valid=True

    return hour,minute
#confirm schedule
def confirm_schedule(sport,sportcntr,num,day,hour,minute):
    confirm=False
    while confirm==False:
        time=hour+':'+minute
        print(  '\n1. Sport    : '+sport+
                '\n2. Center   : '+sportcntr+'\n3. Day      : '+day+'\n4. Time     : '+time)
        yon=input("To confirm the data\nEnter 'y' for YES, 'n' for NO to change: ")
        while yon!='y' and yon!='n':
            yon=input("Incorrect input!\nTo confirm the data\nEnter 'y' for YES, 'n' for NO to change: ")
        if yon=='y':
            confirm=True
        elif yon=='n':
            print(  '\n1. Sport    : '+sport+'\n2. Center   : '+sportcntr+'\n3. Day      : '+day+'\n4. Time     : '+time)
            fix=(input("Enter '1', '2', '3' or '4': "))
            valid=False
            while  valid==False:
                while fix!='1' and fix!='2' and fix!='3' and fix!='4':
                    print( '\n1. Sport    : '+sport+'\n2. Center   : '+sportcntr+'\n3. Day      : '+day+'\n4. Time     : '+time)                
                    fix=(input("Incorrect Input\nEnter '1', '2', '3' or '4': "))
                if fix=='1' or fix=='2':
                    print(  '\n1. Sport    : '+sport+'\n2. Center   : '+sportcntr+'\n3. Day      : '+day+'\n4. Time     : '+time)
                    print('Sport and sport center unable to be changed\nTo change this admin has to make new coach id and terminate the old one')
                    fix=(input("Incorrect Input\nEnter '1', '2', '3' or '4': "))
                else: valid=True
            if fix=='3':
                num,day=register_day()
            else: 
                hour, minute=register_time()
                time=hour+':'+minute
    return sport,sportcntr,num,day,hour,minute
#decode schedule id
def schedule_decode(scheduleid):
    scntrid=scheduleid[:2]
    sportid=scheduleid[2:5]
    dayid=scheduleid[5]
    time=scheduleid[6:]

    sport=sport_decode(sportid)
    sportcntr=center_decode(scntrid)
    day=day_decode(dayid)
    time=time[:2]+':'+time[2:]

    return sport+', '+sportcntr+' Real Champion Sport Center'+' on '+day+' at '+time

#Register a schedule
def register_schedule(user):
    print('\nWhich Coach to register Schedule?\nSearch by ID')
    coachidinput=input("Enter the Coach's ID: ")
    coachidinput=coachidinput.upper()

    f=open('coachdata.txt','r')
    filelist=f.readlines()
    f.close()

    for data in filelist:
        datalist=data.split('\t')
        if coachidinput==datalist[0]:
            scntrid=datalist[0][:2]
            sportcntr=center_decode(scntrid)
            sportid=datalist[0][2:5]
            sport=sport_decode(sportid)
            schedule=''
            if datalist[8]!='-':
                print('Coach id has been terminated')
                tryagain=input("Search again?\nEnter 'y' for Yes, 'n' for No to Go back: ")
                while tryagain!='y' and tryagain!='n':
                    tryagain=input("Incorrect input\nCoach with id:"+coachidinput+" not found\nSearch again?\nEnter 'y' for Yes, 'n' for NO to Go back: ")
                if tryagain=='y':
                    register_schedule(user)
                    break
                else:
                    admin_register(user)
                    break
            else:
                #see all schedule
                if len(datalist[10])!=10:
                    schedule='none'
                    lastschedule=10
                else:
                    for i in range(10,len(datalist)):
                        if len(datalist[i])!=10:
                            lastschedule=i
                            break
                        else:
                            schedule+=datalist[i]+', '

                print( '\nID           : '+datalist[0]+
                '\nName         : '+datalist[1]+
                '\nSport        : '+sport+
                '\nSportCenter  : '+sportcntr+
                '\nSchedule     : '+schedule)
                yon=input("Is this the Coach to add the schedule?\nEnter 'y' for YES, 'n' for NO to go back: ")
                while yon!='y' and yon!='n':
                    yon=input("Incorrect input!\nIs this the Coach to add the schedule?\nEnter 'y' for YES, 'n' for NO to go back: ")
                if yon=='n':
                    admin_register(user)
                elif yon=='y':
                    sport=sport_decode(sportid)
                    num,day=register_day()
                    hour,minute=register_time()
                    sport,sportcntr,num,day,hour,minute=confirm_schedule(sport,sportcntr,num,day,hour,minute)
                scheduleid=scntrid+sportid+num+hour+minute

                datalist=datalist[:lastschedule]+[scheduleid]+datalist[lastschedule:]

                coachid=datalist[0].split('.')
                coachidindex=coachid[1]
                x=len(coachidindex)
                coachindex=(int(coachidindex[:x-2]))-1
                textfile='coachdata.txt'

                f=open(textfile,'r')
                filelist1=f.readlines()
                f.close()
                f=open(textfile,'w')
                coachdata=list_to_str(datalist)
                filelist1[coachindex]=coachdata
                for i in filelist1:
                    f.write(i)
                f.close()

                print('\nSchedule ID: '+scheduleid)
                ok=input('This is the schedule id created\nEnter anything to go back: ')

                admin_register(user)
                break

    else: 
        print("\nCoach with id:"+coachidinput+' not found')
        tryagain=input("Search again?\nEnter 'y' for Yes, 'n' for No to Go back: ")
        while tryagain!='y' and tryagain!='n':
            tryagain=input("Incorrect input\nCoach with id:"+coachidinput+" not found\nSearch again?\nEnter 'y' for Yes, 'n' for NO to Go back: ")
        if tryagain=='y':
            register_schedule(user)
        else:
            admin_register(user)

#Register an Admin
def register_admin(user):
    print ("\n\n\t*************Real Champions Sport Academy**************\nRegister Admin")
    #enter name
    def enter_name():
        name=input("Enter name: ")
        confirm=False
        while confirm==False:
            print('\nName: '+name)
            yon=input("To confirm your name\nEnter 'y' for YES, 'n' for NO: ")
            while yon!='y' and yon!='n':
                yon=input("Incorrect input!\nTo confirm your data\nEnter 'y' for YES, 'n' for NO to change: ")
            if yon=='y':
                confirm=True
            elif yon=='n':
                name=input("Enter name: ")
        return name
    name=enter_name()

    textfile='adminlogin.txt'
    #username
    username=enter_username(textfile)
    #password
    password=enter_password()

    #confirm username and password
    username, password=confirm_up(username, password, textfile)

    acc=(username+'\t'+password+'\t'+name+'\n')
    file=open('adminlogin.txt','a')
    file.write(acc)
    file.close()

    #after register go back to the admin portal
    admin_register(user)

#Sort alphabetical
def abc_order(data,abc):
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][abc]<data[j][abc]:
                data[i],data[j]=data[j],data[i]
    return data

#see student
def see_student_data():
    print('\nStudents')
    f=open('studentdata.txt','r')
    filelist=f.readlines()
    f.close()
    students=[]
    for datas in filelist:
        datalist=datas.split('\t')
        #remove '\n'
        if datalist[-1][-1]=='\n':
            datalist[-1]=datalist[-1][:-1]
        students.append(datalist[2:])
    admin=input("Sorted by:\n1. ID\n2. Alphabetical order\nEnter '1' or '2': ")
    while admin!='1' and admin!='2':
        admin=input("Sorted by:\n1. ID\n2. Alphabetical order\nPlease Enter '1' or '2': ")
    if admin=='2':
        abc=1
        abc_order(students,abc)
        num=0
        print("num\t|ID\t|Name|Gender|Date of Birth|Phone Number|Email|Address|ScheduleID(s)")
        for i in students:
            num+=1
            print(str(num),'. ','\t|',i[0],'\t|',i[1],'|',i[2],'|',i[3],'|',i[4],'|',i[5],'|',i[6],'|',i[7:])
    else:
        num=0
        print("num|ID|Name|Gender|Date of Birth|Phone Number|Email|Address|ScheduleID(s)")
        for i in students:
            num+=1
            print(str(num),'. ','|',i[0],'|',i[1],'|',i[2],'|',i[3],'|',i[4],'|',i[5],'|',i[6],'|',i[7:])
    ok=input('Enter anything to continue ')
#find the rating and schedule from txt
def find_rating_schedule(i):
    if i[-1][-1]=='\n':
        i[-1]=i[-1][:-1]
    schedule=[]
    for a in i[10:]:
        if len(a)==10:
            schedule.append(a)
        else:
            break
    for information in i:
        if information[:7]=='rating:':
            ratingindex=i.index(information)

    if i[ratingindex]=='rating:0':
        rating='rating:0'
    else:
        allfeed=0
        for feedbacks in i[ratingindex+1:]:
            allfeed+=1
        rating='rating:'+str(int(i[ratingindex][-1])//allfeed)
    return rating,schedule
#see coach
def see_coach_data():
    print('\nCoaches')
    f=open('coachdata.txt','r')
    filelist=f.readlines()
    f.close()
    coaches=[]
    for datas in filelist:
        datalist=datas.split('\t')
        #remove '\n'
        if datalist[-1][-1]=='\n':
            datalist[-1]=datalist[-1][:-1]
        coaches.append(datalist)
    admin=input("Sorted by:\n1. ID\n2. Alphabetical order\n3. Rating\n4. Hourly Rate\nEnter '1', '2', '3' or '4': ")
    while admin!='1' and admin!='2' and admin!='3' and admin!='4':
        admin=input("Invalid input\nSorted by:\n1. ID\n2. Alphabetical order\n3. Rating\n4. Hourly Rate\nPlease Enter '1', '2', '3' or '4': ")

    if admin=='2':
        abc=1
        abc_order(coaches,abc)
        num=0
        print("num\t|ID\t|Name|Gender|Date of Birth|Phone Number|Email|Address|Join Date|Terminate date|Hourly rate|ScheduleID(s)|Rating")
        for i in coaches:
            rating,schedule=find_rating_schedule(i)
            num+=1
            print(str(num),'. ','|',i[0],'|',i[1],'|',i[2],'|',i[3],'|',i[4],'|',i[5],'|',i[6],'|',i[7],'|',i[8],'|',i[9],'|',schedule,'|',rating)

    elif admin=='3':
        sortedcoach=[]
        print("num\t|Rating\t\t|ID\t\t|Name|Gender|Date of Birth|Phone Number|Email|Address|Join Date|Terminate date|Hourly rate|ScheduleID(s)")
        for i in coaches:
            rating,schedule=find_rating_schedule(i)
            coachdata=('|',rating,'\t|',i[0],'\t|',i[1],'\t|',i[2],'|',i[3],'|',i[4],'|',i[5],'|',i[6],'|',i[7],'|',i[8],'|',i[9],'|',str(schedule))
            sortedcoach.append(coachdata)
        abc_order(sortedcoach,1)
        num=0
        for i in sortedcoach:
            num+=1
            datas=''
            for a in i:
                datas+=' '+a
            print(str(num),'. ',str(datas))
        pass

    elif admin=='4':
        sortedcoach=[]
        print("num\t|Hourly rate\t|ID\t\t|Name\t\t|Gender\t\t|Date of Birth|Phone Number|Email|Address|Join Date|Terminate date|ScheduleID(s)|Rating")
        for i in coaches:
            rating,schedule=find_rating_schedule(i)
            coachdata=('\t| RM',int(i[9][2:]),'\t|',i[0],' \t|',i[1],'\t|',i[2],'|',i[3],'|',i[4],'|',i[5],'|',i[6],'|',i[7],'|',i[8],'|',str(schedule),'|rating: ',rating,)
            sortedcoach.append(coachdata)
        abc_order(sortedcoach,1)
        num=0
        for i in sortedcoach:
            num+=1
            datas=''
            for a in i:
                datas+=' '+str(a)
            print(str(num),'. ',str(datas))
        pass

    else:
        num=0
        print("num\t|ID\t\t|Name\t\t|Gender\t\t|Date of Birth\t|Phone Number|Email|Address|Join Date|Terminate date|Hourly rate|ScheduleID(s)|Rating")
        for i in coaches:
            rating,schedule=find_rating_schedule(i)
            num+=1
            print(str(num),'. ','\t|',i[0],'\t|',i[1],'\t|',i[2],'  \t|',i[3],'\t|',i[4],'|',i[5],'|',i[6],'|',i[7],'|',i[8],'|',i[9],'|',schedule,'|',rating)

    ok=input('\nEnter anything to continue ')
#see all schedule
def see_all_schedule():
    f=open('coachdata.txt','r')
    filelist=f.readlines()
    allschedule=[]
    f.close()
    for data in filelist:
        datalist=data.split('\t')
        for i in datalist[10:]:
            if len(i)==10:
                allschedule.append(i)
                pass
            else: break
    #sort sport alphabetically
    if allschedule==[]:
        print('\nNo schedule available')
    else:
        #'''
        for i in range(len(allschedule)):
            for j in range(len(allschedule)):
                if allschedule[i][2:5]<allschedule[j][2:5]:
                    allschedule[i],allschedule[j]=allschedule[j],allschedule[i]
        #'''
        num=0
        sport=''
        print('\nAll Schedule: ')
        for a in allschedule:
            if sport!=a[2:5]:
                sport=a[2:5]
                num=0
                print(sport_decode(sport),':')
            schedulestr=schedule_decode(a)
            num+=1
            print(num,'. ','ScheduleID:',a,schedulestr)
    ok=input('\nEnter anything to continue: ')

#convert list into string in txt
def list_to_str(a_list):
    if a_list[-1][-1]=='\n':
        a_list[-1]=((a_list[-1])[:-1])
    string=''
    for i in a_list:
        if i==a_list[-1]:
            string+=i+'\n'
            if a_list[-1]=='\n':
                a_list[-1]=(a_list[-1]+'\n')
        else:
            string+=i+'\t'

    return string
#update data
def update_user_data(user,textfile,useridindex,coachdata=False):
    #use find id in list, change it, then update text file

    #use useridindex because the id index of student and coaches are different
    userid=user[useridindex]

    #Find
    f=open(textfile,'r')
    filelist=f.readlines()#list
    f.close()
    #Update
    f=open(textfile,'w')
    for datalist in filelist:
        #split from the string in each datalist
        userlist=datalist.split('\t')

        if userlist[useridindex]==userid:
            if coachdata==True:
                coachid=userid.split('.')
                userid=coachid[1]
            #get the index from id
            x=len(userid)
            #from 202=2
            userindex=(int(userid[:x-2]))-1 #minus 1 because id starts in 1 and not 0
            #Change
            str_user=list_to_str(user)
            filelist[userindex]=str_user
            break

    for i in filelist:
        f.write(i)
    f.close()

#update student data
def update_student_data(user,useradmin=False,userad='',studentidinput=''):
    name=user[3]
    gender=user[4]
    dob=user[5]
    phone=user[6]
    email=user[7]
    address=user[8]
    userid=user[2]
    textfile='studentdata.txt'
    useridindex=2

    user[3],user[4],user[5],user[6],user[7],user[8]=confirm_data(name,gender,dob,phone,email,address)
    update_user_data(user,textfile,useridindex)

    if useradmin==True:
        search_modify_studentid(userad,studentidinput)
    else:
        student_personal_data(user)
#update username and password
def update_student_up(user,useradmin=False,userad='',studentidinput=''):
    username=user[0]
    password=user[1]
    useridindex=2
    textfile='studentdata.txt'

    user[0],user[1]=confirm_up(username,password,textfile)
    update_user_data(user,textfile,useridindex)
    if useradmin==True:
        search_modify_studentid(userad,studentidinput)
    else:
        student_personal_data(user)
#Modify student schedule
def update_student_schedule(datalist,schedule):
    if schedule==[]:
        print('This Student has no schedule')
        yon=input("Enter 'y' to Add schedule and 'n' to go back: ")
        while yon!='y' and yon!='n':
            print('\nIncorrect Inpute\nThis student has no schedule')
            yon=input("Enter 'y' to add schedule and 'n' to go back: ")
        if yon=='n':
            pass
        else:
            #add student schedule
            datalist=add_student_schedule(datalist)
    elif schedule[0]=='none' or schedule==[]:
        print('This Student has no schedule')
        yon=input("Enter 'y' to Add schedule and 'n' to go back: ")
        while yon!='y' and yon!='n':
            print('\nIncorrect Inpute\nThis student has no schedule')
            yon=input("Enter 'y' to add schedule and 'n' to go back: ")
        if yon=='n':
            pass
        else:
            #add student schedule
            datalist=add_student_schedule(datalist)
    else:
        num=0
        validlist=['a','b']
        print('Schedule(s):')
        for i in schedule:
            num+=1
            nums=str(num)
            validlist.append(nums)
            print(nums+'. '+i+': '+schedule_decode(i))
        choose=(input("\nEnter the number schedule to modify\nor Enter 'a' to Add schedule\nor Enter 'b' to go Back: "))
        while choose not in validlist:
            choose=(input("\nInvalid input\nEnter the number schedule to modify\nor Enter 'a' to Add schedule\nor Enter 'b' to go Back: "))

        if choose=='a':
            datalist=add_student_schedule(datalist)
            pass
        elif choose=='b':
            pass
        else:
            choose=int(choose)
            choosenschedule=schedule[choose-1]
            print('\nschedule id: '+choosenschedule)
            choose=input("1. Remove\n2. to go choose again\n3. To go Back\nEnter '1', '2', '3', or'4':")
            validlist=['1','2','3']
            while choose not in validlist:
                print('\n'+choosenschedule)
                choose=input('Incorrect input\n1. Remove\n2. to go choose again\n 3. to go Back:')

            if choose=='1':
                datalist[-1]=datalist[-1][:-1]
                datalist.remove(choosenschedule)
            elif choose=='2':
                update_student_schedule(datalist,schedule)
            else:
                pass
    #return datalist
    #return schedule,datalist,sportid,scntrid
    textfile='studentdata.txt'
    useridindex=2
    update_user_data(datalist,textfile,useridindex)

#Have all schedule id in a list to check
def all_scheduleid():
    scheduleidlist=[]
    f=open('coachdata.txt','r')
    filelist=f.readlines()#list
    f.close()
    for data in filelist:
        coachdata=data.split('\t')
        if coachdata[8]=='-':
            #for i in range(len(coachdata):
            for i in coachdata[10:]:
                if len(i)==10:
                    scheduleidlist.append(i)
    return(scheduleidlist)
#add student schedule
def add_student_schedule(datalist):
    allscheduleid=all_scheduleid()
    enterscheduleid=input('\nEnter the schedule ID to add: ')
    enterscheduleid=enterscheduleid.upper()
    found=False
    while found==False:
        if enterscheduleid in allscheduleid:
            print("\nAre you sure you would like to add "+enterscheduleid+'?')
            yon=input("Enter 'y' for Yes, 'n' for No to cancel: ")
            while yon!='y' and yon!='n':
                print("\nIncorrect input\nAre you sure you would like to add "+enterscheduleid+'?')
                yon=input("\nIncorrect input\nEnter 'y' for Yes, 'n' for No to cancel: ")
            if yon=='y':
                datalist[-1]=datalist[-1][:-1]
                datalist.append(enterscheduleid+'\n')
                found=True
            else:
                add_student_schedule(datalist)
                break
        else:
            yon=input("\nSchedule id not found, try again?\nEnter 'y' to try again, 'n' to go back")
            while yon!='y' and yon!='n':
                yon=input("\nIncorrect input\nSchedule id not found, try again?\nEnter 'y' to try again, 'n' to go back")
            if yon=='y':
                add_student_schedule(datalist)
                break
            else: found=True
    return datalist

#modify student data by admin
def update_student(user,datalist,schedule,studentidinput):
    textfile='studentdata.txt'
    useridindex=2

    schedule=[]
    if (datalist[8][-1])=='\n':
        schedule.append('none')
    else:
        for i in datalist[9:]:
            if i[-1]=='\n':
                i=i[:-1]
            schedule.append(i)

    print ("\n\n\t*************Real Champions Sport Academy**************")
    print("\nId            : ",datalist[2],
    '\n1. Personal Data:',
    '\n\tName          : ',datalist[3],
    '\n\tGender        : ',datalist[4],
    '\n\tDate of Birth : ',datalist[5],
    '\n\tEmail         : ',datalist[6],
    '\n\tAddress       : ',datalist[7],
    '\n2. Username Password',
    '\n\tUsername     : ',datalist[0],
    '\n\tPassword     : ',datalist[1],
    '\n3. Sports Schedule(s): ')
    num=0
    validlist=[]
    if schedule[0]!='none':
        for i in schedule:
            num+=1
            nums=str(num)
            validlist.append(nums)
            print('\t'+nums+'. '+i)
        print('4. Go back')
    else: print('\tnone\n4. Go back' )

    choose=input("\nModify:\n1. Personal data\n2. Username Password\n3. Sport data\n4. To go back\nEnter '1', '2', '3', or '4': ")
    while choose!='1' and choose!='2' and choose!='3' and choose!='4':
        print("\n\tId            : ",datalist[2],
        '\n1. Personal Data:',
        '\n\tName          : ',datalist[3],
        '\n\tGender        : ',datalist[4],
        '\n\tDate of Birth : ',datalist[5],
        '\n\tPhone Number  : ',datalist[6],
        '\n\tEmail         : ',datalist[7],
        '\n\tAddress       : ',datalist[8],
        '\n2. Username Password',
        '\n\tUsername     : ',datalist[0],
        '\n\tPassword     : ',datalist[1],
        '\n3. Sports Schedule(s): ')
        num=0
        validlist=[]
        if schedule[0]!='none':
            for i in schedule:
                num+=1
                nums=str(num)
                validlist.append(nums)
                print('\t'+nums+'. '+i)#': '+schedule_decode(i))
        else: print('\tnone')
        choose=input("\nIncorrect Input\nModify:\n1. Personal data\n2. Username Password\n3. Sport data\n4. To go back\nEnter '1', '2', '3', or '4': ")
    
    if choose=='1':
        print('\nModify Personal Data')
        name,gender,dob,phone,email,address=datalist[3],datalist[4],datalist[5],datalist[6],datalist[7],datalist[8]
        datalist[3],datalist[4],datalist[5],datalist[6],datalist[7],datalist[8]=confirm_data(name,gender,dob,phone,email,address)
        update_user_data(datalist,textfile,useridindex)
        search_modify_studentid(user,studentidinput)

    elif choose=='2':
        useradmin=True
        update_student_up(datalist,useradmin,user,studentidinput)

    elif choose=='3':
        print('\nModify Sport Data')
        print('\n1. Sports Schedule(s): ')
        num=0
        validlist=[]
        if schedule[0]!='none':
            for i in schedule:
                num+=1
                nums=str(num)
                validlist.append(nums)
                print('\t'+nums+'. '+i)#': '+schedule_decode(i))
        else: print('\tnone')
        print('2. To go Back')
        choose=input("Enter '1' to modify schedule or '2' to go back: ")
        while choose!='1' and choose!='2':
            print('\n1. Sports Schedule(s): ')
            num=0
            validlist=[]
            if schedule[0]!='none':
                for i in schedule:
                    num+=1
                    nums=str(num)
                    validlist.append(nums)
                    print('\t'+nums+'. '+i)#': '+schedule_decode(i))
            else: print('\tnone')
            print('2. To go Back')
            choose=input("\nIncorrect Input\nEnter '1' to modify schedule or '2' to go back: ")
        if choose=='1':
            update_student_schedule(datalist,schedule)
            search_modify_studentid(user,studentidinput)
        else:
            search_modify_studentid(user,studentidinput)
    else: 
        pass
#continue to update the data while searching
def search_modify_studentid(user,studentidinput):
    f=open('studentdata.txt','r')
    filelist=f.readlines()
    f.close()
    for data in filelist:
        datalist=data.split('\t')
        if studentidinput==datalist[2]:
            schedule=''
            #see all schedule
            if len(datalist[8][-1])=='\n':
                schedule='none'
                lastschedule=10
            else:
                for i in range(8,len(datalist)):
                    if len(datalist[i])!=10:
                        lastschedule=i
                        break
                    else:
                        schedule+=datalist[i]+', '
            update_student(user,datalist,schedule,studentidinput)
#target the student id to modify
def search_modify_student(user):
    print('\nWhich Student to Modify?\nSearch by ID')
    studentidinput=input("Enter the Student's ID: ")
    f=open('studentdata.txt','r')
    filelist=f.readlines()
    f.close()
    for data in filelist:
        datalist=data.split('\t')
        if studentidinput==datalist[2]:
            schedule=[]
            update_student(user,datalist,schedule,studentidinput)
            break
    else: 
        print('Student ID Not Found')
        yon=input("Enter 'y' for yes to search again, or 'n' to go Back: ")
        while yon!='y' and yon!='n':
            yon=input("Incorrect input\nEnter 'y' for yes to search again, or 'n' to go Back: ")
        if yon=='y':
            search_modify_student(user)
        else:
            pass

#modify coach data
def update_coach_data(user,datalist,sport,sportid,sportcntr,scntrid,schedule,coachidinput): 
    textfile='coachdata.txt'
    useridindex=0
    coachdata=True

    print ("\n\n\t*************Real Champions Sport Academy**************")
    print( '\nID           : '+datalist[0]+
    '\n\t1.Personal Data:\nName         : '+datalist[1]+
    '\n\tGender       : '+datalist[2]+
    '\n\tDate of Birth: '+datalist[3]+
    '\n\tPhone Number : '+datalist[4]+
    '\n\tEmail Address: '+datalist[5]+
    '\n\tAddress      : '+datalist[6]+
    '\n2.Coach Data:'+
    '\n\tDate Joined      : '+datalist[7]+
    '\n\tDate Terminated  : '+datalist[8]+
    '\n\tHourly Rate      : '+datalist[9]+
    '\n3.Sport Data:'+'\n\tSport and Center : '+sport+', '+sportcntr+
    '\n\tSchedule ID      : '+schedule)
    choose=input("\nModify:\n\t1. Personal data\n\t2. Coach data\n\t3. Sport data\n\t4. To go back\nEnter '1', '2', '3', or '4': ")
    while choose!='1' and choose!='2' and choose!='3' and choose!='4':
        print( '\nID           : '+datalist[0]+
        '\n\t1.Personal Data:\nName         : '+datalist[1]+
        '\nGender       : '+datalist[2]+
        '\nDate of Birth: '+datalist[3]+
        '\nPhone Number : '+datalist[4]+
        '\nEmail Address: '+datalist[5]+
        '\nAddress      : '+datalist[6]+
        '\n\n2.Coach Data:'+
        '\nDate Joined      : '+datalist[7]+
        '\nDate Terminated  : '+datalist[8]+
        '\nHourly Rate      : '+datalist[9]+
        '\n\n3.Sport Data:'+'\nSport and Center : '+sport+', '+sportcntr+
        '\nSchedule ID      : '+schedule+
        '\n\n4.Back')
        choose=input("\nIncorrect Input\nModify: \n\t1. Personal data\n\t2. Coach data\n\t3. Sport data\n\t4. To go back\nEnter '1', '2', '3', or '4': ")
    if choose=='1':
        print('\nModify Personal Data')
        name,gender,dob,phone,email,address=datalist[1],datalist[2],datalist[3],datalist[4],datalist[5],datalist[6]

        datalist[1],datalist[2],datalist[3],datalist[4],datalist[5],datalist[6]=confirm_data(name,gender,dob,phone,email,address)
        name,gender,dob,phone,email,address=datalist[1],datalist[2],datalist[3],datalist[4],datalist[5],datalist[6]

        update_user_data(datalist,textfile,useridindex,coachdata)
        search_modify_coachid(user,coachidinput)

    elif choose=='2':
        datejoin,dateterminate,rate=datalist[7],datalist[8],datalist[9]
        datalist[7],datalist[8],datalist[9]=confirm_date_rate(datejoin,dateterminate,rate)
        update_user_data(datalist,textfile,useridindex,coachdata)
        search_modify_coachid(user,coachidinput)

    elif choose=='3':
        print('\nModify Sport Data')
        print(  '\n1. Sport and Center  : '+sport+', '+sportcntr+
                '\n2. Schedule ID       : '+schedule+'\n3. To go back')
        choose=input("Enter the data '1' or '2' to modify or '3' to go back: ")
        while choose!='1' and choose!='2' and choose!='3':
            print(  '\n1. Sport and Center  : '+sport+', '+sportcntr+
            '\n2. Schedule ID       : '+schedule+'\n3. To go back')            
            choose=input("Incorrect Input\nEnter the data '1' or '2' to modify or '3' to go back: ")
        if choose=='1':
            print('Sport and Sport Center unable to be modified\nTo change this admin will need to terminate this coach id and create a new one')
            ok=input('Enter anything to continue: ')
            search_modify_coachid(user,coachidinput)
        elif choose=='2':
            schedule,datalist,sportid,scntrid=update_coach_schedule(schedule,datalist,sportid,scntrid)
            update_user_data(datalist,textfile,useridindex,coachdata)
            search_modify_coachid(user,coachidinput)
        else:
            search_modify_coachid(user,coachidinput)

        #coachid=datalist[0]
    else:
        pass
#modify coach schedule(add or remove)
def update_coach_schedule(schedule,datalist,sportid,scntrid):
    if schedule=='none':
        print('This coach has no schedule\nTo add go to register, then register schedule.')
        ok=(input('Enter anything to continue: '))
    else:
        schedulelist=schedule.split(', ')
        schedulelist.remove(schedulelist[-1])
        num=0
        validlist=[]
        print('\n Schedule List')
        for i in schedulelist:
            num+=1
            nums=str(num)
            validlist.append(nums)
            print(nums+'. '+i)#+'\n')
        choose=(input('To add schedule, go to register then register schedule\nEnter the schedule to modify: '))
        while choose not in validlist:
            choose=(input('Invalid input\nEnter the schedule to modify: '))
        choose=int(choose)
        choosenschedule=schedulelist[choose-1]
        print('\nschedule id: '+choosenschedule)
        choose=input("1. Modify\n2. Remove\n3. to go choose again\n4. to go Back\nEnter '1', '2', '3', or'4':")
        validlist=['1','2','3','4']
        while choose not in validlist:
            print('\n'+choosenschedule)
            choose=input('Incorrect input\n1. Modify\n2. Remove\n3. to go choose again\n 4. to go Back:')
        if choose=='1':
            print('Modify: '+choosenschedule)
            schedulebefore=choosenschedule

            datalist.remove(choosenschedule)

            sportid=schedulebefore[2:5]
            sport=sport_decode(sportid)
            sportcntrid=schedulebefore[:2]
            sportcntr=center_decode(sportcntrid)
            num=schedulebefore[5]
            day=day_decode(num)
            hour=schedulebefore[6:8]
            minute=schedulebefore[-2:]

            lastschedule=''
            #see all schedule
            if len(datalist[10])!=10:
                schedule='none'
                lastschedule=10
            else:
                for i in range(10,len(datalist)):
                    if len(datalist[i])!=8:
                        lastschedule=i
                        break
                    else:
                        schedule+=datalist[i]+', '

            sport,sportcntr,num,day,hour,minute=confirm_schedule(sport,sportcntr,num,day,hour,minute)

            #sportid=
            #sportcntrid=
            scheduleid=scntrid+sportid+num+hour+minute

            datalist=datalist[:lastschedule]+[scheduleid]+datalist[lastschedule:]

        elif choose=='2':
            datalist.remove(choosenschedule)

    return schedule,datalist,sportid,scntrid
#use existing coach and display
def search_modify_coachid(user,coachidinput):
    coachidinput=coachidinput.upper()
    f=open('coachdata.txt','r')
    filelist=f.readlines()
    f.close()
    for data in filelist:
        datalist=data.split('\t')
        if coachidinput==datalist[0]:
            scntrid=datalist[0][:2]
            sportcntr=center_decode(scntrid)

            sportid=datalist[0][2:5]
            sport=sport_decode(sportid)

            schedule=''

            #see all schedule
            if len(datalist[10])!=10:
                schedule='none'
                lastschedule=10
            else:
                for i in range(10,len(datalist)):
                    if len(datalist[i])!=10:
                        lastschedule=i
                        break
                    else:
                        schedule+=datalist[i]+', '
            update_coach_data(user,datalist,sport,sportid,sportcntr,scntrid,schedule,coachidinput)
#search the coach
def search_modify_coach(user):
    coachidinput=input("\nEnter the Coach's ID: ")
    coachidinput=coachidinput.upper()
    f=open('coachdata.txt','r')
    filelist=f.readlines()
    f.close()
    for data in filelist:
        datalist=data.split('\t')
        if coachidinput==datalist[0]:
            scntrid=datalist[0][:2]
            sportcntr=center_decode(scntrid)

            sportid=datalist[0][2:5]
            sport=sport_decode(sportid)

            schedule=''

            #see all schedule
            if len(datalist[10])!=10:
                schedule='none'
                lastschedule=10
            else:
                for i in range(10,len(datalist)):
                    if len(datalist[i])!=10:
                        lastschedule=i
                        break
                    else:
                        schedule+=datalist[i]+', '
            update_coach_data(user,datalist,sport,sportid,sportcntr,scntrid,schedule,coachidinput)
            break
    else: 
        print("\nCoach with id:"+coachidinput+' not found')
        tryagain=input("Search again?\nEnter 'y' for Yes, 'n' for No to Go back: ")
        while tryagain!='y' and tryagain!='n':
            tryagain=input("Incorrect input\nCoach with id:"+coachidinput+" not found\nSearch again?\nEnter 'y' for Yes, 'n' for NO to Go back: ")
        if tryagain=='y':
            search_modify_coach(user)
        else:
            pass

#search schedule id
def search_modify_schedule(user):
    scheduleidinput=input("\nWhich Schedule to Modify\nSearch Schedule ID: ")
    while scheduleidinput=='' or scheduleidinput==' ':
        scheduleidinput=input("\nIncorrect input\nWhich Schedule to Modify\nSearch Schedule ID: ")
    scheduleidinput=scheduleidinput.upper()
    #find scheduleid from coachdata
    f=open('coachdata.txt','r')
    filelist=f.readlines()
    f.close()
    coachwithschedule=[]
    for data in filelist:
        coachdatalist=data.split('\t')
        for i in range(10,len(coachdatalist)):
            if coachdatalist[i]==scheduleidinput:
                coachwithschedule.append(coachdatalist)
                break

    f=open('studentdata.txt','r')
    filelist=f.readlines()
    f.close()
    studentwithschedule=[]
    for data in filelist:
        studentdatalist=data.split('\t')
        for i in range(9,len(studentdatalist)):
            if studentdatalist[i][-1]=='\n':
                scheduleid=studentdatalist[i][:-1]
            else:
                scheduleid=studentdatalist[i]
            if scheduleid==scheduleidinput:
                studentwithschedule.append(studentdatalist)

    if coachwithschedule==[] and studentwithschedule==[]:
        yon=input("\nScheduleID not found\nEnter 'y' for yes to search again, or 'n' to go Back: ")
        while yon!='y' and yon!='n':
            yon=input("\nIncorrect input\nEnter 'y' for yes to search again, or 'n' to go Back: ")
        if yon=='y':
            search_modify_schedule(user)
        else:
            pass

    else:
        print('\n'+schedule_decode(scheduleidinput))
        print('Coach with ScheduleID '+scheduleidinput+':')
        for i in coachwithschedule:
            print('CoachID: '+i[0]+'\t|Name: '+i[1])
        print('\nStudent with ScheduleID '+scheduleidinput+':')
        for i in studentwithschedule:
            print('StudentID: '+i[2]+'\t|Name: '+i[3])

        yon=input("\nDelete schedule "+scheduleidinput+"?\nEnter 'y' yes to Delete, 'n' no to go back: ")
        while yon!='y' and yon!='n':
            yon=input("\nIncorrect input\nDelete schedule?\nEnter 'y' yes to Delete, 'n' no to go back: ")
        if yon=='n':
            pass
        elif yon=='y':
            for i in coachwithschedule:
                i.remove(scheduleidinput)
                update_user_data(i,'coachdata.txt',0,True)
            for i in studentwithschedule:
                if i[-1][-1]=='\n':
                    i[-1]=i[-1][:-1]
                i.remove(scheduleidinput)
                update_user_data(i,'studentdata.txt',2)

            print(scheduleidinput+' Deleted')
            ok=input('Enter anything to continue')
            pass
    #find scheduleid from studentdata

#See and update personal data
def student_personal_data(user):
    print('\nPersonal Data:'+'\n\tName          : '+user[3]
                            +'\n\tId            : '+user[2]
                            +'\n\tGender        : '+user[4]
                            +'\n\tDate of Birth : '+user[5]
                            +'\n\tPhone Number  : '+user[6]
                            +'\n\tEmail         : '+user[7]
                            +'\n\tAddress       : '+user[8])
    print("What would you like to do?\n1. Update data\n2. Change Username and Password\n3. Back to Student Menu")
    student=input("Enter '1', '2', or '3': ")
    while student!='1' and student!='2' and student!='3':
        print('\nIncorrect input')
        student=input("Please enter either '1', '2', '3': ")
    if student=='1':
        update_student_data(user)
    elif student=='2':
        update_student_up(user)
    else:
        registered_student_portal(user)

#see today schedule
def see_today_schedule():
    num,day=register_day()
    f=open('coachdata.txt','r')
    filelist=f.readlines()
    todayschedule=[]
    f.close()
    for data in filelist:
        datalist=data.split('\t')
        for i in datalist[10:]:
            if len(i)==10:
                if i[5]==num:
                    todayschedule.append(i)
                    pass
            else: break
    #todayschedule
    print("\nToday's schedule: ")
    if todayschedule==[]:
        print('\nNo schedule available')
    else:
        for i in range(len(todayschedule)):
            for j in range(len(todayschedule)):
                if todayschedule[i][2:5]<todayschedule[j][2:5]:
                    todayschedule[i],todayschedule[j]=todayschedule[j],todayschedule[i]
        #'''
        num=0
        sport=''
        print('\nAll Schedule: ')
        for a in todayschedule:
            if sport!=a[2:5]:
                sport=a[2:5]
                print(sport_decode(sport),':')
            schedulestr=schedule_decode(a)
            num+=1
            print(num,'. ','ScheduleID:',a,schedulestr)
    ok=input('\nEnter anything to continue: ')
    #print(num,day)

#Search the coach with the sport and sport center chosen
def search_sport_center():
    print('\n\n\t*************Real Champions Sport Academy**************\nSports')
    sportcntrid=enter_sportcenter()
    sportcntr=center_decode(sportcntrid)
    sportid=enter_sport()
    sport=sport_decode(sportid)
    findid=sportcntrid+sportid

    f=open('coachdata.txt','r')
    filelist=f.readlines()
    f.close()

    print('\n'+sport+', at '+sportcntr+':\n')
    num1=0
    for data in filelist:
        datalist=data.split('\t')
        coachid=datalist[0][:5]

        schedule=[]
        schedulestr=''
        if findid==coachid:
            ratingindex=find_rating(datalist)
            if (datalist[10][-1])=='\n':
                schedule.append('none')
                schedulestr+='none'
                #lastschedule=10
            else:
                for i in datalist[10:]:
                    if len(i)==10:
                        schedule.append(i)
                        schedulestr+='\n\t'+schedule_decode(i)
                    else:break
            num1+=1
            if datalist[ratingindex][-1]=='\n':
                rating='not rated'
            else:
                allfeed=0
                for i in datalist[ratingindex:]:
                    allfeed+=1
                rating=str(int(datalist[ratingindex][-1])//allfeed)
            print(str(num1),'. CoachID',datalist[0],'\t|Coach Name:',datalist[1],
            '\t|Gender:',datalist[2],'\t|Phone Number:',datalist[4],
            '\t|Hourly Rate:',datalist[9],
            "\n|Schedule(s):",schedulestr,
            '\n|Rating:',rating)
            if (datalist[ratingindex+1:])!=[]:
                print('|Feedbacks:')
                num=0
                for i in datalist[ratingindex+1:]:
                    num+=1
                    print ('\t'+str(num)+'. '+i)
            else:print('\tNo Feedbacks yet\n')
            print('\n')
        
    ok=input('Enter anything to go back ')
#find schedule in list
def find_schedule(datalist):
    schedule=[]
    if (datalist[8][-1])=='\n':
        schedule.append('none')
        #lastschedule=10
    else:
        for i in datalist[9:]:
            if i[-1]=='\n':
                i=i[:-1]
            schedule.append(i)
    return schedule
#find coach by schedule func
def find_coach_with_schedule(schedule):
    coachschedule=[]
    f=open('coachdata.txt','r')
    filelist=f.readlines()
    f.close()
    for i in schedule:
        for data in filelist:
            datalist=data.split('\t')
            for coachdata in datalist:
                if i == coachdata:
                    num=filelist.index(data)
                    if num in coachschedule:
                        pass
                    else:    
                        coachschedule.append(num)
                    break
    return coachschedule

#find by rating index
def find_rating(datalist):
    for i in datalist:
        if i[:7] =='rating:':
            ratingindex=datalist.index(i)
            break
        else:ratingindex=8
    return ratingindex
#rating coach for registered students
def rating_coach(coachschedule,user):
    f=open('coachdata.txt','r')
    filelist=f.readlines()
    f.close()
    num=0
    validlist=['b']
    print('Schedule(s):')

    for i in coachschedule:
        num+=1
        nums=str(num)
        validlist.append(nums)

        coach=filelist[i].split('\t')
        for data in coach:
            if data[:7]=='rating:':
                ratingindex=coach.index(data)
        print(coach[ratingindex])
        if coach[ratingindex]=='rating:0\n':
            if coach[ratingindex][-1]=='\n':
                coach[ratingindex]=coach[ratingindex][:-1]
            rating='rating:0'
        else:
            allfeed=0
            for coaches in coach[ratingindex+1:]:
                allfeed+=1
            print(coach[ratingindex],allfeed)
            rating='rating:'+str(int(coach[ratingindex][-1])//allfeed)
        print(nums+'. CoachID: '+coach[0]+'| Name:'+coach[1]+'|'+'|'+rating,end='')
        if (coach[ratingindex+1:])!=[]:
            print('\nFeedbacks:')
            for i in coach[ratingindex+1:]:
                print (i)
        else:print('\nNo Feedbacks yet\n')
    choose=(input("\nEnter the number to rate\nor Enter 'b' to go Back: "))
    while choose not in validlist:
        choose=(input("Invalid input\nEnter the number schedule to modify\nor Enter 'a' to Add schedule\nor Enter 'b' to go Back: "))
    if choose=='b':
        registered_student_portal(user)
    else:
        ratingcoach=input('Rate Coach from 1, 2, 3, 4, or 5\nEnter rating: ')
        while ratingcoach!='1' and ratingcoach!='2' and ratingcoach!='3' and ratingcoach!='4' and ratingcoach!='5':
            ratingcoach=input('\nIncorrect input\nRate Coach from 1, 2, 3, 4, or 5\nEnter rating:')
        if ratingcoach=='1' or ratingcoach=='2' or ratingcoach=='3' or ratingcoach=='4' or ratingcoach=='5':
            yon=input('Are you sure you want to rate this coach: '+ratingcoach+"\nEnter 'y' for yes, 'n' to cancel: ")
            while yon!='y' and yon!='n':
                yon=input('Incorrect input\nAre you sure you want to rate this coach: '+ratingcoach+"Enter 'y' for yes, 'n' to cancel: ")
            if yon=='n':
                ratingcoach=input('Rate Coach from 1, 2, 3, 4, or 5\nEnter rating: ')
            elif yon=='y':
                if coach[ratingindex]=='rating:0\n':
                    if coach[ratingindex][-1]=='\n':
                        coach[ratingindex]=coach[ratingindex][:-1]
                    coach[ratingindex]='rating:'+ratingcoach
                else:
                    allfeed=1
                    for i in coach[ratingindex+1:]:
                        allfeed+=1
                    ratingnum=int(coach[ratingindex][-1])
                    ratingnum=(ratingnum+int(ratingcoach))
                    coach[ratingindex]='rating:'+str(ratingnum)
                feedback=input('Enter Feedback: ')
        if coach[-1][-1]=='\n':
                coach[-1]=coach[-1][:-1]
        coach=coach+[feedback]
        coachdata=True
        update_user_data(coach,'coachdata.txt',0,coachdata)
        registered_student_portal(user)


#Main Function
def main():
    print("\n\n\t********Welcome to Real Champions Sport Academy********\nMain Menu\nSelect User:\n1. Admin\n2. Student\n3. Exit")
    user=input("Enter '1', '2', '3' to Exit: ")
    while user!='1' and user!='2' and user!='3':
        print('\nIncorrect input')
        user=input("Please type '1' for Admin, '2' for Student, '3' to Exit: ")
    if user=='1':
        print('admin')
        login_admin()       #goes to login admin
    elif user =='2':
        print('student')
        student_portal()    #goes to student portal
    else:print('\nGoodbye') #Ends the program

#Login Admin
def login_admin():
    user='Admin'
    txtfile='adminlogin.txt'
    previousfunc=main
    nextfunc=admin_portal
    login(user,txtfile,nextfunc,previousfunc)
#Admin Portal
def admin_portal(user):
    print ("\n\n\t*************Real Champions Sport Academy**************\nAdmin Portal"+"\nHello "+user[2]+
    "\nWhat would you like to do?\n1. Register Records\n2. See and Search Records(Sorted)\n3. Modify Records\n4. Back to Main Menu")
    admin=input("Enter '1', '2', '3', or '4': ")
    while admin!='1' and admin!='2' and admin!='3' and admin!='4':
        print('\nIncorrect input')
        admin=input("Please enter either '1', '2', '3', or '4': ")
    if admin=='1':
        admin_register(user)
    elif admin=='2':
        admin_see_search(user)
    elif admin=='3':
        admin_modify(user)
    else:
        main()
#Admin Register
def admin_register(user):
    print ("\n\n\t*************Real Champions Sport Academy**************\nAdmin Portal"+"\nRegister"+'\n'+
    "\nWho would you like to Register?\n1. Register a Student\n2. Register a Coach\n3. Register Schedule\n4. Register an Admin\n5. Back to Admin Menu")
    admin=input("Enter '1', '2', '3', '4', or '5': ")
    while admin!='1' and admin!='2' and admin!='3' and admin!='4' and admin!='5':
        print('\nIncorrect input')
        admin=input("Please enter either '1', '2', '3', '4', or '5': ")
    if admin=='1':
        register_student(user,useradmin=True)
    elif admin=='2':
        register_coach(user)
    elif admin=='3':
        register_schedule(user)
    elif admin=='4':
        register_admin(user)
    elif admin=='5':
        admin_portal(user)
#admin see or search
def admin_see_search(user):
    print ("\n\n\t*************Real Champions Sport Academy**************\nAdmin Portal"+"\nSee or Search\n"+
    "\nWhat would you like to do?\n1. See Records\n2. Search Records\n3. Back to Admin Menu")
    admin=input("Enter '1', '2', or '3': ")
    while admin!='1' and admin!='2' and admin!='3':
        admin=input("\nIncorrect Input\nEnter '1', '2', or '3': ")
    if admin=='1':
        admin_see(user)
    elif admin=='2':
        admin_search(user)
    else: admin_portal(user)
#admin see display according
def admin_see(user):
    print ("\n\n\t*************Real Champions Sport Academy**************\nAdmin Portal"+"\nSee\n"+
    "\nWhat would you like to See?\n1. Student Records\n2. Coach Records\n3. See Today's Schedule\n4. Schedule by Sport and Center\n5. Back to Admin Menu")
    admin=input("Enter '1', '2', '3', '4' or '5': ")
    while admin!='1' and admin!='2' and admin!='3' and admin!='4' and admin!='5':
        admin=input("\nIncorrect Input\nEnter '1', '2', '3', '4' or '5': ")
    if admin=='1':
        see_student_data()
        admin_see(user)
    elif admin=='2':
        see_coach_data()
        admin_see(user)
    elif admin=='3':
        see_today_schedule()
        admin_see(user)
    elif admin=='4':
        search_sport_center()
        admin_see(user)
    else: admin_portal(user)
#admin search according 
def admin_search(user):
    print ("\n\n\t*************Real Champions Sport Academy**************\nAdmin Portal"+"\nSearch\n"+
    "\nWhat would you like to Search?\n1. Search StudentID\n2. Search CoachID\n3. Search ScheduleID\n4. Back to Admin Menu")
    admin=input("Enter '1', '2', '3', or '4': ")
    while admin!='1' and admin!='2' and admin!='3' and admin!='4':
        admin=input("\nIncorrect Input\nEnter '1', '2', '3', '4': ")
    if admin=='1':
        search_modify_student(user)
        admin_search(user)
    elif admin=='2':
        search_modify_coach(user)
        admin_search(user)
    elif admin=='3':
        search_modify_schedule(user)
        admin_search(user)
    else: admin_portal(user)
#Admin modify
def admin_modify(user):
    print ("\n\n\t*************Real Champions Sport Academy**************\nAdmin Portal"+"\nModify"+'\n'+
    "\nWhich data would you like to Modify?\n1. Student\n2. Coach\n3. Schedule\n4. Back to Admin Menu")
    admin=input("Enter '1', '2', '3', or '4': ")
    while admin!='1' and admin!='2' and admin!='3' and admin!='4':
        print('\nIncorrect input')
        admin=input("Please enter either '1', '2', '3', or '4': ")
    if admin=='1':
        search_modify_student(user)
        admin_modify(user)
    elif admin=='2':
        print('\nWhich Coach to Modify?\nSearch by ID')
        search_modify_coach(user)
        admin_modify(user)
    elif admin=='3':
        search_modify_schedule(user)
        admin_modify(user)
    elif admin=='4':
        admin_portal(user)

#Student Portal
def student_portal():
    function='Student Portal'
    user='Student'
    c1='Login or Register'
    func1=registered_student
    c2='Sports'
    func2=sport_student
    c3='Back'
    func3=main
    print ("\n\n\t*************Real Champions Sport Academy**************\n"+function+'\n'+user+'\n1. '+c1+'\n2. '+c2+'\n3. '+c3+' to Main menu')
    user=input("Enter '1', '2', or '3': ")
    while user!='1' and user!='2' and user!='3':
        print('\nIncorrect input')
        user=input("Please Enter '1' to "+ c1 +", '2' to "+c2+" '3' to go "+ c3+" to Main menu: ")
    if user=='1':
        func1()
    elif user=='2':
        print(c2)
        func2()
    else:
        func3()
#Sports
def sport_student():
    print("\n\n\t*************Real Champions Sport Academy**************\nSports"+
    "\n1. See All Sport Schedule\n2. See Today's schedule\n3. See Schedule and Coaches by Sport and Sport Center\n4. Join Real Sport Academy\n5. Back")
    student=input("Enter '1', '2', '3', '4' or '5': ")
    while student!='1' and student!='2' and student!='3' and student!='4'  and student!='5':
        print('\nIncorrect input')
        student=input("Please Enter '1', '2', '3', '4', or '5' to go back to Student Portal: ")
    if student=='1':
        see_all_schedule()
        sport_student()
        pass
    elif student=='2':
        see_today_schedule()
        sport_student()
        pass
    elif student=='3':
        search_sport_center()
        sport_student()
    elif student=='4':
        register_student('Student',useradmin=False)
    else:
        student_portal()
    pass
#Registered Student
def registered_student():
    function='Registered Student'
    user='Student'
    c1='Login'
    func1=login_student
    c2='Register'
    func2=register_student
    c3='Back'
    func3=student_portal
    print ("\n\n\t*************Real Champions Sport Academy**************\n"+function+'\n'+user+'\n1. '+c1+'\n2. '+c2+'\n3. '+c3)
    user=input("Enter '1', '2', or '3': ")
    while user!='1' and user!='2' and user!='3':
        print('\nIncorrect input')
        user=input("Please Enter '1' to "+ c1 +", '2' to "+c2+" '3' to go "+ c3+": ")
    if user=='1':
        func1()
    elif user=='2':
        print(c2)
        func2(user,useradmin=False)
    else:
        print(c3)
        func3()
#Login Student
def login_student():
    user='Student'
    txtfile='studentdata.txt'
    previousfunc=registered_student
    nextfunc=registered_student_portal
    login(user,txtfile,nextfunc,previousfunc)
#Registered Student Portal
def registered_student_portal(user):
    print ("\n\n\t*************Real Champions Sport Academy**************\nStudent Portal"+"\nHello "+user[3]+'\n'
    "\nWhat would you like to do?\n1. Personal Data\n2. Personal Sport Schedule\n3. See All Sport Schedules\n4. See Today's Schedule\n5. See Schedule by Sports and Centers\n6. Rate Coach\n7. Back to Main Menu")
    admin=input("Enter '1', '2', '3', '4', '5', '6', or '7': ")
    while admin!='1' and admin!='2' and admin!='3' and admin!='4' and admin!='5' and admin!='6' and admin!='7':
        print('\nIncorrect input')
        admin=input("Please enter either '1', '2', '3', '4', '5', '6', or '7': ")
    if admin=='1':
        print('Personal Data')
        student_personal_data(user)
    elif admin=='2':
        print('\nPersonal Sport Schedule')
        schedule=find_schedule(user)
        update_student_schedule(user,schedule)
        registered_student_portal(user)
    elif admin=='3':
        see_all_schedule()
        registered_student_portal(user)
    elif admin=='4':
        see_today_schedule()
        registered_student_portal(user)
    elif admin=='5':
        search_sport_center()
        registered_student_portal(user)
    elif admin=='6':
        print('\nRate Coach')
        schedule=find_schedule(user)
        coachschedulejoined=find_coach_with_schedule(schedule)
        rating_coach(coachschedulejoined,user)
    else:
        main()

main()