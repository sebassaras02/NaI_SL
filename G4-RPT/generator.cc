#include "generator.hh"

primarygenerator::primarygenerator()
{
    fparticlegun= new G4GeneralParticleSource;
}

primarygenerator::~primarygenerator()
{
    delete fparticlegun;
}

 void primarygenerator::GeneratePrimaries(G4Event* anEvent) {
     fparticlegun->GeneratePrimaryVertex(anEvent);
 }
