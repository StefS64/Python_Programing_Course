import argparse

from generating_directory_structure import generate_directory_structure

# List of potential input parameters
MONTHS = ["Styczen", "Luty", "Marzec", "Kwiecień", "Maj",
          "Czerwiec", "Lipiec", "Sierpien", "Wrzesien", "Pazdziernik", "Listopad", "Grudzien"]
DAY_PARTS = ["r", "w"]
# Creating days range list with loop
DAYS_RANGES = ['pn', 'wt', 'śr', 'cz', 'pt', 'sb', 'nd']

for i in range(7):
    for j in range(7):
        if i != j:
            DAYS_RANGES.append(DAYS_RANGES[i] + "-" + DAYS_RANGES[j])

parser = argparse.ArgumentParser()
parser.add_argument("--months", type=str, nargs="+", choices=MONTHS, help="selection of months")
parser.add_argument("--days_ranges", type=str, nargs="+",
                    choices=DAYS_RANGES, help="selection of days ranges (same number as months)")
parser.add_argument(
   "--day_parts", type=str, nargs="+", default="r",
   choices=DAY_PARTS, help="selection of day part: morning (r) or evening (w) (default morning)")
parser.add_argument(
   "-w", action="store_const", const=True, default=False, help="write (default read)")
parser.add_argument(
   "-c", action="store_const", const=True, default=False, help="csv type of file (default json)")

args = parser.parse_args()

generate_directory_structure(args.months, args.days_ranges, args.day_parts, args.w, args.c)
