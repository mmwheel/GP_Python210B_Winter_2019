#!/usr/bin/env python3

'''
Title: Object oriented Mailroom: Donor and DonorCollection Classes
Dev: Marsha Wheeler
Date: 03/17/19
'''


import sys
import datetime
import copy
from donor_models import Donor
from donor_models import DonorCollection

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

    return donors


def show_list():
    """Show list of donors"""
    initialize_donor_dict().print_donors()

