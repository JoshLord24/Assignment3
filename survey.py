# This is a Market Survey Analyzer

def analyze_survey(survey_list):

    counts = {}

    for item in survey_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    total = len(survey_list)

    print("Market Share Summary")
    for product, count in counts.items():
        percent = (count/total) * 100
        print(f"{product}: {count} ({percent:.2f}%)")

# fake survey data
survey_data = ["water", "tea", "tea", "coffee", "soda", "water", "coffee", "water", "water", "tea", "tea", "coffee"]

# analyzes data from survey
analyze_survey(survey_data)