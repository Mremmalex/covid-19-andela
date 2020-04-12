
#listing the varibles for the covid-19 assessment from Andala
#region
name = 'Africa'
avgAge = 19.7
avgDailyIncomeInUSD = 5
avgDailyIncomePopulation = 0.71

#other varibles to look out
periodType = "days"
timeToElapse = 58
reportedCases = 674
population = 66622705
totalHospitalBeds = 1380614
#starting the coding for the covid-19 assessment
# declaring global varibles

currentlyInfected  = reportedCases * 10
severelyInfected = reportedCases * 50

infectionByRequestedTime = currentlyInfected * 10242
infectionByRequestedTime2 = severelyInfected * 10242


#solving challenage 2
#estimating the sun of severe positive patients

severeCasesByRequestedTime = infectionByRequestedTime / 15



#declaring function
def estimator():

    data = {
        name,
        avgAge,
        avgDailyIncomeInUSD,
        avgDailyIncomePopulation

    }
    impact = {
        currentlyInfected,
        infectionByRequestedTime
    }
    severeImpact = {
        severelyInfected,
        infectionByRequestedTime2
    }
    print('\ncomputing the data of the affected area')
    print(f'name = {list(data)[3]}')
    print(f'avgAge = {list(data)[2]}')
    print(f'avgDailyIncomeInUSD = {list(data)[1]}')
    print(f'avgDailyIncomePopulation = {list(data)[0]}')

    print('\nestimating the impact level of the pendemic')
    print(f'currentlyInfected = {list(impact)[1]}')
    print(f'currentlyInfected = {list(impact)[0]}')


    print('\nestimating the severeImpact level of the pandemic')
    print(f'severelyInfected = {list(severeImpact)[1]}')
    print(f'infectionByRequestedTime = {list(severeImpact)[0]}')


estimator()



# class estimator():
#
#     def __init__(self,reportedCases):
#          self.reportedCases = reportedCases
#
#     def timator(self):
#         print(self.reportedCases * 10)
#
# case = estimator(reportedCases)
# case.timator()
