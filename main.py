print (8/3)         # 2.66666666666665
print (int(8/3))    # 2
print (round(8/3))  #  3
print (round(8/3,2 )) # 2.67
print ( round(2.6666666661, 2))  # 2.67

#F -string
score =0  #integer
height = 1.8   #float
isWinning = True  #boolean
print(f"your score is {score},your height is {height}, you are winning is {isWinning}")

x = int(90 * 365)
y = int (90 * 52)
z = int (90 * 12)

age = int (input(" Enter you age : "))

print (f" You have {x- (age * 365)} days , {y- (age * 52)} weeks,and {z -(age * 12)} months left")

# or another way for F- string
age = input (" Enter your current age :  ")
age_as_int = int (age)  # convert age into integer number

years_remaining = 90 - age_as_int
days_remaining = years_remaining  * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f" You have {days_remaining}days, {weeks_remaining}weeks, {years_remaining} years left"

print (message)
