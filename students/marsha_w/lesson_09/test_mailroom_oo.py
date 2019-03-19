#!/usr/bin/env python3

'''
Title: Object oriented Mailroom: Unit testing
Dev: Marsha Wheeler
Date: 03/17/19
'''

# import * is often bad form, but makes it easier to test everything in a module.
from donor_models import Donor

########
# Step 1
########

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
    d = Donor('Marsha Wheeler', 10)

    expected_text = "Dear Marsha Wheeler, \n We are writing to thank you for your generous donation of a total $10.00 to our organization. \
                             \n Sincerely,"

    assert expected_text == d.send_thank_you()




