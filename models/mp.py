from sqlalchemy import Column, Integer, Boolean, String
from database import Base

""" Member of Parliament """
class MP(Base):
    __tablename__ = 'mps'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150))
    last_name = Column(String(150))
    party = Column(String(150))
    list_mp = Column(Boolean)
    details_url = Column(String(150))
    image_url = Column(String(150))

    _base_url = 'http://www.parliament.nz'

    """ Init a new MP """
    def __init__(self, name=None, details_url=None, electoral_details=None):
        self.last_name, self.first_name = [n.strip() for n in name.split(',')]
        self.details_url = self._base_url + details_url
        self.party, self.electorate = [e.strip() for e in electoral_details.split(',')]
        self.list_mp = False
        self._parse_electorate()

    def __repr__(self):
        return('<MP %s>' % self._formatted_title())

    def _formatted_title(self):
        return("id=%i first_name='%s' last_name='%s' party='%s'" % (self.id, self.first_name, self.last_name, self.party))

    def image_from_src(self, src):
        self.image_url = self._base_url + src

    def as_json(self):
        return {
                'id': self.id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'party': self.party,
                'list_mp': self.list_mp,
                'details_url': self.details_url,
                'image_url': self.image_url
                }

    """ Parses 'List' as a List MP """
    def _parse_electorate(self):
        if self.electorate == 'List':
            self.electorate = None
            self.list_mp = True

