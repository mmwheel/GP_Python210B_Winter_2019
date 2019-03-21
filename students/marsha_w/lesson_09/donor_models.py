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

    def create_report(self):
        """
        Create report summary for each donor
        """
        total = self.total_donations
        avg = self.average_donations
        num = len(self.donations)

        donor_report = [self.name, float(total), int(num), float(avg)]

        return donor_report


class DonorCollection(object):
    """
        Donor Collection Class which handles information for multiple donors
    """

    def __init__(self):
        self.donor_dict = {}

    def add_donor(self, donor_object):

        """ Add donor and donation to data structure """
        self.donor_dict[donor_object.name] = donor_object

    def add_donation(self, name, amount):

        """ Add donor and donation to data structure """
        self.donor_dict[name].add_donation(amount)

    def print_donors(self):
        for k in self.donor_dict.keys():
            print(k)

    def display_report_summary(self):
        """
        Generates a report summary for donors in dictionary
        I am sure there is a better way to do this
        """

        report_summary = []

        for key, item in self.donor_dict.items():
            report_summary.append(item.create_report())

        #def sort_key(report_summary):
        #    return report_summary[1]

        #sorted_summary = (sorted(report_summary, key=sort_key, reverse=True))


        table_header = ["Name", "Total Given", "Numb of Gifts", "Average Gift"]
        report_summary.insert(0, table_header)
        dash = '-' * 70
        for i in range(len(report_summary)):
            if i == 0:
                print(dash)
                print('{:20} | {:>10s} | {:>15s} | {:>15s}'.format(report_summary[i][0], report_summary[i][1],
                                                                   report_summary[i][2], report_summary[i][3]))
                print(dash)
            else:
                print('{:20} ${:>10.1f}{:>20d} ${:>16.1f}'.format(report_summary[i][0], report_summary[i][1],
                                                                  report_summary[i][2], report_summary[i][3]))

