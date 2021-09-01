medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]

def createMedalTable(results):
	# Use the results object above to create a medal table
    # The winner gets 3 points, second place 2 points and third place 1 point
	final_output = {}
	for data in medalResults:
		for val in data['podium']:
			pos = val[0:1]
			country = val[2:]
			if pos == '1':
				final_output[country] = final_output.get(country, 0) + 3
			elif pos == '2':
				final_output[country] = final_output.get(country, 0) + 2
			elif pos == '3':
				final_output[country] = final_output.get(country, 0) + 1
	return final_output


def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    } 
    assert medalTable == expectedTable

test_function()
