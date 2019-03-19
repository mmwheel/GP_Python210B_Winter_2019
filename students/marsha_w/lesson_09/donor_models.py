#!/usr/bin/env python3

'''
Title: Object oriented Mailroom: Donor and DonorCollection Classes
Dev: Marsha Wheeler
Date: 03/17/19
'''


class Donor(object):

    '''
    Donor Class which handles information for individual donors
    '''

    def __init__(self, name='', *args):
        self.name = name
        self.donations = list(args)

    def __str__(self):
        return '{}: {}'.format(self.name, str(self.donations).strip('[]'))


    def add_donation(self, amount):
        # Function to add a donation to the list of donations for this donor
        self.donations.append(amount)

    def send_thank_you(self):
        # Generates thank you note for this

        thank_you_text = "Dear {:s}, \n We are writing to thank you for your generous donation of a total ${:.2f} to our organization. \
                             \n Sincerely,"

        return thank_you_text.format(self.name, self.donations[-1])


    @property
    def name(self):
        ''' I am read only'''
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def total_donations(self):
        return sum(self.donations)


    @property
    def average_donations(self):
        return sum(self.donations)/len(self.donations)


class DonorCollection(object):
    """
        Donor Collection Class which handles information for multiple donors
    """

    def __init__(self):
        self.donor_dict = {}

    def add_donor(self, donor_object):
        """ Look to see if donor with name already exists, if exists add donations to donor,
        if not add donor and donation to data structure """

        if donor_object.name in self.donor_dict.keys():
            value = str(donor_object.donations).strip('[]')
            value = int(value)
            self.donor_dict[donor_object.name].append(value)
            return self.donor_dict

        else:
            self.donor_dict[donor_object.name] = donor_object.donations
            return self.donor_dict

    def print_donors(self):
        for k in self.donor_dict.keys():
            print(k)

    def create_report(self):
        # create a new list with donor names, total donation, number of donations and average donations
        donor_list = list(self.donor_dict.items())

        # Use comprehension to create a new list
        donor_summary = [[donor[0], float(sum(donor[1])), int(len(donor[1])), float(sum(donor[1])) / int(len(donor[1]))]
                         for donor in donor_list]

        def sort_key(donor_summary):
            return donor_summary[1]

        sorted_donor_summary = (sorted(donor_summary, key=sort_key, reverse=True))
        return sorted_donor_summary

    def display_report_summary(self):
        sorted_summary = self.create_report()
        table_header = ["Name", "Total Given", "Numb of Gifts", "Average Gift"]
        sorted_summary.insert(0, table_header)
        dash = '-' * 70
        for i in range(len(sorted_summary)):
            if i == 0:
                print(dash)
                print('{:20} | {:>10s} | {:>15s} | {:>15s}'.format(sorted_summary[i][0], sorted_summary[i][1],
                                                                   sorted_summary[i][2], sorted_summary[i][3]))
                print(dash)
            else:
                print('{:20} ${:>10.1f}{:>20d} ${:>16.1f}'.format(sorted_summary[i][0], sorted_summary[i][1],
                                                                  sorted_summary[i][2], sorted_summary[i][3]))

