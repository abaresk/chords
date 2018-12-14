
import os

# Song parser

'''
Input: song in text file
	- name
	- tonic
	- comma-delimited integers representing eighth notes
	- comma-delimited chord names: one for every bar (8 notes)

Output: Song class
	- name
	- array of [reformatted bar]
	- array of chord names
'''

class Song():
	BAR_SIZE = 8
	OCTAVE_SIZE = 12

	def __init__(self, name=None, bars=[], chords=[]):
		self.name = name
		self.bars = bars
		self.chords = chords

	def fileParse(self, file):

		with open(file) as f:
			self.name = f.readline().strip()

			tonic = int(f.readline())

			# Parse notes
			notes = [x.strip() for x in f.readline().strip().split(',')]


			bars, bar = [], []
			lastPlayed = None
			count = self.BAR_SIZE

			for note in notes:
				if note != '.' and note != '-':
					lastPlayed = (int(note) - tonic) % self.OCTAVE_SIZE
				
				bar.append(lastPlayed)

				count = (count-1) % self.BAR_SIZE

				if count == 0:
					bars.append(bar)
					bar = []

			# flush the rest
			if bar:
				for i in range(count):
					bar.append(lastPlayed)
				bars.append(bar)


			# Parse chords
			chords = [x.strip() for x in f.readline().strip().split(',')]

			self.bars = bars
			self.chords = chords

		return



# Test
os.chdir('../data/input/')
file = 'route3.txt'
s = Song()
s.fileParse(file)
os.chdir('../../src')

