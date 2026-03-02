# grades.py

def compute_average(scores):
    """Calculates the mean of a list of scores."""
    return sum(scores) / len(scores)

def assign_grade(avg):
    """Assigns a letter grade based on the numerical average."""
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

def generate_remark(grade):
    """Returns a performance description based on the letter grade."""
    remarks = {
        "A": "Excellent Performance",
        "B": "Good Performance",
        "C": "Satisfactory Performance",
        "D": "Needs Improvement",
        "F": "Failing Status"
    }
    return remarks.get(grade, "Invalid Grade")