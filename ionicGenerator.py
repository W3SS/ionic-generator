import sys
import os

'''
Python Script to Generate Ionic-2 Pages
'''

def createHtml(path, filename):
	content = '''<ion-navbar *navbar>
  <button menuToggle>
    <icon menu></icon>
  </button>
  <ion-title>''' + filename + '''</ion-title>
</ion-navbar>

<ion-content padding class="''' + filename + '''">
  ''' + filename + '''
</ion-content>'''

	filename = filename + '.html'
	saveInFile(path, filename, content)

def createJs(path, filename):
	content = '''import {Page, NavController} from 'ionic/ionic';

@Page({
  templateUrl: 'build/pages/''' + filename + '/' + filename + '''.html',
})

export class ''' + filename.title() + ''' {
  constructor(nav: NavController) {
    this.nav = nav;
  }
}'''

	filename = filename + '.js'
	saveInFile(path, filename, content)

def createCss(path, filename):
	content = '/* Your CSS goes here */'
	filename = filename + '.css'
	saveInFile(path, filename, content)

def saveInFile(path, filename, content):
	if not os.path.exists(path):
		os.makedirs(path)
	
	f = open(path + filename, 'a')
	f.write(content)
	f.close()	

def main():
	print 'dir: ' + os.getcwd()
	print 'filename: ' + sys.argv[1]

	projDir = os.getcwd()
	filename = sys.argv[1]
	path = projDir + '/app/pages/' + filename + '/'

	createHtml(path, filename)
	createJs(path, filename)
	createCss(path, filename)

	print 'Done'

if __name__ == '__main__':
	main()
