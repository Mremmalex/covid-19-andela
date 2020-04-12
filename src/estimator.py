#! /usr/bin/env python3.8.2

#declaring function
def estimator():
        data = {
        "region" : {
            'name' : 'Africa',
            'avgAge' : 19.7,
            'avgDailyIncomeInUSD' : 5,
            'avgDailyIncomePopulation' : 0.71
        },
        "periodType" : "days",
        "timeToElapse":  58,
        "reportedCases": 674,
        "population" : 66622705,
        "totalHospitalBeds" : 1380614
        }

        currentlyInfected  = data["reportedCases"] * 10
        severelyInfected = data["reportedCases"] * 50

        def factor():
            period = data['periodType']
            multiplier = ''

            if period == "days":
                multiplier = 1;
            elif period == "weeks":
                multiplier = 7
            elif period == "months":
                multiplier = 30
            return int( multiplier * data['timeToElapse'] / 3)


        factor()
        infectionByRequestedTime = currentlyInfected * 2**factor()
        infectionByRequestedTime2 = severelyInfected * 2**factor()

        data["impact"] = {
                "currentlyInfected": currentlyInfected,
                "infectionByRequestedTime": infectionByRequestedTime
            }

        data["severeImpact"] = {
               "severelyInfected": severelyInfected,
               "infectionByRequestedTime": infectionByRequestedTime2
            }
        return data

print(estimator())
