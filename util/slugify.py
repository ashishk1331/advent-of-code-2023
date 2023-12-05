def slugify(s):
	return s.strip().lower().replace(" ", "_")

def main():
	string = """
		If You Give A Seed A Fertilizer
	"""
	print(slugify(string))

if __name__ == '__main__':
	main()