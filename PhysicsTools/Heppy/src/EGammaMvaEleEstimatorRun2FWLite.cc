#include "PhysicsTools/Heppy/interface/EGammaMvaEleEstimatorRun2FWLite.h"
#include "RecoEgamma/ElectronIdentification/interface/ElectronMVAEstimatorRun2.h"
#include <TFile.h>
#include <cassert>

heppy::EGammaMvaEleEstimatorRun2FWLite::EGammaMvaEleEstimatorRun2FWLite(const std::string &mvaTag, 
			   const std::string &mvaName, 
			   const std::vector <std::string> &weightFileNames, 
			   const int &nCategories, 
			   const bool debug, 
			   const std::string variableDefinition, 
			   const std::vector <std::string> categoryCutStrings)
{
    
}

heppy::EGammaMvaEleEstimatorRun2FWLite::~EGammaMvaEleEstimatorRun2FWLite()
{
    delete mvaReader_;
}

float heppy::EGammaMvaEleEstimatorRun2FWLite::operator()(const pat::Electron& electron, const edm::EventBase& iEvent) const 
{
  int icategory = mvaReader_->findCategory(electron)
    return mvaReader_->mvaValue(electron, iEvent, icategory);
}
