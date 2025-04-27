class DateCalculator:
    #Describe the constructor
    def __init__(self,year:int, month:str, day:int):
        self.year: int=year
        self.month: str=month
        self.day :int=day
        #Set up the other attributes to be used in calculation to zero
        self.month_count :int=0
        self.year_of_century : int=0
        self.zero_based_century : int=0

    def get_date(self):
        #How to manipulate the year and month count based on month provided
        if self.month=="March":
            self.month_count=3
        elif self.month=="April":
            self.month_count=4
        elif self.month=="May":
            self.month_count=5
        elif self.month=="June":
            self.month_count=6
        elif self.month=="July":
            self.month_count=7
        elif self.month=="August":
            self.month_count=8
        elif self.month=="September":
            self.month_count=9
        elif self.month=="October":
            self.month_count=10
        elif self.month=="November":
            self.month_count=11
        elif self.month=="December":
            self.month_count=12

        #These two months will alter the year as well
        elif self.month=="January":
            self.month_count=13
            self.year -= 1
        elif self.month=="February":
            self.month_count=14
            self.year -= 1
        #This handles events when month entered wrongly
        else:
            print("Please Enter Month as String starting with capital letter")

        #Get the year of century
        self.year_of_century = self.year % 100

        #Get the floor of century
        self.zero_based_century = self.year // 100

        #Use Zeller's Formula to get the day of the week
        q = self.day
        m = self.month_count
        y = self.year
        k = self.year_of_century
        j = self.zero_based_century

        #Function
        #Did some research -> all division is to be floor division i.e. truncated
        h:int = (q + (13*(m+1)//5) + k + (k//4) + (j//4) + 5*j) % 7

        #Day of the week
        day_of_the_week=["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]

        return day_of_the_week[h]

if __name__ == "__main__":
    #Allow users to check multiple dates
    print("For which date do you want the day of the week")

    #Declare variables and get input
    input_year: int = int(input("Year: "))
    input_month: str = input("Month (Start with capital letter): ")
    input_day: int = int(input("Day of month: "))

    #Create the object
    obj: DateCalculator = DateCalculator(input_year,input_month,input_day)

    #Output the results
    print(f"\n{obj.year}, {obj.day} {obj.month} was a {obj.get_date()}")