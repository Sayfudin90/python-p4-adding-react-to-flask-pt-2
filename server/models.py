from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer)
    genre = db.Column(db.String)
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "genre": self.genre
        }