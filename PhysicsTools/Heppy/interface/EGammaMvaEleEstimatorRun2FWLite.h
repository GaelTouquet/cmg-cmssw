#ifndef _heppy_EGammaMvaEleEstimatorRun2FWLite_h
#define _heppy_EGammaMvaEleEstimatorRun2FWLite_h
#include "RecoEgamma/ElectronIdentification/interface/ElectronMVAEstimatorRun2.h"
#include "DataFormats/PatCandidates/interface/Electron.h"


namespace heppy {
    class EGammaMvaEleEstimatorRun2FWLite {
        public:
            EGammaMvaEleEstimatorRun2FWLite() : mvaReader_(nullptr) {}
            EGammaMvaEleEstimatorRun2FWLite(const std::string &mvaTag, 
			   const std::string &mvaName, 
			   const std::vector <std::string> &weightFileNames, 
			   const int &nCategories, 
			   const bool debug, 
			   const std::string variableDefinition, 
			   const std::vector <std::string> categoryCutStrings) ;
            ~EGammaMvaEleEstimatorRun2FWLite();
            EGammaMvaEleEstimatorRun2FWLite(const EGammaMvaEleEstimatorRun2FWLite & other) = delete;
            EGammaMvaEleEstimatorRun2FWLite & operator=(const EGammaMvaEleEstimatorRun2FWLite & other) = delete;

            float operator()(const pat::Electron& electron) const ;

        private:
            const ElectronMVAEstimatorRun2* mvaReader_;
    };
}

#endif
