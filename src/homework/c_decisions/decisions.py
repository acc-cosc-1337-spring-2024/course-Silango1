#
def get_options_ratio(option,total):
     if total != 0:
          ratio = option / total
          return ratio
     else:
          return "Total can not be Zero"

def get_faculty_rating(ratio):
    rating = ""
    if (ratio >= 0.9 and ratio < 1):
         rating == "Excellent"
    elif (ratio >= 0.8):
         rating = "Very Good"
    elif (ratio >= 0.7):
         rating = "Good"
    elif (ratio >= 0.6):
         rating = "Needs Improvement"
    else:
         rating = "Unacceptable"

    return rating