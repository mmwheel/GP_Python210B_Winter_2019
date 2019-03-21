#!/usr/bin/env python3

'''
Title: Object oriented Mailroom: Donor and DonorCollection Classes
Dev: Marsha Wheeler
Date: 03/17/19
'''


import sys
from donor_models import Donor
from donor_models import DonorCollection

user_prompt = "\n".join(("Please choose from the options below:",
                         "1 - To view a list of donors type 'list'",
                         "2 - Send a Thank You to a single donor",
                         "3 - Create a Report",
                         "4 - Exit the Program",
                         ">>> "))


donors = DonorCollection()

def initialize_donor_dict():
    """  Initialize the donor dictionary """

    d1 = Donor("William Gates", 653772.32, 12.17)
    d2 = Donor("Jeff Bezos", 877.33)
    d3 = Donor("Paul Allen", 663.23, 43.87, 1.32)
    d4 = Donor("Mark Zuckerberg", 1663.23, 4300.87, 10432.0)

    donors.add_donor(d1)
    donors.add_donor(d2)
    donors.add_donor(d3)
    donors.add_donor(d4)


def show_list():
    '''Show list of donors'''

    return donors.print_donors()


def send_thank_you():
    user_name = input("Please enter a donor name:").title()
    user_amount = float(input("Please enter a donation amount for " + user_name + ":"))

    if user_name in donors.donor_dict.keys():
        donors.donor_dict[user_name].add_donation(float(user_amount))
        print(donors.donor_dict[user_name].send_thank_you())

    else:

        new_donor = Donor(user_name, user_amount)
        donors.add_donor(new_donor)
        print(donors.donor_dict[user_name].send_thank_you())


def display_report():
    print(donors.display_report_summary())


def exit_program():
    print("You chose to exit the program, Bye!")
    sys.exit()  # exit the interactive script


def main():
    while True:
        try:
            initialize_donor_dict()
            user_response = input(user_prompt)
            switch_func_dict = {
                '1': show_list,
                '2': send_thank_you,
                '3': display_report,
                '4': exit_program,
            }

            switch_func_dict.get(user_response)()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()


