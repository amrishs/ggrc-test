'''
Created on Jul 18, 2013

@author: ukyo.duong

This are individual files from SmokeTestScript.  It's not 1-to-1 because some test cases go 
together and you can't separate them.

'''

import unittest

from SmokeTest.TestAllTabsIntegrity import TestAllTabsIntegrity
from SmokeTest.TestCreatePersonAuthorizationLogInOut import TestCreatePersonAuthorizationLogInOut
from SmokeTest.TestCreateUpdateDeleteProgram import TestCreateUpdateDeleteProgram
from SmokeTest.TestCreateUpdateDeleteRegulation import TestCreateUpdateDeleteRegulation
from SmokeTest.TestCreateUpdateDeleteSystem import TestCreateUpdateDeleteSystem
from SmokeTest.TestEventLog import TestEventLog
from SmokeTest.TestFourLevelsMapping import TestFourLevelsMapping
from SmokeTest.TestImportExportPeople import TestImportExportPeople
from SmokeTest.TestImportExportProcess import TestImportExportProcess
from SmokeTest.TestImportExportSystem import TestImportExportSystem
from SmokeTest.TestMapRegulationToSystem import TestMapRegulationToSystem
from SmokeTest.TestMapSystemToPeople import TestMapSystemToPeople
from SmokeTest.TestRelevantMapping import TestRelevantMapping
from SmokeTest.WorkflowSmokeTest import WorkflowSmokeTest


#from SmokeTest.TestImportPeopleValidation import TestImportPeopleValidation
#from SmokeTest.TestImportProcessesValidation import TestImportProcessesValidation