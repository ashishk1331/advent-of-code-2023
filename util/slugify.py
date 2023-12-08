def slugify(s):
	return s.strip().lower().replace(" ", "_")

def main():
	string = """
		 Haunted Wasteland
	"""
	print(slugify(string))

if __name__ == '__main__':
	main()