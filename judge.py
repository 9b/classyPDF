__description__ = \
    'Analyzes PDF files and classifies them based on features present'
__author__ = 'Brandon Dixon'
__version__ = '1.0'
__date__ = '2012/04/28'

import math
import os
import os.path
import optparse

import Orange

from itertools import ifilter
from peepdf_classy.bsdPDFCore import PDFParser
from classyPDF import FullMetalExtractor


MALWARE_DATA = Orange.data.Table("data/complete.tab")
_learner = Orange.classification.knn.kNNLearner()
classifier = _learner(MALWARE_DATA)


def decision(data):
    '''make a decision for the given dataset d'''

    c = []
    # probabilities for being good, bad or targeted
    g = ""
    b = ""
    t = ""

    try:
        tmp = Orange.data.Instance(MALWARE_DATA.domain, data)
        c = classifier(tmp, Orange.classification.Classifier.GetBoth)
        g = int(math.ceil(c[1][0] * 100))
        b = int(c[1][1] * 100)
        t = int(c[1][2] * 100)
    except Exception, ex:
        print data
        print ex
        c.append(666)

    if c[0] == 0:
        des = "non-malicious"
    elif c[0] == 1:
        des = "malicious\t"
    elif c[0] == 2:
        des = "targeted\t"
    else:
        return "failed"

    return "{0}\t(G:{1:3}%\tB:{2:3}%\tT:{3:3}%)".format(des, g, b, t)


def handle_file(f):
    pdfParser = PDFParser()
    ret, pdf = pdfParser.parse(f, True, False)
    obj = FullMetalExtractor(pdf, "_")
    tab = obj.getTab().split("\t")
    return decision(tab)


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
        result = handle_file(options.file)
        print options.file + " : " + result
    elif options.dir:
        pdfs = []
        files = ifilter(os.path.isfile,
                        map(lambda x: os.path.join(options.dir, x),
                            os.listdir(os.path.expanduser(options.dir))))

        for file in sorted(files):
            result = handle_file(file)
            print result + " : " + file
    else:
        return oParser.print_help()


if __name__ == '__main__':
    main()
