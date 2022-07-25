// define de header file 
// it's telling that please if is not define something (detector construction)
#ifndef detectorconstruction_hh
// please define detector construction with the next stuffs
#define detectorconstruction_hh

#include "G4VUserDetectorConstruction.hh"
#include "G4VPhysicalVolume.hh"
// charge the class which helps to allow our own units
#include "G4SystemOfUnits.hh"
// charge classes for material definitions
#include "G4Isotope.hh"
#include "G4Element.hh"
#include "G4Material.hh"
#include "G4UnitsTable.hh"
// classes for NIST data base
#include "globals.hh"
#include "G4Material.hh"
#include "G4NistManager.hh"
// classes for solids
#include "G4Tubs.hh"
#include "G4Box.hh"
// clases for boleean operations
#include "G4SubtractionSolid.hh"
#include "G4UnionSolid.hh"
// classes for logical and physical volumes
#include "G4LogicalVolume.hh"
#include "G4VPhysicalVolume.hh"
#include "G4PVPlacement.hh"
#include "G4ThreeVector.hh"
#include "G4RunManager.hh"
#include "detectormessenger.hh"

class detectormessenger;


// define the class
class detectorconstruction:public G4VUserDetectorConstruction
{
    // creater class constructor and  destructor
    public:
    detectorconstruction();
    ~detectorconstruction();
    
    G4LogicalVolume *GetScoringVolume() const {return fScoringVolume;}
    void SetPos_NaI(G4ThreeVector dims);
    
    // create the function to create detector
    virtual G4VPhysicalVolume* Construct();
private:
    // solids
    G4LogicalVolume *logic_nai1;
    G4LogicalVolume *fScoringVolume;
 
    

    // messenger
    detectormessenger *fmessenger;
    // position first detector
    G4double posNaI_x, posNaI_y, posNaI_z;
    
};

#endif
// end up all this definition
