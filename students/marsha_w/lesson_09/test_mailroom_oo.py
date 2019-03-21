#!/usr/bin/env python3

'''
Title: Object oriented Mailroom: Unit testing
Dev: Marsha Wheeler
Date: 03/17/19
'''

from donor_models import Donor
from donor_models import DonorCollection

########################
# Step1 Test Donor Class
########################

def test_init():
    """
    This only tests that it can be initialized with and without some content but it is a start
    """

    d = Donor()

    d = Donor('Marsha Wheeler', 10)


def test_add_donation():
    """
    This tests if you can append a donation

    It doesn't test if it works
    """

    d = Donor('Marsha Wheeler', 10)
    d.add_donation(20)


def test_donor_entry():
    """
    This tests whether methods are are entering donor information correctly
    """

    d = Donor('Marsha Wheeler', 10)
    d.add_donation(20)
    entry = str(d)

    assert('Marsha Wheeler') in entry
    assert ('10') in entry
    assert ('20') in entry

def test_thank_you():
    """
    This tests whether thank you text matches expectation
    """

    d = Donor('Marsha Wheeler', 10)

    expected_text = "Dear Marsha Wheeler, \n We are writing to thank you for your generous donation of a total $10.00 to our organization. \
                             \n Sincerely,"

    assert expected_text == d.send_thank_you()

def test_total_donations():
    d = Donor('Marsha Wheeler', 10, 20)

    expected_total = 30

    assert expected_total == d.total_donations

def test_average_donations():
    d = Donor('Marsha Wheeler', 10, 20)

    expected_average = 15

    assert expected_average == d.average_donations


##################################
# Step2 Test DonorCollection Class
##################################


def test_add_donor():
    """ This tests whether donors are added to the dictionary
    """
    d1 = Donor('Marsha Wheeler', 10)
    d2 = Donor('Andrew Magis', 20)

    dc = DonorCollection()

    dc.add_donor(d1)
    dc.add_donor(d2)

    print(dc.donor_dict)

    assert 'Marsha Wheeler' in dc.donor_dict.keys()
    assert 'Andrew Magis' in dc.donor_dict.keys()
    assert [10] in dc.donor_dict.values()
    assert [20] in dc.donor_dict.values()








