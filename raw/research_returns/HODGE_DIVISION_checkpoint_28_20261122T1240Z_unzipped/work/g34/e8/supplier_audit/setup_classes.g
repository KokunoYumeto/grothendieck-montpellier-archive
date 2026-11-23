Read("common_actual.g");
startclasses:=Runtime();;
WCL := ConjugacyClasses(GW);;
Assert(0,Length(WCL)=NC);
CLASSMAP := [];;
for cl in WCL do
  gp:=Representative(cl);;
  dd:=Decomp(gp);; Assert(0,dd[1]=0);
  inv:=[Order(gp),CycleStructurePerm(dd[3]),CharacteristicPolynomial(dd[2])];;
  ix:=Position(INVLIB,inv);; Assert(0,ix<>fail and not IsBound(CLASSMAP[ix]));
  Assert(0,Size(cl)=WORDER/cent[ix]);
  Assert(0,TraceMat(dd[2])=irr[reflidx][ix]);
  CLASSMAP[ix]:=gp;
od;
Assert(0,Length(CLASSMAP)=NC);
# Check every power, including scalars, against the library's power maps.
for ix in [1..NC] do
  for e in [0..ords[ix]-1] do
    Assert(0,GKey(CLASSMAP[ix]^e)=[0,pw(ix,e)]);
  od;
od;
Print("Fresh112 classes, cardinalities, natural traces and every power PASS, ms ",
      Runtime()-startclasses,"\n");
PrintTo("actual_setup_data.g","CLASSMAP := ",CLASSMAP,";\n",
        "ACTUAL_BR_SAVED := ",ACTUAL_BR,";\n",
        "FS_SAVED := ",FS,";\n",
        "COORDS_SAVED := ",COORDS,";\n",
        "TARGET_SAVED := ",target,";\n");

QUIT;
