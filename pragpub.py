"""
	Downloads pragprog magazines
"""

from BeautifulSoup import BeautifulSoup
import urllib2

def get_issues(soup):
	"""docstring for get"""
	issues = []
	cleaned_issues = []
	issues = soup.findAll("h3")
	for issue in issues:
		cleaned_issue = issue.string.encode("UTF-8").strip()
		cleaned_issues.append(cleaned_issue)
	return cleaned_issues
		
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

# not working correctly but I'm tired. need to use BeautifulSoup .string method
def link_cleaner(html_element):
	"""Takes HTML element including takes, and returns new string encoded UTF-8 char encoding and stips whitespace"""
	try:
		clean_element = html_element.string.encode("UTF-8").strip()
	except AttributeError:
		pass
	finally:
		clean_element = html_element.string.strip()

def make_soup(magazine_url):
	"""docstring for make_soup"""
	html = urllib2.urlopen(magazine_url)
	soup = BeautifulSoup(html)
	return soup


def main():
	"""docstring for main"""
	soup = make_soup("http://pragprog.com/magazines")
	issues = get_issues(soup)
	get_formats(issues, soup)

if __name__ == "__main__":
	main()