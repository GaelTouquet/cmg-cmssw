from ROOT import TFile, heppy, Double

import os
import logging 
import pprint 

class ElectronMVAIDRun2(object):

    def __init__(self, mvaTag, mvaName, weightFileNames,
                 nCategories, False, variableDefinition,
                 categoryCutStrings):
        logging.info('initializing electron id MVA')
        logging.info(pprint.pformat([mvaTag, mvaName, 
                                     weightFileNames,
                                     nCategories, False,
                                     variableDefinition,
                                     categoryCutStrings]))
        self._mvaid = heppy.EGammaMvaEleEstimatorRun2FWLite(
            mvaTag, mvaName, weightFileNames,
            nCategories, False, variableDefinition,
            categoryCutStrings
            ) 

    def score(self, electron, event):
        return self._mvaid(electron, event)

    def threshold(self, pt, working_point):
        # need to test the pt-dependant cuts, they should be given as argument to the constructor? sone examples can be found RecoEgamma/ElectronIdentification/python/Identification/mvaElectronID_Fall17_iso_V2_cff.py

# see RecoEgamma/ElectronIdentification/python/Identification/mvaElectronID_Fall17_iso_V2_cff.py for categories and weightfiles
# variabledefinition should be the pqth to this file : RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt (or probably ElectronMVAEstimatorRun2Fall17V1Variables.txt ?)
ElectronMVAID2017Isov2 = ElectronMVAIDRun2(
    
)
