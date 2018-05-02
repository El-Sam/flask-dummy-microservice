from model.models import db, Person


class PersonRepository(object):

    def save(self, person: Person):
        db.session.add(person)
        db.session.commit()

    def remove(self, person: Person):
        db.session.delete(person)
        db.session.commit()
