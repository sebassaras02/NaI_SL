#ifndef detectormessenger_h
#define detectormessenger_h 


#include "G4UImessenger.hh"
#include "globals.hh"
#include "detectorconstruction.hh"
#include "G4UIcmdWith3VectorAndUnit.hh"
#include "G4UIcommand.hh"

class detectorconstruction;

// hola mi primer cambio 
/// Detector construction class to define materials and geometry.

class detectormessenger : public  G4UImessenger
{
  public:
    detectormessenger(detectorconstruction* detector_);
    virtual ~detectormessenger();

    virtual void SetNewValue(G4UIcommand*, G4String);

  private:
    
    G4UIdirectory *fDetectorDir;
    G4UIcmdWith3VectorAndUnit *pos_NaI;
    detectorconstruction *f_det;

    
};


#endif