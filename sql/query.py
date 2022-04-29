import csv
import sqlite3
import pandas as pd

class SavingToSQL:
	def __init__(self, df:pd.DataFrame):
		self.df = df
		self.connection = sqlite3.connect('twitter-data-analysis.db')
		self.cursor = self.connection.cursor()
		print('Automation in Action...!!!')

	def create_table(self):
		create_table = '''CREATE TABLE tweets(id INTEGER PRIMARY KEY AUTOINCREMENT,
							created_at TEXT NOT NULL,
							source TEXT NOT NULL,
							original_text TEXT NOT NULL,
							polarity FLOAT NOT NULL,
							subjectivity FLOAT NOT NULL,
							lang TEXT NOT NULL,
							favorite_count FLOAT NOT NULL,
							retweet_count FLOAT NOT NULL,
							original_author TEXT NOT NULL,
							followers_count FLOAT NOT NULL,
							friends_count FLOAT NOT NULL,
							possibly_sensitive FLOAT NOT NULL,
							hashtags TEXT NOT NULL,
							user_mentions TEXT NOT NULL,
							place TEXT NOT NULL
						)
						'''
		print('Table creaton in action...!!!')
		try:
			self.cursor.execute(create_table)
		except sqlite3.OperationalError:
			print('Table already exists...')

	def csv_to_sql(self):
		contents = pd.read_csv(self.df)
		self.connection.commit()
		contents.to_sql('tweets', self.connection, if_exists='replace', index=True)
		self.cursor.execute('''SELECT * FROM tweets''')
		display = pd.DataFrame(self.cursor.fetchall())
		print(display)
		self.connection.close()

if __name__ == '__main__':
	file = '../data/processed_tweet_data.csv'
	obj = SavingToSQL(file)
	obj.create_table()
	obj.csv_to_sql()