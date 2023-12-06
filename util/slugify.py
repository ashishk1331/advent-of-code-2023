def slugify(s):
	return s.strip().lower().replace(" ", "_")

def main():
	string = """
		Wait For It
	"""
	print(slugify(string))

if __name__ == '__main__':
	main()