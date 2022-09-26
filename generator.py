import pandas as pd
import numpy as np

# Delighted to start at <a href="https://twitter.com/kous2v/status/1452667764838215689" target="_blank">Microsoft Research, Montreal</a>. Looking forward to what's ahead!</li>

def read_publications(path="publications.csv"):
	df = pd.read_csv(path, encoding = "ISO-8859-1")
	df = df.values
	unique_years = np.sort(list(set([int(i) for i in df.T[0]])))[::-1]
	shorts = '<div>\n						<h4>'+' | '.join(['<a href="#'+str(y)+'" class="active">'+str(y)+'</a>' for y in unique_years])+'</h4>\n					</div>'
	c = 0
	output = shorts+'\n'
	for year in unique_years:
		curr_count = len(df)-c
		top = '					<div id="'+str(year)+'">\n					<hr class="thin">\n						<h4>'+str(year)+'</h4>\n						<ol reversed start = "'+str(curr_count)+'" class="fa-ol text-left">\n'
		bottom = '						</ol>\n					</div>'
		output+=top
		for row in df:
			if int(row[0])==year:
				a = '						<li itemscope="" itemtype="https://schema.org/CreativeWork">\n							<i class="fa-li fa fa-file-text pub-icon text-justify" aria-hidden="true"></i>\n							<b>'
				a += str(row[1])+'</b>&nbsp;&nbsp;<font size="3em">&nbsp;&nbsp;\n							<a href="'
				a += str(row[3])+'" target="_blank">Link</a>&nbsp;&nbsp;\n							<h6>'
				a += str(row[2])+'<br>\n							<i>'
				a += str(row[4])+'</i></h6>\n						</li>\n'
				output += a
				c+=1
		output += bottom+'\n'
	return output


def read_projects(path="projects.csv"):
	df = pd.read_csv(path)
	df = df.values
	outs = []
	for row in df:
		out = '<li><h5><b>'+str(row[0])+":</b> "+'<a href="'+row[3]+'" target="_blank">'+row[1]+'</a><br>'+row[2]+'</li>'
		outs.append(out)
	return '\n						'.join(outs)


def read_main_experience(path="main_experience.csv"):
	df = pd.read_csv(path)
	df = df.values
	outs = []
	for row in df:
		a = '<li><h5>'+str(row[0])+', '+str(row[1])+', <a href="'+str(row[3])+'" target="_blank">'+str(row[2])+'</a></h5></li>'
		outs.append(a)
	outs = '\n						'.join(outs)
	return outs

def read_main_education(path="main_education.csv"):
	df = pd.read_csv(path)
	df = df.values
	outs = []
	for row in df:
		a = '<li><h5>'+str(row[0])+'</h5><h5>'+str(row[1])+'</h5><h5> <a href="'+str(row[3])+'" target="_blank">'+str(row[2])+'</a></h5></li>'
		outs.append(a)
	outs = '\n						'.join(outs)
	return outs


def read_achievements(path="achievements.csv"):
	df = pd.read_csv(path)
	df = df.values
	outs = []
	for row in df:
		a = '<li><h5><b>'+str(row[0])+' '+str(row[1])+':</b> <a href="'+str(row[4])+'" target="_blank">'+str(row[2])+'</a><br>'+str(row[3])+'</li>'
		outs.append(a)
	outs = '\n						'.join(outs)
	return outs



def main():
	projects = read_projects()
	pub = read_publications()
	exp = read_main_experience()
	edu = read_main_education()
	ach = read_achievements()
	print(ach)

if __name__ == '__main__':
	main()