from ROOT import TFile, heppy, Double

import os
import logging 
import pprint 

class ElectronMVAIDRun2(object):

    def __init__(self, mvaTag, mvaName, weightFileNames,
                 nCategories, variableDefinition,
                 categoryCutStrings):
        logging.info('initializing electron id MVA')
        logging.info(pprint.pformat([mvaTag, mvaName, 
                                     weightFileNames,
                                     nCategories,
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
        pass

# used RecoEgamma/ElectronIdentification/python/Identification/mvaElectronID_Fall17_iso_V2_cff.py for categories and weightfiles
# variabledefinition should be the path to this file : RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt (or probably ElectronMVAEstimatorRun2Fall17V1Variables.txt ?)
mvaWeightFiles = ["EB1_5.weights.xml.gz",
                  "EB2_5.weights.xml.gz",
                  "EE_5.weights.xml.gz",
                  "EB1_10.weights.xml.gz",
                  "EB2_10.weights.xml.gz",
                  "EE_10.weights.xml.gz"]

categoryCuts = [
     "pt < 10. && abs(superCluster.eta) < 0.800", # EB1_5
     "pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479", # EB2_5
     "pt < 10. && abs(superCluster.eta) >= 1.479", # EE_5
     "pt >= 10. && abs(superCluster.eta) < 0.800", # EB1_10
     "pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479", # EB2_10
     "pt >= 10. && abs(superCluster.eta) >= 1.479", # EE_10
     ]

ElectronMVAID2017Isov2 = ElectronMVAIDRun2(
    'Fall17IsoV2',
    'mvaElectronID_Fall17_iso_v2',
    [os.path.join("RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2",fileName) for fileName in mvaWeightFiles],
    len(categoryCuts),
    "RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt",
    categoryCuts
)
