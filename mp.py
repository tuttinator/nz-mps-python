""" Member of Parliament """
class MP:
    """ Init a new MP """
    def __init__(self, name=None, details_link=None, electoral_details=None):
        self.last_name, self.first_name = [n.strip() for n in name.split(',')]
        self.details_link = details_link
        print(electoral_details)
        self.party, self.electorate = [e.strip() for e in electoral_details.split(',')]
        self.list_mp = False
        self._parse_electorate()

    def __repr__(self):
        return('<MP %s>' % self.title())

    def title(self):
        return('%s %s, %s' % (self.first_name, self.last_name, self.party))

    """ Parses 'List' as a List MP """
    def _parse_electorate(self):
        if self.electorate == 'List':
            self.electorate = None
            self.list_mp = True

