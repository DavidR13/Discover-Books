from wtforms import StringField, SelectField, SubmitField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import Length, InputRequired
from wtforms.fields.html5 import DateField


class Options(FlaskForm):
    option = SelectField("option", choices=[
        ('title', 'Book Title'),
        ('isbn', 'ISBN'),
        ('author', 'Author')
    ], default='title')
    submit = SubmitField("Submit")


class BookForms(FlaskForm):
    date_field = DateField('Date Picker', format='%Y-%m-%d')
    title = StringField("Title", validators=[InputRequired()])
    isbn = IntegerField("ISBN", validators=[Length(min=10, max=13), InputRequired()])
    author = StringField("Author", validators=[InputRequired()])
    genre = SelectField("genre", choices=[
        ('combined-print-and-e-book-fiction', 'Combined Print and E-Book Fiction'),
        ('combined-print-and-e-book-nonfiction',
         'Combined Print and E-Book Nonfiction'),
        ('hardcover-fiction', 'Hardcover Fiction'),
        ('hardcover-nonfiction', 'Hardcover Nonfiction'),
        ('trade-fiction-paperback', 'Trade Fiction Paperback'),
        ('mass-market-paperback', 'Mass Market Paperback'),
        ('paperback-nonfiction', 'Paperback Nonfiction'),
        ('e-book-fiction', 'E-Book Fiction'),
        ('e-book-nonfiction', 'E-Book Nonfiction'),
        ('hardcover-advice', 'Hardcover Advice'),
        ('paperback-advice', 'Paperback Advice'),
        ('advice-how-to-and-miscellaneous', 'Advice How-To and Miscellaneous'),
        ('hardcover-graphic-books', 'Hardcover Graphic Books'),
        ('paperback-graphic-books', 'Paperback Graphic Books'),
        ('manga', 'Manga'),
        ('combined-print-fiction', 'Combined Print Fiction'),
        ('combined-print-nonfiction', 'Combined Print Nonfiction'),
        ('chapter-books', 'Chapter Books'),
        ('childrens-middle-grade', 'Childrens Middle Grade'),
        ('childrens-middle-grade-e-book', 'Childrens Middle Grade E-Book'),
        ('childrens-middle-grade-hardcover', 'Childrens Middle Grade Hardcover'),
        ('childrens-middle-grade-paperback', 'Childrens Middle Grade Paperback'),
        ('paperback-books', 'Paperback Books'),
        ('picture-books', 'Picture Books'),
        ('series-books', 'Series Books'),
        ('young-adult', 'Young Adult'),
        ('young-adult-e-book', 'Young Adult E-Book'),
        ('young-adult-hardcover', 'Young Adult Hardcover'),
        ('young-adult-paperback', 'Young Adult Paperback'),
        ('animals', 'Animals'),
        ('audio-fiction', 'Audio Fiction'),
        ('audio-nonfiction', 'Audio Nonfiction'),
        ('business-books', 'Business Books'),
        ('celebrities', 'Celebrities'),
        ('crime-and-punishment', 'Crime and Punishment'),
        ('culture', 'Culture'),
        ('education', 'Education'),
        ('espionage', 'Espionage'),
        ('expeditions-disasters-and-adventures',
         'Expeditions Disasters and Adventures'),
        ('fashion-manners-and-customs', 'Fashion Manners and Customs'),
        ('food-and-fitness', 'Food and Fitness'),
        ('games-and-activities', 'Games and Activities'),
        ('graphic-books-and-manga', 'Graphic Books and Manga'),
        ('hardcover-business-books', 'Hardcover Business Books'),
        ('health', 'Health'),
        ('humor', 'Humor'),
        ('indigenous-americans', 'Indigenous Americans'),
        ('relationships', 'Relationships'),
        ('mass-market-monthly', 'Mass Market Monthly'),
        ('middle-grade-paperback-monthly', 'Middle Grade Paperback Monthly'),
        ('paperback-business-books', 'Paperback Business Books'),
        ('family', 'Family'),
        ('hardcover-political-books', 'Hardcover Political Books'),
        ('race-and-civil-rights', 'Race and Civil Rights'),
        ('religion-spirituality-and-faith', 'Religion Spirituality and Faith'),
        ('science', 'Science'),
        ('sports', 'Sports'),
        ('travel', 'Travel'),
        ('young-adult-paperback-monthly', 'Young Adult Paperback Monthly')
    ], default="hardcover-fiction")
    search = SubmitField("Search")