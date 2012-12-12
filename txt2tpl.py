#coding=utf-8
import string
import sys
print sys.argv 
dumpFile = sys.argv[1]

tplFile = open(dumpFile[:dumpFile.rfind('.')] + '.tpl', 'w')
for line in open(dumpFile):
    tplFile.write( ':'.join(map(string.strip, line.split('\t')[:2])) + '\n')

print 'convertion completed'