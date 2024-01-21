def slugify(s):
	return s.strip().lower().replace(" ", "_")

def main():
	string = """
		 The Floor Will Be Lava
	"""
	print(slugify(string))

if __name__ == '__main__':
	main()