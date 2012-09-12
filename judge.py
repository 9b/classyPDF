__description__ = \
    'Analyzes PDF files and classifies them based on features present'
__author__ = 'Brandon Dixon'
__version__ = '1.0'
__date__ = '2012/04/28'

import Orange
import math
import os
from classyPDF import *
from peepdf_classy.bsdPDFCore import PDFParser
import optparse


mal = Orange.data.Table("data/complete.tab")
learner = Orange.classification.knn.kNNLearner()
classifier = learner(mal)


def decision(d):
    c = []
    g = ""
    b = ""
    t = ""

    try:
        tmp = Orange.data.Instance(mal.domain, d)
        c = classifier(tmp, Orange.classification.Classifier.GetBoth)
        g = int(math.ceil(c[1][0] * 100))
        b = int(c[1][1] * 100)
        t = int(c[1][2] * 100)
    except Exception, ex:
        print d
        print ex
        c.append(666)

    if c[0] == 0:
        des = "non-malicious\t(G:{0}%\tB:{1}%\tT:{2}%)".format(g, b, t)
    elif c[0] == 1:
        des = "malicious\t\t(G:{0}%\tB:{1}%\tT:{2}%)".format(g, b, t)
    elif c[0] == 2:
        des = "targeted\t\t(G:{0}%\tB:{1}%\tT:{2}%)".format(g, b, t)
    else:
        des = "failed"

    return des


def handle_file(f):
    pdfParser = PDFParser()
    ret, pdf = pdfParser.parse(f, True, False)
    obj = FullMetalExtractor(pdf, "_")
    tab = obj.getTab().split("\t")
    des = decision(tab)
    return des


def main():
    oParser = optparse.OptionParser(usage='usage: %prog [options]\n' +
                                    __description__, version='%prog ' +
                                    __version__)
    oParser.add_option('-f', '--file', default='', type='string',
                       help='file to build an object from')
    oParser.add_option('-d', '--dir', default='', type='string',
                       help='dir to build an object from')
    oParser.add_option('-r', '--report', default='', type='string',
                       help='create basic report')
    (options, args) = oParser.parse_args()

    if options.file:
        decision = handle_file(options.file)
        print options.file + " : " + decision
    elif options.dir:
        files = []
        pdfs = []
        dirlist = os.listdir(options.dir)
        for fname in dirlist:
            files.append(fname)
        files.sort()
        for file in files:
            decision = handle_file(options.dir + file)
            print decision + " : " + file
    else:
        return oParser.print_help()


if __name__ == '__main__':
    main()
