#include "detectorconstruction.hh"

// contructor
detectorconstruction::detectorconstruction()
{
  // default values
  fmessenger=  new detectormessenger(this);
  posNaI_x=0*cm; 
  posNaI_y=0*cm;
  posNaI_z=0*cm;
}

void detectorconstruction::SetPos_NaI(G4ThreeVector dims) {
  posNaI_x=dims[0];
  posNaI_y=dims[1];
  posNaI_z=dims[2];
  G4RunManager::GetRunManager()->ReinitializeGeometry();
}
// destructor
detectorconstruction::~detectorconstruction()
{}
// define a function to create NaI detectors 

// add properties and volumenes
G4VPhysicalVolume* detectorconstruction::Construct()
{
  G4NistManager*  nist = G4NistManager::Instance();
  nist->SetVerbose(1);

  // define the world 
  // define the size
  G4double long_x1= 120*cm;
  G4double long_y1= 120*cm;
  G4double long_z1= 120*cm;
  G4Material* air = nist->FindOrBuildMaterial("G4_AIR");
   
    // define world solid
    G4Box* solidWorld =    
    new G4Box("World",                       //its name
       long_x1, long_y1, long_z1);           //its size
    // define world logic
    G4LogicalVolume* logicWorld =                         
    new G4LogicalVolume(solidWorld,          //its solid
                        air,           //its material
                        "World");            //its name
                                   
    // define physics solid
    G4VPhysicalVolume* physWorld = 
    new G4PVPlacement(0,                     //no rotation
                      G4ThreeVector(),       //at (0,0,0)
                      logicWorld,            //its logical volume
                      "World",               //its name
                      0,                     //its mother  volume
                      false,                 //no boolean operation
                      0,                     //copy number
                      true);        //overlaps checking

  // include de pipe
  // G4Material* cu= nist->FindOrBuildMaterial("G4_Cu");
  G4double len_pipe=0.4883760011793035*m, ra_pipe=5*cm, th_pipe=0.1*cm;
  G4Tubs *pipe_solid= new G4Tubs ("pipe_solid",0*cm,(ra_pipe+th_pipe),len_pipe,0.*deg,360.*deg);
  G4LogicalVolume *pipe_logic= new G4LogicalVolume(pipe_solid, air,"pipe_logic");
  // define rotation matrix
  auto m_rot= new G4RotationMatrix();
  m_rot->rotateY(90.*deg);
  // define physical volume
   new G4PVPlacement(m_rot,                       //no rotation
              G4ThreeVector(),                    //at position
              pipe_logic,                //its logical volume
              "pipe_phys",              //its name
              logicWorld,                   //its mother  volume
              false,                   //no boolean operation
              0,                       //copy number
              true);          //overlaps checking
  // define the water inside the pipe
  /*
  G4Material *water= nist->FindOrBuildMaterial("G4_WATER");
  G4Tubs *water_solid= new G4Tubs ("water_solid",0*cm,ra_pipe,(len_pipe-0.001*cm),0.*deg,360.*deg);
  G4LogicalVolume *water_logic= new G4LogicalVolume(water_solid, water,"water_logic");
    // define physical volume
  new G4PVPlacement(0,                       //no rotation
                G4ThreeVector(),                    //at position
                water_logic,                //its logical volume
                "water_phys",              //its name
                pipe_logic,                   //its mother  volume
                false,                   //no boolean operation
                0,                       //copy number
                true);          //overlaps checking
  */
    // define aluminium layer
    G4Material* al_mat = nist->FindOrBuildMaterial("G4_Al");
    // define solid
    G4Tubs* al_solid= new G4Tubs ("al_solid",0.0*cm,4.045*cm,4.1025*cm,0.*deg,360.*deg);
    // define logic
    G4LogicalVolume* al_logic= new G4LogicalVolume(al_solid,         //its solid
                                                    al_mat,                 //its material
                                                    "Aluminium_logic");         //its name
   
    G4ThreeVector pos_det1 = G4ThreeVector(posNaI_x,posNaI_y,posNaI_z+ra_pipe+th_pipe+4.1025*cm);

    // define rotation matrix
    auto m_rot2= new G4RotationMatrix();
    m_rot2->rotateY(180.*deg);

    // define physical volume
     new G4PVPlacement(m_rot2,                       //no rotation
                    pos_det1,                    //at position
                    al_logic,                //its logical volume
                    "al_phys",              //its name
                    logicWorld,                   //its mother  volume
                    false,                   //no boolean operation
                    0,                       //copy number
                    true);          //overlaps checking
                    
    // define SiO2 layer
    G4Material* si_mat = nist->FindOrBuildMaterial("G4_SILICON_DIOXIDE");
    // define solid
    G4Tubs* si_solid= new G4Tubs ("si_solid",0.0*cm,3.995*cm,0.15*cm,0.*deg,360.*deg);
    // define logic
    G4LogicalVolume* si_logic= new G4LogicalVolume(si_solid,         //its solid
                                                    si_mat,                 //its material
                                                  "si_logic");         //its name
    G4double j=(4.1025-0.05-0.15)*cm;
    G4ThreeVector pos2 = G4ThreeVector(0,0,-j);
    // define physical volume
    new G4PVPlacement(0,                       //no rotation
                    pos2,                    //at position
                    si_logic,                //its logical volume
                    "si_phys",              //its name
                    al_logic,                   //its mother  volume
                    false,                   //no boolean operation
                    0,                       //copy number
                    true);          //overlaps checking
                    
    // define MgO layer
    G4Material* mg_mat = nist->FindOrBuildMaterial("G4_MAGNESIUM_OXIDE");
    // define solid
    G4Tubs* mg_solid= new G4Tubs ("mg_solid",0.0*cm,3.995*cm,3.9025*cm,0.*deg,360.*deg);
    // define logic
    G4LogicalVolume* mg_logic= new G4LogicalVolume(mg_solid,         //its solid
                                                    mg_mat,                 //its material
                                                  "mg_logic");         //its name
    G4double j1=(0.15)*cm;
    G4ThreeVector pos3 = G4ThreeVector(0,0,j1);
    // define physical volume
    new G4PVPlacement(0,                       //no rotation
                    pos3,                    //at position
                    mg_logic,                //its logical volume
                    "mg_phys",              //its name
                    al_logic,                   //its mother  volume
                    false,                   //no boolean operation
                    0,                       //copy number
                    true);          //overlaps checking
    
    G4Material* na_mat = nist->FindOrBuildMaterial("G4_SODIUM_IODIDE");
    // define solid
    G4Tubs* na_solid= new G4Tubs ("na_solid",0.0*cm,3.81*cm,3.81*cm,0.*deg,360.*deg);
    // define logic
    logic_nai1 =  new G4LogicalVolume(na_solid,         //its solid
                        na_mat,                 //its material
                        "na_logic");         //its name
               
    G4double j2=(0.0915)*cm;
    G4ThreeVector pos4 = G4ThreeVector(0,0,-j2);
    
    new G4PVPlacement(0,                       //no rotation
                    pos4,                    //at position
                    logic_nai1,             //its logical volume
                    "na_phys",              //its name
                    mg_logic,              //its mother  volume
                    false,                   //no boolean operation
                    0,                       //copy number
                    true);          //overlaps checking
    
    
    fScoringVolume =logic_nai1; 


  

    return physWorld;
}


