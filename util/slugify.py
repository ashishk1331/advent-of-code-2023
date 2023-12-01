def slugify(s):
	return s.strip().lower().replace(" ", "_")

def main():
	string = """
		Trebuchet
	"""
	print(slugify(string))

if __name__ == '__main__':
	main()