#include "detectormessenger.hh"

detectormessenger::detectormessenger(detectorconstruction* detector_):f_det(detector_){

  // set directory to change NaI
  fDetectorDir = new G4UIdirectory("/NaI/detector/");
  fDetectorDir->SetGuidance("Detector geometry position");

  //Various commands for modifying detector geometry
  pos_NaI = new G4UIcmdWith3VectorAndUnit("/NaI/detector/dimensions",this);
  pos_NaI->SetGuidance("Set the positions of the detector volume.");
  pos_NaI->SetParameterName("scint_x","scint_y","scint_z",false);
  pos_NaI->SetDefaultUnit("cm");
  pos_NaI->AvailableForStates(G4State_PreInit,G4State_Idle);
  pos_NaI->SetToBeBroadcasted(false);
}

detectormessenger::~detectormessenger(){
  delete pos_NaI;
}

void detectormessenger::SetNewValue(G4UIcommand* command, G4String newValue)
{
  if( command == pos_NaI ){
    f_det->SetPos_NaI(pos_NaI->GetNew3VectorValue(newValue));
  }
}

