import logging

class FullMetalExtractor:
	def __init__(self,pdf,logging="_"):
		self._pdf = pdf
		self._class = None
		self._logger(logging)
		
		#general data
		self._md5 = None
		self._filesize = None
		self._header = None
		self._nObjs = 0
		self._nVersions = 0
		self._pageCount = 0
		self._images = 0
		self._nStreams = 0
		self._linearized = 0
		self._encrypted = 0
		
		#specifics
		self._nSusObjs = 0
		self._nLrgObjs = 0
		self._nSmlObjs = 0
		self._sActions = 0
		self._sElements = 0
		self._sEvents = 0
		
		#named dicts
		self._openAction = 0
		self._aa = 0
		self._names = 0
		self._acroform = 0
		self._js = 0
		self._javascript = 0
		self._launch = 0
		self._submitForm = 0
		self._importData = 0
		self._encrypt = 0
		self._jbig2decode = 0
		self._embeddedFiles = 0
		self._flash = 0	
		
		#filters
		self._asciiHexDecode = 0
		self._ascii85Decode = 0
		self._lzwDecode = 0
		self._flateDecode = 0
		self._runLengthDecode = 0
		self._ccittfaxDecode = 0
		self._dctDecode = 0
		self._jpxDecode = 0
		self._crypt = 0
		
		#call to action
		self._fullClip()
		
	def getFileHeader(self):
		one = '' + \
			"filesize\t" + \
			"nObjs\t" + \
			"nVersions\t" + \
			"pageCount\t" + \
			"images\t" + \
			"nStreams\t" + \
			"linearized\t" + \
			"encrypted\t" + \
			"nLrgObjs\t" + \
			"nSmlObjs\t" + \
			"sActions\t" + \
			"sElements\t" + \
			"sEvents\t" + \
			"openAction\t" + \
			"aa\t" + \
			"names\t" + \
			"acroform\t" + \
			"js\t" + \
			"javascript\t" + \
			"launch\t" + \
			"submitForm\t" + \
			"importData\t" + \
			"encrypt\t" + \
			"jbig2decode\t" + \
			"embeddedFiles\t" + \
			"flash\t" + \
			"asciiHexDecode\t" + \
			"ascii85Decode\t" + \
			"lzwDecode\t" + \
			"flateDecode\t" + \
			"runLengthDecode\t" + \
			"ccittfaxDecode\t" + \
			"dctDecode\t" + \
			"jpxDecode\t" + \
			"crypt\t" + \
			"class"
		two = '' + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t" + \
			"d\t"
		three = '' + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"\t" + \
			"class\t" 
		return one + "\n" + two + "\n" + three + "\n"
		
	def getTab(self):
		out = '' + \
			self._filesize + "\t" + \
			str(self._nObjs) + "\t" + \
			str(self._nVersions) + "\t" + \
			str(self._pageCount) + "\t" + \
			str(self._images) + "\t" + \
			str(self._nStreams) + "\t" + \
			str(self._linearized) + "\t" + \
			str(self._encrypted) + "\t" + \
			str(self._nLrgObjs) + "\t" + \
			str(self._nSmlObjs) + "\t" + \
			str(self._sActions) + "\t" + \
			str(self._sElements) + "\t" + \
			str(self._sEvents) + "\t" + \
			str(self._openAction) + "\t" + \
			str(self._aa) + "\t" + \
			str(self._names) + "\t" + \
			str(self._acroform) + "\t" + \
			str(self._js) + "\t" + \
			str(self._javascript) + "\t" + \
			str(self._launch) + "\t" + \
			str(self._submitForm) + "\t" + \
			str(self._importData) + "\t" + \
			str(self._encrypt) + "\t" + \
			str(self._jbig2decode) + "\t" + \
			str(self._embeddedFiles) + "\t" + \
			str(self._flash) + "\t" + \
			str(self._asciiHexDecode) + "\t" + \
			str(self._ascii85Decode) + "\t" + \
			str(self._lzwDecode) + "\t" + \
			str(self._flateDecode) + "\t" + \
			str(self._runLengthDecode) + "\t" + \
			str(self._ccittfaxDecode) + "\t" + \
			str(self._dctDecode) + "\t" + \
			str(self._jpxDecode) + "\t" + \
			str(self._crypt) + "\t" + \
			str("?")
		return out
		
	def _fullClip(self):
		self._processGeneral()
		self._collectData()
		
	def _logger(self,level):
		self._log = logging.getLogger('PDFMeta')
		if level == "INFO":
			logging.basicConfig(level=logging.INFO)
		elif level == "ERROR":
			logging.basicConfig(level=logging.ERROR)
		else:
			pass
		
	def _processGeneral(self):
		statsHandle = self._pdf.getStats()
		
		if statsHandle.has_key('MD5'):
			self._md5 = statsHandle['MD5']
		if statsHandle.has_key('Size'):
			self._filesize = statsHandle['Size']
		if statsHandle.has_key('Version'):
			self._header = statsHandle['Version']
		if statsHandle.has_key('Objects'):
			self._nObjs = statsHandle['Objects']
		if statsHandle.has_key('Updates'):
			self._nVersions = statsHandle['Updates']
		if statsHandle.has_key('Pages'):
			self._pageCount = statsHandle['Pages']
		if statsHandle.has_key('Images'):
			if statsHandle['Images'] == 'True':
				self._images = 1
		if statsHandle.has_key('Streams'):
			self._nStreams = statsHandle['Streams']
		if statsHandle.has_key('Linearized'):
			if statsHandle['Linearized'] == 'True':
				self._linearized = 1
		if statsHandle.has_key('Encrypted'):
			if statsHandle['Encrypted'] == 'True':
				self._encrypted = 1
		
		#DEBUG
		self._log.info("MD5: %s" % (self._md5))
		self._log.info("SIZE: %s" % (self._filesize))
		self._log.info("HEADER: %s" % (self._header))
		self._log.info("OBJECTS: %s" % (self._nObjs))
		self._log.info("UPDATES: %s" % (self._nVersions))
		self._log.info("PAGES: %s" % (self._pageCount))
		self._log.info("IMAGES: %s" % (self._images))
		self._log.info("STREAMS: %s" % (self._nStreams))
		self._log.info("LINEARIZED: %s" % (self._linearized))
		self._log.info("ENCRYPTED: %s" % (self._encrypted))
		
	def _collectData(self):
			
		bodyHandler = self._pdf.body
		
		masterEvents = []
		masterActions = []
		masterElements = []
		
		for body in bodyHandler:
			objsHandler = body.objects
			for index in objsHandler:
				detailHandler = objsHandler[index].object
				try:
					masterEvents = masterEvents + detailHandler.suspiciousEvents
					masterActions = masterActions + detailHandler.suspiciousActions
					masterElements = masterElements + detailHandler.suspiciousElements
				except:
					pass
					
				if len(masterEvents) > 0 or len(masterActions) > 0 or len(masterElements) > 0:
					self._nSusObjs += 1
			
				sizeHandler = objsHandler[index].size
				if sizeHandler > 650:
					self._nLrgObjs += 1
				else:
					self._nSmlObjs += 1
				
		masterEvents = list(set(masterEvents))
		masterActions = list(set(masterActions))
		masterElements = list(set(masterElements))
		
		self._sActions = len(masterEvents)
		self._sElements = len(masterActions)
		self._sEvents = len(masterElements)
		
		#DEBUG
		self._log.info("#SUSOBJS: %s" % (self._nSusObjs))
		self._log.info("#LOBJS: %s" % (self._nLrgObjs))
		self._log.info("#SOBJS: %s" % (self._nSmlObjs))
		self._log.info("#ACTONS: %s" % (self._sActions))
		self._log.info("#ELEMENTS: %s" % (self._sElements))
		self._log.info("#EVENTS: %s" % (self._sEvents))
		
		self._handleNamed(masterEvents,masterActions,masterElements)
		
	def _handleNamed(self,events,elements,actions):
	
		self._tracking = {
		    '/OpenAction' : 0,\
		    '/AA' : 0,\
		    '/Names' : 0,\
		    '/AcroForm' : 0,\
		
		    '/JS' : 0,\
		    '/JavaScript' : 0,\
		    '/Launch' : 0,\
		    '/SubmitForm' : 0,\
		    '/ImportData' : 0,\
		    '/Encrypt' : 0,\
		
		    '/JBIG2Decode' : 0,\
		    '/EmbeddedFiles' : 0,\
		    '/Flash' : 0,\
		    
		    '/ASCIIHexDecode' : 0,\
		    '/ASCII85Decode' : 0,\
		    '/LZWDecode' : 0,\
		    '/FlateDecode' : 0,\
		    '/RunLengthDecode' : 0,\
		    '/CCITTFaxDecode' : 0,\
		    '/DCTDecode' : 0,\
		    '/JPXDecode' : 0,\
		    '/Crypt' : 0
		}
		
		try:
			for i in events:
				self._tracking[i] = self._tracking[i] + 1
		except:
			pass
		try:
			for i in elements:
				self._tracking[i] = self._tracking[i] + 1
		except:
			pass
		try:
			for i in actions:
				self._tracking[i] = self._tracking[i] + 1
		except:
			pass
		
		self._openAction = self._tracking['/OpenAction']
		self._aa = self._tracking['/AA']
		self._names = self._tracking['/Names']
		self._acroform = self._tracking['/AcroForm']
		self._js = self._tracking['/JS']
		self._javascript = self._tracking['/JavaScript']
		self._launch = self._tracking['/Launch']
		self._submitForm = self._tracking['/SubmitForm']
		self._importData = self._tracking['/ImportData']
		self._encrypt = self._tracking['/Encrypt']
		self._jbig2decode = self._tracking['/JBIG2Decode']
		self._embeddedFiles = self._tracking['/EmbeddedFiles']
		self._flash = self._tracking['/Flash']
		self._asciiHexDecode = self._tracking['/ASCIIHexDecode']
		self._ascii85Decode = self._tracking['/ASCII85Decode']
		self._lzwDecode = self._tracking['/LZWDecode']
		self._flateDecode = self._tracking['/FlateDecode']
		self._runLengthDecode = self._tracking['/RunLengthDecode']
		self._ccittfaxDecode = self._tracking['/CCITTFaxDecode']
		self._dctDecode = self._tracking['/DCTDecode']
		self._jpxDecode = self._tracking['/JPXDecode']
		self._crypt = self._tracking['/Crypt']
		
		#DEBUG
		self._log.info("OPENACTION: %s" % (self._openAction))
		self._log.info("AA: %s" % (self._aa))
		self._log.info("NAMES: %s" % (self._names))
		self._log.info("ACROFORM: %s" % (self._acroform))
		self._log.info("JS: %s" % (self._js))
		self._log.info("JAVASCRIPT: %s" % (self._javascript))
		self._log.info("LAUNCH: %s" % (self._launch))
		self._log.info("SUBMITFORM: %s" % (self._submitForm))
		self._log.info("IMPORTDATA: %s" % (self._importData))
		self._log.info("ENCRYPT: %s" % (self._encrypt))
		self._log.info("JBIG2DECODE: %s" % (self._jbig2decode))
		self._log.info("EMBEDDEDFILES: %s" % (self._embeddedFiles))
		self._log.info("FLASH: %s" % (self._flash))
		self._log.info("ASCIIHEXDECODE: %s" % (self._asciiHexDecode))
		self._log.info("ASCII85DECODE: %s" % (self._ascii85Decode))
		self._log.info("LZWDECODE: %s" % (self._lzwDecode))
		self._log.info("FLATEDECODE: %s" % (self._flateDecode))
		self._log.info("RUNLENGTHDECODE: %s" % (self._runLengthDecode))
		self._log.info("CCITTFAXDECODE: %s" % (self._ccittfaxDecode))
		self._log.info("DCTDECODE: %s" % (self._dctDecode))
		self._log.info("JPXDECODE: %s" % (self._jpxDecode))
		self._log.info("CRYPT: %s" % (self._crypt))



