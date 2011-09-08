"""
	Downloads pragprog magazines
"""
"""Downloads specified version of PragPub magazine from http://pragprog.com/magazines"""

from BeautifulSoup import BeautifulSoup
import urllib2

def get_issues(soup):
	"""Returns clean list of strings with magazine date and issue number from http://pragprog.com/magazines."""
	issues = []
	cleaned_issues = []
	issues = soup.findAll("h3")
	for issue in issues:
		cleaned_issue = link_cleaner(issue)
		cleaned_issues.append(cleaned_issue)
	return cleaned_issues

# not working either. just trying to get some thinking down
def get_formats(issue, format, soup):
	"""Grabs specified issue(s) and its format"""
	issue_formats = {}
	cleaned_formats = []
	for issue in list_of_issues:
		mag_formats = soup.findAll("span","link")
		for format in mag_formats:
			clean_format = link_cleaner(format)
			print clean_format
		print mag_format

# sort of working now. works if a unicode string is passed.
# next get it to work no matter what type of string is passed
def link_cleaner(html_element):
	"""Takes HTML elementand returns new string encoded UTF-8 char encoding and stips whitespace"""
	try:
		clean_element = html_element.string.encode("UTF-8").strip()
		return clean_element
	except AttributeError:
		clean_element = html_element.string.strip()
		return	clean_element

def make_soup(magazine_url):
	"""docstring for make_soup"""
	html = urllib2.urlopen(magazine_url)
	soup = BeautifulSoup(html)
	return soup

def main():
	"""docstring for main"""
	soup = make_soup("http://pragprog.com/magazines")
	issues = get_issues(soup)
	print issues
	# get_formats(issues, soup)

if __name__ == "__main__":
	main()